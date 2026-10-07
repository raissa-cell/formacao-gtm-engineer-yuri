# ICP da Patagon AI

Documento de referência para pesquisa, enriquecimento, qualificação e campanhas. A classificação deve ser feita primeiro no nível da **empresa** e depois no nível da **pessoa**.

## 1. Posicionamento usado na qualificação

A Patagon AI atende, qualifica e acompanha novos leads pelo WhatsApp, preservando o contexto da conversa até o momento certo de envolver o time comercial.

O melhor fit não é uma empresa que apenas possui WhatsApp. É uma operação que:

- gera demanda por mídia paga;
- recebe novos leads comerciais pelo WhatsApp;
- precisa responder, qualificar, acompanhar e distribuir esse volume;
- possui estrutura humana para assumir as oportunidades qualificadas.

## 2. ICP primário — grupos de concessionárias autorizadas

### Definição

Grupos ou redes com concessionárias autorizadas organizadas por marca/bandeira, com **quatro ou mais unidades** no grupo, aquisição ativa por Ads e volume recorrente de novos leads entrando pelo WhatsApp.

O grupo pode representar várias montadoras. O que caracteriza o fit é operar concessionárias oficiais e jornadas comerciais próprias para cada marca — não funcionar como uma revenda independente que mistura veículos de várias marcas no mesmo modelo de loja. Na personalização, a abordagem pode partir do grupo e usar uma bandeira, região ou operação específica como gancho.

### Critérios da empresa

| Critério | Campo | Regra | Fonte preferencial |
|---|---|---|---|
| Segmento | `segmento` | Concessionária/rede autorizada automotiva | Site oficial, LinkedIn da empresa, página da montadora |
| Modelo de operação | `modelo_operacao` | `concessionarias_autorizadas_por_marca` | Site do grupo, páginas das unidades e localizador oficial da montadora |
| Marcas trabalhadas | `marcas_representadas` | Uma ou mais montadoras identificadas | Site e redes oficiais |
| Número de unidades | `unidades_ativas` | **Maior ou igual a 4** | Localizador oficial, site da rede, páginas das unidades |
| Ads ativos | `ads_ativos` | `sim` | Meta Ad Library, Google Ads Transparency Center, landing pages de campanha |
| Entrada comercial no WhatsApp | `whatsapp_novos_leads` | `sim` | CTA do site/landing page, botão de campanha ou teste manual do fluxo |
| Volume de novos leads | `leads_novos_whatsapp_mes` | Acima do corte comercial da Patagon | CRM, Nuvia, WhatsApp Business, plataforma de Ads ou informação declarada pelo prospect |
| Estrutura para assumir oportunidades | `estrutura_comercial` | Time de vendas, BDC, pré-vendas ou atendimento comercial identificável | LinkedIn, vagas, organograma ou informação declarada |

**Importante:** anúncio ativo confirma investimento em mídia, mas não confirma o valor investido. Da mesma forma, um botão de WhatsApp confirma o canal, mas não o volume. Quando o dado exato não for público, registrar como `nao_verificado` e validar na descoberta.

### ICP pessoa

| Papel | Cargos prioritários | Senioridade / área | Papel na compra |
|---|---|---|---|
| Decisor econômico | Diretor Comercial, Diretor de Marketing, Diretor de Operações, Head Comercial, Head de Marketing/Growth, CEO ou proprietário da rede | Diretoria/C-level; Vendas, Marketing ou Operações | Decide, aprova orçamento e assina |
| Champion | Gerente Comercial, Gerente de CRM/BDC, Gerente de Marketing/Performance, Coordenador Comercial | Gerência/coordenação; Vendas, CRM ou Marketing | Sente a dor, constrói o caso e influencia |
| Usuário | Líder de BDC/pré-vendas, SDR, atendimento comercial, vendedores e gestores de loja | Operação/gerência | Opera ou recebe os leads qualificados |

Campos obrigatórios da pessoa: `cargo`, `senioridade`, `area`, `papel_na_compra`, `tempo_no_cargo_meses` e `atividade_publica_relevante`.

Sinais úteis de timing: entrada recente no cargo, expansão de unidades, lançamento de uma marca/modelo, contratação para CRM/BDC/performance, campanha ativa de test-drive ou menções públicas a atendimento, conversão e velocidade de resposta.

