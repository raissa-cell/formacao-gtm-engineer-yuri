---
name: agent-tester
description: "Skill genérica pra TESTAR agentes conversacionais de IA (builder Nuvia) ponta a ponta: modelagem da bateria de testes, execução via simulação, documentação com histórico de rodadas, e o loop completo de correção (Batch 1 → draft de v2 → aplicar via API quando for System, checkpoint humano só para decisão crítica → reteste). Correções de System (rules/communication_style/personality/role/mission) são aplicáveis DIRETO via API (PUT /v1/agents/{id}, testado e confirmado) e registradas num Agent Log; correções de steps continuam manuais (API não persiste steps, confirmado empiricamente). Complementa a skill agent-prompt-builder (que cobre COMO escrever o prompt); esta cobre COMO validar e evoluir o que já foi escrito. Gatilhos: 'testar o agente', 'rodar bateria de testes', 'reexecutar os testes', 'agente reprovou, corrige e testa de novo', 'ciclo de teste e correção', 'valide esse agente antes de publicar', 'atualiza o agente via API', 'agent log'."
license: MIT
compatibility: any-agent
---

# Agent Tester — modelagem, execução, documentação e loop de correção

Ver também [`agent-prompt-builder`](../agent-prompt-builder/SKILL.md) pro catálogo de anti-padrões e templates de prompt — esta skill assume que os campos/etapas já existem e foca em VALIDAR e EVOLUIR o agente com rastreabilidade.

## Quando usar

- Agente novo, antes de ir pra produção → rodar o ciclo completo (Fases 1-4).
- Agente já em produção que reprovou num teste, teve queixa de comportamento, ou mudou de prompt → Fase 2 (reteste focado) + Fase 4 (loop) a partir do estado existente da planilha.
- Usuário pede só "roda os testes de novo" → Fase 2 + 3, sem reabrir a Fase 1 inteira.

---

## Fase 0 — Pré-requisito

Antes de modelar qualquer teste:
1. `builder_list_agents` → achar o `agentId`.
2. `builder_get_agent(agentId)` → ler o prompt ATUAL por completo (`prompts.rules`, `communication_style`, cada `steps[].description`). Nunca modelar teste em cima de memória de uma versão antiga — o prompt pode ter mudado desde a última bateria.
3. Se já existe uma planilha de bateria anterior para este agente, ler antes de criar uma nova (não duplicar arquivo).

---

## Fase 1 — Modelagem dos testes

Para cada etapa (`steps[]`, na ordem), ler `description` e extrair cenários de:

| Fonte no prompt | Vira teste de... |
|---|---|
| Cada "Saídas: EtapaX (condição)" | 1 teste de transição por condição de saída |
| Cada critério de desqualificação/fora do âmbito | 1 teste de "cai fora do critério" + 1 teste de "está dentro do critério" |
| Cada Passo com Fallback | 1 teste que força o fallback (resposta vaga, ambígua, fora de regra) |
| Cada `assign_user`/tool prometida no texto | 1 teste que confirma a tool foi de fato disparada, não só prometida em texto |
| Cada Template | 1 teste que confirma o texto final não vaza placeholder cru |
| Regras em `communication_style` | testes "Transversais" (idioma, estilo, reconhecimento, emojis, travessão) — rodar 1x, valem pra qualquer etapa |
| Regras de negócio sensíveis (preço, dado institucional) | 1 teste específico de alucinação/precisão, mesmo que pareça óbvio — é onde mais aparece bug |

Cobertura mínima obrigatória, sempre: (a) toda transição de etapa; (b) todo critério de desqualificação, nas duas direções; (c) toda regra transversal; (d) retomada de lead desengajado/desqualificado; (e) pelo menos 1 caso adversarial (pedido ofensivo/fora de escopo/ambíguo).

