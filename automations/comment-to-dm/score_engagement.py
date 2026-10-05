"""Calcula o engagement_score dos leads a partir das interações nos posts.

Mantém um LEDGER global (engagement_ledger.json nesta pasta) com os sinais crus por lead,
e recalcula o score inteiro a cada rodada. Recalcular do zero é o que torna a coisa
idempotente: rodar duas vezes não infla nada, e mudar um peso reprecifica todo mundo.

Cada sinal guarda a DATA em que foi visto pela primeira vez (nunca sobrescrita):
  "posts": {"post_humanize_ptbr": {"gatilho": "2026-08-12", "like": "2026-08-12"}}

Sinais por POST (contam uma vez por post):
  gatilho   - comentou a palavra-gatilho (pediu o material)
  comentou  - comentou sem a palavra-gatilho
  like      - reagiu ao post
'gatilho' e 'comentou' são exclusivos no mesmo post.

Flags por LEAD (contam uma vez no total, marcadas fora daqui):
  conversou, comunidade, formacao  -> ver --set-flag

Escreve na Nuvia: post-interacao (lista acumulada dos posts) e engagement-score (número).
Lead que ainda não existe no CRM é CRIADO aqui (inclusive quem só curtiu), com
telefone-sentinela. Enrollment em campanha continua sendo só de quem comentou o gatilho.

Uso:
  python3 score_engagement.py --config <pasta-do-post>/nuvia.config.json [--dry-run]
  python3 score_engagement.py --set-flag <slug>:<conversou|comunidade|formacao> [--push]
  python3 score_engagement.py --selftest
"""

import argparse
import contextlib
import fcntl
import json
import os
import sys

import collect_to_nuvia as base

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "engagement_ledger.json")
WEIGHTS = os.path.join(HERE, "weights.json")
FLAGS = ("conversou", "comunidade", "formacao")


@contextlib.contextmanager
def ledger_lock():
    """Serializa o acesso ao ledger.

    O launchd roda uma rodada a cada 30 min e um backfill pode rodar em paralelo:
    sem lock, quem salvar por último apaga o que o outro escreveu. Bloqueia até liberar.
    """
    with open(LEDGER + ".lock", "w") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_ledger(led):
    with open(LEDGER, "w", encoding="utf-8") as fh:
        json.dump(led, fh, ensure_ascii=False, indent=1, sort_keys=True)


def weights():
    return {k: v for k, v in load_json(WEIGHTS, {}).items() if not k.startswith("_")}


def score_of(entry, w):
    """Score = sinais de post (uma vez por post) + flags de lead (uma vez no total)."""
    total = sum(w.get(sig, 0) for sigs in entry.get("posts", {}).values() for sig in sigs)
    total += sum(w.get(f, 0) for f, on in (entry.get("flags") or {}).items() if on)
    return total


def entry_for(led, slug, name=None):
    e = led.setdefault(slug, {"name": name or slug, "contact_id": None,
                              "posts": {}, "flags": {f: False for f in FLAGS}})
    if name and e.get("name") in (None, slug):
        e["name"] = name
    e.setdefault("posts", {})
    e.setdefault("flags", {f: False for f in FLAGS})
    return e


def today():
    """Data em UTC: a máquina troca de fuso em viagem e a data do sinal não pode andar."""
    from datetime import datetime as _dt, timezone as _tz
    return _dt.now(_tz.utc).date().isoformat()


def is_urn(ident):
    """O ator de reações às vezes devolve o URN opaco (ACoAA...) em vez do slug público."""
    return ident.startswith("acoaa")


def add_signal(led, slug, name, post_tag, signal, date=None):
    """Registra o sinal com a data da primeira vez que ele foi visto.

    Data existente nunca é sobrescrita: o que importa é QUANDO a pessoa interagiu,
    não quando a rodada rodou de novo.
    """
    e = entry_for(led, slug, name)
    sigs = e["posts"].get(post_tag) or {}
    if isinstance(sigs, list):          # formato antigo (só a lista de sinais)
        sigs = {s: None for s in sigs}
    if signal == "gatilho":
        sigs.pop("comentou", None)      # gatilho substitui comentou no mesmo post
    elif signal == "comentou" and "gatilho" in sigs:
        return e                         # já tem o sinal mais específico
    if signal not in sigs or not sigs.get(signal):
        sigs[signal] = date or today()
    e["posts"][post_tag] = dict(sorted(sigs.items()))
    return e


