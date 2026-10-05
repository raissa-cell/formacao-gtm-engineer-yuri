# Mapa da sua conta Nuvia (template)

Preencha ANTES de buscar ou escrever na Nuvia: IDs, o que cada coisa é e como achar. IDs mudam quando alguém recria step ou campo no builder. Se algo não bater, releia ao vivo e atualize este arquivo na mesma sessão.
Última verificação: `AAAA-MM-DD`.

## 1. Conta

| Item | Valor |
|---|---|
| Company | `{{nome}}` · `{{id}}` |
| Seu usuário | `{{id}}` · alvo do `assign_user` |
| Inbox (remetente) | `{{nome}}` · LINKEDIN · `{{id}}` |
| Funil (agent flow) | `{{nome}}` · `{{id}}` |
| Auth REST | `NUVIA_API_KEY` em `.env` · User-Agent de navegador obrigatório |

Se a conta hospeda outros projetos, liste aqui o que deve ser **ignorado** (agentes, inboxes, campos).

## 2. Ontologia (como as peças se ligam)

```
Inbox (LinkedIn)
  └─ Campaign (MANUAL) ── audience = List ── mensagens usam colunas da lista ({{var_list_msg_1}})
       └─ Enrollment (snapshot: linha nova na lista NÃO entra sem bulk enroll)
            └─ Conversation (contato × inbox) ── current_step, who_answering (AGENT|HUMAN)
                 └─ Agent ── System (regras gerais, vale em todo step)
                      └─ Step (prompt da etapa + mentions = tools)
Contact ── campos nativos + custom fields de contato (ICP, Cargo do lead, engagement_score…)
```

- **System** (`prompts.rules`, `communication_style`, `role`, `mission`, `icp_description`): edita via `PUT /v1/agents/{id}` com API key. Dado que não pode errar (link, data, preço) mora AQUI, não no step: o step some do contexto quando o agente troca de etapa.
- **Step**: `description` = prompt. `type` DEFAULT (andamento) · SUCCESS (conta como qualificado) · CLOSED (encerrado). `should_auto_run_on_enter=true` = fala sozinho ao entrar. Editar step = builder, a API ignora.
- **Mention** = tool. Só funciona se estiver em `step.mentions[]`. Texto colado `[@...]` = tool morta, o agente improvisa.
- **Custom field**: `context contact` (vale em toda a Nuvia; escrever via `additional_attributes` com o slug) ou `conversation` (só na conversa; escrito pelo agente via `update_field`).

## 3. Agentes

| Agente | ID | Status | Modelo | Papel |
|---|---|---|---|---|
| | | | | |

Steps de cada agente:

| # | Step | ID | Tipo | Sai para |
|---|---|---|---|---|
| | | | | |

## 4. Dicionário de campos

| Campo | ID (= uuid da mention) | Slug | Tipo | Contexto | Quem escreve · quem lê |
|---|---|---|---|---|---|
| ICP | | `v_c_icp` | text | contato | `triagem_icp.py` · agente |
| engagement_score | | `v_c_engagement_score` | number | contato | comment-to-dm |
| post-interacao | | `v_c_post_interacao` | text | contato | comment-to-dm |

Campos nativos usados nos prompts: `contact.name`, `contact.job_title`, `contact.email`, `contact.department`, `contact.seniority`, `linkedin_identifier` (chave de dedup).

## 5. Campanhas e listas

| Campanha | ID | Status | Lista / nota |
|---|---|---|---|
| | | | |

## 6. Receitas

- **Conversa de um lead**: `list_contacts {search:"Nome"}` → `list_conversations {agent_id}` → `list_messages {conversation_id}`.
- **Funil da campanha**: REST `GET /v1/conversations?page=N&rowsPerPage=100`, agrupar por `current_step`.
- **Step dispara a tool?**: REST `GET /v1/agents/{id}` → a tool está em `mentions[]` e a `description` não tem `[@`.
- **Testar mudança**: `builder_simulate_conversation` (dry-run).
- **Editar System**: GET → patch em `prompts.rules` → PUT → GET; logar num `agent_log.md`.
- **Parâmetro numérico no MCP falha** (`page`, `page_size`): usar REST.