Classificar cada teste por Criticidade:
- **Crítica**: quebra o funil (não desqualifica quem deveria, não transiciona) ou entrega dado errado ao lead (preço inventado, produto inexistente).
- **Alta**: comportamento errado mas recuperável (pergunta duas vezes, não usa o template certo).
- **Média**: estilo/tom fora do padrão.
- **Baixa**: cosmético (emoji, formatação).

Formato de planilha (uma linha por cenário):

```
Teste | Etapa | Criticidade | Output Esperado | Output do Agent (Transcrição Literal) | Resultado (Pass/Fail) | Correção | Observações
```

Salvar como CSV na pasta da conta/campanha do agente (ex.: `Signals/lote_X/contas/<conta>/bateria_testes_agente.csv`).

---

## Fase 2 — Execução

Rodar via `builder_simulate_conversation` (Nuvia, dry-run — não cria conversa real, não tem efeito colateral):

- `startStepOrder`: pular direto pra etapa-alvo do teste (evita ter que reconstruir toda a jornada a cada cenário).
- `leadContext`: simular `contact`/`conversation` já preenchidos (email já registrado, telefone com DDI, etc.) quando o teste depender de estado pré-existente.
- `messages[]`: array multi-turno (até 10) — cada item é 1 turno do lead; o step avança entre turnos dentro da mesma chamada.
- Rodar cenários independentes em paralelo (múltiplas chamadas na mesma mensagem) pra economizar tempo.

**Limitação estrutural a documentar, não ignorar:** tools de integração/tabela (busca de produto, calendário, etc.) NUNCA executam de verdade no dry-run — sempre retornam `[SIMULADO] would call X`. Todo teste cujo resultado dependeria do dado real dessas tools deve ser marcado **"Não conclusivo"**, nunca forçado como Pass ou Fail. Anotar explicitamente que precisa validação em staging/produção.

---

## Fase 3 — Documentação (com histórico de rodadas)

- Preencher a transcrição do agente **literalmente**, sem parafrasear — é o que permite auditar depois se o "Pass" foi por sorte de fraseado.
- **Nunca sobrescrever a rodada anterior.** Cada rodada nova de teste adiciona colunas: `Resultado Batch N`, `Correção Batch N`, `Observações N`. Isso preserva o histórico de "o que já foi tentado" e evita reabrir debate sobre coisa já resolvida.
- Testes que já passavam e não foram afetados por nenhuma mudança de prompt na rodada: marcar `Não retestado (sem mudança de prompt relacionada)` em vez de gastar uma simulação — só reexecutar o que mudou ou depende do que mudou.
- Todo Fail deve sair da Fase 3 com uma hipótese de causa objetiva (qual campo, qual trecho do texto, por que o modelo se comportou assim) — vira input direto da Fase 4.

---

## Fase 4 — Loop de correção (Batch 1 → v2 → checkpoint humano → v3 → reteste)

```
┌─→ 1. TESTAR (Fase 1+2+3) ──────────────────────────────┐
│                                                          │
│   2. Pra cada Fail/Parcial: draft de v2                 │
│      → texto COMPLETO e pronto-pra-colar do campo/etapa │
│        afetado (não só "mude X por Y" em prosa)         │
│                                                          │
│   3. CHECKPOINT HUMANO (obrigatório antes de aplicar    │
│      qualquer correção que não seja bugfix mecânico —   │
│      ver critério abaixo)                                │
│                                                          │
│   4. v3 = aplicar (MANUAL, ver nota de API abaixo)      │
│                                                          │
│   5. RETESTAR só o que mudou / depende do que mudou ────┘
```

Repetir até: todos os testes Críticos = Pass, e nenhum Fail restante sem justificativa de limitação de ambiente (não de prompt).

### 4.1 — Quando o checkpoint humano é obrigatório (passo 3)

