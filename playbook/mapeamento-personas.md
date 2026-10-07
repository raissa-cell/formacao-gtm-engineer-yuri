# Mapeamento de personas da Patagon AI

Guia para descobrir, confirmar e priorizar pessoas dentro das empresas aderentes ao ICP. A configuração operacional está em [`../automations/leads/config/personas-patagon.json`](../automations/leads/config/personas-patagon.json) e o formato de registro em [`../automations/leads/schemas/persona-publica.schema.json`](../automations/leads/schemas/persona-publica.schema.json).

## Regra central

Cada fonte pública responde uma pergunta diferente. Encontrar um nome não confirma o cargo; encontrar o cargo não confirma autoridade de compra; uma fala sobre o tema não confirma dor, orçamento ou intenção.

Antes de priorizar uma pessoa, separar:

1. identidade;
2. vínculo atual;
3. cargo exato;
4. senioridade e área;
5. escopo sobre a jornada de leads;
6. papel de compra estimado;
7. evidência e data da verificação.

## O que cada fonte pode responder

| Fonte | Pergunta que responde melhor | Não prova sozinha |
|---|---|---|
| LinkedIn | Quem ocupa o cargo, em qual empresa e com qual senioridade? | Autoridade final, orçamento e dor interna |
| Instagram | Quem aparece ligado à operação, eventos, unidades e liderança local? | Cargo atual sem bio/publicação institucional ou segunda fonte |
| Google | Quem foi nomeado, entrevistado, premiado ou falou publicamente sobre o tema? | Atualidade do vínculo sem conferir data e origem |
| Site da empresa | Quem integra a liderança oficial e qual o escopo divulgado? | Processo interno não publicado |
| Imprensa, eventos e associações | Qual cargo e responsabilidade foram declarados naquela data? | Que a posição continua atual indefinidamente |
| Reddit, reviews e comentários | Como o mercado descreve dores e objeções em voz alta? | Que uma pessoa ou empresa específica possui aquela dor |
| Concorrentes e clientes públicos | Quem compra categoria semelhante e para qual caso de uso? | Intenção de compra do prospect pesquisado |

Reddit, comentários e concorrentes ajudam a escrever hipóteses e perguntas. Não devem ser usados para atribuir uma opinião, reclamação ou problema a alguém.

## Critérios operacionais da pessoa

| Critério | Campo | Resultado |
|---|---|---|
| Vínculo atual confirmado | `current_employment_confirmed` | `sim/nao/nao_verificado` |
| Cargo exato localizado | `title_exact_found` | `sim/nao/nao_verificado` |
| Área relacionada à jornada comercial | `eligible_area` | `sim/nao/nao_verificado` |
| Senioridade | `seniority` | Owner, C-level, VP, diretoria, head, gerência, coordenação, lead ou IC |
| Escopo | `unit_or_region` e `scope_evidence` | Grupo, marca, região, unidade ou `nao_verificado` |
| Papel estimado | `role_estimated` | Decisor, champion, usuário/influenciador, não prioritário ou desconhecido |
| Confiança | `role_confidence` | Alta, média ou baixa |
| Estado final | `status_persona` | T1, T2, T3, não prioritária ou desatualizada |

## Status da persona

- **T1:** vínculo e cargo confirmados; decisor ou champion; escopo aderente; fonte forte.
- **T2:** vínculo e cargo confirmados; papel de compra ou escopo ainda estimado.
- **T3:** nome promissor, mas vínculo, cargo ou escopo precisa de segunda fonte.
- **Não prioritária:** cargo atual confirmado, porém sem relação ou influência sobre a jornada de leads.
- **Desatualizada:** a pessoa saiu da empresa ou mudou de função.

Pessoa não prioritária ou desatualizada não elimina a empresa. A ação correta é buscar outro contato.

## Persona automotiva

### Prioridade 1 — decisores

- proprietário, sócio ou presidente;
- CEO ou diretor executivo;
- diretor comercial;
- diretor de marketing;
- diretor de operações;
- diretor de negócios ou digital;
- head comercial, de marketing ou growth.

### Prioridade 2 — champions

