# Tabelas CNPJ — Schema e Granularidade

Dois datasets:

- **`data-hacker-488115.bronze_cnpj`** — snapshot mensal completo da RFB (10 tabelas + dimensões). Granularidade-fonte.
- **`data-hacker-488115.silver_cnpj`** — derivado da bronze, indexado pra **descoberta de grupo via domínio + busca por sócio**. 2 tabelas + 6 views. **Detalhe completo em [`07-silver-cnpj.md`](07-silver-cnpj.md)**.

> **Default operacional:** se a pergunta é sobre **domínio de e-mail, nome de sócio, holding PJ, ou endereço normalizado**, comece pela silver. Para tudo o mais (CNAEs secundárias, capital social, telefone, MEI, datas detalhadas), use bronze.

## Visão geral

| Tabela | Linhas (~) | Granularidade | Chave |
|---|---:|---|---|
| `empresas` | 67,6M | 1 linha por **CNPJ raiz** (matriz fiscal) | `CNPJ_BASICO` (8 dígitos) |
| `estabelecimentos` | 70,9M | 1 linha por **estabelecimento físico** (matriz + filiais) | `(CNPJ_BASICO, CNPJ_ORDEM, CNPJ_DV)` |
| `socios` | 27,5M | 1 linha por **vínculo sócio↔empresa** | `(CNPJ_BASICO, CNPJ_CPF_SOCIO, DATA_ENTRADA_SOCIEDADE)` |
| `simples` | 48,1M | 1 linha por **opção tributária** | `CNPJ_BASICO` |
| `cnaes` | 1.359 | dimensão CNAE 7-dig | `CODIGO` |
| `motivos` | 63 | dimensão motivo de baixa/suspensão | `CODIGO` |
| `municipios` | 5.572 | dimensão IBGE | `CODIGO` |
| `naturezas` | 91 | dimensão natureza jurídica | `CODIGO` |
| `paises` | 255 | dimensão país | `CODIGO` |
| `qualificacoes` | 68 | dimensão qualificação de sócio | `CODIGO` |

**CNPJ completo**: `CNPJ_BASICO || CNPJ_ORDEM || CNPJ_DV` = 14 dígitos.
**Matriz**: `CNPJ_ORDEM = '0001'` e `ID_MATRIZ_FILIAL = '1'`.

---

## `empresas` — colunas principais

| Coluna | Tipo | Descrição |
|---|---|---|
| `CNPJ_BASICO` | STRING | 8 dígitos — chave de grupo econômico |
| `RAZAO_SOCIAL` | STRING | Razão social oficial |
| `NATUREZA_JURIDICA` | STRING | Código 4-dig (ver naturezas) |
| `QUALIFICACAO_RESPONSAVEL` | STRING | Código (ver qualificacoes) |
| `CAPITAL_SOCIAL` | STRING | ⚠️ **Vírgula como separador decimal**: `"50000,00"` |
| `PORTE` | STRING | `01`=ME, `03`=EPP, `05`=Demais |
| `ENTE_FEDERATIVO_RESPONSAVEL` | STRING | Apenas adm. pública |

**⚠️ Múltiplas linhas por CNPJ_BASICO** (snapshot histórico). Sempre agregar com `ANY_VALUE`/`MAX` em GROUP BY.

---

## `estabelecimentos` — colunas principais

| Coluna | Tipo | Descrição |
|---|---|---|
| `CNPJ_BASICO`, `CNPJ_ORDEM`, `CNPJ_DV` | STRING | Compõem o CNPJ-14 |
| `ID_MATRIZ_FILIAL` | STRING | `1`=matriz, `2`=filial |
| `NOME_FANTASIA` | STRING | ⚠️ Vazio em ~40-50% dos casos |
| `SITUACAO_CADASTRAL` | STRING | Ver `02-codigos-rfb.md` |
| `DATA_SITUACAO_CADASTRAL` | STRING | `YYYYMMDD` |
| `MOTIVO_SITUACAO_CADASTRAL` | STRING | Código (ver motivos) |
| `NOME_CIDADE_EXTERIOR` | STRING | Apenas estabelecimentos no exterior |
| `PAIS` | STRING | Código (ver paises) |
| `DATA_INICIO_ATIVIDADE` | STRING | `YYYYMMDD` |
| `CNAE_FISCAL_PRINCIPAL` | STRING | 7 dígitos (ver cnaes) |
| `CNAE_FISCAL_SECUNDARIA` | STRING | Lista separada por vírgula |
| `TIPO_LOGRADOURO` | STRING | `RUA`, `AVENIDA`, `RODOVIA` etc. — **separado** de LOGRADOURO |
| `LOGRADOURO` | STRING | Apenas o nome (sem o tipo) |
| `NUMERO` | STRING | ⚠️ Texto livre — `'SN'`, `'KM 10'`, `'100A'`, etc. |
| `COMPLEMENTO` | STRING | |
| `BAIRRO` | STRING | |
| `CEP` | STRING | ⚠️ Pode ter pontuação — normalizar |
| `UF` | STRING | Sigla 2 letras |
| `MUNICIPIO` | STRING | Código IBGE — JOIN com `municipios.CODIGO` |
| `DDD1`, `TELEFONE1` | STRING | Telefone fixo principal |
| `DDD2`, `TELEFONE2` | STRING | Telefone secundário |
| `DDD_FAX`, `FAX` | STRING | Geralmente vazio |
| `CORREIO_ELETRONICO` | STRING | E-mail (1 por estabelecimento) |
| `SITUACAO_ESPECIAL` | STRING | Recuperação judicial, falência etc. |
| `DATA_SITUACAO_ESPECIAL` | STRING | `YYYYMMDD` |