**Autorização permanente (opt-in): só vale se o usuário a conceder explicitamente na sessão.** Com a autorização, dentro deste loop, correções que vivem em conteúdo de **System prompt** — dos and don'ts, tom de voz, exemplos de mensagens, informação de produto, informação sobre a empresa (ou seja: `prompts.rules`, `communication_style`, `personality`, `role`, `mission`) — **não precisam de checkpoint humano**. Aplicar direto via API (§4.2) e retestar. Ainda assim, **logar toda alteração no Agent Log (§4.3)**, sem exceção — autorização de aplicar direto não dispensa registro.

Isso NÃO cobre automaticamente qualquer coisa que more nesses campos — a exceção é por TIPO de conteúdo, não por nome de campo. Parar e perguntar ao usuário mesmo que o texto esteja em `rules`/`communication_style`, sempre que a correção envolver:

- **Critério de negócio numérico/estrutural**: o que conta como dentro/fora de escopo, orçamento mínimo, região atendida, definição de "lead qualificado".
- **Política de escalonamento**: quando o agente pode decidir sozinho vs. quando é obrigado a transferir pra humano.
- **Dado sensível/comercial**: preço, condições comerciais, garantias, qualquer promessa nova em nome da empresa que ainda não estava no prompt.
- **Steps**: qualquer mudança em `description` de step é sempre reportada ao usuário para aplicação manual (não editável via API — ver §4.2). Não se aplica autorização de edição direta aqui, só porque não há como.

