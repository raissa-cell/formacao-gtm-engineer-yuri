# `silver_cnpj.estabelecimentos_dominios` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** 48,941,572
**Chave:** _TODO_
**Cluster BY:** `email_dominio_raiz`, `uf`
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj14` | STRING |  |  |
| `cnpj_basico` | STRING |  |  |
| `razao_social` | STRING |  |  |
| `nome_fantasia` | STRING |  |  |
| `natureza_juridica` | STRING |  |  |
| `situacao_cadastral` | STRING |  |  |
| `email` | STRING |  |  |
| `email_local` | STRING |  |  |
| `email_dominio` | STRING |  |  |
| `email_dominio_raiz` | STRING |  |  |
| `email_eh_pessoal_provider` | BOOLEAN |  |  |
| `uf` | STRING |  |  |
| `cep8` | STRING |  |  |
| `cep5` | STRING |  |  |
| `cnae_principal` | STRING |  |  |
| `tipo_logradouro` | STRING |  |  |
| `logradouro` | STRING |  |  |
| `numero` | STRING |  |  |
| `endereco_norm` | STRING |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj14": "10199860000230",
    "cnpj_basico": "10199860",
    "razao_social": "BASE ADMINISTRATIVA DO COMANDO DE OPERACOES ESPECIAIS",
    "nome_fantasia": "BASE ADMINISTRATIVA DA BRIGADA DE OPERACOES ESPECIAIS",
    "natureza_juridica": "1015",
    "situacao_cadastral": "02",
    "email": "setfin_badm@yahoo.com.br",
    "email_local": "setfin_badm",
    "email_dominio": "yahoo.com.br",
    "email_dominio_raiz": "yahoo.com.br",
    "email_eh_pessoal_provider": true,
    "uf": "GO",
    "cep8": "74675240",
    "cep5": "74675",
    "cnae_principal": "8422100",
    "tipo_logradouro": "AVENIDA",
    "logradouro": "CONTORNO",
    "numero": "S/N",
    "endereco_norm": "contorno sn",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:20.635741+00:00"
  },
  {
    "cnpj14": "10199860000150",
    "cnpj_basico": "10199860",
    "razao_social": "BASE ADMINISTRATIVA DO COMANDO DE OPERACOES ESPECIAIS",
    "nome_fantasia": "BASE ADMINISTRATIVA DA BRIGADA DE OPERACOES ESPECIAIS",
    "natureza_juridica": "1015",
    "situacao_cadastral": "02",
    "email": "setfin_badm@yahoo.com.br",
    "email_local": "setfin_badm",
    "email_dominio": "yahoo.com.br",
    "email_dominio_raiz": "yahoo.com.br",
    "email_eh_pessoal_provider": true,
    "uf": "GO",
    "cep8": "74675240",
    "cep5": "74675",
    "cnae_principal": "8422100",
    "tipo_logradouro": "AVENIDA",
    "logradouro": "CONTORNO",
    "numero": "S/N",
    "endereco_norm": "contorno sn",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:20.635741+00:00"
  },
  {
    "cnpj14": "24977127000123",
    "cnpj_basico": "24977127",
    "razao_social": "BATALHAO DE POLICIA AMBIENTAL",
    "nome_fantasia": "BPAPMMA",
    "natureza_juridica": "1023",
    "situacao_cadastral": "02",
    "email": "edilenedireita@yahoo.com.br",
    "email_local": "edilenedireita",
    "email_dominio": "yahoo.com.br",
    "email_dominio_raiz": "yahoo.com.br",
    "email_eh_pessoal_provider": true,
    "uf": "MA",
    "cep8": "65043840",
    "cep5": "65043",
    "cnae_principal": "8424800",
    "tipo_logradouro": "AVENIDA",
    "logradouro": "SARNEY FILHO",
    "numero": "000001",
    "endereco_norm": "sarney filho 000001",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:20.635741+00:00"
  },
  {
    "cnpj14": "05022633000114",
    "cnpj_basico": "05022633",
    "razao_social": "ESTADO DO MARANHAO - SECRETARIA DE ESTADO DO PLANEJAMENTO E ORCAMENTO",
    "nome_fantasia": "SEPLAN",
    "natureza_juridica": "1023",
    "situacao_cadastral": "02",
    "email": "alineribeiro20@yahoo.com.br",
    "email_local": "alineribeiro20",
    "email_dominio": "yahoo.com.br",
    "email_dominio_raiz": "yahoo.com.br",
    "email_eh_pessoal_provider": true,
    "uf": "MA",
    "cep8": "65051200",
    "cep5": "65051",
    "cnae_principal": "8411600",
    "tipo_logradouro": "AVENIDA",
    "logradouro": "JERONIMO DE ALBUQUERQUE",
    "numero": "S/N",
    "endereco_norm": "jeronimo de albuquerque sn",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:20.635741+00:00"
  },
  {
    "cnpj14": "54581671000112",
    "cnpj_basico": "54581671",
    "razao_social": "SECRETARIA MUNICIPAL DE EDUCACAO DE CEDRAL - MA",
    "nome_fantasia": "SECRETARIA MUNICIPAL DE EDUCACAO DE CEDRAL MA",
    "natureza_juridica": "1031",
    "situacao_cadastral": "02",
    "email": "eleiedenecuba@yahoo.com.br",
    "email_local": "eleiedenecuba",
    "email_dominio": "yahoo.com.br",
    "email_dominio_raiz": "yahoo.com.br",
    "email_eh_pessoal_provider": true,
    "uf": "MA",
    "cep8": "65260000",
    "cep5": "65260",
    "cnae_principal": "8412400",
    "tipo_logradouro": "RUA",
    "logradouro": "MARIANO VITAL DE NEGREIRO",
    "numero": "SN",
    "endereco_norm": "mariano vital de negreiro sn",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:20.635741+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.estabelecimentos_dominios\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.estabelecimentos_dominios`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
