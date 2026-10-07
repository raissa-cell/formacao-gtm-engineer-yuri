# ICP e personas da Patagon AI

Documento de referência para pesquisa, enriquecimento, qualificação e campanhas. A classificação acontece primeiro no nível da **empresa** e depois no nível da **pessoa**.

## 1. Posicionamento usado na qualificação

A Patagon AI atende, qualifica e acompanha novos leads pelo WhatsApp, preservando o contexto da conversa até o momento certo de envolver o time comercial.

O melhor fit é uma operação que:

- gera demanda por mídia paga;
- recebe novos leads comerciais pelo WhatsApp;
- precisa responder, qualificar, acompanhar e distribuir esse volume;
- possui estrutura humana para assumir as oportunidades qualificadas.

## 2. Princípio de pesquisa: público não é discovery

O ICP possui duas etapas independentes:

1. **Fit público de prospecção:** usa apenas informações que podem ser encontradas antes da abordagem.
2. **Fit validado em discovery:** confirma volume, investimento, processo, equipe e dor diretamente com o prospect.

Na pesquisa, usar somente estes estados:

- `sim`: existe evidência pública;
- `nao`: existe evidência pública que nega o critério;
- `nao_verificado`: a informação não foi localizada.

`nao_verificado` nunca deve ser convertido automaticamente em `nao`. Um anúncio, uma landing page ou um número de WhatsApp pode não estar indexado publicamente.

## 3. ICP primário — grupos de concessionárias autorizadas

### Definição

Grupos ou redes com concessionárias autorizadas organizadas por marca/bandeira e **quatro ou mais unidades comerciais ativas** no grupo.

O grupo pode representar várias montadoras. O que caracteriza o fit é operar concessionárias oficiais e jornadas próprias para cada marca — não funcionar como uma revenda independente que mistura veículos de várias marcas no mesmo modelo de loja.

### Filtros públicos para montar a lista

| Critério verificável | Campo | Regra | Fonte |
|---|---|---|---|
| É concessionária autorizada? | `concessionaria_autorizada` | `sim/nao/nao_verificado` | Localizador da montadora, site do grupo |
| A operação é organizada por bandeira? | `operacao_por_bandeira` | `sim/nao/nao_verificado` | Site, página da unidade, Instagram oficial |
| Possui pelo menos quatro unidades comerciais? | `unidades_comerciais_ativas` | Número inteiro ou `nao_verificado`; gate `>=4` quando confirmado | Site, Google Maps, Google, localizador da montadora |
| Foram localizados anúncios ativos? | `ads_ativos_detectados` | `sim/nao_verificado` | Meta Ad Library, Google Ads Transparency, landing pages |
| Foi localizado WhatsApp em contexto comercial? | `whatsapp_comercial_publico` | `sim/nao_verificado` | Site, oferta, landing page, Instagram, Google Business |
| Foi localizada estrutura comercial? | `estrutura_comercial_publica` | `sim/nao_verificado` | LinkedIn, Instagram, vagas, site, imprensa |
| Foi encontrada uma persona prioritária? | `persona_prioritaria_encontrada` | `sim/nao_verificado` | LinkedIn, Instagram, Google, site, imprensa |

Gates estruturais para entrar na lista:

- `concessionaria_autorizada = sim`;
- `operacao_por_bandeira = sim`;
- `unidades_comerciais_ativas >= 4`.

Ads, WhatsApp público, estrutura comercial e persona encontrada aumentam a prioridade, mas sua ausência pública não elimina a conta.

### Como pesquisar a empresa

- **Google:** pesquisar grupo, marcas representadas, cidades, expansão e páginas das unidades.
- **Google Maps:** descobrir endereços e unidades. Confirmar depois no site ou localizador da montadora para não contar oficina, peças, seminovos ou endereço duplicado como nova unidade comercial.
- **Site da montadora:** confirmar autorização e vínculo por bandeira.
- **Site e Instagram do grupo/unidade:** confirmar marcas, ofertas, WhatsApp, campanhas, inaugurações e estrutura comercial.
- **Meta e Google:** detectar mídia ativa. Anúncio não encontrado significa `nao_verificado`, não ausência comprovada de Ads.

