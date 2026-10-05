"""Cruza os leads de um post com o export de conexões do LinkedIn e classifica ICP.

Entrada : processed.csv da pasta do post + Connections.csv do export do LinkedIn
Saída   : <prefixo>_conectados.csv e <prefixo>_nao_conectados.csv (na mesma pasta)

Vocabulário de ICP por palavras-chave de cargo/headline (listas ICP e NIVEL abaixo).
Ajuste ao SEU ICP antes do primeiro uso.

PADRÃO PARA TODOS OS LEADS: todo post que gera lead passa por aqui antes de virar
campanha. O ICP não é opinião por post; é este vocabulário, revisado à mão e preservado via icp_manual.

Uso:
  python3 triagem_icp.py --pasta "campaigns/<publico>/conteudo/AAAA-MM/<post>/signals" [--prefixo xxx]
  python3 triagem_icp.py --pasta ... --conexoes "Connections 20260823.csv"

Sem --conexoes, usa o export de conexões mais recente na raiz do projeto.
Saída: <prefixo>_conectados.csv e <prefixo>_nao_conectados.csv na pasta do post.
"""

import argparse
import csv
import json
import os
import re
import urllib.parse
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
# .../automations/leads -> raiz do projeto
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
HERE = AQUI  # pasta dos dados do post; setada por --pasta
CONEXOES = None  # resolvida em conexoes_mais_recentes()
RUNTIME = os.path.expanduser("~/gtm-automation")

# Testes, amigos e família: nunca entram em campanha. Slug do LinkedIn em minúsculas.
EXCLUIR = {
    # "slug-do-linkedin",
}

# ordem importa: a primeira que casar vence. Growth antes de Marketing/Vendas
# porque "growth marketing" e "growth sales" devem cair em Growth.
# Siglas de C-level entram aqui porque o cargo costuma vir SO como sigla
# ("CMO", "CO-CEO & CRO"). Sem isso o lead cai em Fora (6 casos em 24/08).
# "CRO" conta como Growth (decisao do usuário, 24/08): os dois sentidos uteis
# (Chief Revenue Officer e Conversion Rate Optimization) sao ICP. O terceiro,
# Chief Risk Officer, e neutralizado por RISCO_CRO abaixo.
# Grau lido A MAO no LinkedIn quando o export esta defasado (prints do usuário).
# Vence o export: 1 = conectado, 2 = nao conectado. Lido em 26/08/2026, quando
# o export mais novo era de 23/08 e 12 pessoas ja tinham aceitado convite.
CONECTADO_MANUAL = {
    # "slug-do-linkedin": 1,  # 1 = conectado, 2 = não conectado
}

RISCO_CRO = re.compile(r"chief risk|risk officer|gest[ãa]o de risco|risco de cr[ée]dito", re.I)

ICP = [
    ("Growth",    r"\b(growth|chief growth|\bcgo\b|\bcro\b|demand gen\w*|revops|rev ops|revenue operations|aquisi[çc][ãa]o|gtm\b|go.?to.?market)"),
    # "product marketing" (PMM) é Marketing, não Produto: cortado no lookahead.
    # "product design" ficou de fora de propósito: puxava Art Director junto.
    ("Produto",   r"\b(product(?! marketing) (manager|owner|lead|director)|produto digital|gerente de produto|gest[ãa]o de produtos?|head of product|chief product|\bcpo\b|\bpo\b|product management)"),
    ("Dados",     r"\b(data scien\w*|cientista de dados|data analy\w*|analista de dados|engenheiro de dados|data engineer|\bbi\b|business intelligence|analytics|estat[íi]stic\w*|machine learning|\bml\b|dados)"),
    ("Tech",      r"\b(desenvolvedor|developer|software engineer|engenheiro de software|back.?end|front.?end|full.?stack|devops|programador|\bqa\b|analista de sistemas|\bsre\b|\bdba\b|arquiteto de solu|tech lead|\bcto\b|engenheiro de \w*(ia|ai)|\bia\b|artificial intelligence|automa[çc][ãa]o)"),
    ("Vendas",    r"\b(sdr|chief revenue|bdr|pr[ée].?vendas|inside sales|outbound|prospec\w*|account executive|\bae\b|executivo de vendas|executivo comercial|vendas|sales|comercial|closer|hunter|new business|business development|desenvolvimento de neg[óo]cios|account manager|gerente de contas|customer success|\bcs\b)"),
    ("Marketing", r"\b(marketing|\bcmo\b|\bccmo\b|chief marketing|m[íi]dia paga|tr[áa]fego|social media|conte[úu]do|content|branding|publicidad\w*|\bseo\b|\bads\b|comunica[çc][ãa]o)"),
]

