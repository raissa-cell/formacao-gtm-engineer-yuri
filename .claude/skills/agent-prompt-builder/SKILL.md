---
name: agent-prompt-builder
description: "Skill genérica para PROJETAR e ESCREVER prompts de agentes conversacionais de IA (builder Nuvia ou similar), com templates por seção e por etapa, e checklist de anti-padrões coletados em auditorias reais. Use SEMPRE que a tarefa for: criar um agente novo do zero, escrever/revisar as etapas (steps) de um agente existente, montar a bateria de testes de um agente, ou corrigir um agente que reprovou em testes (alucinação, escalar em vez de agir, checagem tardia, placeholder cru, etc). Gatilhos: 'criar agente de IA', 'escrever prompt de etapa', 'agente para WhatsApp/Nuvia', 'revisar prompt do agente', 'agente alucinando', 'bateria de testes do agente', 'agente não está seguindo a regra'."
license: MIT
compatibility: any-agent
---

# Agent Prompt Builder — projetar, escrever e testar prompts de agente conversacional

Metodologia + templates pra montar agentes de atendimento/vendas (builder Nuvia, mas a lógica serve pra qualquer builder de agente por etapas). Consolida os anti-padrões encontrados em auditorias reais (ver `Signals/*/contas/*/bateria_testes_agente.csv` como exemplo de aplicação).

## Quando usar cada seção deste doc

- Criando agente do zero → §1 (Anatomia) + §2 (Templates por seção) + §3 (Templates por etapa).
- Escrevendo/revisando UMA etapa específica → §3.
- Agente reprovou em teste → §4 (Anti-padrões) — ache o sintoma, aplique a correção.
- Montando ou reexecutando a bateria de testes → §5.

---

## 1. Anatomia de um agente por etapas (state machine)

Um agente desse tipo é composto por:

| Campo | Papel | Escopo |
|---|---|---|
| `service_prompt` | Template-mãe que injeta tudo abaixo em ordem: persona → empresa → personalidade → regras → estilo → prompt da etapa atual | Fixo, raramente editado |
| `role` | Quem o agente é: cargo/função + empresa que representa, em 1-2 frases | Persona |
| `mission` | O que ele existe pra fazer nesta conversa: o objetivo funcional, em 1-2 frases | Persona |
| `rules` | Conhecimento institucional: dados da empresa, portfólio/produto, objeções, dados de mercado, **fora do âmbito** | Global, todas as etapas |
| `communication_style` | Tom, ritmo, formato, regras de reconhecimento, exemplos-âncora (bom/mau) | Global, todas as etapas |
| `steps[]` (ordenados) | Cada etapa = 1 estado da conversa. Só a etapa ativa é injetada no prompt do turno. | Local à etapa |
| `knowledge_base` | Documento(s) de referência consultados sob demanda (não fica sempre no prompt) | Sob demanda |

Uma etapa (`step.description`) segue sempre esta estrutura interna:

```
Objetivo: <o que essa etapa entrega>
Saídas: <para quais outras etapas ela pode transitar, e sob qual condição>

### Regras Gerais
<restrições que valem pra qualquer passo desta etapa>

### Passos
#### Passo N: <nome>
Regras: <pré-condição pra este passo disparar>
Objetivo: <o que fazer — pergunta, tool call, update_field, update_step>
Fallback: <o que fazer se a resposta do lead não servir>

### Templates
<mensagens literais reutilizáveis, referenciadas por nome nos Passos>
```

---

## 2. Templates por seção global

### 2.1 `rules` (esqueleto)

```
# Regras e Limitações

## Sobre a EMPRESA
Nome, site, região de atuação, histórico, diferenciais — só fatos verificáveis.

## Portefólio / Produto
Fonte de verdade (tool de busca, KB). 
REGRA CRÍTICA DE GROUNDING: nunca cite nome, característica ou dado de produto que não tenha vindo literalmente do retorno da tool nesta conversa. Proibido inventar.
REGRA CRÍTICA DE PREÇO (se aplicável): nunca informar valor/faixa, mesmo estimado — encaminhar para humano.

## Critérios de objeção
"<objeção comum 1>" → <como responder>
"<objeção comum 2>" → <como responder>

## Fora do âmbito
- <lista explícita do que o agente NUNCA deve tentar resolver sozinho>
- Cada item de "fora do âmbito" que também é um critério de desqualificação (região, orçamento mínimo, etc.) precisa ter um espelho na etapa que faz essa checagem — ver §4.1.
```