### Hipóteses de dor para pesquisar — não afirmar sem evidência

- demora no primeiro atendimento após o lead de Ads;
- distribuição manual entre unidades ou vendedores;
- qualificação inconsistente antes de envolver o vendedor;
- perda de contexto e follow-up entre WhatsApp, CRM e equipe comercial;
- capacidade do time não acompanhar picos de campanha.

### Desqualificadores

- revenda multimarcas independente, sem operação autorizada organizada por bandeira;
- menos de quatro unidades na rede/operação abordada;
- ausência de aquisição paga ativa;
- WhatsApp usado apenas para suporte ou pós-venda, sem entrada de novos leads;
- baixo volume ou volume ainda não validado para justificar automação;
- ausência de equipe comercial para assumir as oportunidades;
- contato sem responsabilidade sobre demanda, atendimento, CRM, vendas ou orçamento.

## 3. ICP secundário — plataformas B2B e SaaS com aquisição assistida

### Definição

Há dois subperfis válidos:

1. **Plataformas B2B de alto volume para PMEs**, marketplaces ou ecossistemas de tecnologia que precisam adquirir, cadastrar, ativar ou qualificar muitos estabelecimentos parceiros — como restaurantes, lojas e prestadores.
2. **SaaS B2B ou B2C high ticket**, com venda assistida, novos leads entrando pelo WhatsApp, time de SDR/pré-vendas e investimento mensal em Ads superior a **R$ 10 mil**.

Nos dois casos, o fit da Patagon depende de existir uma jornada comercial ou de aquisição de parceiros com conversa, qualificação e acompanhamento. Uma plataforma puramente self-service, sem etapa conversacional relevante, não entra apenas por ter grande volume.

### Critérios da empresa

| Critério | Campo | Regra | Fonte preferencial |
|---|---|---|---|
| Segmento | `segmento` | `plataforma_b2b_pmes`, `marketplace_b2b`, `saas_b2b` ou `saas_b2c` | Site, página de produto, LinkedIn da empresa |
| Público atendido | `publico_cliente` | PMEs/parceiros em escala ou compradores de solução high ticket | Site, cases e páginas de cadastro |
| Modelo comercial | `modelo_venda` | Aquisição/ativação assistida, demo, diagnóstico ou consultoria | Site, formulário, página de preços e fluxo comercial |
| Ticket | `ticket_medio` | Obrigatório para o subperfil SaaS high ticket; não é gate isolado para plataforma B2B de volume | Página de preços, proposta pública ou informação declarada |
| Entrada pelo WhatsApp | `whatsapp_novos_leads` | `sim` | Site, landing page, anúncio ou teste manual do fluxo |
| Estrutura de aquisição | `possui_sdr` | SDR, pré-vendas, aquisição/ativação de parceiros ou time equivalente | LinkedIn, vagas, página do time ou informação declarada |
| Investimento em Ads | `investimento_ads_mes` | **Maior que R$ 10.000/mês** para SaaS; em plataformas, validar mídia e volume da jornada pesquisada | Conta de Ads, agência, relatório ou informação declarada pelo prospect |
| Ads ativos — proxy | `ads_ativos` | `sim` | Meta Ad Library, Google Ads Transparency Center e landing pages |

O valor de mídia e o ticket precisam de fonte direta. Bibliotecas públicas de anúncios servem como sinal de atividade, não como comprovação de investimento superior a R$ 10 mil.

### ICP pessoa

| Papel | Cargos prioritários | Papel na compra |
|---|---|---|
| Decisor econômico | CRO, VP/Head/Diretor de Vendas, Growth, Marketing, Aquisição de Parceiros ou Operações; COO ou CEO/fundador | Decide, aprova orçamento e assina |
| Champion | Gerente de SDR/Pré-vendas, RevOps, Sales Ops, Growth/Performance, CRM, Aquisição ou Ativação de Parceiros | Sente a dor, avalia e influencia |
| Usuário | SDRs, BDRs, inside sales, consultores e equipes de onboarding/ativação de parceiros | Opera ou recebe as oportunidades qualificadas |

### Desqualificadores

