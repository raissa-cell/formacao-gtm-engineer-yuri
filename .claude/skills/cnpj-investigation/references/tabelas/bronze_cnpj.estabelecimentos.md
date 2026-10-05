# `bronze_cnpj.estabelecimentos` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 70,863,993
**Chave:** _TODO_
**Cluster BY:** —
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `CNPJ_BASICO` | STRING |  |  |
| `CNPJ_ORDEM` | STRING |  |  |
| `CNPJ_DV` | STRING |  |  |
| `ID_MATRIZ_FILIAL` | STRING |  |  |
| `NOME_FANTASIA` | STRING |  |  |
| `SITUACAO_CADASTRAL` | STRING |  |  |
| `DATA_SITUACAO_CADASTRAL` | STRING |  |  |
| `MOTIVO_SITUACAO_CADASTRAL` | STRING |  |  |
| `NM_CIDADE_EXTERIOR` | STRING |  |  |
| `PAIS` | STRING |  |  |
| `DATA_INICIO_ATIVIDADE` | STRING |  |  |
| `CNAE_FISCAL_PRINCIPAL` | STRING |  |  |
| `CNAE_FISCAL_SECUNDARIA` | STRING |  |  |
| `TIPO_LOGRADOURO` | STRING |  |  |
| `LOGRADOURO` | STRING |  |  |
| `NUMERO` | STRING |  |  |
| `COMPLEMENTO` | STRING |  |  |
| `BAIRRO` | STRING |  |  |
| `CEP` | STRING |  |  |
| `UF` | STRING |  |  |
| `MUNICIPIO` | STRING |  |  |
| `DDD1` | STRING |  |  |
| `TELEFONE1` | STRING |  |  |
| `DDD2` | STRING |  |  |
| `TELEFONE2` | STRING |  |  |
| `DDD_FAX` | STRING |  |  |
| `FAX` | STRING |  |  |
| `CORREIO_ELETRONICO` | STRING |  |  |
| `SITUACAO_ESPECIAL` | STRING |  |  |
| `DATA_SITUACAO_ESPECIAL` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "CNPJ_BASICO": "06148652",
    "CNPJ_ORDEM": "0001",
    "CNPJ_DV": "54",
    "ID_MATRIZ_FILIAL": "1",
    "NOME_FANTASIA": null,
    "SITUACAO_CADASTRAL": "02",
    "DATA_SITUACAO_CADASTRAL": "20040318",
    "MOTIVO_SITUACAO_CADASTRAL": "00",
    "NM_CIDADE_EXTERIOR": null,
    "PAIS": "249",
    "DATA_INICIO_ATIVIDADE": "20040318",
    "CNAE_FISCAL_PRINCIPAL": "6630400",
    "CNAE_FISCAL_SECUNDARIA": null,
    "TIPO_LOGRADOURO": null,
    "LOGRADOURO": "500 WOODWARD, SUITE 3000",
    "NUMERO": "000000",
    "COMPLEMENTO": null,
    "BAIRRO": "DETROIT",
    "CEP": null,
    "UF": "EX",
    "MUNICIPIO": "9707",
    "DDD1": "11",
    "TELEFONE1": "40090000",
    "DDD2": null,
    "TELEFONE2": null,
    "DDD_FAX": null,
    "FAX": null,
    "CORREIO_ELETRONICO": "CONTATOCNPJ@CITI.COM",
    "SITUACAO_ESPECIAL": null,
    "DATA_SITUACAO_ESPECIAL": null,
    "_arquivo_origem": "Estabelecimentos0.zip",
    "_data_carga": "2026-04-22T18:24:25+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "05630679",
    "CNPJ_ORDEM": "0001",
    "CNPJ_DV": "16",
    "ID_MATRIZ_FILIAL": "1",
    "NOME_FANTASIA": null,
    "SITUACAO_CADASTRAL": "02",
    "DATA_SITUACAO_CADASTRAL": "20030429",
    "MOTIVO_SITUACAO_CADASTRAL": "00",
    "NM_CIDADE_EXTERIOR": null,
    "PAIS": "863",
    "DATA_INICIO_ATIVIDADE": "20030429",
    "CNAE_FISCAL_PRINCIPAL": "6462000",
    "CNAE_FISCAL_SECUNDARIA": null,
    "TIPO_LOGRADOURO": null,
    "LOGRADOURO": "THE CREQUE BUILDING",
    "NUMERO": "S/N",
    "COMPLEMENTO": "CAIXA POSTAL 116",
    "BAIRRO": "TORTOLA",
    "CEP": null,
    "UF": "EX",
    "MUNICIPIO": "9707",
    "DDD1": null,
    "TELEFONE1": null,
    "DDD2": null,
    "TELEFONE2": null,
    "DDD_FAX": null,
    "FAX": null,
    "CORREIO_ELETRONICO": null,
    "SITUACAO_ESPECIAL": null,
    "DATA_SITUACAO_ESPECIAL": null,
    "_arquivo_origem": "Estabelecimentos0.zip",
    "_data_carga": "2026-04-22T18:24:25+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "40193248",
    "CNPJ_ORDEM": "0001",
    "CNPJ_DV": "30",
    "ID_MATRIZ_FILIAL": "1",
    "NOME_FANTASIA": "MARLIM1 MV33",
    "SITUACAO_CADASTRAL": "02",
    "DATA_SITUACAO_CADASTRAL": "20201223",
    "MOTIVO_SITUACAO_CADASTRAL": "00",
    "NM_CIDADE_EXTERIOR": "AMSTELVEEN",
    "PAIS": "573",
    "DATA_INICIO_ATIVIDADE": "20201223",
    "CNAE_FISCAL_PRINCIPAL": "0910600",
    "CNAE_FISCAL_SECUNDARIA": null,
    "TIPO_LOGRADOURO": null,
    "LOGRADOURO": "GOEDHARTAAN VAN HEUVEN  13 D",
    "NUMERO": "S/N",
    "COMPLEMENTO": "1181 LE",
    "BAIRRO": "AMSTELVEEN",
    "CEP": null,
    "UF": "EX",
    "MUNICIPIO": "9707",
    "DDD1": null,
    "TELEFONE1": null,
    "DDD2": null,
    "TELEFONE2": null,
    "DDD_FAX": null,
    "FAX": null,
    "CORREIO_ELETRONICO": "SOICHI.IDE@MODEC.COM",
    "SITUACAO_ESPECIAL": null,
    "DATA_SITUACAO_ESPECIAL": null,
    "_arquivo_origem": "Estabelecimentos0.zip",
    "_data_carga": "2026-04-22T18:24:25+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "39586173",
    "CNPJ_ORDEM": "0001",
    "CNPJ_DV": "79",
    "ID_MATRIZ_FILIAL": "1",
    "NOME_FANTASIA": null,
    "SITUACAO_CADASTRAL": "02",
    "DATA_SITUACAO_CADASTRAL": "20201027",
    "MOTIVO_SITUACAO_CADASTRAL": "00",
    "NM_CIDADE_EXTERIOR": null,
    "PAIS": "023",
    "DATA_INICIO_ATIVIDADE": "20201027",
    "CNAE_FISCAL_PRINCIPAL": "6630400",
    "CNAE_FISCAL_SECUNDARIA": null,
    "TIPO_LOGRADOURO": null,
    "LOGRADOURO": "WEIBFRAUENSTABE 7",
    "NUMERO": "000000",
    "COMPLEMENTO": null,
    "BAIRRO": "FRANKFURT AM MAIN",
    "CEP": null,
    "UF": "EX",
    "MUNICIPIO": "9707",
    "DDD1": null,
    "TELEFONE1": null,
    "DDD2": null,
    "TELEFONE2": null,
    "DDD_FAX": null,
    "FAX": null,
    "CORREIO_ELETRONICO": null,
    "SITUACAO_ESPECIAL": null,
    "DATA_SITUACAO_ESPECIAL": null,
    "_arquivo_origem": "Estabelecimentos0.zip",
    "_data_carga": "2026-04-22T18:24:25+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "19483878",
    "CNPJ_ORDEM": "0001",
    "CNPJ_DV": "53",
    "ID_MATRIZ_FILIAL": "1",
    "NOME_FANTASIA": "MONTANA",
    "SITUACAO_CADASTRAL": "02",
    "DATA_SITUACAO_CADASTRAL": "20140103",
    "MOTIVO_SITUACAO_CADASTRAL": "00",
    "NM_CIDADE_EXTERIOR": "MILAO",
    "PAIS": "386",
    "DATA_INICIO_ATIVIDADE": "20140103",
    "CNAE_FISCAL_PRINCIPAL": "6462000",
    "CNAE_FISCAL_SECUNDARIA": null,
    "TIPO_LOGRADOURO": null,
    "LOGRADOURO": "VIA ANGELO CARLO FUMAGALLI",
    "NUMERO": "6",
    "COMPLEMENTO": "      CAP 20143",
    "BAIRRO": "MILAO",
    "CEP": null,
    "UF": "EX",
    "MUNICIPIO": "9707",
    "DDD1": null,
    "TELEFONE1": null,
    "DDD2": null,
    "TELEFONE2": null,
    "DDD_FAX": null,
    "FAX": null,
    "CORREIO_ELETRONICO": "joao.soares@kntsbrasil.com.br",
    "SITUACAO_ESPECIAL": null,
    "DATA_SITUACAO_ESPECIAL": null,
    "_arquivo_origem": "Estabelecimentos0.zip",
    "_data_carga": "2026-04-22T18:24:25+00:00",
    "_periodo": "202604"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_cnpj.estabelecimentos\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos`
WHERE ...
```

## Histórico

- 2026-04-26: última modificação BQ
- 2026-05-03: doc criado
