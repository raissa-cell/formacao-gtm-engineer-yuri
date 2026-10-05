# Automação comment-to-dm

**Regra:** quem interage com um post comment-gate vira lead pontuado na Nuvia. Quem comenta a palavra-gatilho também recebe a sequência de DM com o material rico.

Duas coisas acontecem por rodada, e elas são independentes:

| Etapa | O que faz | Quem entra |
|---|---|---|
| **enroll** (`collect_to_nuvia.py`) | cria contato e enrolla na campanha de DM | só quem comentou a palavra-gatilho |
| **score** (`score_engagement.py`) | registra o sinal no ledger e grava `engagement_score` + `post-interacao` | todo mundo: gatilho, comentário sem gatilho e like |

## ⚠️ O runtime NÃO roda a partir do Desktop

O macOS (TCC) bloqueia qualquer acesso do launchd a `~/Desktop`. Um agente apontado pra cá falha com `exit 126` / `Operation not permitted`, **sem erro visível no log do projeto** — descoberto em 12/08/2026 depois de 9 disparos silenciosamente falhos e 5h sem coleta.

Por isso o runtime vive em **`~/gtm-automation/`**: scripts, `.env`, `engagement_ledger.json`, configs, `rounds.log` e `processed_*.csv`. Esta pasta do projeto guarda a **fonte editável** e as cópias de registro; o espelho de volta é feito pelo resumo horário do Claude Code, que tem a permissão que o launchd não tem.

Ao mexer num script aqui, **copiar pra `~/gtm-automation/`** ou a mudança não entra em produção.

## Checklist de um post novo comment-gate

1. **Mensagens**: escrever a sequência de 3 DMs a partir de `mensagens-modelo.md` (anatomia canônica + filtro pré-envio). Registrar o texto final em `<pasta do post>/signals/nuvia-campanha.md`.
2. **Material rico**: página no Notion, link público.
3. **Agendar o post** e guardar o `job_id`. Depois de publicar, resolver a URL via `GET /api/uploadposts/status?job_id=`.
4. **o usuário cria a campanha na UI da Nuvia** (canal LinkedIn, sem connection request, stop-on-reply) e passa o `campaign_id`.
5. **`nuvia.config.json` na pasta do post:**
   ```json
   {
     "post_id": "...", "post_url": "...", "trigger_word": "humano",
     "author_slug": "{{SEU_LINKEDIN_SLUG}}",
     "apify_actor": "harvestapi/linkedin-post-comments",
     "max_items": 500, "processed_csv": "signals/processed.csv",
     "default_date": "AAAA-MM-DD",
     "route_conversation": false,
     "nuvia": { "campaign_id": "...", "custom_field_slug": "post-interacao",
                "custom_field_value": "post_<slug_do_post>" }
   }
   ```
   - `default_date` = data de publicação do post. Reações não trazem timestamp; sem isso a interação seria datada da rodada. Dá pra extrair do ID de atividade do LinkedIn: `datetime.fromtimestamp((id >> 22)/1000)`.
   - `route_conversation: false` quando a entrega é por campanha. `true` só se o post também tiver que rotear conversa pra agente/etapa (aí exige `inbox_id`, `agent_id`, `step_id`).
6. **Copiar o config pra `~/gtm-automation/`** com `processed_csv` apontando pra lá, e apontar o plist do launchd (`~/Library/LaunchAgents/com.exemplo.comment-to-dm.<post>.plist`, `StartInterval` 1800, argumentos = caminho do config + `desativar_em`).
7. **Registrar o post em `active_posts.json`** (post_url, t0, desativar_em = t0+48h, palavra-gatilho, material, ids de lista e campanha).
8. **Armar o resumo horário** (CronCreate na sessão do Claude Code): lê o log, marca as flags semânticas, espelha o ledger de volta e reporta. Cron é session-bound: se o Claude Code fechar, só o resumo para; o launchd continua.

## Triagem de ICP (obrigatória antes de virar campanha)

Coletar e enrollar entrega o material. **Transformar esses leads em campanha de outbound passa antes pela triagem de ICP**, que é padrão de todo lead do projeto:

