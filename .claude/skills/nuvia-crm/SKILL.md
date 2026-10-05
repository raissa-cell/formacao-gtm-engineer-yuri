---
name: nuvia-crm
description: "Procedimento VALIDADO para manipular o CRM Nuvia via MCP/REST. Use SEMPRE que a tarefa envolver escrita na Nuvia: criar contatos (com telefone fictício + dedup), criar lista/tabela, criar colunas/campos personalizados, POPULAR uma lista com contatos, adicionar registros (add_records), auditar linhas, deletar lista, ou criar campanha + bulk enroll de contatos. Gatilhos: 'criar lista na Nuvia', 'popular lista', 'adicionar contatos à lista', 'add_records', 'linha em branco/órfã na Nuvia', 'bulk enroll', 'enrollar campanha', 'criar campo personalizado Nuvia', 'lista aparece vazia', 'Nuvia table/rows'. Contém os macetes que evitam loops: popular lista SÓ via MCP add_records (REST /rows não linka), User-Agent obrigatório no REST (WAF 403 code 1010), dedup de telefone, DELETE /tables preserva contatos. TAMBÉM cobre o AGENT BUILDER: editar agente, prompt de etapa/step, follow-ups, mentions ({get_field}/{update_step}/{update_field}/{assign_user}), e o achado crítico de que PUT /v1/agents IGNORA steps/followups (edição de etapa = só no builder). Gatilhos extra: 'editar agente Nuvia', 'atualizar prompt de etapa', 'push_agent', 'PUT agents', 'follow-up do agente', 'builder_get_agent', 'agente não salva pela API'."
license: MIT
compatibility: any-agent
---

# Nuvia CRM — Manipulação (contatos, listas, campos, popular, campanha)

Instruções operacionais testadas ponta a ponta (última validação: população de lista via `add_records`, 10/10 linkados). Siga na ordem. **Não reinvente com REST o que o MCP resolve** — o erro clássico é tentar popular lista via REST e ver tudo em branco.

## Mapa da conta (consulte ANTES de buscar na Nuvia)
Mapa da sua conta Nuvia (agentes, steps com IDs, campos, campanhas, listas, receitas de busca): [references/conta-nuvia-template.md](references/conta-nuvia-template.md). Se um ID não bater, reler ao vivo e atualizar o arquivo.

## Regra de ouro (leia antes de tudo)

- **POPULAR lista = MCP `add_records`. SEMPRE.** O REST `POST /tables/{id}/rows` insere linha mas **NÃO vincula o contato** (`record_id: null` → linha órfã, tudo em branco na UI). Já foi testado com todos os shapes; nenhum linka. Não perca tempo com ele.
- **REST exige User-Agent de navegador.** O WAF (Cloudflare) bloqueia `urllib`/`python-requests` sem UA com **403 `error code: 1010`**. Use `curl` (via subprocess) ou header `User-Agent: Mozilla/5.0 (...)`. 
- **Criar contato exige telefone.** Leads sem telefone (ex. LinkedIn) precisam de um fictício **com dedup antes**.
- **Créditos:** só `enrich_list` custa. Todo o resto (busca, CRM, listas, campanhas) é grátis.

## Auth / base
- REST base: `https://api.nuvia.ai/v1` · Header `Authorization: Bearer <NUVIA_API_KEY>` (JWT company-scoped).
- Key no `.env` do pilar: `.env` e `campaigns/.env` (`load_env` sobe a árvore).
- Respostas às vezes vêm `{meta, result}`, às vezes diretas → sempre _unwrap_ `result` se existir.

