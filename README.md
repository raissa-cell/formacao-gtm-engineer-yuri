<div align="center">

# AI GTM Machine

**O repositório base da sua máquina de Go-To-Market, operada por IA.**
Conteúdo, ads e outbound como um único sistema. Skills, agentes e automações prontos para você adaptar.

`Claude Code` · `Nuvia` · `Apify` · `Upload-Post` · `Python 3`

</div>

---

## O que é

Um repositório para ser **clonado e transformado em seu**. Ele já traz:

- **25 skills** de Claude Code (estratégia, copy, outbound, CRM, agentes)
- **Automações** prontas: comment-to-dm, triagem de ICP, publicação, curadoria
- **Templates de marca** (voz, design, background) que as skills leem antes de escrever
- **Estrutura de campanha** por público-alvo
- **Playbook** com as lições de quem já rodou isso em produção
- Um **`CLAUDE.md`** que ensina a sua IA a operar tudo isso

A ideia central: **conteúdo é o ímã**. Ele gera sinal (comentário, visita, download) que as automações roteiam para o outbound. Inbound e outbound são a mesma máquina vista de dois lados.

```
Conteúdo / Ads ──► sinal (comentário, like, download)
                        │
                        ▼
              comment-to-dm ──► contato + score na Nuvia
                        │
                        ▼
              triagem de ICP ──► DM direta  |  convite + DM
                        │
                        ▼
              agente qualificador ──► reunião
```

## Quickstart (~15 min)

**Pré-requisitos:** [Claude Code](https://claude.com/claude-code), Python 3.10+, conta na [Nuvia](https://nuvia.ai) com o MCP conectado ao Claude Code. Apify e Upload-Post são opcionais no começo.

```bash
# 1. Clone e entre na pasta
git clone https://github.com/{{ORG}}/ai-gtm-machine.git meu-gtm
cd meu-gtm

# 2. Crie seu .env (nunca suba esse arquivo)
cp .env.example .env

# 3. Abra o Claude Code aqui
claude
```

Dentro do Claude Code:

```
/setup
```

O `/setup` entrevista você, preenche `brand/` com a sua voz e o seu visual, troca os `{{placeholders}}`, cria sua primeira campanha e mapeia sua conta Nuvia. Depois disso, peça o que quiser:

> "Planeje a campanha para `{{seu público}}`"
> "Gere 5 hooks sobre `{{tema}}`"
> "Monte a sequência de DM para esses leads"

## Mapa do repositório

| Pasta | O que tem | Quando usar |
|---|---|---|
| [`brand/`](brand) | Templates de voz, voz de outbound, background, design | Preencher UMA vez; toda skill de copy lê daqui |
| [`campaigns/`](campaigns) | `_template/` e um exemplo real anonimizado | Uma pasta por público-alvo |
| [`automations/`](automations) | comment-to-dm, leads, publishing, content-curation, keepalive, runtime | Rodar o motor de sinal → DM → score |
| [`playbook/`](playbook) | 3 pilares, comment-gate, lições aprendidas, workflow, experimentos | Antes de automatizar e ao planejar |
| [`formacao/`](formacao) | Mapa dos 7 módulos | Acompanhar a formação |
| [`.claude/skills/`](.claude/skills) | 25 skills | A IA carrega sozinha pela descrição |
| [`.claude/agents/`](.claude/agents) | `sdr-qualificador`, `auditor-de-copy` | Qualificar leads e auditar copy |
| [`.claude/commands/`](.claude/commands) | `/setup` | Onboarding |

## Skills por momento

| Momento | Skill |
|---|---|
| Estratégia, ICP, growth loop | `saas-b2b-growth-strategist` |
| Oferta | `grand-slam-offer-builder` |
| Plano de campanha | `campaign-plan` |
| Hook / headline | `hook-generator` |
| Post LinkedIn / X-Threads | `linkedin-post-generator` · `threads-x-post-generator` |
| Copy comercial | `impact-copywriter` |
| Humanizar texto | `humanize-pt-br` · `humanize-en` |
| Mensagem 1:1 (DM, e-mail, WhatsApp) | `outbound-personalization` |
| Sequência de e-mail | `email-sequence` · `proposal-followup-email` |
| Empresas BR por CNPJ | `cnpj-investigation` |
| Lookalike de empresas | `company-lookalike` |
| Escrever na Nuvia | `nuvia-crm` |
| Agentes de qualificação | `agent-prompt-builder` · `agent-tester` |
| Voz da marca | `brand-voice-enforcement` · `guideline-generation` |
| Análise e relatórios | `growth-data-analyst` · `performance-report` · `competitive-brief` |
| Narrativa de deck | `mckinsey-storytelling` |

## Fluxo de um post (comment-gate)

1. **Hook**: 5 opções, você escolhe.
2. **Rascunho** → **revisão** (5 perguntas) → **humanizar**.
3. **Salvar** em `campaigns/<publico>/conteudo/AAAA-MM/<post>/`.
4. **Comment-gate**: palavra-gatilho no post. Quem comenta vira contato, recebe 3 DMs e ganha score. Passo a passo em [`playbook/comment-gate.md`](playbook/comment-gate.md).
5. **Triagem de ICP** nos leads antes de qualquer campanha de outbound.

## Regras que poupam dor de cabeça

- **Script é infraestrutura, conteúdo é dado.** Legenda e mídia entram por arquivo/argumento, nunca hardcoded.
- **Um CTA por post.**
- **Agendamento fora de `~/Desktop`**: o macOS bloqueia o launchd lá. Use `~/gtm-automation` ([`automations/runtime`](automations/runtime)).
- **Dedup na Nuvia por `linkedin_identifier`**, nunca por nome.
- **Dados de lead nunca vão para o git**: o `.gitignore` já cobre `.env`, CSVs e `signals/`.

Mais em [`playbook/licoes-aprendidas.md`](playbook/licoes-aprendidas.md).

## Segurança e privacidade

- Segredos só em `.env` (ignorado pelo git). Referência: `.env.example`.
- Leads são dados pessoais: mantenha-os fora de repositórios públicos e respeite LGPD/GDPR no seu outbound.
- Se publicar o seu fork, rode antes `grep -rn "{{" .` e revise `brand/` para não vazar nada que você não queira público.

## Créditos e licença

Material de apoio da formação AI GTM Engineer. Os arquivos de referência de templates de post dentro de `linkedin-post-generator` e `threads-x-post-generator` pertencem aos seus autores originais e são mantidos aqui apenas para uso didático da formação.
