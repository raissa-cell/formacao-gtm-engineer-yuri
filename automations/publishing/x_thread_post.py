"""Posta uma thread encadeada no X via upload-post.com API.

Uso:
  python3 x_thread_post.py --thread-file thread.json [--dry-run]

Formato do thread.json (image opcional por tweet):
  [
    {"text": "Tweet 1 com imagem...", "image": "/caminho/infografico.png"},
    {"text": "Tweet 2 só texto..."},
    {"text": "Tweet 3..."}
  ]

⚠️ Threads NÃO agendam server-side (cada reply precisa do ID do tweet anterior).
Este script posta NA HORA em que roda — agendar = rodar o script na hora certa.

A chave UPLOAD_POST_API_KEY é carregada automaticamente do .env desta pasta.
"""

import argparse
import json
import mimetypes
import os
import sys
import time

import requests

PHOTO_URL = "https://api.upload-post.com/api/upload_photos"
TEXT_URL = "https://api.upload-post.com/api/upload_text"
STATUS_URL = "https://api.upload-post.com/api/uploadposts/status"
DEFAULT_USER = os.environ.get("UPLOAD_POST_USER", "")  # perfil criado no upload-post.com


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
    p = argparse.ArgumentParser(description="Posta uma thread no X a partir de um JSON.")
    p.add_argument("--thread-file", required=True,
                   help='JSON: [{"text": "...", "image": "opcional.png"}, ...]')
    p.add_argument("--user", default=DEFAULT_USER)
    p.add_argument("--dry-run", action="store_true", help="Valida o JSON e mostra a thread sem postar")
    return p.parse_args()


def load_thread(path):
    with open(path, encoding="utf-8") as fh:
        thread = json.load(fh)
    if not isinstance(thread, list) or not thread:
        sys.exit("thread.json deve ser uma lista não-vazia de objetos {text, image?}.")
    for i, tweet in enumerate(thread, 1):
        if not tweet.get("text"):
            sys.exit(f"Tweet {i} sem campo 'text'.")
        if len(tweet["text"]) > 280:
            sys.exit(f"Tweet {i} com {len(tweet['text'])} caracteres (máx 280).")
        image = tweet.get("image")
        if image and not os.path.exists(image):
            sys.exit(f"Tweet {i}: imagem não encontrada: {image}")
    return thread


def wait_for_result(request_id, headers, max_attempts=40, interval=5):
    for _ in range(max_attempts):
        r = requests.get(STATUS_URL, headers=headers, params={"request_id": request_id})
        r.raise_for_status()
        payload = r.json()
        if payload.get("status") == "completed":
            results = payload["results"]
            return results[0] if isinstance(results, list) else next(iter(results.values()))
        time.sleep(interval)
    sys.exit(f"Timeout esperando request_id={request_id} completar.")


def post_tweet(image_path, text, reply_to_id, user, headers):
    data = {
        "user": user,
        "platform[]": "x",
        "title": text,
    }
    if reply_to_id:
        data["reply_to_id"] = reply_to_id

    if image_path:
        mime = mimetypes.guess_type(image_path)[0] or "image/png"
        with open(image_path, "rb") as fh:
            files = [("photos[]", (os.path.basename(image_path), fh, mime))]
            response = requests.post(PHOTO_URL, headers=headers, data=data, files=files)
    else:
        response = requests.post(TEXT_URL, headers=headers, data=data)
    response.raise_for_status()
    payload = response.json()

    if "results" in payload:
        results = payload["results"]
        result = results[0] if isinstance(results, list) else next(iter(results.values()))
    elif "platform_post_id" in payload or "post_id" in payload:
        result = payload
    else:
        result = wait_for_result(payload["request_id"], headers)

    if not result.get("success"):
        sys.exit(f"Falha ao postar tweet: {result}")

    post_id = result.get("platform_post_id") or result.get("post_id")
    post_url = result.get("post_url") or result.get("url")
    return post_id, post_url


def main():
    load_env()
    args = parse_args()
    thread = load_thread(args.thread_file)

    if args.dry_run:
        for i, tweet in enumerate(thread, 1):
            img = f" [img: {tweet['image']}]" if tweet.get("image") else ""
            print(f"{i}/ ({len(tweet['text'])} chars){img}\n{tweet['text']}\n")
        return

    api_key = os.environ.get("UPLOAD_POST_API_KEY")
    if not api_key:
        sys.exit("UPLOAD_POST_API_KEY não encontrada (nem no ambiente, nem no .env desta pasta).")

    headers = {"Authorization": f"Apikey {api_key}"}

    reply_to_id = None
    for tweet in thread:
        post_id, post_url = post_tweet(tweet.get("image"), tweet["text"], reply_to_id, args.user, headers)
        print(f"Tweet postado: {post_id} {post_url or ''}")
        reply_to_id = post_id


if __name__ == "__main__":
    main()