## Matriz MCP × REST (o que usar)
| Operação | Ferramenta |
|---|---|
| Buscar contato no CRM | MCP `list_contacts` (busca nome/email/tel + filtro nativo `contact.linkedin_identifier`) ou REST `GET /contacts?filters=[...]` |
| Dedup por telefone | MCP `find_contacts_by_phone` (≤50) ou REST `POST /contacts/find-by-phones {phones:["<cc><num>"]}` |
| Criar contato | MCP `create_contacts` (bulk, exige phone) ou REST `POST /contacts` (exige name+country_code+phone_number) |
| Criar lista | MCP `create_list` (sem dedup de nome — cheque `list_lists` antes) |
| Criar coluna | MCP `add_list_column` (guarde os `key` UUID) |
| Ler colunas/stats | MCP `get_list` ou REST `GET /tables/{id}` |
| **Popular lista** | ✅ **MCP `add_records`** — REST `/tables/{id}/rows` ❌ não linka |
| **Preencher células em massa** (texto longo, ex. msg por lead) | ✅ REST `PATCH /tables/{id}/rows/{rowId} {data:{<colKey>:{state:'active',isValid:true,value}}}` — preserva o vínculo com o contato (testado 29/09/2026). Fluxo: `add_records` só com `contact_id` → GET `/tables/{id}/rows?limit=200` (mapeia `contact_id`→`_id`) → PATCH por linha. Evita mandar 200KB de texto pelo MCP |
| Ler/auditar linhas | MCP `list_records` (checar `record_id != null` + `name`) |
| Deletar lista | REST `DELETE /tables/{id}` (204; **preserva contatos**) — MCP não deleta |
| Deletar coluna | ❌ não existe via API → recriar a lista |
| Campo custom **de contato** | escrita via `additional_attributes` (create/update); **criar o campo** = REST `POST /v1/custom-fields {title,type,context:'contact',description}` com **JWT de usuário** (`NUVIA_USER_JWT`, 201, testado 30/09/2026). Com API key = 401 |
| Campanha: ler | MCP `list_campaigns` / `get_campaign` (read-only) |
| Criar conversa / mover funil / atribuir agente | REST (ver memória `nuvia_rest_api_conversations`) |
| **Bulk enroll** | REST `POST /campaigns/{id}/enrollments/bulk {contact_ids:[...]}` |

## Conceitos que evitam erro
- **Lista = "table" na REST.** Linha referencia 1 `contact_id`; a coluna `name` é auto-resolvida do contato (`source:'record'`).
- **Coluna custom:** `add_list_column`, `key` = UUID (é ela no `data` do `add_records`).
- **Célula** = `{state:'active', isValid:true, value:...}`. O MCP `add_records` normaliza valor cru → célula. Você passa só o valor cru.
- **Coluna de lista ≠ campo custom de contato.** Coluna de lista: só naquela lista, via MCP, sem UI (lugar certo de dado de campanha: Fit, Msg, etc.). Campo de contato (`additional_attributes`): aparece no contato em toda a Nuvia, mas só cria na UI.
- **`linkedin_identifier`** (slug de `/in/<slug>`) é o campo nativo/chave do lead de LinkedIn. Dedup por ele; nunca coluna custom.

## FLUXO A — Criar e popular uma lista (passo a passo)
1. **Dedup + criar contatos** (se não existem): por lead, cheque `list_contacts` por `linkedin_identifier` (e/ou `find_contacts_by_phone`). Existe → reaproveite o `contact_id`. Não existe → `POST /contacts` (curl/UA) com name, country_code, phone_number, linkedin_identifier, job_title.
   - **Telefone fictício + dedup:** gere candidato de faixa reservada, cheque com `find_contacts_by_phone`; ocupado → +1 até livre. (`collect_to_nuvia.py`: base `999002000`, cc=55 — já tem 1000+ usados e a varredura 1 a 1 leva minutos; campanha nova = faixa própria, ex. live Brian usa `999010000`. Faixa US fictícia `555-01XX`/cc=1 também serve.) Guarde `name → contact_id`.