---

## `socios` — colunas

| Coluna | Tipo | Descrição |
|---|---|---|
| `CNPJ_BASICO` | STRING | Empresa (chave para JOIN) |
| `ID_SOCIO` | STRING | `1`=PJ, `2`=PF, `3`=Estrangeiro |
| `NOME_SOCIO` | STRING | Nome completo (PF) ou razão social (PJ) |
| `CNPJ_CPF_SOCIO` | STRING | ⚠️ CPF mascarado: `***123456**` (3 dígitos do meio) |
| `QUALIFICACAO_SOCIO` | STRING | Código (ver qualificacoes) |
| `DATA_ENTRADA_SOCIEDADE` | STRING | `YYYYMMDD` |
| `PAIS` | STRING | Para sócios PJ estrangeiros |
| `REPRESENTANTE_LEGAL` | STRING | CPF mascarado do representante (se houver) |
| `NOME_REPRESENTANTE` | STRING | Nome do representante legal |
| `QUALIFICACAO_REPRESENTANTE_LEGAL` | STRING | Código |
| `FAIXA_ETARIA` | STRING | `0`–`9` (ver `02-codigos-rfb.md`) |

**⚠️ Sócios PJ:** `CNPJ_CPF_SOCIO` é o CNPJ da empresa-sócia (14 dígitos, sem máscara).

---

## `simples` — colunas

| Coluna | Tipo | Descrição |
|---|---|---|
| `CNPJ_BASICO` | STRING | |
| `OPCAO_SIMPLES` | STRING | `S` ou `N` |
| `DATA_OPCAO_SIMPLES` | STRING | `YYYYMMDD` |
| `DATA_EXCLUSAO_SIMPLES` | STRING | `YYYYMMDD` ou vazio |
| `OPCAO_MEI` | STRING | `S` ou `N` |
| `DATA_OPCAO_MEI` | STRING | `YYYYMMDD` |
| `DATA_EXCLUSAO_MEI` | STRING | `YYYYMMDD` ou vazio |

---

## Dimensões

Todas têm formato `(CODIGO STRING, DESCRICAO STRING)`:

- `bronze_cnpj.cnaes` — 1.359 CNAEs
- `bronze_cnpj.municipios` — 5.572 municípios IBGE
- `bronze_cnpj.naturezas` — 91 naturezas jurídicas
- `bronze_cnpj.paises` — 255 países
- `bronze_cnpj.qualificacoes` — 68 qualificações de sócio
- `bronze_cnpj.motivos` — 63 motivos de baixa/suspensão

## Metadata em todas as tabelas

| Coluna | Tipo | Descrição |
|---|---|---|
| `_arquivo_origem` | STRING | Nome do arquivo CSV de origem |
| `_data_carga` | TIMESTAMP | Momento do upload |
| `_periodo` | STRING | Período do snapshot `YYYYMM` |

---

## `silver_cnpj` — derivações pra descoberta de grupo

| Tabela/View | Linhas (~) | Granularidade | Pra quê |
|---|---:|---|---|
| `silver_cnpj.estabelecimentos_dominios` | 49M (25,5M ativos) | 1 linha por estab com email parseado | descoberta via domínio (`email_dominio_raiz`) |
| `silver_cnpj.socios` | 27,5M | 1 linha por vínculo (denormalizado) | busca por nome (`socio_nome_norm`) ou holding (`socio_cnpj_basico`) |
| `silver_cnpj.grupos_por_dominio` (view) | — | agrupa por domínio | "que CNPJs usam o domínio X?" |
| `silver_cnpj.empresas_por_endereco` (view) | — | descoberta inversa | "quem está nesse CEP/endereço?" |
| `silver_cnpj.socios_por_pessoa` (view) | — | agrupa por (nome_norm, cpf_visible) | "em que empresas a pessoa Y aparece?" |
| `silver_cnpj.empresas_por_socio_pj` (view) | — | agrupa por holding PJ | "que empresas são controladas por Z?" |
| `silver_cnpj.grupos_via_socios` (view) | — | self-join holding em comum | "que CNPJs compartilham sócio PJ?" |
| `silver_cnpj.rede_executivos` (view) | — | top sócios PF por # de empresas | board members serial |

**Casos de uso, templates SQL e limitações detalhadas:** [`07-silver-cnpj.md`](07-silver-cnpj.md).