### 2.2 `communication_style` (esqueleto)

```
Princípio: <1 frase definindo o tom-alvo>
REGRA DE OURO: o output deve conter APENAS a resposta final ao lead, nada mais (sem raciocínio, sem menção a tools).

Idioma: detectar pela 1ª mensagem do lead, manter até ele mudar.
Canal: <limite de linhas/caracteres do canal>.
No máximo 1 pergunta por mensagem (exceto lead que já respondeu várias coisas de uma vez).
Nunca informar ao lead as ações internas (update_field/update_step/nomes de tool).

## Regras de reconhecimento (acknowledgement)
Padrão: 0 reconhecimentos. Não é hábito, é exceção.
Lead cordial: 1 token breve, sem repetir na mesma mensagem nem em mensagens seguidas.
Momentos sensíveis: 0 reconhecimentos.

## Exemplos (âncoras)
Bom: <exemplo que NÃO abre com reconhecimento — ver §4.6, isso é o erro mais comum>
Mau: <exemplo com floreio, emoji excessivo, ou tom de formulário>
```

---

## 3. Template de etapa (`step.description`)

Copiar e preencher por etapa nova:

```
# <Nome da Etapa>

Objetivo: <1 frase>
Saídas: <EtapaA> (<condição>), <EtapaB> (<condição>)

### Regras Gerais
- <restrição 1>
- <restrição 2>
- Se esta etapa faz um checkpoint de desqualificação (região, orçamento, fit), ele deve ser o PRIMEIRO passo depois de coletar o dado — nunca adiado para depois de outras perguntas (ver §4.1).

### Passos
#### Passo 0 (se a etapa depende de uma tool): Buscar/Consultar
Objetivo: acionar a tool ANTES de decidir como responder. Esta busca é obrigatória — nunca pular direto pro fallback sem tentar.
Fallback: só usar quando a tool genuinamente não retornar nada útil (nunca como primeira opção por padrão — ver §4.2).

#### Passo 1: <ação principal>
Regras: <pré-condição>
Objetivo: <pergunta ou entrega, 1 coisa por vez>
Fallback: <o que fazer com resposta vaga/negativa>

#### Passo N: Decidir rota
Regras: <lead respondeu ao passo anterior>
Objetivo:
- <condição A>: {update_step X}
- <condição B>: {update_field Y} + {update_step Z}
- Se a rota promete uma ação (encaminhar, enviar link, agendar): a tool correspondente tem que ser DISPARADA no mesmo turno, nunca só prometida em texto (ver §4.3).

### Templates
<nome>: "<texto literal, sem placeholder cru — ver §4.5>"
```

---

## 4. Anti-padrões (catálogo de bugs reais + a correção que funciona)

Cada item abaixo foi observado em auditoria real de agente em produção. Use como checklist antes de publicar qualquer etapa nova.

### 4.1 Checagem crítica feita tarde demais
**Sintoma:** lead claramente fora de critério (região não atendida, abaixo do orçamento mínimo) passa por 2-3 perguntas antes de ser desqualificado, ou nunca é.
**Causa:** a regra de desqualificação existe só no ÚLTIMO passo da etapa (ex.: junto com orçamento), mas o dado que dispara ela é coletado num passo anterior (ex.: localização).
**Correção:** mover a checagem pro passo IMEDIATAMENTE seguinte à coleta do dado que a dispara. Nunca acumular checagens pro fim da etapa "por organização".