2. **Criar lista:** MCP `create_list { name, object_type:'contact', description }` (cheque `list_lists` antes).
3. **Criar colunas custom:** MCP `add_list_column { list_id, columns:[{name,type,settings:{source:'custom'}}] }`. Guarde os `key` UUID.
4. **Popular:** MCP `add_records { table_id, records:[{contact_id, data:{"<colKeyUUID>": valor}}] }` — ≤100/call, valor cru, idempotente (já-presente → `skipped`). Para >100, faça em lotes.
5. **Auditar:** MCP `list_records` → cada linha deve ter `record_id != null` e `fields.name` preenchido (senão é órfã, veio do `/rows`). `get_list` → `stats.row_count`.
6. **Corrigir:** REST `DELETE /tables/{id}` apaga a lista (contatos permanecem); recrie e repopule.

## FLUXO B — Campanha + bulk enroll (quando o objetivo é ENVIAR)
1. Contatos já existem (Fluxo A §1).
2. **o usuário cria a campanha na UI** (inbox/sender + passos + agente) → passa o `campaign_id`. Campanhas atuais são `trigger_type: MANUAL` (não disparam sozinhas). Se não for MANUAL, teste com 1 contato antes (enroll pode acionar o agente e iniciar outreach real no LinkedIn).
3. **Bulk enroll:** REST `POST /campaigns/{id}/enrollments/bulk {contact_ids:[...]}` (curl/UA; reaproveita `Nuvia.bulk_enroll` do `collect_to_nuvia.py`).
4. **Limitações:** campanha não guarda colunas de dados (Fit/Msg → lista ou custom field). Envio é **template com variável** (`{{first_name}}`), não corpo único por lead — pra usar Msg personalizada, ela vira custom field de contato e o template referencia `{{msg_1}}`.

## Reaproveitável
- `automations/comment-to-dm/collect_to_nuvia.py` — classe `Nuvia`: UA de navegador, `create_contact`, `next_free_phone` (dedup), `find_contact`, `bulk_enroll`. **Não tem** população de lista (isso é MCP `add_records`).
- Endpoints de conversa/funil/agente/enrollment: memória `nuvia_rest_api_conversations`.

## Helper anti-WAF (curl via subprocess Python)
```python
import subprocess, json
def nuvia(method, path, token, body=None):
    args = ["curl","-s","-X",method,f"https://api.nuvia.ai/v1{path}",
            "-H",f"Authorization: Bearer {token}","-H","Content-Type: application/json","-w","|%{http_code}"]
    if body is not None: args += ["-d", json.dumps(body)]
    out = subprocess.run(args, capture_output=True, text=True, timeout=60).stdout
    payload, _, code = out.rpartition("|")
    return code, (json.loads(payload) if payload.strip() else {})
```

---

# Agent Builder (agentes, etapas, follow-ups) — VALIDADO 2026-07-29

Manipulação do agente conversacional Nuvia (persona + steps + follow-ups). **Aprendizados testados ponta a ponta.**

## ⛔ Regra de ouro (o achado que economiza horas)
- **`PUT /v1/agents/{id}` (endpoint público) NÃO grava `steps` nem `followups`.** Retorna **200**, mas ignora o array — a resposta nem ecoa os steps, e um GET seguinte mostra o texto antigo. **TESTADO.** Serve só p/ nível-agente: `name`, `prompts` (`service_prompt, role, mission, personality[], communication_style[], rules[]`), `model_config`, `general_config`, `specialist_config` (inclui `icp_description`), `status`, `personality_presets`, `avatar_*`.
- **Editar STEP (prompt de etapa) SE FAZ por endpoint INTERNO `/v1/agent-steps/*`** (não pelo `/v1/agents`). Ver seção abaixo. **Não estão na swagger pública** (allow-list só expõe ops com `@RequireApiKeyScope`).
- **Campo certo do step = `description`** (o runtime injeta `step.description` como `{{step_prompt}}`). `prompts.interaction_prompt` existe no DTO mas o runtime **ignora** (legado) — editar isso dá 200 e não muda nada. Pegadinha.
- **Nunca confie no HTTP 200** — sempre reverifique relendo (GET agent-steps ou `builder_get_agent`).