- produto low ticket ou venda self-service sem volume e sem etapa conversacional relevante;
- ausência de SDR/pré-vendas ou de time equivalente de aquisição/ativação de parceiros;
- WhatsApp usado somente para suporte;
- investimento comprovado de Ads igual ou inferior a R$ 10 mil/mês;
- falta de volume de novos leads;
- negócio de serviço ou e-commerce classificado incorretamente como SaaS.

## 4. Regra de classificação

### A — prioridade imediata

Todos os critérios obrigatórios da empresa foram confirmados por fonte, existe decisor ou champion aderente e o volume de leads foi validado.

### B — bom fit, requer descoberta

Os critérios públicos centrais foram confirmados, mas volume, ticket ou investimento ainda dependem de validação direta. Há proxies fortes, nunca números inventados.

### C — hipótese

Há aderência parcial, porém faltam dois ou mais dados essenciais. Enriquecer antes de personalizar ou abordar.

### Fora do ICP

Falha em um critério estrutural: segmento/modelo inadequado, menos de quatro unidades no ICP automotivo, ausência de SDR ou time equivalente no ICP secundário, ausência de entrada comercial pelo WhatsApp ou outro desqualificador.

## 5. Campos mínimos para a base

```text
empresa
site
linkedin_empresa
icp_tipo
segmento
modelo_operacao
marcas_representadas
unidades_ativas
modelo_venda
ticket_medio
ads_ativos
investimento_ads_mes
whatsapp_novos_leads
leads_novos_whatsapp_mes
possui_sdr
estrutura_comercial
nome_contato
linkedin_contato
cargo
senioridade
area
papel_na_compra
tempo_no_cargo_meses
atividade_publica_relevante
classificacao_icp
fonte_por_criterio
data_verificacao
confianca
proxima_acao
```

Valores desconhecidos devem ser registrados como `nao_verificado`, nunca preenchidos por suposição. Cada critério deve guardar a URL ou a origem do dado e a data da verificação.

## 6. Ordem operacional

1. Qualificar a empresa pelos critérios obrigatórios.
2. Registrar campo, fonte, data e nível de confiança.
3. Encontrar decisor, champion e possíveis usuários.
4. Buscar um fato verificável da empresa e uma responsabilidade real do cargo.
5. Formular a dor como hipótese quando ela não estiver explicitamente confirmada.
6. Só então criar lista, mensagem ou campanha.

O script atual `automations/leads/triagem_icp.py` classifica pessoas por palavras-chave de cargo. Ele não substitui esta qualificação de conta e não deve, sozinho, decidir se uma empresa pertence ao ICP da Patagon.

## 7. Pontos ainda a definir com dados reais

- corte mínimo de `leads_novos_whatsapp_mes` para concessionárias e SaaS;
- valor mínimo de ticket para considerar o SaaS high ticket;
- janela de validade de cada fonte;
- meta de conversão e capacidade máxima de atendimento por segmento.

Esses cortes devem ser definidos a partir dos clientes que mais convertem, permanecem e extraem valor da Patagon — não por uma estimativa sem histórico.

## 8. Contas-âncora para calibrar a pesquisa

| Conta | O que ela ensina sobre o ICP | O que ainda precisa ser validado antes da abordagem |
|---|---|---|
| [Grupo Navesa](https://www.navesa.com.br/) | Grupo com 12 lojas e operações autorizadas separadas por marcas como Ford, Renault, Peugeot, Citroën, GWM e GAC. Confirma que um grupo pode ser multimarca no portfólio e ainda pertencer ao ICP. | Ads ativos, volume de novos leads no WhatsApp, estrutura de distribuição e qual bandeira/região oferece o melhor gancho. |
| [iFood para Parceiros](https://parceiros.ifood.com.br/) | Plataforma B2B de aquisição em escala, voltada principalmente a restaurantes e outros pequenos e médios estabelecimentos. Confirma o subperfil de plataforma para PMEs. | Existência de entrada comercial pelo WhatsApp, atuação de SDR/aquisição assistida, mídia da jornada de parceiros e ponto em que uma conversa automatizada agrega valor. |

Conta-âncora descreve o **tipo de operação desejado**; não significa aprovação automática. Os gates continuam sendo verificados por campo e fonte.
