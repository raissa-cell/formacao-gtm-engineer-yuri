"""Coleta comentários de um post (Apify) e roteia cada lead NOVO pro funil + campanha da Nuvia.

Fluxo por lead NOVO (não existe no CRM):
  1. dedup (processed.csv + linkedin_identifier no CRM)
  2. cria o contato com telefone-sentinela GARANTIDO livre (checa a base antes) + custom field
  3. cria/reaproveita conversa no inbox -> atribui agente -> move pra etapa de entrega
  4. registra no processed.csv
Ao final, faz BULK ENROLLMENT dos novos na campanha.

Leads que JÁ existem no CRM NÃO são tocados pelo script (o PUT/contacts REST é destrutivo e
o custom field em contato existente só via MCP). Eles vão pra signals/pending_existing.json
pra tratamento manual/MCP.

Nada de conteúdo hardcoded: post, palavra-gatilho, ids de funil/etapa/campanha, slug e valor
do custom field vêm do nuvia.config.json.

Uso:
  python3 collect_to_nuvia.py --config <pasta-do-post>/nuvia.config.json [--trigger-word VIRAL] [--dry-run]

Chaves lidas do .env do pilar (sobe a árvore até achar): NUVIA_API_KEY, APIFY_API_KEY.
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.parse

import requests

NUVIA_BASE = "https://api.nuvia.ai/v1"
APIFY_BASE = "https://api.apify.com/v2"
HERE = os.path.dirname(os.path.abspath(__file__))
# User-Agent de navegador é OBRIGATÓRIO: o WAF da Nuvia bloqueia python-requests com 403.
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
PHONE_BASE = 999002000  # base das sentinelas; a checagem na base garante que nunca colide


# ---------- infra ----------

def load_env():
    # Sobe a árvore até achar o .env do pilar (.env).
    env_path = ""
    d = HERE
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, ".env")):
            env_path = os.path.join(d, ".env")
            break
        d = os.path.dirname(d)
    if os.path.exists(env_path):
        with open(env_path) as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def load_config(path):
    with open(path, encoding="utf-8") as fh:
        cfg = json.load(fh)
    for k in ["post_url", "apify_actor", "nuvia"]:
        if k not in cfg:
            sys.exit(f"config incompleto, falta: {k}")
    nv = cfg["nuvia"]
    required = ["custom_field_slug", "custom_field_value"]
    # Roteamento de conversa (inbox/agente/etapa) é opcional: posts que só enrollam
    # na campanha usam "route_conversation": false e não precisam desses ids.
    if cfg.get("route_conversation", True):
        required += ["inbox_id", "agent_id", "step_id"]
    for k in required:
        if k not in nv:
            sys.exit(f"config.nuvia faltando: {k}")
    return cfg


def _unwrap(d):
    return d["result"] if isinstance(d, dict) and "result" in d else d


def items_of(d):
    r = _unwrap(d)
    if isinstance(r, list):
        return r
    if isinstance(r, dict):
        return r.get("data", [])
    return []


def id_of(d):
    r = _unwrap(d)
    return (r.get("_id") or r.get("id")) if isinstance(r, dict) else None


# ---------- Nuvia ----------

class Nuvia:
    def __init__(self, token):
        self.s = requests.Session()
        self.s.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": UA,
        })
        self._phone_cursor = PHONE_BASE

    def _req(self, method, path, body=None, tries=3):
        """Retenta timeout e 5xx: um pico da API não pode derrubar a rodada inteira.

        Incidente 13/08: um ReadTimeout no meio do push_scores abortou o script e
        metade dos contatos ficou sem score. Recalcular do ledger conserta na rodada
        seguinte, mas o certo é não cair por causa de um pico.
        """
        delay = 5
        for attempt in range(tries):
            try:
                r = self.s.request(method, NUVIA_BASE + path, json=body, timeout=45)
                if r.status_code >= 500 and attempt < tries - 1:
                    time.sleep(delay); delay = min(delay * 2, 20); continue
                r.raise_for_status()
                try:
                    return r.json()
                except ValueError:
                    return {}  # 200 sem corpo (a REST da Nuvia às vezes devolve vazio)
            except requests.exceptions.RequestException:
                if attempt == tries - 1:
                    raise
                time.sleep(delay); delay = min(delay * 2, 20)

    def find_contact(self, linkedin_identifier):
        filt = json.dumps([{"field": "contact.linkedin_identifier", "operator": "eq", "value": linkedin_identifier}])
        url = f"/contacts?filters={urllib.parse.quote(filt)}&rowsPerPage=1"
        its = items_of(self._req("GET", url))
        return its[0] if its else None

    def phone_taken(self, phone, cc="55"):
        # find-by-phones SÓ acha se passar cod_pais + numero concatenado (ex: 55 + 999001105).
        d = self._req("POST", "/contacts/find-by-phones", {"phones": [f"{cc}{phone}"]})
        return bool(_unwrap(d).get("contacts")) if isinstance(_unwrap(d), dict) else False

    def find_lead(self, linkedin=None, phone=None, cc="55"):
        """Acha um contato: primeiro pelo slug do LinkedIn, se não achar, pelo telefone.

        linkedin: slug ("joao-silva-123") ou URL do perfil. phone: com ou sem DDI/máscara.
        Retorna (contato, "linkedin" | "phone") ou (None, None).
        Telefone fictício do comment-gate não bate com o real, então pra esses leads só o LinkedIn acha.
        """
        if linkedin:
            slug = urllib.parse.unquote(_slug(linkedin) if "/" in linkedin else linkedin).strip().lower()
            c = self.find_contact(slug) if slug else None
            if c:
                return c, "linkedin"
        if phone:
            digits = "".join(ch for ch in str(phone) if ch.isdigit())
            # ponytail: BR com DDI tem 12-13 dígitos; sem DDI, até 11 (DDD 55 existe, então não dá pra testar só o prefixo)
            if len(digits) <= 11:
                digits = cc + digits
            r = _unwrap(self._req("POST", "/contacts/find-by-phones", {"phones": [digits]}))
            cs = r.get("contacts") if isinstance(r, dict) else None
            if cs:
                return cs[0], "phone"
        return None, None

    def next_free_phone(self, assigned, cc="55"):
        # Gera um numero, CHECA na base antes; se existir, +1 e checa de novo, ate achar livre.
        while True:
            cand = str(self._phone_cursor)
            self._phone_cursor += 1
            if cand in assigned:
                continue
            if self.phone_taken(cand, cc):
                continue
            assigned.add(cand)
            return cand

    def create_contact(self, name, slug, headline, field_slug, field_value, assigned, cc="55"):
        phone = self.next_free_phone(assigned, cc)
        payload = {
            "name": name or slug,
            "country_code": cc,
            "phone_number": phone,
            "linkedin_identifier": slug,
            "additional_attributes": {field_slug: field_value},
        }
        if headline:
            payload["job_title"] = headline  # best-effort; o create REST as vezes nao persiste
        d = self._req("POST", "/contacts", payload)
        cid = id_of(d)
        if not cid:  # resposta veio vazia -> re-busca pelo slug
            ex = self.find_contact(slug)
            cid = id_of(ex) if ex else None
        return cid, phone

    def contact_conversation(self, cid, inbox_id):
        its = items_of(self._req("GET", f"/contacts/{cid}/conversations"))
        for c in its:
            inb = c.get("inbox") or {}
            if (inb.get("id") or inb.get("_id")) == inbox_id:
                return c.get("_id") or c.get("id")
        return (its[0].get("_id") or its[0].get("id")) if its else None

    def route_conversation(self, cid, inbox_id, agent_id, step_id):
        convid = self.contact_conversation(cid, inbox_id)
        if not convid:
            d = self._req("POST", "/conversations", {"contactId": cid, "inboxId": inbox_id})
            convid = id_of(d) or self.contact_conversation(cid, inbox_id)
        if convid:
            self._req("PUT", f"/conversations/{convid}/assign-agent", {"agentId": agent_id})
            self._req("PUT", f"/conversations/{convid}/step", {"stepId": step_id})
        return convid

    # Campos escalares que o PUT /contacts aceita. O PUT é FULL REPLACE: o que não
    # for reenviado some. Por isso o round-trip devolve tudo que veio no GET.
    WRITABLE = ["name", "email", "phone_number", "country_code", "linkedin_identifier",
                "job_title", "city", "region", "country", "department", "seniority",
                "skills", "experience"]

    def score_contact(self, cid, post_tag):
        """Acumula o post em post-interacao e recalcula engagement-score.

        post-interacao guarda TODOS os posts em que o lead interagiu, separados por ', '.
        engagement-score = quantos posts distintos. Idempotente: rodar de novo não duplica.
        Escrita é por SLUG ('engagement-score'); a leitura volta pelo TÍTULO
        ('engagement_score'), por isso as duas grafias são limpas antes de reescrever.
        """
        cur = _unwrap(self._req("GET", f"/contacts/{cid}"))
        attrs = {k: (v.get("value") if isinstance(v, dict) else v)
                 for k, v in (cur.get("additional_attributes") or {}).items()}
        # aceita ',' e ';' na leitura (histórico gravado antes da padronização)
        raw = str(attrs.get("post-interacao") or "").replace(";", ",")
        posts = [p.strip() for p in raw.split(",") if p.strip()]
        if post_tag not in posts:
            posts.append(post_tag)
        for k in ("post-interacao", "engagement-score", "engagement_score"):
            attrs.pop(k, None)
        attrs["post-interacao"] = ", ".join(posts)
        attrs["engagement-score"] = len(posts)
        payload = {k: cur[k] for k in self.WRITABLE if cur.get(k) is not None}
        payload["additional_attributes"] = attrs
        self._req("PUT", f"/contacts/{cid}", payload)
        return len(posts), attrs["post-interacao"]

    def bulk_enroll(self, campaign_id, contact_ids):
        d = self._req("POST", f"/campaigns/{campaign_id}/enrollments/bulk", {"contact_ids": contact_ids})
        return _unwrap(d)


# ---------- Apify (async: dispara -> espera/poll com backoff -> baixa) ----------

def _apify(method, url, body=None, tries=6):
    """Retenta com backoff. tries=6 e teto de 30s porque a máquina dorme muito:
    ao acordar, o DNS ainda não resolve api.apify.com por dezenas de segundos
    (incidente 13/08: collect exit=1 por NameResolutionError, enroll pulado)."""
    delay = 5
    last = None
    for _ in range(tries):
        try:
            r = requests.request(method, url, json=body, headers={"User-Agent": UA}, timeout=120)
            if r.status_code >= 500 or r.status_code == 429:
                last = f"HTTP {r.status_code}"
                time.sleep(delay); delay = min(delay + 10, 30); continue
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            last = str(e)  # sem resposta / DNS / connection fail -> espera crescente
            time.sleep(delay); delay = min(delay + 10, 30)
    raise RuntimeError(f"Apify inacessível após {tries} tentativas: {last}")


def scrape_comments(actor, post_url, token, max_items):
    actor_path = actor.replace("/", "~")
    start = _apify("POST", f"{APIFY_BASE}/acts/{actor_path}/runs?token={token}",
                   {"posts": [post_url], "maxItems": max_items, "scrapeReplies": False, "profileScraperMode": "short"})
    run_id = (start.get("data") or {}).get("id")
    if not run_id:
        raise RuntimeError("Apify não retornou runId")
    delay = 5
    for _ in range(40):
        time.sleep(delay)  # espera ANTES de checar se o ator rodou
        st = _apify("GET", f"{APIFY_BASE}/actor-runs/{run_id}?token={token}")
        status = (st.get("data") or {}).get("status")
        if status == "SUCCEEDED":
            break
        if status in ("FAILED", "ABORTED", "TIMED-OUT"):
            raise RuntimeError(f"Apify run {status}")
        delay = min(delay + 5, 15)  # crescente: 5 -> 10 -> 15
    else:
        raise RuntimeError("Apify: run não concluiu no tempo esperado")
    items = _apify("GET", f"{APIFY_BASE}/actor-runs/{run_id}/dataset/items?token={token}")
    return items if isinstance(items, list) else items.get("items", items.get("data", []))


def _slug(url):
    if not url:
        return ""
    return urllib.parse.urlparse(url).path.strip("/").split("/")[-1]


def parse_comment(item):
    a = item.get("actor") or {}
    name = (a.get("name") or "").strip()
    ident = (a.get("publicIdentifier") or _slug(a.get("linkedinUrl") or a.get("url") or "")).strip().lower()
    headline = (a.get("position") or a.get("headline") or "").strip()
    text = (item.get("commentary") or "").strip()
    return name, ident, headline, text


# ---------- processed.csv ----------

FIELDS = ["name", "linkedin_identifier", "headline", "contact_id", "conversation_id",
          "posts_tocados", "status"]


def load_processed(csv_path):
    seen = set()
    if os.path.exists(csv_path):
        with open(csv_path, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("linkedin_identifier"):
                    seen.add(row["linkedin_identifier"].strip().lower())
    return seen


def append_processed(csv_path, rows):
    if not rows:
        return
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    new = not os.path.exists(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow(r)


# ---------- main ----------

def main():
    p = argparse.ArgumentParser(description="Coleta comentários e roteia leads novos pro funil + campanha da Nuvia.")
    p.add_argument("--config", required=True, help="Caminho do nuvia.config.json do post")
    p.add_argument("--trigger-word", help="Palavra-gatilho (sobrepõe a do config)")
    p.add_argument("--dry-run", action="store_true", help="Raspa e classifica, sem escrever nada")
    args = p.parse_args()

    load_env()
    nuvia_token = os.environ.get("NUVIA_API_KEY")
    apify_token = os.environ.get("APIFY_API_KEY")
    if not nuvia_token:
        sys.exit("NUVIA_API_KEY não encontrada no .env do pilar (.env).")
    if not apify_token:
        sys.exit("APIFY_API_KEY não encontrada no .env do pilar (.env).")

    cfg = load_config(args.config)
    nv = cfg["nuvia"]
    author = (cfg.get("author_slug") or "").strip().lower()
    trigger_raw = args.trigger_word or cfg.get("trigger_word") or ""
    trigger = trigger_raw.strip().lower()
    if not trigger:
        sys.exit("palavra-gatilho ausente: passe --trigger-word ou defina trigger_word no config.")
    max_items = cfg.get("max_items", 500)
    campaign_id = nv.get("campaign_id")
    cfg_dir = os.path.dirname(os.path.abspath(args.config))
    csv_path = cfg.get("processed_csv", "signals/processed.csv")
    if not os.path.isabs(csv_path):
        csv_path = os.path.join(cfg_dir, csv_path)
    pending_path = os.path.join(cfg_dir, "signals", "pending_existing.json")

    print(f"coletando comentários de {cfg['post_url']} (gatilho: {trigger_raw})")
    items = scrape_comments(cfg["apify_actor"], cfg["post_url"], apify_token, max_items)
    print(f"  {len(items)} comentários brutos")

    seen = load_processed(csv_path)
    brutos_viral = 0
    candidatos = []  # (name, slug, headline)
    for it in items:
        name, ident, headline, text = parse_comment(it)
        if not ident or ident == author:
            continue
        if trigger not in text.lower():
            continue
        brutos_viral += 1
        if ident in seen:
            continue
        seen.add(ident)
        candidatos.append((name, ident, headline))

    if args.dry_run:
        print(f"[dry-run] com_VIRAL={brutos_viral} | novos_a_processar={len(candidatos)}")
        for name, ident, headline in candidatos:
            print(f"    - {name} ({ident})")
        return

    nuvia = Nuvia(nuvia_token)
    assigned_phones = set()
    novos_rows = []
    novos_ids = []
    existentes = []
    erros = []
    for name, ident, headline in candidatos:
        try:
            ex = nuvia.find_contact(ident)
            if ex:  # JÁ EXISTE -> não editar o contato (PUT é destrutivo), mas ENROLLAR:
                # quem comentou pediu o material, e enroll só usa o id, não altera o cadastro.
                exid = id_of(ex)
                existentes.append({"name": name, "linkedin_identifier": ident,
                                   "headline": headline, "contact_id": exid})
                if exid:
                    novos_ids.append(exid)
                    score, _ = nuvia.score_contact(exid, nv["custom_field_value"])
                    novos_rows.append({"name": name, "linkedin_identifier": ident, "headline": headline,
                                       "contact_id": exid, "conversation_id": "",
                                       "posts_tocados": score,
                                       "status": "existente_enrollado"})
                continue
            cid, phone = nuvia.create_contact(name, ident, headline,
                                              nv["custom_field_slug"], nv["custom_field_value"], assigned_phones)
            if not cid:
                erros.append(f"{ident}: create sem id")
                continue
            convid = (nuvia.route_conversation(cid, nv["inbox_id"], nv["agent_id"], nv["step_id"])
                      if cfg.get("route_conversation", True) else "")
            score, _ = nuvia.score_contact(cid, nv["custom_field_value"])
            novos_ids.append(cid)
            novos_rows.append({"name": name, "linkedin_identifier": ident, "headline": headline,
                               "contact_id": cid, "conversation_id": convid or "",
                               "posts_tocados": score,
                               "status": "roteado" if convid else "novo_enrollado"})
            print(f"  novo  {ident:30} cid={cid} phone={phone} conv={convid}")
        except Exception as e:
            erros.append(f"{ident}: {e}")

    append_processed(csv_path, novos_rows)

    if existentes:
        os.makedirs(os.path.dirname(pending_path), exist_ok=True)
        prev = []
        if os.path.exists(pending_path):
            try:
                prev = json.load(open(pending_path, encoding="utf-8"))
            except Exception:
                prev = []
        known = {e["linkedin_identifier"] for e in prev}
        prev.extend([e for e in existentes if e["linkedin_identifier"] not in known])
        json.dump(prev, open(pending_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    enrolled = None
    if novos_ids:
        if campaign_id:
            enrolled = nuvia.bulk_enroll(campaign_id, novos_ids)
        else:
            print("  AVISO: campaign_id ausente no config -> enrollment PULADO. Defina nuvia.campaign_id.")

    print("\n=== RESUMO ===")
    print(f"brutos={len(items)} | com_VIRAL={brutos_viral} | ja_processados={brutos_viral - len(candidatos)}")
    print(f"novos criados+roteados={len(novos_rows)} | enrollment={json.dumps(enrolled) if enrolled else '—'}")
    print(f"existentes pendentes (tratar via MCP): {len(existentes)}")
    for e in existentes:
        print(f"    · {e['name']} ({e['linkedin_identifier']}) id={e['contact_id']}")
    if erros:
        print(f"erros={len(erros)}")
        for e in erros:
            print(f"    ! {e}")
    if existentes:
        print(f"\npendências salvas em: {pending_path}")


if __name__ == "__main__":
    main()