Um botão de WhatsApp prova a existência pública do canal, mas não prova volume nem como ele é usado.

### Persona automotiva

| Papel estimado | Cargos prioritários | Prioridade |
|---|---|---|
| Decisor econômico | Proprietário, sócio, presidente, CEO, diretor executivo, diretor comercial, diretor de marketing, diretor de operações, diretor de negócios/digital, head comercial/marketing/growth | 1 |
| Champion | Gerente comercial, gerente geral/regional, gerente ou coordenador de CRM/BDC, vendas digitais/e-commerce, marketing/performance, relacionamento/central de leads, coordenador comercial | 2 |
| Usuário/influenciador | Líder de BDC/central de atendimento, pré-vendas, gestor de loja, equipe de CRM, consultores e vendedores | 3 |

#### Onde encontrar as pessoas

- **LinkedIn:** melhor para diretorias, heads e funções corporativas.
- **Instagram:** relevante no automotivo para proprietários, diretores, gerentes gerais, comerciais e gestores de loja. Usar bio, marcações, eventos, premiações e inaugurações.
- **Site oficial:** páginas institucionais, “quem somos”, imprensa e diretoria.
- **Google e imprensa local/setorial:** nomeações, entrevistas, expansão e eventos.
- **Montadoras, associações e premiações:** confirmação adicional de vínculo e cargo.

Um perfil no Instagram pode revelar a pessoa, mas cargo e vínculo devem ser confirmados na bio profissional, em publicação institucional ou em uma segunda fonte.

#### Campos da pessoa

Obrigatórios para prospecção:

```text
nome_contato
cargo_exato
empresa
unidade_ou_regiao
area
url_perfil
canal_fonte
fonte_do_cargo
data_verificacao
papel_compra_estimado
confianca_papel_compra
```

Opcionais para timing e personalização:

```text
tempo_no_cargo_meses
atividade_publica_relevante
```

O papel na compra é uma estimativa antes da call. Não tratá-lo como fato confirmado.

O método completo de pesquisa, confirmação e priorização está no [mapeamento de personas](mapeamento-personas.md).

### Confirmar na discovery

- entrada de novos leads comerciais pelo WhatsApp e volume mensal;
- origem e percentual de leads vindos de Ads;
- investimento mensal em mídia;
- tempo de primeira resposta;
- distribuição por unidade ou vendedor;
- processo de qualificação e follow-up;
- capacidade do time para assumir oportunidades;
- CRM, ferramentas e integrações;
- gargalo e impacto real na operação.

### Hipóteses de dor — não afirmar sem evidência

- demora no primeiro atendimento após o lead de Ads;
- distribuição manual entre unidades ou vendedores;
- qualificação inconsistente antes de envolver o vendedor;
- perda de contexto e follow-up entre WhatsApp, CRM e equipe comercial;
- capacidade do time não acompanhar picos de campanha.

### Desqualificadores da empresa

**Antes da call, somente quando comprovado:**

- não é concessionária autorizada;
- é revenda multimarcas independente, sem operação autorizada por bandeira;
- possui menos de quatro unidades comerciais ativas;
- o vínculo com o grupo ou com a bandeira foi comprovadamente negado.

**Após a discovery:**

- não recebe volume relevante de novos leads comerciais pelo WhatsApp;
- não investe em aquisição paga;
- não possui equipe para assumir oportunidades qualificadas;
- o volume não justifica automação;
- não existe um problema de atendimento, qualificação, acompanhamento ou distribuição que a Patagon resolva;
- não há prioridade, orçamento ou capacidade operacional.

## 4. ICP secundário — plataformas B2B e SaaS com aquisição assistida

### Definição

Há dois subperfis válidos:

1. **Plataformas B2B de alto volume para PMEs:** marketplaces ou ecossistemas de tecnologia que precisam adquirir, cadastrar, ativar ou qualificar muitos estabelecimentos parceiros, como restaurantes, lojas e prestadores.
2. **SaaS B2B ou B2C high ticket:** venda assistida, fluxo de entrada comercial e time de SDR/pré-vendas, com investimento mensal em Ads superior a **R$ 10 mil**.