### 4.2 Escalar para humano como reflexo em vez de última opção
**Sintoma:** agente diz "vou encaminhar para um consultor" na primeira dúvida, sem tentar resolver com as tools que tem.
**Causa:** o fallback de handoff humano não está condicionado a "a tool tentou e não achou nada" — está disponível como saída fácil a qualquer momento de incerteza.
**Correção:** todo fallback de handoff precisa do texto explícito "SOMENTE quando a tool genuinamente não retornar nada" ou equivalente, e o passo anterior tem que deixar claro que acionar a tool é obrigatório antes de decidir.

### 4.3 Prometer ação sem executar a tool
**Sintoma:** a mensagem do lead recebe "vou encaminhar seu contato" mas a lista de ações do turno não tem nenhum `assign_user`/tool correspondente.
**Causa:** a instrução da etapa descreve o texto a dizer, mas não amarra explicitamente "execute a tool no mesmo turno".
**Correção:** toda vez que o texto promete uma ação de sistema, escrever ao lado: "EXECUTE a tool X no mesmo turno — nunca prometa sem acionar."

### 4.4 Alucinação de dado (nome de produto, preço, característica)
**Sintoma:** agente cita produto/valor que não existe em nenhuma fonte real.
**Causa:** a regra de grounding existe só uma vez, longe do ponto onde o agente decide o que dizer; sob incerteza o modelo preenche a lacuna com algo plausível.
**Correção:** repetir a regra de grounding perto de cada Passo que apresenta dado ao lead ("você SÓ pode citar o que veio literalmente do retorno da tool NESTA conversa"), não só na seção global de regras. Regra de preço específica sempre que o domínio tiver preço sensível — mesmo que pareça óbvio, testar isso está no §5.

### 4.5 Placeholder cru vazando pro lead
**Sintoma:** template final contém `{{variavel}}` ou `nome_generico_sem_valor` literal.
**Causa:** template foi escrito com placeholder mas o campo/variável nunca foi de fato ligado a um valor real.
**Correção:** antes de publicar, grep visual em todos os templates por `{{`, `_generico`, `snake_case` solto sem valor. Resolver o valor real ou reescrever o texto sem depender da variável — nunca deixar pro modelo "adivinhar" em runtime (funciona às vezes, não é confiável entre execuções/modelos).

### 4.6 Regra de estilo anulada por um exemplo-âncora contraditório
**Sintoma:** regra explícita ("0 reconhecimentos por padrão") não é seguida de jeito nenhum, mesmo reforçada.
**Causa:** a seção de exemplos ("Bom"/"Mau") tem um exemplo que MODELA o comportamento proibido — o modelo aprende mais forte pelo exemplo do que pela regra escrita.
**Correção:** toda vez que uma regra de estilo for adicionada ou reforçada, auditar TODOS os exemplos-âncora existentes contra ela. Um exemplo contraditório pesa mais que uma frase de regra.

### 4.7 Aceitar valor sem validar contra o que foi oferecido
**Sintoma:** lead responde algo ambíguo (horário sem fuso claro, opção sem repetir o rótulo exato) e o agente "calcula" uma correspondência própria em vez de confirmar.
**Correção:** adicionar regra explícita: "antes de aceitar a resposta do lead, confirme que ela corresponde EXATAMENTE a uma das opções oferecidas no turno anterior; se houver ambiguidade, pergunte antes de prosseguir — nunca resolva a ambiguidade sozinho."

### 4.8 Assumir contexto ambíguo (fuso, idioma, país) de forma inconsistente
**Sintoma:** a mesma pergunta, sem nenhum sinal de contexto, gera respostas diferentes em execuções diferentes (ora assume Brasil, ora Portugal).
**Correção:** regra explícita: "se não houver NENHUM sinal do dado X na conversa, pergunte diretamente — nunca assuma um padrão por default de forma silenciosa."