## Editar STEP via API (endpoints internos — JWT de USUÁRIO)
`agent-steps.controller.ts`:
- `GET /v1/agent-steps/agent/:agentId` — lista os steps (pega o `_id`).
- `PUT /v1/agent-steps/:id` — atualiza um step, mas **SÓ grava `description`** (IGNORA `mentions` mesmo se enviado). Use para editar texto de etapa.
- `PUT /v1/agent-steps/agent/:agentId/steps` — **upsert em lote** (o que o editor usa) — **é o ÚNICO que grava `mentions`**. Body = **ARRAY PURO** de steps (`[{...}]`); enviar `{"steps":[...]}` dá **400** ("expected array, received object"). Envie os steps completos (do `GET /agents/:id`) com as `mentions` novas — full replace, então mande TODOS pra não apagar nenhum.
- ⛔ **Wire de tool (o achado que economiza horas):** para o agente DISPARAR `update_field`/`update_step` (não narrar como texto e vazar), a mention `{type,uuid,tool,label,icon}` precisa estar no **array `mentions` do step** — não basta a tag inline na `description`. Como `PUT /agent-steps/:id` não grava mentions, use o batch acima. Copie a estrutura de uma mention que já funciona (ex.: `agendar_visita` tem `update_field(data-reuniao)`).
- **AUTH = a pegadinha:** esses usam `JwtAuthGuard` PURO (não `JwtOrApiKeyGuard`). **API key da empresa NÃO funciona → 401** (testado). Precisa de **JWT de USUÁRIO** (login da plataforma): `POST /v1/auth/login {email,password}` → role `USER` + permissão `agent:edit`. O mesmo app serve `api.nuvia.ai` e `api-platform.nuvia.ai` (sem restrição por host).
- **WAF:** User-Agent de navegador obrigatório (senão 403 `1010`), como no resto.
- Receita segura: GET steps → patch cirúrgico na `description` (string replace, sem reescrever à mão) → `PUT /v1/agent-steps/{_id}` → reler p/ verificar. Script de referência: `Motocred/scripts/apply-step-fixes.py`.
- ✅ **Token salvo:** `NUVIA_USER_JWT` em `.env` (validade ~2,7 dias). Conferir o payload: `type: user` serve; `type: api_key` (chave criada em Configurações/API) dá 401 mesmo sendo JWT. Pegar em app.nuvia.ai → Conversas → DevTools → Network → Fetch/XHR `conversations` → header `authorization`. Gravar com `pbpaste` direto no .env.
- ⚠️ **Login = o usuário faz** (não manuseie senha). Peça o JWT de usuário pronto (sessão logada: DevTools → Network → `Authorization`) ou que ele rode o `auth/login`.
- ✅ **CONFIRMADO 2026-07-29:** `PUT /v1/agent-steps/:id` com **JWT de usuário** gravou `description` (reativacao + visita_agendada) e persistiu — verificado relendo. Resposta do GET vem `{meta, result}` → **unwrap `result`**. Dica de idempotência: se a string-fonte não bate mas o texto-ALVO já está lá, é "já aplicado" (não é falha) — não aborte.
- **Gotcha de clone:** em agente recém-clonado, `GET /agent-steps/agent/{id}` dá **404** (steps ainda não indexados nessa rota). Pegue os steps embutidos em `GET /agents/{id}` (traz `_id` por step) e edite por `PUT /agent-steps/{_id}` (description) ou pelo batch (mentions).
- **Follow-ups:** `/v1/agent-followups/agent/:id`, `/agent-follow-ups/...` e `/agents/:id/followups` deram **404** com JWT de usuário — rota interna NÃO localizada. Por ora, editar follow-up = **builder**. MCP não tem write de agente/step/followup.

