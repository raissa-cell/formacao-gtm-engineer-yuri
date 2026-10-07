# Atividade feita — ICP, personas e fontes públicas da Patagon AI

**Data:** 07/10/2026  
**Módulo relacionado:** Dia 02 — Sourcing  
**Status:** concluída e salva no repositório  
**Responsável:** Raissa

## Objetivo

Transformar o ICP da Patagon AI em critérios pesquisáveis, verificáveis e reutilizáveis para criação de listas, enriquecimento e priorização de contas e pessoas.

## Contexto utilizado

- A Patagon AI atende, qualifica e acompanha novos leads pelo WhatsApp antes de envolver o time comercial.
- O ICP automotivo prioriza grupos com concessionárias autorizadas organizadas por bandeira e quatro ou mais unidades comerciais.
- As operações precisam gerar demanda por Ads e receber volume relevante de novos leads pelo WhatsApp, mas volume, investimento e uso real do canal só podem ser confirmados na discovery.
- O ICP secundário inclui plataformas B2B de aquisição de PMEs em escala e SaaS B2B/B2C high ticket com venda assistida.
- Grupo Navesa e iFood para Parceiros foram usados como contas-âncora para calibrar os dois perfis.

## O que foi feito

### 1. ICP da empresa

- Separação entre fit público de prospecção e fit validado em discovery.
- Definição de gates automotivos verificáveis:
  - concessionária autorizada;
  - operação organizada por bandeira;
  - quatro ou mais unidades comerciais ativas.
- Ads, WhatsApp público, estrutura comercial e persona encontrada passaram a ser sinais públicos de prioridade.
- Volume de leads, investimento, processo, equipe e dor ficaram para discovery.
- Uso dos estados `sim`, `nao` e `nao_verificado`, evitando transformar ausência de evidência em resposta negativa.
- Separação entre desqualificador da empresa e contato inadequado.

Documento: [`../../playbook/icp-patagon-ai.md`](../../playbook/icp-patagon-ai.md).

### 2. Mapeamento das marcas automotivas

- Mapeamento de 23 marcas presentes no Brasil.
- Divisão em 13 marcas de prioridade inicial e 10 de expansão/premium.
- Registro de aliases, sites oficiais, localizadores de concessionárias, modo de busca e sinais comerciais.
- Consultas reutilizáveis para Google, sites, Instagram e LinkedIn.
- Regras para não contar oficinas, peças, seminovos no mesmo endereço ou duplicidades como novas unidades comerciais.
- Confirmação de autorização pela montadora antes de contabilizar a unidade.

Arquivos:

- [`../../playbook/mapeamento-marcas-automotivas.md`](../../playbook/mapeamento-marcas-automotivas.md)
- [`../../automations/leads/config/marcas-automotivas-br.json`](../../automations/leads/config/marcas-automotivas-br.json)
- [`../../automations/leads/schemas/concessionaria-web.schema.json`](../../automations/leads/schemas/concessionaria-web.schema.json)

### 3. Personas

- Mapeamento de decisores, champions e usuários/influenciadores para automotivo e SaaS/plataformas.
- Inclusão de proprietários, presidentes, diretorias, gerências comerciais, CRM, BDC, vendas digitais, performance, RevOps e aquisição/ativação de parceiros.
- Definição do que LinkedIn, Instagram, Google, sites, imprensa, eventos, Reddit e concorrentes podem ou não comprovar.
- Regra de segunda fonte para cargo ou vínculo descoberto pelo Instagram.
- Classificação das pessoas em:
  - T1: forte e confirmada;
  - T2: confirmada, com papel ou escopo estimado;
  - T3: precisa de segunda fonte;
  - não prioritária;
  - desatualizada.
- Separação entre fato público e hipótese de dor/KPI.

Arquivos:

- [`../../playbook/mapeamento-personas.md`](../../playbook/mapeamento-personas.md)
- [`../../automations/leads/config/personas-patagon.json`](../../automations/leads/config/personas-patagon.json)
- [`../../automations/leads/schemas/persona-publica.schema.json`](../../automations/leads/schemas/persona-publica.schema.json)

## Fontes e perguntas

| Fonte | Principal pergunta respondida |
|---|---|
| Localizador da montadora | A unidade é autorizada e possui vendas? |
| Google e Google Maps | Quais empresas e unidades existem nessa região? |
| Site do grupo/unidade | Quem controla a operação e quais sinais comerciais aparecem? |
| LinkedIn | Quem ocupa o cargo e em qual empresa? |
| Instagram | Quem aparece ligado à liderança, unidade, evento ou inauguração? |
| Imprensa, eventos e associações | Qual cargo e responsabilidade foram declarados naquela data? |
| Reddit, reviews e comentários | Como o mercado descreve dores e objeções? |
| Concorrentes e clientes públicos | Quais casos de uso e categorias semelhantes já são comprados? |

Reddit, comentários e concorrentes servem para linguagem e hipóteses. Não comprovam que uma pessoa ou empresa específica possui aquela dor ou intenção de compra.

## Decisões importantes

1. Grupo com várias montadoras pode pertencer ao ICP quando opera concessionárias autorizadas separadas por bandeira.
2. Revenda multimarcas independente permanece fora do ICP automotivo.
3. Google Maps é fonte de descoberta, não confirmação final de autorização.
4. WhatsApp público confirma a presença do canal, mas não volume nem uso efetivo.
5. “WhatsApp usado somente para suporte/pós-venda” foi removido dos desqualificadores pré-call porque não é verificável publicamente.
6. Pessoa inadequada não elimina a empresa; outro contato deve ser procurado.
7. Cargo, atividade pública ou reclamação de mercado não comprovam dor, orçamento ou autoridade final.

## Validações realizadas

- JSON das marcas e das personas validado sintaticamente.
- IDs das 23 marcas verificados sem duplicidade.
- Schemas de empresa/unidade e pessoa criados separadamente.
- Links entre ICP, mapeamentos, configurações e schemas adicionados.
- Materiais integrados ao playbook da campanha de concessionárias.

## Commits relacionados

- `250bdec` — revisão do ICP e das personas por evidências públicas.
- `53b7023` — mapeamento de marcas e schema de concessionárias.
- `5d72f86` — mapeamento de personas e fontes públicas.

## Resultado

A Patagon AI agora possui uma definição operacional de ICP e persona que pode orientar pesquisa manual, planilhas, Nuvia e futuras automações sem depender de achismo ou de informação impossível de obter antes da call.

## Próximos passos

- executar o sourcing da primeira lista real usando as marcas prioritárias;
- testar o schema com grupos e unidades reais;
- localizar duas ou três personas por conta;
- classificar empresas em P1/P2/P3 e pessoas em T1/T2/T3;
- validar volume, Ads, WhatsApp, equipe e dor durante a discovery;
- ajustar critérios conforme conversão e qualidade das reuniões.

Nenhuma mensagem foi enviada e nenhuma lista real de pessoas foi adicionada ao Git nesta atividade.