# ponytail: senioridade por regex, heurística grosseira o suficiente pra ordenar triagem
NIVEL = [
    ("C-level",   r"\b(ceo|cfo|coo|cto|cmo|cro|c-level|chief|founder|fundador|co-?founder|s[óo]cio|owner|presidente|partner)\b"),
    ("Diretoria", r"\b(diretor|director|vp|vice-?president|head\b|head of)\b"),
    ("Gerência",  r"\b(gerente|manager|coordenador|coordinator|l[ií]der|lead\b|supervisor)\b"),
    ("Consultor", r"\b(consultor|consultant|advisor|mentor|professor|especialista)\b"),
]


def slug(url):
    return urllib.parse.unquote(url.rstrip("/").split("/in/")[-1]).lower()


def icp_de(cargo, headline):
    """ICP pelo texto. CRO conta como Growth, menos quando e CRO de RISCO:
    nesse caso a sigla e apagada antes de classificar."""
    txt = f"{cargo} {headline}".lower()
    if RISCO_CRO.search(txt):
        txt = re.sub(r"\bcro\b", "", txt)
    return primeiro(ICP, txt, "Fora")


def primeiro(tabela, texto, default):
    for nome, rx in tabela:
        if re.search(rx, texto):
            return nome
    return default


def conexoes_mais_recentes():
    """A base de conexões envelhece rápido (186 novas entre 16/08 e 17/08), então o
    default é sempre o export mais novo que existir na raiz, não um nome fixo."""
    import glob
    arqs = glob.glob(os.path.join(RAIZ, "Connections*.csv"))
    if not arqs:
        raise SystemExit(f"nenhum Connections*.csv em {RAIZ} (exportar do LinkedIn)")
    return max(arqs, key=os.path.getmtime)


def carregar_conexoes():
    linhas = open(CONEXOES, encoding="utf-8").readlines()
    ini = next(i for i, l in enumerate(linhas) if l.startswith("First Name,"))
    return {slug(r["URL"]): r for r in csv.DictReader(linhas[ini:]) if r.get("URL")}


def score_ledger():
    pesos = json.load(open(os.path.join(RUNTIME, "weights.json")))
    ledger = json.load(open(os.path.join(RUNTIME, "engagement_ledger.json")))

    def calc(e):
        s = sum(pesos[f] for f in ("formacao", "comunidade", "conversou") if e["flags"].get(f))
        for p in e.get("posts", {}).values():
            s += pesos["gatilho"] if "gatilho" in p else pesos["comentou"] if "comentou" in p else 0
            s += pesos["like"] if "like" in p else 0
        return s

    return {k: calc(v) for k, v in ledger.items()}


PREFIXO = ["mck"]  # setado no main; lista para o icp_manual enxergar sem passar argumento


def icp_manual():
    """ICP já classificado à mão nas rodadas anteriores, indexado por slug.

    O regex é só fallback para lead novo. Sem isto, rodar de novo apagaria a
    revisão manual (101 correções em 17/08).
    """
    manual = {}
    for nome in (f"{PREFIXO[0]}_conectados.csv", f"{PREFIXO[0]}_nao_conectados.csv"):
        caminho = os.path.join(HERE, nome)
        if not os.path.exists(caminho):
            continue
        for r in csv.DictReader(open(caminho, encoding="utf-8-sig")):
            if r.get("icp"):
                manual[urllib.parse.unquote(r["slug"]).lower()] = r["icp"]
    return manual