## Acesso / permissão
- MCP expõe **só leitura/simulação**: `builder_get_agent`, `builder_list_agents`, `builder_list_agent_flows`, `builder_list_custom_fields`, `builder_get_skill`/`builder_list_skills`, `builder_agent_quality_stats`, `builder_simulate_conversation` (dry-run, sem efeito). **`push_agent`/escrita NÃO é exposta.**
- **Gate de autoria = role `COMPANY_ADMIN`** (flag `agent_builder_mcp_enabled`, default true por empresa). Usuário comum só lê/simula. Por isso a tool de escrita não aparece no `/mcp`.

## REST (nível-agente, o que dá pra automatizar)
- `PUT /v1/agents/{id}` · base `https://api.nuvia.ai` · `Authorization: Bearer <NUVIA_API_KEY>` · `x-company-id` só p/ API key global.
- **WAF:** mesmo problema do resto — **User-Agent de navegador obrigatório** (senão 403 `code 1010`).
- **GET `/v1/agents/{id}`** devolve a entidade **completa e crua** (NÃO embrulhada em `{data}`): steps com `_id`, `slug`, `agent`, `company`, `createdAt`, `__v`. Fluxo seguro p/ editar nível-agente = **GET → patch cirúrgico → PUT** (round-trip preserva campos obrigatórios `_id, name, agent_flow, prompts, company, model_config, status`).
- `builder_get_agent` (MCP) = **view legível** (`agentFlow` vira string; `prompts` como arrays `{type:text,content}`). Difere do GET REST.
- Outros paths de agente: `POST /v1/agents` (criar), `POST /v1/agents/{id}/clone`, `DELETE /v1/agents/{id}`. **Nenhum** `/steps` ou `/followups`.

## Sintaxe de mentions (dentro de `step.description`)
Referências não são texto solto — são objetos-mention (o builder também guarda um array `mentions` espelhando os inline):
- **Consultar campo:** `[apelido] = {type:"field",uuid:"<fieldId | contact.name>",tool:"get_field",label:"Consultar: <nome>",icon:"Search"}` → usa `[apelido]` no texto.
- **Transição de etapa:** `{type:"step",uuid:"<stepId>",tool:"update_step",label:"<nome>",icon:"Workflow"}`.
- **Gravar campo:** `{type:"field",uuid:"<fieldId>",tool:"update_field",label:"<slug>",icon:"Calendar"}`.
- **Atribuir humano:** `{type:"user",uuid:"<userId>",tool:"assign_user",label:"<nome>",icon:"User"}`.
- ⚠️ `builder_get_agent` **não expõe o `_id` do próprio step**; o uuid de um step só aparece quando OUTRO step o referencia numa mention (ou via GET REST, que traz `_id`). Ao recriar um step no builder, o uuid muda → conferir mentions órfãs (transição apontando p/ uuid morto).

## Campos personalizados
- `builder_list_custom_fields` (MCP, read) → `{id, title, slug, type, context}`. Use o `id` como `uuid` nos mentions `get_field`/`update_field`.
- Criar campo custom de contato = **UI** (REST `/custom-fields` = 401 com key de empresa). Escrita de valor via `additional_attributes`.

## Escrever prompt de etapa/step (regras de qualidade)
→ ver skill **`agent-prompt-builder`** (anatomia por etapa, anti-padrões: checagem de DQ cedo, não vazar contexto de outra etapa, sem placeholder cru, etc.).

## Verificar o agente
- **Dry-run:** `builder_simulate_conversation {agentId, messages:[...], leadContext:{contact:{additional_attributes:{<slug>:...}}}, startStepOrder}` — roda o LLM real, registra as tools que dispararia, **sem efeito colateral** e sem aparecer em Conversas.
- **Qualidade:** `builder_agent_quality_stats` (piso da taxa de qualificação; use p/ comparar agentes, não como número absoluto).