```bash
python3 "automations/leads/triagem_icp.py" --pasta "campaigns/<publico>/conteudo/AAAA-MM/<post>/signals" --prefixo <xxx>
```

Ela cruza o `processed.csv` com o export de conexões do LinkedIn e classifica ICP (Growth, Produto, Dados, Tech, Vendas, Marketing, Fora) + nível hierárquico, puxando o `engagement_score` do ledger. Separa conectados de não conectados, porque a sequência de DM é diferente nos dois casos. Vocabulário, exclusões fixas e a pegadinha da revisão manual estão em `automations/leads/README.md`.

## Modelo de engagement_score

Ledger global: `engagement_ledger.json` (fonte de verdade; a Nuvia é espelho). Uma entrada por lead, sinais por post, com a data do primeiro avistamento, que nunca é sobrescrita:

```json
"maxribeiro": {
  "contact_id": "...", "name": "Max Ribeiro",
  "posts": { "post_humanize_ptbr": { "gatilho": "2026-08-12", "like": "2026-08-12" } },
  "flags": { "conversou": false, "comunidade": false, "formacao": false }
}
```

Pesos em `weights.json` (mudar lá reprecifica todo mundo na rodada seguinte, sem tocar em código):

| Sinal | Peso | Escopo |
|---|---|---|
| formacao | 50 | uma vez por lead |
| comunidade | 15 | uma vez por lead |
| conversou | 10 | uma vez por lead |
| comentou (sem gatilho) | 5 | uma vez por post |
| gatilho | 3 | uma vez por post |
| like | 1 | uma vez por post |

- `gatilho` e `comentou` são **exclusivos no mesmo post**: quem comentou a palavra leva 3, não 3+5.
- O score é **recalculado do zero** a cada rodada somando o ledger inteiro. Isso é o oposto de substituir: preserva o histórico e torna a rodada idempotente.
- As 3 flags exigem leitura de conversa, então só o Claude Code marca, via `python3 score_engagement.py --set-flag <slug>:<flag> --push`. **Só marcar pelo que a pessoa escreveu.** "Vou entrar na comunidade" é intenção, não entrada.
- Lead que só curtiu **também vira contato** (decisão do usuário, 12/08).
- Selftest da lógica: `python3 score_engagement.py --selftest`.

## Coleta: atores e custo

- Comentários: `harvestapi/linkedin-post-comments`, ~$0.002/comentário.
- Reações: `harvestapi/linkedin-post-reactions` **com `profileScraperMode: "main"`** (~$0.004/reação). O modo `short` devolve só o URN opaco (`ACoAA...`), que não casa com o slug dos comentários e **duplica a pessoa** — causou 7 contatos duplicados em 12/08. O modo `main` traz `publicIdentifier`, headline, localização e seguidores.
- Cada rodada raspa o post inteiro, então o custo cresce com o volume. A 30 min por 48h, algo entre $3 e $6/dia num post que performa.

## Backfill de posts antigos

`python3 score_engagement.py --config <config do post antigo>` com `default_date` = data do post. Pontua sem enrollar ninguém (enroll é o outro script). Feito em 12/08 pros 3 posts de julho: 329 leads por ~$1.

## Enrollment

Bulk enroll manual dos leads novos de cada rodada, direto na mesma campanha, via `contact_ids`. **Sem lotes e sem lista nova por rodada** — o modelo de lotes de julho está superado, era necessário quando o enrollment dependia do snapshot da lista.

- Quem **já existe** no CRM também é enrollado (o contato não é editado; enroll usa só o id). Antes de 12/08 esses leads caíam em `pending_existing.json` e ficavam sem material.
- A lista da Nuvia é registro, não mecanismo de envio.

## Modo sob demanda (padrão depois da janela)

Passada a janela de 48h/50h, o post sai do agendamento e a coleta vira manual. `run_round.sh` sem o segundo argumento não tem prazo e sempre executa:

```bash
~/gtm-automation/run_round.sh ~/gtm-automation/nuvia.<post>.config.json
```

Depois de rodar, espelhar ledger/CSV/log de volta pra pasta do post. Nada mais precisa estar ligado: launchd descarregado e cron de resumo apagado.

## Cadência agendada (durante a janela)