def main():
    global HERE
    ap = argparse.ArgumentParser(description="Triagem de ICP dos leads de um post.")
    ap.add_argument("--pasta", required=True, help="pasta signals/ do post")
    ap.add_argument("--prefixo", help="prefixo dos CSVs de saida (default: derivado da pasta)")
    ap.add_argument("--conexoes", help="export de conexoes (default: o mais recente na raiz)")
    args = ap.parse_args()
    HERE = os.path.abspath(args.pasta)
    prefixo = args.prefixo or os.path.basename(os.path.dirname(HERE)).split("-")[0]
    global CONEXOES
    CONEXOES = os.path.abspath(args.conexoes) if args.conexoes else conexoes_mais_recentes()
    print(f"conexoes: {os.path.basename(CONEXOES)} | pasta: {HERE} | prefixo: {prefixo}")

    conn = carregar_conexoes()
    scores = score_ledger()
    PREFIXO[0] = prefixo
    manual = icp_manual()
    novos = []

    out = []
    for l in csv.DictReader(open(os.path.join(HERE, "processed.csv"), encoding="utf-8")):
        s = urllib.parse.unquote(l["linkedin_identifier"]).lower()
        if s in EXCLUIR:
            continue
        c = conn.get(s)
        grau = CONECTADO_MANUAL.get(s)
        conectado = "sim" if (grau == 1 or (grau is None and c)) else "nao"
        cargo = (c or {}).get("Position", "").strip()
        headline = l["headline"].strip()
        out.append({
            "nome": l["name"],
            "slug": l["linkedin_identifier"],
        "conectado": conectado,
            "conectado_em": (c or {}).get("Connected On", ""),
            "empresa": (c or {}).get("Company", ""),
            "cargo": cargo,
            "headline": headline,
            "nivel": primeiro(NIVEL, (cargo or headline).lower(), "Outro"),
            "icp": manual.get(s) or icp_de(cargo, headline),
            "score": scores.get(s, ""),
            "posts_tocados": l.get("posts_tocados", ""),
            "contact_id": l["contact_id"],
            "status": l["status"],
        })
        if s not in manual:
            novos.append(out[-1])

    ordem = {n: i for i, (n, _) in enumerate(NIVEL)}
    out.sort(key=lambda r: (ordem.get(r["nivel"], 9), -(r["score"] or 0)))

    for nome, rows in (("conectados", [r for r in out if r["conectado"] == "sim"]),
                       ("nao_conectados", [r for r in out if r["conectado"] == "nao"])):
        caminho = os.path.join(HERE, f"{prefixo}_{nome}.csv")
        with open(caminho, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=out[0].keys())
            w.writeheader()
            w.writerows(rows)
        print(f"{nome}: {len(rows)}  {dict(Counter(r['icp'] for r in rows).most_common())}")
    print(f"\nleads NOVOS (icp por regex, precisa revisao manual): {len(novos)}")
    for r in novos:
        print(f"  {r['conectado']:<4} {r['icp']:<10} {r['slug'][:30]:<32} {(r['cargo'] or r['headline'])[:60]}")


def demo():
    for cargo, esperado in [("Product Manager", "Produto"),
                            ("Product Marketing Manager", "Marketing"),  # PMM não é Produto
                            ("Growth Product Manager", "Growth"),
                            ("Data Scientist", "Dados"),
                            ("Desenvolvedor Full Stack", "Tech"),
                            ("Analista Sr. de Vendas", "Vendas"),
                            ("Diretor Jurídico", "Fora")]:
        got = primeiro(ICP, cargo.lower(), "Fora")
        assert got == esperado, f"{cargo}: {got} != {esperado}"
    assert primeiro(NIVEL, "sócio consultor", "Outro") == "C-level"
    print("demo ok")


if __name__ == "__main__":
    demo()
    main()
