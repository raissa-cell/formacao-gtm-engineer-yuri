"""Posta/agenda um vídeo (Reel) no Instagram via upload-post.com API.

Uso:
  python3 instagram_video_post.py --caption-file caption.txt --video clip.mp4 \
      [--first-comment "..."] [--schedule 2026-07-08T13:07:00] [--dry-run]

A chave UPLOAD_POST_API_KEY é carregada automaticamente do .env desta pasta.
"""

import argparse
import mimetypes
import os
import sys

import requests

API_URL = "https://api.upload-post.com/api/upload"
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
    p = argparse.ArgumentParser(description="Posta/agenda um vídeo (Reel) no Instagram.")
    caption = p.add_mutually_exclusive_group(required=True)
    caption.add_argument("--caption-file", help="Arquivo .txt/.md com a legenda completa")
    caption.add_argument("--caption", help="Legenda inline (pra textos curtos)")
    p.add_argument("--video", required=True, help="Caminho do arquivo de vídeo")
    p.add_argument("--first-comment", default=None, help="Primeiro comentário (opcional)")
    p.add_argument("--first-comment-file", default=None, help="Arquivo com o primeiro comentário")
    p.add_argument("--schedule", default=None,
                   help="Agendamento ISO local, ex: 2026-07-08T13:07:00 (omitir = postar agora)")
    p.add_argument("--timezone", default=DEFAULT_TIMEZONE)
    p.add_argument("--user", default=DEFAULT_USER)
    p.add_argument("--media-type", default=None, choices=["REELS", "STORIES"],
                   help="Instagram media_type (default da API: REELS)")
    p.add_argument("--dry-run", action="store_true", help="Mostra o payload sem postar")
    return p.parse_args()


def main():
    load_env()
    args = parse_args()

    api_key = os.environ.get("UPLOAD_POST_API_KEY")
    if not api_key:
        sys.exit("UPLOAD_POST_API_KEY não encontrada (nem no ambiente, nem no .env desta pasta).")

    if not os.path.exists(args.video):
        sys.exit(f"Vídeo não encontrado: {args.video}")

    caption = args.caption or open(args.caption_file, encoding="utf-8").read().strip()
    first_comment = args.first_comment
    if args.first_comment_file:
        first_comment = open(args.first_comment_file, encoding="utf-8").read().strip()

    data = {
        "user": args.user,
        "platform[]": "instagram",
        "title": caption,
    }
    if first_comment:
        data["first_comment"] = first_comment
    if args.media_type:
        data["media_type"] = args.media_type
    if args.schedule:
        data["scheduled_date"] = args.schedule
        data["timezone"] = args.timezone

    if args.dry_run:
        print({k: (v[:80] + "..." if isinstance(v, str) and len(v) > 80 else v) for k, v in data.items()})
        print("video:", args.video)
        return

    headers = {"Authorization": f"Apikey {api_key}"}
    mime = mimetypes.guess_type(args.video)[0] or "video/mp4"
    with open(args.video, "rb") as fh:
        files = [("video", (os.path.basename(args.video), fh, mime))]
        response = requests.post(API_URL, headers=headers, data=data, files=files)
    response.raise_for_status()
    payload = response.json()

    if "results" in payload:
        results = payload["results"]
        result = results[0] if isinstance(results, list) else next(iter(results.values()))
    else:
        result = payload

    print(result)
    return result


if __name__ == "__main__":
    main()
