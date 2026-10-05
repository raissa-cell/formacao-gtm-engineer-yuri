"""Extrai os posts mais engajados de LinkedIn e Instagram dos perfis em
`perfis.csv`, calcula a taxa de engajamento, extrai
transcript de vídeo (Instagram) e cria cards em 'ideias' no ClickUp.

Uso:
  python3 extract_top_posts.py [--days 7] [--top-ig 10] [--top-li 10] \
      [--skip-transcripts] [--skip-linkedin] [--skip-instagram] \
      [--tag "semana 2026-07-12"] [--dry-run]

APIFY_TOKEN e CLICKUP_API_TOKEN são carregados automaticamente do .env
desta pasta (crie o arquivo com essas duas chaves antes de rodar).
  - APIFY_TOKEN: console.apify.com > Settings > Integrations > API tokens
  - CLICKUP_API_TOKEN: clickup.com > perfil > Apps > API Token (pessoal)

Fórmula de engajamento (fixa por decisão do usuário, ver memory
engagement_rate_formula.md): (likes + comentários×3 + reposts×5) / (seguidores×100)
Instagram não expõe repost/share count publicamente, então reposts=0 nesse caso.

Sempre salva um relatório local em output/relatorio-<data>.json, mesmo em --dry-run.
"""

import argparse
import csv
import json
import os
import re
import sys
from datetime import date, timedelta

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PERFIS_PATH = os.path.join(SCRIPT_DIR, "perfis.csv")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")

CLICKUP_LIST_ID = os.environ.get("CLICKUP_LIST_ID", "")
CLICKUP_STATUS = "ideas"
CUSTOM_FIELD_POST_REFERENCIA = os.environ.get("CLICKUP_FIELD_POST_REFERENCIA", "")
CUSTOM_FIELD_LINK_REFERENCIA = os.environ.get("CLICKUP_FIELD_LINK_REFERENCIA", "")

ACTOR_LINKEDIN_POSTS = "harvestapi/linkedin-profile-posts"
ACTOR_LINKEDIN_PROFILE = "harvestapi/linkedin-profile-scraper"
ACTOR_INSTAGRAM_POSTS = "instagram-scraper/instagram-profile-posts-scraper"
ACTOR_INSTAGRAM_TRANSCRIPT = "apple_yang/instagram-transcripts-scraper"

APIFY_BASE = "https://api.apify.com/v2"
CLICKUP_BASE = "https://api.clickup.com/api/v2"


def load_env():
    env_path = ""
    _dir = SCRIPT_DIR
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
    p = argparse.ArgumentParser(description="Extrai top posts de IA (LinkedIn+Instagram) e cria cards no ClickUp.")
    p.add_argument("--days", type=int, default=7, help="Janela de dias pra trás (default: 7)")
    p.add_argument("--top-ig", type=int, default=10, help="Quantos posts do Instagram no ranking (default: 10)")
    p.add_argument("--top-li", type=int, default=10, help="Quantos posts do LinkedIn no ranking (default: 10)")
    p.add_argument("--li-max-posts-per-profile", type=int, default=25)
    p.add_argument("--ig-max-posts-per-profile", type=int, default=15)
    p.add_argument("--skip-transcripts", action="store_true", help="Não extrai transcript de vídeo do Instagram")
    p.add_argument("--skip-linkedin", action="store_true", help="Roda só o Instagram")
    p.add_argument("--skip-instagram", action="store_true", help="Roda só o LinkedIn")
    p.add_argument("--list-id", default=CLICKUP_LIST_ID, help="ClickUp list_id (default: CLICKUP_LIST_ID do .env)")
    p.add_argument("--tag", default=None, help='Tag pra aplicar nos cards, ex: "semana 2026-07-12"')
    p.add_argument("--dry-run", action="store_true", help="Não cria cards no ClickUp, só salva o relatório local")
    return p.parse_args()


def load_profiles(path=PERFIS_PATH):
    """Lê `perfis.csv` (colunas: Nome, Rede, Link do perfil; Rede = IG ou LKN)."""
    li_slugs, seen_li = [], set()
    ig_usernames, seen_ig = [], set()

    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            rede = (row.get("Rede") or "").strip().upper()
            link = (row.get("Link do perfil") or "").strip()
            if not link:
                continue

            if rede == "LKN":
                m = re.search(r"linkedin\.com/in/([A-Za-z0-9\-_]+)", link)
                if m and m.group(1) not in seen_li:
                    seen_li.add(m.group(1))
                    li_slugs.append(m.group(1))
            elif rede == "IG":
                m = re.search(r"instagram\.com/([A-Za-z0-9_.]+)", link)
                if m and m.group(1) not in seen_ig:
                    seen_ig.add(m.group(1))
                    ig_usernames.append(m.group(1))

    return {
        "linkedin": [f"https://www.linkedin.com/in/{slug}/" for slug in li_slugs],
        "linkedin_slugs": li_slugs,
        "instagram": ig_usernames,
    }