Nos dois casos precisa existir uma jornada comercial ou de aquisição de parceiros com conversa, qualificação e acompanhamento. Uma plataforma puramente self-service, sem etapa conversacional relevante, não entra apenas por ter grande volume.

### Filtros públicos para montar a lista

| Critério verificável | Campo | Regra pública | Fonte |
|---|---|---|---|
| Qual é o segmento? | `segmento` | `saas_b2b`, `saas_b2c` ou `plataforma_b2b_pmes` | Site, LinkedIn |
| O segmento pertence ao recorte? | `segmento_elegivel` | `sim/nao/nao_verificado` | Site, LinkedIn |
| Atende PMEs ou parceiros em escala? | `publico_pme_parceiros` | `sim/nao/nao_verificado` | Site, cases, página de produto |
| Há evidência pública de high ticket? | `perfil_high_ticket_publico` | `sim/nao/nao_verificado` | Preços, oferta, cases e fluxo de vendas |
| Existe venda ou ativação assistida visível? | `venda_assistida_visivel` | `sim/nao/nao_verificado` | Demo, diagnóstico, consultor, “fale com vendas”, onboarding |
| Foi localizado WhatsApp comercial? | `whatsapp_comercial_publico` | `sim/nao_verificado` | Site, landing page, anúncio, Instagram |
| Foi localizado SDR ou time equivalente? | `time_aquisicao_publico` | `sim/nao_verificado` | LinkedIn, vagas, site |
| Foram localizados Ads ativos? | `ads_ativos_detectados` | `sim/nao_verificado` | Meta Ad Library, Google Ads Transparency, landing pages |
| Foi encontrada persona prioritária? | `persona_prioritaria_encontrada` | `sim/nao_verificado` | LinkedIn, site, Google, imprensa |

Para plataformas como iFood, “time equivalente” pode ser aquisição, ativação, onboarding ou vendas para parceiros. Não exigir literalmente o título SDR.

Não são dados públicos confiáveis e devem ir para discovery:

- investimento superior a R$ 10 mil/mês;
- volume mensal de novos leads;
- `ticket_medio_confirmado` quando não há preço público;
- uso efetivo do WhatsApp na jornada;
- tamanho e capacidade reais do time.

### Persona de plataformas e SaaS

| Papel estimado | Cargos prioritários |
|---|---|
| Decisor econômico | CRO, VP/Head/Diretor de Vendas, Growth, Marketing, Aquisição de Parceiros ou Operações; COO, CEO ou fundador |
| Champion | Gerente de SDR/Pré-vendas, RevOps, Sales Ops, Growth/Performance, CRM, Aquisição, Onboarding ou Ativação de Parceiros |
| Usuário/influenciador | SDR, BDR, inside sales, consultores e equipes de onboarding/ativação de parceiros |

LinkedIn, página do time, vagas, eventos, entrevistas e imprensa são as fontes prioritárias. Aplicam-se os mesmos campos obrigatórios e opcionais definidos para a persona automotiva.

Consultar também o [mapeamento de personas](mapeamento-personas.md) para cargos normalizados, consultas e evidência mínima.

### Desqualificadores da empresa

**Antes da call, somente quando comprovado:**

- não é SaaS nem plataforma elegível;
- possui venda comprovadamente low ticket e puramente self-service;
- é negócio de serviço ou e-commerce classificado incorretamente como SaaS/plataforma.

**Após a discovery:**

- não recebe volume relevante de novos leads comerciais pelo WhatsApp;
- no subperfil SaaS, não investe mais de R$ 10 mil/mês em Ads;
- não possui venda assistida nem equipe para assumir oportunidades;
- o volume não justifica automação;
- não existe problema aderente à Patagon;
- não há prioridade, orçamento ou capacidade operacional.

## 5. Pessoa inadequada não elimina a empresa

Marcar a pessoa como `nao_prioritaria` e continuar procurando outro contato quando:

- não possui responsabilidade ou influência sobre vendas, marketing, CRM, atendimento comercial, operações ou orçamento;
- o vínculo ou cargo está desatualizado;
- atua em área sem relação com a jornada de leads;
- é apenas usuário operacional quando o objetivo é falar com champion ou decisor.