- gerente comercial, geral ou regional;
- gerente/coordenador de CRM ou BDC;
- gerente de vendas digitais ou e-commerce;
- gerente de marketing ou performance;
- gerente de relacionamento ou central de leads;
- coordenador comercial.

### Usuários e influenciadores

- líder de BDC ou central de atendimento;
- pré-vendas;
- gestor de loja;
- equipe de CRM;
- consultores e vendedores.

### Onde encontrar no automotivo

1. LinkedIn para diretorias, heads e cargos corporativos.
2. Instagram do grupo e das unidades para proprietários, gerentes locais, marcações, premiações, eventos e inaugurações.
3. Site oficial e páginas “quem somos”, imprensa e diretoria.
4. Google com nome do grupo, marca, cidade e cargo.
5. Montadoras, associações, eventos e premiações para confirmar vínculo e responsabilidade.

Se a descoberta começar no Instagram, confirmar cargo e vínculo na bio profissional, em publicação institucional ou em uma segunda fonte.

## Persona de SaaS e plataformas B2B

### Prioridade 1 — decisores

- CRO, VP/Diretor/Head de Vendas ou Comercial;
- CMO, VP/Diretor de Marketing ou Head de Growth;
- Diretor/Head de Aquisição de Parceiros;
- Diretor de Operações ou COO;
- CEO ou fundador em operações menores.

### Prioridade 2 — champions

- gerente/head de SDR ou pré-vendas;
- RevOps ou Sales Ops;
- gerente de Growth, Performance ou CRM;
- gerente de aquisição, onboarding ou ativação de parceiros;
- gerente de vendas SMB ou operações comerciais.

Para plataformas parecidas com iFood, procurar termos como `merchant acquisition`, `partner growth`, `partner activation`, `SMB sales`, `commercial operations` e equivalentes em português.

## Hipóteses por função

Estas conexões ajudam a personalizar, mas continuam sendo hipóteses até a pessoa confirmar.

| Função | KPI provável | Ponte com a Patagon AI |
|---|---|---|
| Direção comercial/revenue | Conversão, pipeline, produtividade e receita | Qualificação e acompanhamento antes de envolver o time comercial |
| Marketing/Growth/Performance | Aproveitamento dos leads de Ads, CPL até oportunidade e velocidade | Continuidade entre aquisição paga e conversa no WhatsApp |
| CRM/BDC/RevOps/Sales Ops | SLA, contato, distribuição, dados e follow-up | Padronização, contexto e encaminhamento das oportunidades |
| Gerência regional/geral | Resultado por unidade, capacidade e consistência | Distribuição e acompanhamento entre lojas ou equipes |
| Aquisição/ativação de parceiros | Cadastro, ativação, conclusão do onboarding e conversão | Conversa e acompanhamento em escala para parceiros/PMEs |

Nunca escrever “vocês sofrem com X” com base apenas no cargo. Transformar a hipótese em uma pergunta ligada a um fato verificável da empresa.

## Consultas reutilizáveis

```text
site:linkedin.com/in "NOME DA EMPRESA" "diretor comercial"
site:linkedin.com/in "NOME DA EMPRESA" (CRM OR BDC OR "gerente comercial")
site:instagram.com "MARCA OU UNIDADE" (diretor OR gerente OR proprietário)
site:instagram.com "MARCA OU UNIDADE" (inauguração OR premiação OR equipe)
site:DOMINIO-DA-EMPRESA (diretoria OR equipe OR liderança OR imprensa)
"NOME DA PESSOA" "NOME DA EMPRESA" (diretor OR gerente OR head)
"NOME DA EMPRESA" (nomeia OR anuncia OR inaugura) (diretor OR gerente OR head)
```

## Evidência mínima

Para T1 ou T2, registrar:

- nome completo;
- empresa atual;
- cargo exatamente como publicado;
- unidade, região ou escopo quando aplicável;
- URL do perfil ou publicação;
- tipo da fonte;
- o que aquela fonte confirma;
- data da verificação;
- confiança do papel de compra estimado.

Dados de pessoas reais e listas de leads continuam fora do Git. O repositório guarda apenas configuração, schema e método.