`StartInterval` de 1800s (30 min) durante as 48h. O launchd **não perde** a janela quando a máquina dorme: agrupa os disparos e roda uma vez ao acordar. Pra cadência garantida: `nohup caffeinate -dimsu -t 165600 >/dev/null 2>&1 &`.

Encerrar ao fim da janela: `launchctl unload ~/Library/LaunchAgents/com.exemplo.comment-to-dm.<post>.plist` + `CronDelete` do resumo.

## Instagram (não mudou)

- **Instagram**: ler comentários ✅ · private reply ✅ · DM direta ✅ · AutoDM ✅ (server-side, checa a cada 15 min)
- **LinkedIn na upload-post**: só publicação/agendamento. Endpoints de leitura/DM retornam `Platform 'linkedin' not supported`.
- Resposta pública ao comentário no LinkedIn não tem API: é manual, e é alcance, não cortesia.

## Política não-conectado (LinkedIn)

- o usuário NUNCA envia convite de conexão. A pessoa é quem manda.
- Não conectado → responder o comentário publicamente (V4) pedindo conexão. Status `aguardando_conexao`.
- Conectou → DM. Não conectou em 7 dias → `expirado`, sem segunda cobrança.

## Textos base

> **Sequência de DM (3 mensagens): usar `mensagens-modelo.md` desta pasta.** Anatomia canônica, com as regras de escrita e o filtro pré-envio. Carregar antes de escrever a sequência de qualquer post novo.

Respostas de comentário público (exemplos, randomizar V1-V3 e adaptar à sua voz):
- V1: "Enviado! Confere aí no privado."
- V2: "Tá no seu inbox. Qualquer dúvida na implementação, me chama lá."
- V3: "Mandei no privado! Me conta depois o que você achou da estrutura."
- V4 (não conectado): "Vi seu {{PALAVRA}}! Como a gente ainda não está conectado, o LinkedIn não me deixa te chamar no privado. Me manda um convite de conexão que o material chega na hora."

## Qualidade de dado

- **Dedup por `linkedin_identifier`**, nunca por nome: a busca da Nuvia é sensível a acento ("Fabrizio" ≠ "Fabrízio").
- Relação anterior fora do CRM (DM manual, WhatsApp) é invisível pro dedup: a Nuvia não sincroniza histórico do LinkedIn. Contato que você já conhece pode entrar como lead novo sem erro nenhum do fluxo.
- **Seu próprio perfil (`{{SEU_LINKEDIN_SLUG}}`) nunca entra na coleta.**
- Todo contato leva nome, `linkedin_identifier` e `job_title` (headline, vem de graça no `actor.position`). Telefone-sentinela `9990000XX` com checagem de livre na base antes.
- Escrita de `additional_attributes` por REST é **PUT com round-trip** (GET → altera → PUT com todos os campos). Não existe PATCH; PUT sem os campos apaga o que faltar.

## Arquivos

| Arquivo | Onde | O quê |
|---|---|---|
| `collect_to_nuvia.py` | aqui + `~/gtm-automation` | coleta comentários → contato → enroll |
| `score_engagement.py` | aqui + `~/gtm-automation` | comentários + likes → ledger → score |
| `weights.json` | aqui + `~/gtm-automation` | pesos do score |
| `engagement_ledger.json` | `~/gtm-automation` (vivo), cópia local opcional | sinais crus por lead |
| `run_round.sh` | `~/gtm-automation` | uma rodada (enroll + score) |
| `mensagens-modelo.md` | aqui | anatomia das 3 DMs |
| `active_posts.json` | aqui | posts com automação ativa |
| `rounds.log`, `processed.csv` | `~/gtm-automation` (vivo), cópia em `<post>/signals/` | histórico da execução |

## Pendências

- [ ] Runner genérico: hoje é um plist por post. O natural é um `run_all.sh` varrendo `~/gtm-automation/active/*.config.json`, e aí post novo = soltar um arquivo.
- [ ] 4 slugs com encoding de URL no ledger (`michel-gon%c3%a7alves-...`): perfis com acento em que o ator devolveu a URL. Não duplica hoje, mas duplicaria se a pessoa comentar num post futuro com slug decodificado. Falta um `unquote` no parser.
- [ ] Script IG: monitor AutoDM + recomment público.
