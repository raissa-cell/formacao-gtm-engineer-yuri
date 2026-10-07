# CLAUDE.md: AI GTM Machine

Este repositório é o ponto de partida da máquina de GTM (Go-To-Market) de um aluno da formação AI GTM Engineer. Você (a IA) opera sobre ele a pedido do aluno. Este arquivo explica o que cada pasta faz e como agir.

Responda em PT-BR, salvo pedido em contrário.

## Primeiro contato
1. Procure `{{` nos arquivos (`grep -rn "{{" brand/ CLAUDE.md`). Se `brand/voice.md` ainda tem `{{...}}`, a marca não está configurada: sugira rodar `/setup` antes de escrever qualquer copy.
2. Se `.env` não existe, `cp .env.example .env` e oriente o aluno a preencher. Nunca peça para ele colar chaves no chat nem escreva chaves em arquivos versionados.

## Estratégia: 3 pilares conectados
Conteúdo (ímã de autoridade e sinal) + Ads (amplifica o mesmo ângulo) + Outreach (usa os sinais). **Campanhas são organizadas por público-alvo, não por canal.** Detalhes: `playbook/3-pilares.md`.

## Mapa de pastas
```
brand/                  Identidade do aluno (TEMPLATES a preencher). Fonte de verdade de voz e visual.
  voice.md              Voz de CONTEÚDO (post, ad). Carregar antes de qualquer copy.
  voice-outbound.md     Voz de PROSPECÇÃO 1:1. Carregar SEMPRE antes de nota de conexão/DM/e-mail frio.
  background.md         Trajetória e pontos em comum, para personalizar outbound.
  design.md             Cores, fontes, formatos de qualquer visual.
  estrutura-dm-oferta-direta.md   Método de DM que apresenta oferta (5 blocos).

campaigns/              Uma pasta por PÚBLICO-ALVO.
  _template/            Copie para campaigns/<publico>/ (conteudo, ads/creative, outbound, signals, scripts).
  exemplo-imobiliarias-pt-Playbook.md   Campanha real anonimizada: referência de como documentar.

automations/            Scripts. Infraestrutura, não conteúdo.
  comment-to-dm/        Comment-gate: comentou a palavra → vira contato → recebe DM → ganha score. LEIA o README antes de usar.
  leads/                triagem_icp.py (classifica ICP), preencher_campos.py (grava ICP/cargo na Nuvia).
  publishing/           Publicação via Upload-Post (LinkedIn, Instagram, X). Legenda e mídia entram por argumento/arquivo.
  content-curation/     Puxa top posts de perfis de referência (perfis.csv) e cria cards no ClickUp.
  autodm-keepalive/     Mantém o monitor de AutoDM vivo (launchd).
  runtime/              Como instalar jobs agendados fora de ~/Desktop.

playbook/               Conhecimento operacional.
  3-pilares.md · comment-gate.md · licoes-aprendidas.md (LEIA antes de automatizar)
  workflow-publicacao-multicanal.md   Pipeline tema → hook → arte → agendamento → registro.
  nuvia-mcp-boas-praticas.md          Antes de criar contatos/listas em massa na Nuvia.
  experimentos/         Guia e templates (hipótese, resultado, priorização ICE) para testes controlados.

formacao/modulos.md     Mapa dos 7 módulos da formação e quais skills cada um usa.

.claude/skills/         25 skills (ver mapa abaixo). Carregam pela descrição; puxe a certa proativamente.
.claude/agents/         Subagents: sdr-qualificador, auditor-de-copy. Crie novos aqui.
.claude/commands/       /setup (onboarding).
```

