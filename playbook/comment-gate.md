# Comment-gate: o fluxo padrão de todo post com material

O post promete um material para quem comentar uma palavra-gatilho. A automação transforma cada comentário em contato, entrega o material por DM e pontua o engajamento.

## Checklist por post (8 passos)
Detalhe completo em `automations/comment-to-dm/README.md`. Resumo:
1. Escolher palavra-gatilho e material (um CTA só no post).
2. Escrever as 3 DMs a partir de `automations/comment-to-dm/mensagens-modelo.md`.
3. Criar `nuvia.config.json` na pasta do post (gatilho, URL, `campaign_id`, tag, data).
4. Registrar o post em `automations/comment-to-dm/active_posts.json`.
5. Copiar scripts e config para `~/gtm-automation` e armar o launchd (ver `automations/runtime/README.md`).
6. Rodar `--dry-run` antes da primeira rodada real.
7. Resumo diário por cron.
8. Triar ICP dos leads (`automations/leads/triagem_icp.py`) antes de qualquer campanha de outbound.

Ao agendar qualquer post, SEMPRE pergunte: "é comment-gate?"