### 4.9 Vazamento de contexto de outras etapas (info negativa / cross-step)
**Sintoma:** o agente age de forma inconsistente, "narra" regras de roteamento, menciona etapas que não são a dele, ou alucina por causa de instruções que descrevem o que NÃO fazer ou o que acontece em outra etapa.
**Causa:** o prompt da etapa inclui informação que o agente não precisa para executar ESTA etapa — "leads de reativação não passam por aqui", "isso é tratado na etapa X", "o lead não passou por identificação", listas de exclusão, ou a condição de qual etapa a campanha inicia. Só a etapa ativa é injetada no prompt do turno; tudo que fala de fora dela é ruído que o modelo pode interpretar como instrução e agir errado.
**Correção:** cada etapa contém APENAS o que fazer nela, em instruções **positivas** ("faça X quando Y"). Regras válidas de manter: o objetivo da etapa, seus próprios passos e as **Saídas** (para quais etapas ela transita e sob qual condição — isso é a transição dela, não descrição alheia). Regras a REMOVER do texto da etapa:
- "não passa por aqui" / "quem faz isso é a outra etapa" / "o lead não veio de tal etapa";
- pré-condição de ENTRADA da etapa (qual campanha/roteamento leva o lead até ela) — isso é **config de roteamento**, não prompt;
- qualquer estado que descreva o que já aconteceu em etapas anteriores, a menos que a etapa precise dele para agir (aí afirmar o estado de forma positiva: "o lead já tem proposta e os campos X preenchidos", sem citar por onde ele passou).
Onde essa info deve morar: em um doc/comentário de **roteamento e entrada de campanha** para o humano que configura o agente — nunca dentro do `step.description`.

---

## 5. Bateria de testes e evolução

Estrutura de planilha recomendada (uma linha por cenário):

`Teste | Etapa | Criticidade | Output Esperado | Output do Agent (Transcrição Literal) | Resultado (Pass/Fail) | Correção | Observações`

- **Criticidade**: Crítica (quebra o funil ou vaza dado errado ao lead) / Alta / Média / Baixa.
- Cobrir sempre: 1 teste por transição de etapa, 1 por critério de desqualificação, 1 por regra "transversal" (idioma, estilo, reconhecimento, dados sensíveis), e cenários de retomada (lead volta depois de desengajar/desqualificar).
- Rodar com a tool de simulação do builder (dry-run: registra as tools que seriam chamadas, mas NÃO as executa de verdade — testes que dependem do retorno real de uma tool de busca/integração ficam "Não conclusivo" até testar em produção/staging).

**Ao reexecutar após correções, não sobrescrever o histórico:** adicionar colunas novas (`Resultado Batch 2`, `Correção Batch 2`, `Observações 2`, e assim por diante a cada rodada) em vez de substituir as colunas da rodada anterior. Isso preserva o rastro de evolução e evita perder contexto de "o que já foi tentado".

Ao reexecutar, focar nos testes que eram Fail/Parcial/Não conclusivo — testes que já passavam e não foram afetados pela mudança de prompt não precisam ser reexecutados; marcar como "Não retestado (sem mudança de prompt relacionada)" pra deixar claro que não regridiu por falta de checagem.

---

## 6. Checklist final antes de publicar um agente/etapa

- [ ] Toda checagem de desqualificação está no passo mais cedo possível (§4.1)
- [ ] Todo fallback de handoff humano é condicionado, não reflexo (§4.2)
- [ ] Toda promessa de ação tem a tool correspondente amarrada no mesmo turno (§4.3)
- [ ] Regra de grounding repetida perto de cada Passo que apresenta dado real (§4.4)
- [ ] Nenhum placeholder cru sobrando em nenhum template (§4.5)
- [ ] Exemplos-âncora auditados contra as regras de estilo, sem contradição (§4.6)
- [ ] Resposta ambígua do lead sempre validada contra as opções oferecidas antes de prosseguir (§4.7)
- [ ] Contexto ambíguo (fuso/idioma/país) sempre perguntado, nunca assumido em silêncio (§4.8)
- [ ] Nenhuma etapa contém info de escopo alheio / negativa cross-step ("não passa por aqui", "isso é tratado na etapa X") nem a condição de qual etapa a campanha inicia — só instruções positivas do que fazer NELA (§4.9)
- [ ] Bateria de testes cobre toda transição de etapa + toda regra transversal
