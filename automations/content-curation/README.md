# Content-Curation — extract_top_posts.py

Automatiza a rotina de curadoria de conteúdo: puxa os posts recentes dos perfis
de referência em [`perfis.csv`](perfis.csv), calcula taxa de
engajamento, seleciona o top N de cada plataforma, extrai transcript de vídeo
(Instagram) e cria os cards em `ideias` no ClickUp — tudo numa rodada.

## Setup (uma vez)

Crie `.env` nesta pasta (mesmo padrão do `Publishing/.env`) com:

```
APIFY_API_KEY=apify_api_xxxxxxxx
CLICKUP_API_TOKEN=pk_xxxxxxxx
CLICKUP_LIST_ID=
CLICKUP_FIELD_POST_REFERENCIA=
CLICKUP_FIELD_LINK_REFERENCIA=
```

- `APIFY_API_KEY`: console.apify.com → Settings → Integrations → API tokens
- `CLICKUP_API_TOKEN`: clickup.com → ícone do perfil → Apps → API Token (pessoal)

## Uso

```bash
# Rotina padrão: top 10 LinkedIn + top 10 Instagram, últimos 7 dias, cria cards
python3 extract_top_posts.py

# Testar sem criar nada no ClickUp (só gera o relatório local em output/)
python3 extract_top_posts.py --dry-run

# Ajustar janela e quantidade
python3 extract_top_posts.py --days 14 --top-ig 15 --top-li 5

# Aplicar uma tag nos cards criados (crie a tag no ClickUp antes se ela usar
# caracteres como "/" — nomes com "-" costumam funcionar direto na criação)
python3 extract_top_posts.py --tag "semana 2026-07-12"

# Pular transcript de vídeo (mais rápido/barato) ou uma das plataformas
python3 extract_top_posts.py --skip-transcripts
python3 extract_top_posts.py --skip-linkedin
python3 extract_top_posts.py --skip-instagram
```

## O que o script faz

1. Lê os perfis de `perfis.csv` (colunas `Nome`, `Rede` [IG/LKN], `Link do perfil`),
   deduplicando por handle — se dois nomes na lista apontarem pro mesmo perfil,
   só conta uma vez.
2. Roda os Apify Actors:
   - `harvestapi/linkedin-profile-posts` (posts) + `harvestapi/linkedin-profile-scraper` (seguidores)
   - `instagram-scraper/instagram-profile-posts-scraper` (posts + seguidores já inclusos)
   - `apple_yang/instagram-transcripts-scraper` (transcript de áudio dos vídeos do top Instagram)
3. Calcula `(likes + comentários×3 + reposts×5) / (seguidores×100)` por post
   (fórmula fixa do usuário — não é a fórmula genérica de mercado).
4. Ranqueia **cada plataforma separadamente** e pega o top N de cada uma.
5. Cria um card por post em `ideias` na list `{{CLICKUP_LIST_ID}}`, preenchendo
   nome, descrição completa (métricas + texto/legenda + transcript) e os
   campos `Post de referência` / `Link da referência`.
6. Sempre salva uma cópia local em `output/relatorio-<data>.json`, mesmo
   com `--dry-run` — útil pra auditar antes de mexer no ClickUp.

## Limitações conhecidas

- **Títulos são mecânicos** (plataforma + autor + início do texto), não têm o
  mesmo refinamento de um título escrito à mão. Vale revisar/repolir os
  títulos dos cards novos antes de mover pra `research`.
- **Instagram não expõe reposts/shares publicamente** — o score do Instagram
  usa só likes+comentários (reposts=0 sempre nesse caso).
- **Posts com curtidas ocultas** (perfil desativou contagem pública) são
  descartados do ranking do Instagram, não têm como comparar de forma justa.
- Só reposts/compartilhamentos do LinkedIn feitos pelos próprios perfis
  rastreados entram no ranking — reposts de terceiros que aparecem no feed
  de alguém da lista são ignorados pra não misturar autoria.
- Tags no ClickUp: passar `--tag` inclui a tag direto no payload de criação
  do card (a API do ClickUp cria a tag na hora se ela ainda não existir).