## 6. Classificação em duas etapas

### `status_prospeccao`

- **P1:** gates estruturais confirmados, Ads, WhatsApp comercial, estrutura comercial e persona prioritária detectados.
- **P2:** gates estruturais confirmados, mas um ou mais sinais públicos de prioridade ainda não foram localizados.
- **P3:** conta aparentemente aderente, porém exige enriquecimento dos gates estruturais.
- **Não priorizar:** falhou em critério estrutural confirmado.

### `status_discovery`

- **A:** volume, aquisição, WhatsApp, equipe e dor confirmados.
- **B:** bom fit, mas falta confirmar um critério econômico ou operacional.
- **C:** aderência parcial ou timing fraco.
- **Fora:** falhou em um gate confirmado na conversa.

## 7. Campos mínimos para a base

```text
empresa
site
linkedin_empresa
instagram_empresa
google_maps_url
icp_tipo
segmento
segmento_elegivel
concessionaria_autorizada
operacao_por_bandeira
marcas_representadas
unidades_comerciais_ativas
publico_pme_parceiros
perfil_high_ticket_publico
venda_assistida_visivel
ads_ativos_detectados
whatsapp_comercial_publico
estrutura_comercial_publica
time_aquisicao_publico
persona_prioritaria_encontrada
nome_contato
cargo_exato
empresa_contato
unidade_ou_regiao
area
url_perfil
canal_fonte
fonte_do_cargo
papel_compra_estimado
confianca_papel_compra
tempo_no_cargo_meses
atividade_publica_relevante
status_prospeccao
status_discovery
whatsapp_novos_leads_confirmado
leads_novos_whatsapp_mes
investimento_ads_mes_confirmado
ticket_medio_confirmado
equipe_assumir_oportunidades
dor_patagon_confirmada
fonte_segmento
fonte_concessionaria_autorizada
fonte_operacao_bandeira
fonte_unidades
fonte_ads
fonte_whatsapp
fonte_estrutura_comercial
fonte_persona
data_verificacao
proxima_acao
```

Cada critério deve guardar a URL/origem e a data da verificação. Valores desconhecidos ficam como `nao_verificado`.

Em empresas sem estrutura regional, como alguns SaaS, `unidade_ou_regiao` pode receber `nao_aplicavel`.

## 8. Ordem operacional

1. Descobrir empresas por Google, Google Maps, LinkedIn, Instagram e listas setoriais.
2. Confirmar os gates estruturais com fonte oficial.
3. Registrar os sinais públicos de prioridade.
4. Encontrar decisor e champion nos canais adequados ao segmento.
5. Registrar cargo, fonte e confiança do papel estimado.
6. Criar a abordagem com um fato verificável da empresa e uma responsabilidade real do cargo.
7. Validar os critérios internos na discovery e atribuir `status_discovery`.

Para o automotivo, usar o [mapeamento de marcas e schema de extração](mapeamento-marcas-automotivas.md) como ponto de partida da pesquisa.

O script `automations/leads/triagem_icp.py` classifica pessoas por palavras-chave de cargo. Ele não substitui a qualificação de conta e não deve, sozinho, decidir se uma empresa pertence ao ICP da Patagon.

## 9. Contas-âncora

| Conta | O que ela ensina | O que precisa ser validado |
|---|---|---|
| [Grupo Navesa](https://www.navesa.com.br/) | Grupo com 12 lojas e operações autorizadas separadas por marcas. Confirma que um grupo pode representar várias montadoras e ainda pertencer ao ICP. | Ads, entrada e volume de novos leads no WhatsApp, estrutura de distribuição e melhor bandeira/região para a abordagem. |
| [iFood para Parceiros](https://parceiros.ifood.com.br/) | Plataforma B2B de aquisição em escala voltada principalmente a restaurantes e outros pequenos e médios estabelecimentos. | WhatsApp na aquisição, time responsável, mídia da jornada de parceiros e ponto de valor para automação conversacional. |

Conta-âncora descreve o tipo de operação desejado; não significa aprovação automática.