def run_actor_sync(actor_slug, run_input, token, timeout=280):
    url = f"{APIFY_BASE}/acts/{actor_slug.replace('/', '~')}/run-sync-get-dataset-items"
    resp = requests.post(url, params={"token": token}, json=run_input, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def score(likes, comments, reposts, followers):
    if not followers:
        return 0.0
    return ((likes + comments * 3 + reposts * 5) * 100 / followers)


def scrape_linkedin(profiles, days, max_posts, token):
    posted_limit_date = (date.today() - timedelta(days=days)).isoformat()
    posts = run_actor_sync(ACTOR_LINKEDIN_POSTS, {
        "targetUrls": profiles["linkedin"],
        "maxPosts": max_posts,
        "postedLimitDate": posted_limit_date,
        "includeQuotePosts": True,
        "includeReposts": True,
        "scrapeReactions": False,
        "scrapeComments": False,
    }, token)

    profile_details = run_actor_sync(ACTOR_LINKEDIN_PROFILE, {
        "profileScraperMode": "Profile details no email ($4 per 1k)",
        "urls": profiles["linkedin"],
    }, token)
    followers_by_slug = {item["publicIdentifier"]: item.get("followerCount", 0) for item in profile_details}

    tracked_slugs = set(profiles["linkedin_slugs"])
    ranked = []
    seen_urls = set()
    for post in posts:
        author = post.get("author") or {}
        slug = author.get("publicIdentifier")
        url = post.get("linkedinUrl")
        if not slug or slug not in tracked_slugs or not url or url in seen_urls:
            continue
        seen_urls.add(url)
        followers = followers_by_slug.get(slug)
        if not followers:
            continue
        engagement = post.get("engagement") or {}
        likes = engagement.get("likes", 0) or 0
        comments = engagement.get("comments", 0) or 0
        shares = engagement.get("shares", 0) or 0
        ranked.append({
            "platform": "LinkedIn",
            "author": author.get("name", slug),
            "author_handle": slug,
            "url": url,
            "text": post.get("content", ""),
            "likes": likes,
            "comments": comments,
            "reposts": shares,
            "followers": followers,
            "date": (post.get("postedAt") or {}).get("date"),
            "is_video": bool(post.get("postVideo")),
            "score": score(likes, comments, shares, followers),
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


def scrape_instagram(profiles, days, posts_per_profile, token):
    recent = (date.today() - timedelta(days=days)).isoformat()
    posts = run_actor_sync(ACTOR_INSTAGRAM_POSTS, {
        "instagramUsernames": profiles["instagram"],
        "postsPerProfile": posts_per_profile,
        "recent": recent,
    }, token)

    tracked = set(u.lower() for u in profiles["instagram"])
    ranked = []
    seen_codes = set()
    for post in posts:
        owner = post.get("owner") or {}
        username = (owner.get("username") or "").lower()
        shortcode = post.get("shortcode")
        likes = post.get("like_count", 0)
        if username not in tracked or not shortcode or shortcode in seen_codes or likes is None or likes < 0:
            continue
        seen_codes.add(shortcode)
        followers = owner.get("followers")
        if not followers:
            continue
        comments = post.get("comment_count", 0) or 0
        ranked.append({
            "platform": "Instagram",
            "author": owner.get("username"),
            "author_handle": owner.get("username"),
            "url": post.get("url"),
            "text": post.get("caption", ""),
            "likes": likes,
            "comments": comments,
            "reposts": 0,
            "followers": followers,
            "date": post.get("taken_at"),
            "is_video": bool(post.get("is_video")),
            "score": score(likes, comments, 0, followers),
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


def extract_ig_transcripts(posts, token):
    video_urls = [p["url"] for p in posts if p.get("is_video") and p.get("url")]
    if not video_urls:
        return {}
    items = run_actor_sync(ACTOR_INSTAGRAM_TRANSCRIPT, {"bulkUrls": video_urls}, token)
    return {item["code"]: item.get("text", "") for item in items if item.get("code")}


def make_title(rank, post):
    snippet = " ".join(post["text"].split())[:90].rstrip()
    if len(post["text"]) > 90:
        snippet += "…"
    label = f"@{post['author_handle']}" if post["platform"] == "Instagram" else post["author"]
    prefix = f"[{post['platform']} #{rank}]"
    return f"{prefix} {label}: {snippet}" if snippet else f"{prefix} {label}"


def build_description(post, transcript=None):
    lines = [
        f"**Plataforma:** {post['platform']}",
        f"**Autor:** {post['author']} ({post['followers']:,} seguidores)".replace(",", "."),
        f"**Link:** {post['url']}",
        f"**Métricas:** {post['likes']} likes · {post['comments']} comentários"
        + (f" · {post['reposts']} reposts" if post["platform"] == "LinkedIn" else ""),
        f"**Score de engajamento:** {post['score']:.4f}",
        f"**Data:** {post['date']}",
        "",
        "**Texto/legenda completa:**",
        post["text"] or "(vazio)",
    ]
    if transcript is not None:
        lines += ["", "**Transcript completo (áudio):**", transcript or "(sem fala detectável)"]
    return "\n".join(lines)


def create_clickup_card(post, rank, transcript, list_id, tag, token):
    payload = {
        "name": make_title(rank, post),
        "markdown_description": build_description(post, transcript),
        "status": CLICKUP_STATUS,
        "custom_fields": [
            {"id": CUSTOM_FIELD_POST_REFERENCIA, "value": build_description(post, transcript)[:3000]},
            {"id": CUSTOM_FIELD_LINK_REFERENCIA, "value": post["url"]},
        ],
    }
    if tag:
        payload["tags"] = [tag]

    resp = requests.post(
        f"{CLICKUP_BASE}/list/{list_id}/task",
        headers={"Authorization": token, "Content-Type": "application/json"},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def main():
    load_env()
    args = parse_args()

    apify_token = os.environ.get("APIFY_API_KEY")
    if not apify_token:
        sys.exit("APIFY_API_KEY não encontrada (nem no ambiente, nem no .env do pilar).")
    clickup_token = None
    if not args.dry_run:
        clickup_token = os.environ.get("CLICKUP_API_TOKEN")
        if not clickup_token:
            sys.exit("CLICKUP_API_TOKEN não encontrada (nem no ambiente, nem no .env desta pasta). Use --dry-run pra rodar sem ClickUp.")

    profiles = load_profiles()
    print(f"Perfis carregados: {len(profiles['linkedin'])} LinkedIn, {len(profiles['instagram'])} Instagram")

    top_li, top_ig = [], []

    if not args.skip_linkedin:
        print(f"Raspando LinkedIn (últimos {args.days} dias)...")
        li_ranked = scrape_linkedin(profiles, args.days, args.li_max_posts_per_profile, apify_token)
        top_li = li_ranked[: args.top_li]
        print(f"  {len(li_ranked)} posts válidos, top {len(top_li)} selecionados")

    if not args.skip_instagram:
        print(f"Raspando Instagram (últimos {args.days} dias)...")
        ig_ranked = scrape_instagram(profiles, args.days, args.ig_max_posts_per_profile, apify_token)
        top_ig = ig_ranked[: args.top_ig]
        print(f"  {len(ig_ranked)} posts válidos, top {len(top_ig)} selecionados")

    transcripts = {}
    if top_ig and not args.skip_transcripts:
        print("Extraindo transcript de vídeo dos posts do Instagram...")
        transcripts = extract_ig_transcripts(top_ig, apify_token)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    report_path = os.path.join(OUTPUT_DIR, f"relatorio-{date.today().isoformat()}.json")
    with open(report_path, "w", encoding="utf-8") as fh:
        json.dump({"top_linkedin": top_li, "top_instagram": top_ig, "transcripts": transcripts}, fh, ensure_ascii=False, indent=2)
    print(f"Relatório salvo em {report_path}")

    if args.dry_run:
        print("[dry-run] Nenhum card criado no ClickUp.")
        return

    print(f"Criando cards em '{CLICKUP_STATUS}' na list {args.list_id}...")
    for rank, post in enumerate(top_li, 1):
        result = create_clickup_card(post, rank, None, args.list_id, args.tag, clickup_token)
        print(f"  LinkedIn #{rank}: {result.get('url')}")
    for rank, post in enumerate(top_ig, 1):
        transcript = transcripts.get(post["url"].rstrip("/").rsplit("/", 1)[-1]) if post.get("is_video") else None
        result = create_clickup_card(post, rank, transcript if post.get("is_video") else None, args.list_id, args.tag, clickup_token)
        print(f"  Instagram #{rank}: {result.get('url')}")


if __name__ == "__main__":
    main()
