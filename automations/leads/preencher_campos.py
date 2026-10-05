"""Grava na Nuvia os campos do lead a partir dos CSVs da triagem de ICP.

Padrão de TODO lead: depois de `triagem_icp.py`, rodar isto. Sem ele o contato fica só
com nome e slug, porque `POST /contacts` NÃO persiste `job_title` (só PUT depois de criado).

De-para (runbook-segmentacao.md):
    nome     -> name                 (nativo)
    slug     -> linkedin_identifier  (nativo)
    headline -> job_title            (nativo)
    cargo    -> cargo-do-lead        (custom de contato)
    icp      -> icp                  (custom de contato)
    score    -> engagement-score     (mantido pelo score_engagement.py, NÃO tocar)
    —        -> post-interacao       (acumula, NÃO sobrescrever)

Escrita de campo custom é por SLUG e a leitura volta por TÍTULO (grava `icp`, lê `ICP`;
grava `cargo-do-lead`, lê `Cargo do lead`), então as duas grafias são limpas antes do PUT.

Uso:
  python3 preencher_campos.py --csv "<pasta>/hum_conectados.csv" [--csv outro.csv] [--dry-run]
"""

import argparse
import csv
import os
import sys

sys.path.insert(0, os.path.expanduser("~/gtm-automation"))
import collect_to_nuvia as base  # noqa: E402

# grafia de slug (escrita) e de título (leitura) do mesmo campo
DUPLAS = {"icp": ("icp", "ICP"), "cargo-do-lead": ("cargo-do-lead", "Cargo do lead")}
# nunca tocados aqui: mantidos por score_engagement.py
PRESERVAR = ("post-interacao", "engagement-score", "engagement_score")


def preencher(nuvia, linha, dry_run=False):
    cid = (linha.get("contact_id") or "").strip()
    if not cid:
        return "sem contact_id"
    atual = base._unwrap(nuvia._req("GET", f"/contacts/{cid}"))
    attrs = {k: (v.get("value") if isinstance(v, dict) else v)
             for k, v in (atual.get("additional_attributes") or {}).items()}

    headline = (linha.get("headline") or "").strip()
    cargo = (linha.get("cargo") or "").strip() or headline
    icp = (linha.get("icp") or "").strip()

    ja_ok = (atual.get("job_title") or "") == headline and \
            attrs.get("ICP", attrs.get("icp")) == icp and \
            attrs.get("Cargo do lead", attrs.get("cargo-do-lead")) == cargo
    if ja_ok:
        return "ok"
    if dry_run:
        return f"atualizaria job_title={headline[:35]!r} icp={icp}"

    for slug, (grava, le) in DUPLAS.items():
        attrs.pop(grava, None)
        attrs.pop(le, None)
    attrs["icp"] = icp
    attrs["cargo-do-lead"] = cargo

    payload = {k: atual[k] for k in nuvia.WRITABLE if atual.get(k) is not None}
    if headline:
        payload["job_title"] = headline
    payload["additional_attributes"] = attrs
    nuvia._req("PUT", f"/contacts/{cid}", payload)
    return "gravado"


def main():
    ap = argparse.ArgumentParser(description="Preenche os campos do lead na Nuvia.")
    ap.add_argument("--csv", action="append", required=True, help="CSV da triagem (repetir a flag)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    base.load_env()
    nuvia = base.Nuvia(os.environ["NUVIA_API_KEY"])
    contagem = {}
    for caminho in args.csv:
        linhas = list(csv.DictReader(open(caminho, encoding="utf-8-sig")))
        print(f"{os.path.basename(caminho)}: {len(linhas)} linhas")
        for l in linhas:
            try:
                r = preencher(nuvia, l, args.dry_run)
            except Exception as e:
                r = f"erro: {e}"
            contagem[r.split(":")[0]] = contagem.get(r.split(":")[0], 0) + 1
            if r.startswith("erro"):
                print(f"  ! {l.get('slug')}: {r}")
    print("resultado:", contagem)


if __name__ == "__main__":
    main()