def _reactions(post_url, token, max_items):
    """Mesmo publisher do ator de comentários, mesmo shape de entrada/saída."""
    actor = "harvestapi~linkedin-post-reactions"
    start = base._apify("POST", f"{base.APIFY_BASE}/acts/{actor}/runs?token={token}",
                        {"posts": [post_url], "maxItems": max_items, "profileScraperMode": "main"})
    run_id = (start.get("data") or {}).get("id")
    if not run_id:
        raise RuntimeError("Apify não retornou runId (reactions)")
    import time
    delay = 5
    for _ in range(40):
        time.sleep(delay)
        st = base._apify("GET", f"{base.APIFY_BASE}/actor-runs/{run_id}?token={token}")
        status = (st.get("data") or {}).get("status")
        if status == "SUCCEEDED":
            break
        if status in ("FAILED", "ABORTED", "TIMED-OUT"):
            raise RuntimeError(f"Apify reactions run {status}")
        delay = min(delay + 5, 15)
    else:
        raise RuntimeError("Apify reactions: run não concluiu")
    items = base._apify("GET", f"{base.APIFY_BASE}/actor-runs/{run_id}/dataset/items?token={token}")
    return items if isinstance(items, list) else items.get("items", items.get("data", []))


def parse_reactor(item):
    a = item.get("actor") or item.get("reactor") or item.get("profile") or {}
    # profileScraperMode "main" traz publicIdentifier; sem ele sobraria só o URN opaco
    # (ACoAA...), que não casa com o slug vindo dos comentários e duplica a pessoa.
    name = (a.get("name") or item.get("name") or "").strip()
    headline = (a.get("position") or a.get("headline") or "").strip()
    ident = (a.get("publicIdentifier") or item.get("publicIdentifier")
             or base._slug(a.get("linkedinUrl") or a.get("url") or item.get("profileUrl") or "")).strip().lower()
    return name, ident, headline, item


def item_date(item, fallback=None):
    """Usa a data que o ator devolver; reações não trazem timestamp.

    Sem timestamp, vale o `default_date` do config (essencial em backfill de post
    antigo, senão a interação de julho seria datada de hoje) ou a data da rodada.
    """
    for k in ("createdAt", "postedAt", "date", "publishedAt", "reactedAt"):
        v = item.get(k)
        if isinstance(v, str) and len(v) >= 10 and v[4] == "-":
            return v[:10]
    return fallback or today()


def push_scores(led, w, dry_run=False):
    """Empurra post-interacao + engagement-score pra Nuvia.

    Lead que ainda não existe no CRM é CRIADO (decisão do usuário em 12/08: quem curtiu
    também vira contato, com a pontuação correspondente).
    """
    nuvia = None if dry_run else base.Nuvia(os.environ["NUVIA_API_KEY"])
    assigned = set()
    enviados = criados = 0
    for slug, e in sorted(led.items()):
        sc = score_of(e, w)
        posts = ", ".join(sorted(e.get("posts", {})))
        if dry_run:
            print(f"  [dry] {slug:38} score={sc:<4} posts=[{posts}] flags={[f for f,v in e['flags'].items() if v]}")
            enviados += 1
            continue
        cid = e.get("contact_id")
        if not cid:
            ex = nuvia.find_contact(slug)
            cid = base.id_of(ex) if ex else None
        if not cid:
            cid, _ = nuvia.create_contact(e.get("name") or slug, slug, e.get("headline") or "",
                                          "post-interacao", posts, assigned)
            criados += 1
        e["contact_id"] = cid
        if not cid:
            continue
        cur = base._unwrap(nuvia._req("GET", f"/contacts/{cid}"))
        attrs = {k: (v.get("value") if isinstance(v, dict) else v)
                 for k, v in (cur.get("additional_attributes") or {}).items()}
        for k in ("post-interacao", "engagement-score", "engagement_score"):
            attrs.pop(k, None)
        attrs["post-interacao"] = posts
        attrs["engagement-score"] = sc
        payload = {k: cur[k] for k in nuvia.WRITABLE if cur.get(k) is not None}
        payload["additional_attributes"] = attrs
        nuvia._req("PUT", f"/contacts/{cid}", payload)
        enviados += 1
    return enviados, criados


