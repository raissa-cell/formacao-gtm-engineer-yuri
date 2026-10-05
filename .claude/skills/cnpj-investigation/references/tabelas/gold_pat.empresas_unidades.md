# `gold_pat.empresas_unidades` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** gold
**Granularidade:** _TODO_
**Linhas (~):** 407,226
**Chave:** _TODO_
**Cluster BY:** `uf`, `municipio`, `cnpj_basico`
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj` | STRING |  | CNPJ completo (14 dígitos). Chave da unidade (matriz ou filial). |
| `cnpj_basico` | STRING |  | CNPJ raiz (8 dígitos) — JOIN com gold_pat.empresas. |
| `razao_social` | STRING |  | Razão social RFB (UPPERCASE sem acento). |
| `nome_fantasia` | STRING |  |  |
| `matriz_ou_filial` | STRING |  |  |
| `uf` | STRING |  | UF da RFB. Sempre prefira essa, NÃO o municipio_pat (cadastro centralizado). |
| `municipio` | STRING |  | Município RFB em UPPERCASE (decoded via bronze_cnpj.municipios). |
| `bairro` | STRING |  |  |
| `cep` | STRING |  |  |
| `tipo_logradouro` | STRING |  |  |
| `logradouro` | STRING |  |  |
| `numero` | STRING |  |  |
| `complemento` | STRING |  |  |
| `endereco_completo` | STRING |  | Endereço formatado: TIPO_LOGRADOURO + LOGRADOURO + NUMERO + COMPLEMENTO + BAIRRO. |
| `data_abertura_unidade` | DATE |  |  |
| `data_cadastro_pat` | DATE |  |  |
| `cnae_principal_codigo` | STRING |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `email` | STRING |  |  |
| `email_dominio_raiz` | STRING |  |  |
| `total_trabalhadores` | INTEGER |  | Trabalhadores DESSA unidade (não do grupo). |
| `trabalhadores_ate_5sm` | INTEGER |  |  |
| `trabalhadores_acima_5sm` | INTEGER |  |  |
| `folha_mensal_estimada_brl` | NUMERIC |  | ESTIMATIVA pra ranking, NÃO valor absoluto. Heurística: ≤5SM × 3 SM médio + >5SM × 8 SM médio (SM 2025 = R$ 1518). |
| `porte_grupo` | STRING |  | Porte do grupo RFB (denormalizado pra facilitar filtro). |
| `capital_social_grupo` | NUMERIC |  |  |
| `cnae_principal_grupo_descricao` | STRING |  |  |
| `idade_grupo_anos` | INTEGER |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "92193135000210",
    "cnpj_basico": "92193135",
    "razao_social": "GRANJAS 4 IRMAOS SA AGROPECUARIA INDUSTRIA E COMERCIO",
    "nome_fantasia": null,
    "matriz_ou_filial": "Filial",
    "uf": "RS",
    "municipio": "RIO GRANDE",
    "bairro": "TAIM",
    "cep": "96221000",
    "tipo_logradouro": "RODOVIA",
    "logradouro": "BR 471",
    "numero": "S/N",
    "complemento": "KM    501",
    "endereco_completo": "RODOVIA BR 471, S/N - KM 501, TAIM",
    "data_abertura_unidade": "1966-08-30",
    "data_cadastro_pat": "2008-07-28",
    "cnae_principal_codigo": "0111301",
    "cnae_principal_descricao": "Cultivo de arroz",
    "email": null,
    "email_dominio_raiz": null,
    "total_trabalhadores": 25,
    "trabalhadores_ate_5sm": 19,
    "trabalhadores_acima_5sm": 6,
    "folha_mensal_estimada_brl": "159390",
    "porte_grupo": "DEMAIS",
    "capital_social_grupo": "80806659",
    "cnae_principal_grupo_descricao": "Atividades de apoio à agricultura não especificadas anteriormente",
    "idade_grupo_anos": 60,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:41.724345+00:00"
  },
  {
    "cnpj": "09275081000298",
    "cnpj_basico": "09275081",
    "razao_social": "MORAES & PRADO AGROPECUARIA LTDA",
    "nome_fantasia": null,
    "matriz_ou_filial": "Filial",
    "uf": "RS",
    "municipio": "JAGUARAO",
    "bairro": "2 SUBDISTRITO",
    "cep": "96300000",
    "tipo_logradouro": "VILA",
    "logradouro": "DO JUNCAL",
    "numero": "SN",
    "complemento": null,
    "endereco_completo": "VILA DO JUNCAL, SN, 2 SUBDISTRITO",
    "data_abertura_unidade": "2020-05-11",
    "data_cadastro_pat": "2022-09-01",
    "cnae_principal_codigo": "0111301",
    "cnae_principal_descricao": "Cultivo de arroz",
    "email": "otprado@terra.com.br",
    "email_dominio_raiz": "terra.com.br",
    "total_trabalhadores": 16,
    "trabalhadores_ate_5sm": 15,
    "trabalhadores_acima_5sm": 1,
    "folha_mensal_estimada_brl": "80454",
    "porte_grupo": "NÃO INFORMADO",
    "capital_social_grupo": "96000",
    "cnae_principal_grupo_descricao": "Atividades de pós-colheita",
    "idade_grupo_anos": 19,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:41.724345+00:00"
  },
  {
    "cnpj": "00985778000105",
    "cnpj_basico": "00985778",
    "razao_social": "SULRURAL AGROPECUARIA LTDA",
    "nome_fantasia": null,
    "matriz_ou_filial": "Matriz",
    "uf": "RS",
    "municipio": "PORTO ALEGRE",
    "bairro": "RIO BRANCO",
    "cep": "90430001",
    "tipo_logradouro": "RUA",
    "logradouro": "MOSTARDEIRO",
    "numero": "777",
    "complemento": "SALA  1401",
    "endereco_completo": "RUA MOSTARDEIRO, 777 - SALA 1401, RIO BRANCO",
    "data_abertura_unidade": "1996-01-03",
    "data_cadastro_pat": "2008-06-23",
    "cnae_principal_codigo": "0111301",
    "cnae_principal_descricao": "Cultivo de arroz",
    "email": "denisepjardim@gmail.com",
    "email_dominio_raiz": "gmail.com",
    "total_trabalhadores": 2,
    "trabalhadores_ate_5sm": 1,
    "trabalhadores_acima_5sm": 1,
    "folha_mensal_estimada_brl": "16698",
    "porte_grupo": "DEMAIS",
    "capital_social_grupo": "12000",
    "cnae_principal_grupo_descricao": "Cultivo de arroz",
    "idade_grupo_anos": 30,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:41.724345+00:00"
  },
  {
    "cnpj": "08157624000129",
    "cnpj_basico": "08157624",
    "razao_social": "AGROPECUARIA MAPOCHO LTDA",
    "nome_fantasia": null,
    "matriz_ou_filial": "Matriz",
    "uf": "RS",
    "municipio": "PORTO ALEGRE",
    "bairro": "PETROPOLIS",
    "cep": "90470150",
    "tipo_logradouro": "RUA",
    "logradouro": "JOAO OBINO",
    "numero": "239",
    "complemento": "      CASA",
    "endereco_completo": "RUA JOAO OBINO, 239 - CASA, PETROPOLIS",
    "data_abertura_unidade": "2006-07-06",
    "data_cadastro_pat": "2022-10-03",
    "cnae_principal_codigo": "0111301",
    "cnae_principal_descricao": "Cultivo de arroz",
    "email": "gerencia@mapocho.com.br",
    "email_dominio_raiz": "mapocho.com.br",
    "total_trabalhadores": 50,
    "trabalhadores_ate_5sm": 48,
    "trabalhadores_acima_5sm": 2,
    "folha_mensal_estimada_brl": "242880",
    "porte_grupo": "EMPRESA DE PEQUENO PORTE",
    "capital_social_grupo": "34368849",
    "cnae_principal_grupo_descricao": "Cultivo de arroz",
    "idade_grupo_anos": 20,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:41.724345+00:00"
  },
  {
    "cnpj": "19074758000364",
    "cnpj_basico": "19074758",
    "razao_social": "THIAGO MINORU YOSHIMURA",
    "nome_fantasia": null,
    "matriz_ou_filial": "Matriz",
    "uf": "SP",
    "municipio": "ITAPEVA",
    "bairro": "BAIRRO DAS PEDRAS",
    "cep": "18400970",
    "tipo_logradouro": "FAZENDA",
    "logradouro": "MISSOES",
    "numero": "SN",
    "complemento": null,
    "endereco_completo": "FAZENDA MISSOES, SN, BAIRRO DAS PEDRAS",
    "data_abertura_unidade": "2017-06-21",
    "data_cadastro_pat": "2021-10-28",
    "cnae_principal_codigo": "0111302",
    "cnae_principal_descricao": "Cultivo de milho",
    "email": null,
    "email_dominio_raiz": null,
    "total_trabalhadores": 5,
    "trabalhadores_ate_5sm": 4,
    "trabalhadores_acima_5sm": 1,
    "folha_mensal_estimada_brl": "30360",
    "porte_grupo": "DEMAIS",
    "capital_social_grupo": "0",
    "cnae_principal_grupo_descricao": "Cultivo de milho",
    "idade_grupo_anos": 9,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:41.724345+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_pat.empresas_unidades\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.gold_pat.empresas_unidades`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