## Skills: momento → skill
| Momento | Skill |
|---|---|
| Estratégia GTM, ICP, growth loop | `saas-b2b-growth-strategist` |
| Criar/afinar OFERTA | `grand-slam-offer-builder` |
| Planejar campanha (brief + calendário) | `campaign-plan` |
| Hook, headline, assunto | `hook-generator` |
| Post LinkedIn (pipeline completo) | `linkedin-post-generator` |
| Post X/Threads | `threads-x-post-generator` |
| Copy comercial (LP, ad, CTA) | `impact-copywriter` |
| Humanizar texto (PT / EN) | `humanize-pt-br` / `humanize-en` |
| Repurpose entre plataformas | `social-repurposing` |
| Mensagem 1:1 (conexão, DM, WhatsApp, e-mail) | `outbound-personalization` |
| Sequência de e-mail | `email-sequence` |
| E-mail que acompanha proposta | `proposal-followup-email` |
| Empresas brasileiras via CNPJ | `cnpj-investigation` |
| Lookalike de empresas (clusters + filtros + lista) | `company-lookalike` |
| Escrita na Nuvia (lista, contato, campanha) | `nuvia-crm` |
| Criar / testar agentes da Nuvia | `agent-prompt-builder` / `agent-tester` |
| Aplicar/checar a voz da marca | `brand-voice-enforcement` · `guideline-generation` |
| Battlecard, gap competitivo | `competitive-brief` |
| Diagnóstico de funil, CAC, ROAS | `growth-data-analyst` |
| Relatório de performance | `performance-report` |
| Narrativa de deck persuasivo | `mckinsey-storytelling` |
| Achar outra skill | `skill-finder` |

## Fluxo de criação de conteúdo (nesta ordem)
1. **Hook**: gere 5 opções e ESPERE o aluno escolher.
2. **Rascunho** completo, após hook aprovado.
3. **Revisão**: filtro de 5 perguntas de `brand/voice.md` §7.
4. **Humanizar**: rodar `humanize-pt-br` (ou `-en`) no texto final. Nunca pule.
5. **Salvar** em `campaigns/<publico>/conteudo/AAAA-MM/<nome-do-post>/`.
6. **Agendar/registrar**. Ao agendar qualquer post, pergunte: "é comment-gate?" (ver `playbook/comment-gate.md`).

Prospecção 1:1 segue outro registro: carregue `brand/voice-outbound.md` e use `outbound-personalization`. Para oferta direta, `brand/estrutura-dm-oferta-direta.md`.

## Regras de execução (não negociáveis)
- **Script é infraestrutura, conteúdo é dado.** Nunca hardcode legenda, mídia, thread ou data em `.py`. Publicar um post nunca deve exigir editar código.
- **Um CTA por post.** Nunca empilhar comment-gate com comunidade/follow.
- **Voz:** nada de travessão (—) nem marcadores típicos de IA. Siga `brand/voice.md`.
- **Nuvia:** carregue a skill `nuvia-crm` e `playbook/nuvia-mcp-boas-praticas.md` ANTES de qualquer escrita. Rode `whoami`, deduplique por `linkedin_identifier` (LinkedIn) ou `phone_number` (WhatsApp), nunca por nome. Confirme com o aluno antes de criar lista ou contato em massa.
- **Todo lead passa pela triagem de ICP** (`automations/leads/triagem_icp.py`). Não classifique ICP de cabeça.
- **Raspagem (Apify): respeite o limite pedido.** "20 comentários" = `maxItems: 20`. O ator cobra por item.
- **Agendamento:** o runtime vive em `~/gtm-automation`, nunca em `~/Desktop` (launchd falha com exit 126). Cron usa o fuso da máquina: converta o horário.
- **Prompt de agente:** mostre o texto no chat e espere OK antes de gravar.
- **Segredos e leads (PII):** `.env`, CSVs, ledgers e `signals/` ficam fora do git (`.gitignore`). Nunca imprima chaves nem suba dados de leads.
- **Ações externas** (publicar, enviar DM/e-mail, ativar campanha, criar contatos em massa): confirme com o aluno antes.
- Entrega direta: sem loops de confirmação além dos gates (hook → conteúdo → publicação). Correções do aluno entram na hora, sem justificar a versão anterior.

## Placeholders
`{{SEU_NOME}}`, `{{SEU_LINKEDIN_SLUG}}`, `{{LINK_COMUNIDADE}}`, `{{SEU_USUARIO_GITHUB}}`, `{{CLICKUP_LIST_ID}}` etc. são do aluno. Se faltar o valor, pergunte; não invente.

## Como evoluir este repo
Skill nova: `.claude/skills/<nome>/SKILL.md`. Agente novo: `.claude/agents/<nome>.md`. Campanha nova: copie `campaigns/_template/`. Automação nova: documente gatilho → ação → destino no README da pasta ANTES de codar.
