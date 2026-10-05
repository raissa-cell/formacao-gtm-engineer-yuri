"""Posta/agenda um post no LinkedIn via upload-post.com API (com imagem, documento ou só texto).

Uso:
  python3 linkedin_post.py --caption-file caption.txt --photo img.png \
      [--first-comment "..."] [--schedule 2026-07-08T13:07:00] [--dry-run]

  # post só texto (sem --photo):
  python3 linkedin_post.py --caption-file caption.txt \
      [--schedule 2026-07-29T08:25:00] [--timezone America/Sao_Paulo] [--dry-run]

  # post com documento/carrossel (PDF, PPT, DOC):
  python3 linkedin_post.py --caption-file caption.txt --document carrossel.pdf \
      [--schedule 2026-07-29T08:25:00] [--timezone America/Sao_Paulo] [--dry-run]

A chave UPLOAD_POST_API_KEY é carregada automaticamente do .env desta pasta.

⚠️ Sobre --schedule: internamente o script embute o offset de fuso direto no
scheduled_date (ex: "2026-07-29T08:25:00-03:00") via zoneinfo, porque o endpoint
de documento ignora silenciosamente um scheduled_date sem offset e PUBLICA NA
HORA em vez de agendar (sem erro na resposta -- incidente real em 2026-07-28).
O script também valida a resposta: se --schedule foi passado e a API não
confirmar com job_id/scheduled_date, o script aborta com erro em vez de deixar
passar um post publicado indevidamente.
"""

import argparse
import mimetypes
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import requests

PHOTO_URL = "https://api.upload-post.com/api/upload_photos"
TEXT_URL = "https://api.upload-post.com/api/upload_text"
DOCUMENT_URL = "https://api.upload-post.com/api/upload_document"
DEFAULT_USER = os.environ.get("UPLOAD_POST_USER", "")  # perfil criado no upload-post.com
DEFAULT_TIMEZONE = "Europe/Madrid"


def load_env():
    env_path = ""
    _dir = os.path.dirname(os.path.abspath(__file__))
    while _dir != os.path.dirname(_dir):
        if os.path.exists(os.path.join(_dir, ".env")):
            env_path = os.path.join(_dir, ".env")
            break
        _dir = os.path.dirname(_dir)
    if os.path.exists(env_path):
        with open(env_path) as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def parse_args():
    p = argparse.ArgumentParser(description="Posta/agenda imagem com legenda no LinkedIn.")
    caption = p.add_mutually_exclusive_group(required=True)
    caption.add_argument("--caption-file", help="Arquivo .txt/.md com a legenda completa")
    caption.add_argument("--caption", help="Legenda inline (pra textos curtos)")
    p.add_argument("--photo", action="append", default=None,
                   help="Caminho da imagem (repetir a flag pra múltiplas imagens). Omitir = post só texto.")
    p.add_argument("--document", default=None,
                   help="Caminho de um documento (PDF/PPT/PPTX/DOC/DOCX) — vira carrossel/viewer nativo do LinkedIn.")
    p.add_argument("--document-title", default=None,
                   help="Título curto do documento (obrigatório com --document; a legenda completa vai em 'description', não em 'title' — a API limita 'title' a poucos caracteres).")
    p.add_argument("--first-comment", default=None, help="Primeiro comentário (opcional)")
    p.add_argument("--first-comment-file", default=None, help="Arquivo com o primeiro comentário")
    p.add_argument("--schedule", default=None,
                   help="Agendamento ISO local, ex: 2026-07-08T13:07:00 (omitir = postar agora)")
    p.add_argument("--timezone", default=DEFAULT_TIMEZONE)
    p.add_argument("--user", default=DEFAULT_USER)
    p.add_argument("--dry-run", action="store_true", help="Mostra o payload sem postar")
    return p.parse_args()


def main():
    load_env()
    args = parse_args()

    api_key = os.environ.get("UPLOAD_POST_API_KEY")
    if not api_key:
        sys.exit("UPLOAD_POST_API_KEY não encontrada (nem no ambiente, nem no .env desta pasta).")

    caption = args.caption or open(args.caption_file, encoding="utf-8").read().strip()
    first_comment = args.first_comment
    if args.first_comment_file:
        first_comment = open(args.first_comment_file, encoding="utf-8").read().strip()

    for photo in (args.photo or []):
        if not os.path.exists(photo):
            sys.exit(f"Imagem não encontrada: {photo}")
    if args.document and not os.path.exists(args.document):
        sys.exit(f"Documento não encontrado: {args.document}")
    if args.document and args.photo:
        sys.exit("Use --photo OU --document, não os dois.")
    if args.document and not args.document_title:
        sys.exit("--document exige --document-title (título curto; a legenda completa vai em description).")

    data = {
        "user": args.user,
        "platform[]": "linkedin",
    }
    if args.document:
        data["title"] = args.document_title
        data["description"] = caption
    else:
        data["title"] = caption
    if first_comment:
        data["linkedin_first_comment"] = first_comment
    if args.schedule:
        # A API exige (ao menos pro endpoint de documento) um offset explícito no
        # próprio scheduled_date -- ex: "2026-07-29T08:25:00-03:00", não apenas o
        # campo "timezone" separado. Sem o offset embutido, o endpoint de
        # documento IGNORA o agendamento em silêncio e publica na hora, sem erro
        # (causou um post indevido em 2026-07-28). zoneinfo calcula o offset
        # certo pro fuso e data dados, já considerando horário de verão.
        naive_dt = datetime.fromisoformat(args.schedule)
        aware_dt = naive_dt.replace(tzinfo=ZoneInfo(args.timezone))
        data["scheduled_date"] = aware_dt.isoformat()
        data["timezone"] = args.timezone

    if args.dry_run:
        print({k: (v[:80] + "..." if isinstance(v, str) and len(v) > 80 else v) for k, v in data.items()})
        print("fotos:", args.photo or "(nenhuma)")
        print("documento:", args.document or "(nenhum)")
        return

    headers = {"Authorization": f"Apikey {api_key}"}

    if args.document:
        mime = mimetypes.guess_type(args.document)[0] or "application/pdf"
        with open(args.document, "rb") as fh:
            files = [("document", (os.path.basename(args.document), fh, mime))]
            response = requests.post(DOCUMENT_URL, headers=headers, data=data, files=files)
    elif args.photo:
        files = []
        handles = []
        for photo in args.photo:
            fh = open(photo, "rb")
            handles.append(fh)
            mime = mimetypes.guess_type(photo)[0] or "image/png"
            files.append(("photos[]", (os.path.basename(photo), fh, mime)))
        try:
            response = requests.post(PHOTO_URL, headers=headers, data=data, files=files)
        finally:
            for fh in handles:
                fh.close()
    else:
        response = requests.post(TEXT_URL, headers=headers, data=data)

    response.raise_for_status()
    payload = response.json()

    if "results" in payload:
        results = payload["results"]
        result = results[0] if isinstance(results, list) else next(iter(results.values()))
    else:
        result = payload

    if args.schedule and not (payload.get("job_id") or result.get("job_id") or payload.get("scheduled_date")):
        sys.exit(
            "ERRO DE SEGURANÇA: --schedule foi pedido mas a resposta da API não trouxe "
            f"job_id/scheduled_date -- isso indica que o post foi PUBLICADO NA HORA em vez de "
            f"agendado. Resposta completa: {payload}\n"
            "NÃO repita a chamada sem investigar -- pode estar publicando de novo."
        )

    print(result)
    return result


if __name__ == "__main__":
    main()