def selftest():
    w = {"formacao": 50, "comunidade": 15, "conversou": 10, "comentou": 5, "gatilho": 3, "like": 1}
    led = {}
    # comentou o gatilho e curtiu o mesmo post -> 3 + 1
    add_signal(led, "ana", "Ana", "post_a", "gatilho")
    add_signal(led, "ana", "Ana", "post_a", "like")
    assert score_of(led["ana"], w) == 4, score_of(led["ana"], w)
    # comentou sem gatilho no mesmo post NÃO soma (gatilho é mais específico)
    add_signal(led, "ana", "Ana", "post_a", "comentou")
    assert score_of(led["ana"], w) == 4
    # gatilho chegando DEPOIS de comentou substitui, não empilha
    add_signal(led, "bob", "Bob", "post_a", "comentou")
    assert score_of(led["bob"], w) == 5
    add_signal(led, "bob", "Bob", "post_a", "gatilho")
    assert score_of(led["bob"], w) == 3, score_of(led["bob"], w)
    # sinais somam ENTRE posts
    add_signal(led, "bob", "Bob", "post_b", "like")
    assert score_of(led["bob"], w) == 4
    # idempotência: repetir o mesmo sinal não infla
    for _ in range(3):
        add_signal(led, "bob", "Bob", "post_b", "like")
    assert score_of(led["bob"], w) == 4
    # a data do primeiro avistamento não é sobrescrita numa rodada posterior
    add_signal(led, "cid", "Cid", "post_a", "like", "2026-08-01")
    add_signal(led, "cid", "Cid", "post_a", "like", "2026-08-09")
    assert led["cid"]["posts"]["post_a"]["like"] == "2026-08-01", led["cid"]["posts"]["post_a"]
    # flags contam uma vez no total, não por post
    led["bob"]["flags"]["conversou"] = True
    led["bob"]["flags"]["formacao"] = True
    assert score_of(led["bob"], w) == 64, score_of(led["bob"], w)
    print("selftest ok")


def main():
    p = argparse.ArgumentParser(description="Calcula engagement_score a partir das interações.")
    p.add_argument("--config", help="nuvia.config.json do post a coletar")
    p.add_argument("--set-flag", help="<slug>:<conversou|comunidade|formacao>")
    p.add_argument("--push", action="store_true", help="com --set-flag, já empurra os scores")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        return selftest()

    base.load_env()
    w = weights()

    if args.set_flag:
      with ledger_lock():
        led = load_json(LEDGER, {})
        slug, _, flag = args.set_flag.partition(":")
        if flag not in FLAGS:
            sys.exit(f"flag inválida: {flag} (use {'/'.join(FLAGS)})")
        entry_for(led, slug)["flags"][flag] = True
        save_ledger(led)
        print(f"flag {flag} marcada em {slug} -> score {score_of(led[slug], w)}")
        if args.push:
            print(push_scores(led, w))
            save_ledger(led)
        return

    if not args.config:
        sys.exit("passe --config, --set-flag ou --selftest")

    cfg = base.load_config(args.config)
    # coleta FORA do lock (é a parte lenta); só a leitura/escrita do ledger é serializada.
    tag = cfg["nuvia"]["custom_field_value"]
    trigger = (cfg.get("trigger_word") or "").strip().lower()
    author = (cfg.get("author_slug") or "").strip().lower()
    token = os.environ["APIFY_API_KEY"]
    maxi = cfg.get("max_items", 500)

    comments = base.scrape_comments(cfg["apify_actor"], cfg["post_url"], token, maxi)
    reactions = _reactions(cfg["post_url"], token, maxi)

    # sinais coletados primeiro, ledger tocado depois: o lock fica preso o mínimo possível
    novos = []
    n_gat = n_com = n_like = 0
    for it in comments:
        name, ident, _, text = base.parse_comment(it)
        if not ident or ident == author:
            continue
        sig = "gatilho" if trigger and trigger in text.lower() else "comentou"
        novos.append((ident, name, sig, item_date(it, cfg.get("default_date")), ""))
        n_gat += sig == "gatilho"
        n_com += sig == "comentou"
    for it in reactions:
        name, ident, headline, raw = parse_reactor(it)
        if not ident or ident == author:
            continue
        novos.append((ident, name, "like", item_date(raw, cfg.get("default_date")), headline))
        n_like += 1

    with ledger_lock():
        led = load_json(LEDGER, {})
        for ident, name, sig, quando, headline in novos:
            e = add_signal(led, ident, name, tag, sig, quando)
            if headline and not e.get("headline"):
                e["headline"] = headline
        save_ledger(led)
        print(f"post={tag} | gatilho={n_gat} comentou={n_com} like={n_like} | leads no ledger={len(led)}")
        enviados, criados = push_scores(led, w, args.dry_run)
        save_ledger(led)
        print(f"scores gravados={enviados} | contatos criados nesta rodada={criados}")

    top = sorted(led.items(), key=lambda kv: -score_of(kv[1], w))[:10]
    print("top 10:")
    for slug, e in top:
        print(f"  {score_of(e, w):>4}  {e.get('name','')[:32]:32} {slug}")


if __name__ == "__main__":
    main()
