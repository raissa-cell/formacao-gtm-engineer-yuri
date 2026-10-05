"""Mantém os monitores de AutoDM do upload-post.com vivos.

A Upload Post documenta os monitores como "background 24/7", mas na prática
a thread que roda o polling pode morrer (status vira "resuming": "no live
thread; one was just started"). Sem uma chamada externa periódica, comentários
ficam sem resposta por horas. Este script faz essa chamada de fato a cada
intervalo, sem depender de ninguém estar com o Claude Code aberto.

Uso: python3 ping_autodm_monitors.py
"""

import datetime
import os
import sys

import requests

STATUS_URL = "https://api.upload-post.com/api/uploadposts/autodms/status"
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "autodm_keepalive.log")


def load_env():
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path) as fh:
            for line in fh:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def log(msg):
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(LOG_PATH, "a") as fh:
        fh.write(f"{ts}Z {msg}\n")


def main():
    load_env()
    api_key = os.environ.get("UPLOAD_POST_API_KEY")
    if not api_key:
        log("ERRO: UPLOAD_POST_API_KEY não encontrada no .env")
        sys.exit(1)

    try:
        r = requests.get(
            STATUS_URL,
            params={"include_inactive": "false"},
            headers={"Authorization": f"Apikey {api_key}"},
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
    except Exception as exc:
        log(f"ERRO na chamada: {exc}")
        sys.exit(1)

    monitors = data.get("monitors", [])
    if not monitors:
        log("ok, nenhum monitor ativo")
        return

    for m in monitors:
        stats = m.get("stats", {})
        log(
            f"monitor={m.get('monitor_id')} status={m.get('status')} "
            f"post={m.get('post_url')} total_comments={stats.get('total_comments')} "
            f"successful_replies={stats.get('successful_replies')} "
            f"failed_replies={stats.get('failed_replies')} last_check={m.get('last_check')}"
        )


if __name__ == "__main__":
    main()