Não precisa de checkpoint (aplicar direto): correção mecânica de System (grounding, placeholder cru, tom, exemplo-âncora contraditório, dos/don'ts, mensagens-exemplo, dado de produto/empresa) — ver critério acima — e qualquer correção puramente mecânica de step (mover checagem mais cedo, reforçar grounding) — essa última só que vai pro usuário aplicar manualmente, já que step não é escrevível via API.

Ao levar pro checkpoint (quando ainda obrigatório), apresentar: o Fail observado (transcrição literal), a causa provável, e 2-3 opções concretas de correção (não só "o que você acha?") — decisão de arquitetura crítica precisa de alternativas, não só validação.

### 4.2 — Aplicar a v3: o que é escrevível via API (testado empiricamente em 2026-07-28)

**Confirmado por teste real (round-trip GET → PUT → GET), não por suposição:**

| Alvo | Escrevível via API? | Evidência |
|---|---|---|
| System (`prompts.rules`, `communication_style`, `personality`, `role`, `mission`, `service_prompt`, `name`) | **SIM, persiste de verdade** | Testado no agente "YK - Linkedin Clone" (`6a17826383ef88fa3c28c7bf`): adicionada 1 linha em `rules`, PUT retornou o valor novo, GET seguinte confirmou persistência, e a UI do builder mostrou a linha nova. |
| `steps[].description` (prompt de uma etapa específica) | **NÃO — aceito no body (200 OK) mas silenciosamente ignorado, nunca persiste** | Testado 2x no agente "YK - Lkn Engagement" (`6a4fbced08a95a06385fa307`), em 2 steps diferentes (`desqualificado_recusou_contato` e `modo_consultivo`), incluindo uma tentativa enviando o objeto completo exatamente como veio do GET (sem remontar nada). Nos 3 casos: PUT 200, resposta do PUT nem devolve a chave `steps`, GET posterior confirma que a description não mudou. |

**Endpoint:** `PUT https://api.nuvia.ai/v1/agents/{id}`
**Auth:** `Authorization: Bearer <NUVIA_API_KEY>` (mesma key do `.env` do pilar — ver memória `env_por_pilar`). **User-Agent de navegador obrigatório** no header (mesmo WAF/Cloudflare 403 code 1010 documentado em `nuvia-crm` pra outros endpoints REST da Nuvia — usar `curl`/subprocess com `User-Agent: Mozilla/5.0 (...)`, nunca `urllib`/`requests` puro).
**Header opcional:** `x-company-id` — só necessário com API key global (`type=global`).

**Processo pra aplicar uma correção de System via API:**
1. `GET /v1/agents/{id}` (ou `builder_get_agent`) — sempre ler o estado atual antes, nunca reusar um JSON antigo da sessão.
2. Montar o payload do PUT como **deep copy do objeto inteiro recebido no GET**, alterando só o(s) campo(s) de `prompts.*` necessários (ex.: dar `append` num item novo em `prompts.rules` — cada item é `{"type":"text","content":"..."}`). Não é preciso remover `_id`/`company`/`createdAt`/etc. antes de enviar — testado enviando o objeto completo as-is e funcionou igual.
3. `PUT` o payload completo de volta pro mesmo `{id}`.
4. **Confirmar com um GET novo** que o valor persistiu (não confiar só na resposta do PUT, embora nos testes ela já viesse correta) — é o mesmo hábito de "nunca confie que apliquei sem reconferir" que já valia pro fluxo manual.
5. Reexecutar o(s) teste(s) afetado(s) via `builder_simulate_conversation`.

**Steps continuam manuais**: quando a correção está em `steps[].description`, entregar ao usuário o texto final pronto-pra-colar (nunca só a instrução de mudança), pra ele colar no builder. Depois de confirmação dele, `builder_get_agent`/GET de novo pra confirmar que salvou, antes de reexecutar o teste.

**Nota de rastreio (por precaução, revisitar se o cenário mudar):** não existe endpoint dedicado a step isolado (`GET`/`PUT` por `stepId`) documentado nem descoberto por teste — só o agente inteiro. A descrição de `builder_list_agent_flows` (tool MCP) menciona uma tool `push_agent` que não está exposta nesta conta/sessão — se um dia aparecer disponível via `ToolSearch`, retestar se ela cobre `steps` (o REST direto não cobre).

### 4.3 — Agent Log (registro obrigatório de toda alteração aplicada)

Toda vez que uma correção de System for aplicada via API (§4.2), registrar uma entrada no arquivo **`agent_log.md`**, na mesma pasta da bateria de testes do agente (ex.: `Signals/lote_X/contas/<conta>/agent_log.md`; se o agente não tiver pasta de conta dedicada, colocar ao lado da planilha de teste mais próxima). Criar o arquivo na primeira alteração, se ainda não existir.

Formato de cada entrada (mais recente no topo):

```
## [YYYY-MM-DD HH:MM] — <agentId> (<nome do agente>)
**Campo alterado:** prompts.rules | prompts.communication_style | prompts.personality | prompts.role | prompts.mission | prompts.service_prompt
**Gatilho:** <qual teste/Fail da bateria motivou esta mudança, ou "ajuste solicitado diretamente pelo usuário">
**Antes:** "<trecho exato removido/substituído, ou 'campo novo' se for adição>"
**Depois:** "<trecho exato adicionado>"
**Aplicado via:** PUT /v1/agents/{id} (API direta)
**Checkpoint humano:** dispensado (System, categoria autorizada) | aplicado após aprovação em <data>
**Reteste:** <resultado do builder_simulate_conversation pós-aplicação — Pass/Fail, referência à linha da planilha se houver>
```

Nunca sobrescrever entradas antigas — é um log, sempre append. Serve tanto de auditoria (o que foi mudado e por quê) quanto de histórico pra reverter uma mudança específica se ela causar regressão.

---

## Checklist de saída do loop

- [ ] Toda etapa tem pelo menos 1 teste de transição coberto
- [ ] Todo critério de desqualificação testado nas duas direções
- [ ] Toda promessa de tool testada por execução real (não só texto)
- [ ] Nenhum Fail restante sem hipótese de causa e correção proposta
- [ ] Nenhuma correção de System aplicada sem entrada correspondente no Agent Log (§4.3)
- [ ] Nenhum Fail "resolvido" sem checkpoint humano quando envolvia critério de negócio numérico/estrutural, escalonamento ou dado comercial novo
- [ ] Correção de step sempre passada pro usuário aplicar manualmente + reconfirmada via GET antes do reteste
- [ ] Planilha com histórico de rodadas preservado (colunas Batch N, nunca sobrescritas)
