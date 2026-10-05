# `silver_cnpj.empresas_por_endereco` — _TODO: título curto_

**Tipo:** VIEW
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** (view, sem contagem)
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
| `uf` | STRING |  |  |
| `cep5` | STRING |  |  |
| `cep8` | STRING |  |  |
| `endereco_norm` | STRING |  |  |
| `cnpj14` | STRING |  |  |
| `cnpj_basico` | STRING |  |  |
| `razao_social` | STRING |  |  |
| `nome_fantasia` | STRING |  |  |
| `situacao_cadastral` | STRING |  |  |
| `email` | STRING |  |  |
| `email_dominio_raiz` | STRING |  |  |
| `email_eh_pessoal_provider` | BOOLEAN |  |  |
| `cnae_principal` | STRING |  |  |
| `tipo_logradouro` | STRING |  |  |
| `logradouro` | STRING |  |  |
| `numero` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "uf": "SP",
    "cep5": "01001",
    "cep8": "01001000",
    "endereco_norm": "da se 14478",
    "cnpj14": "63960916000103",
    "cnpj_basico": "63960916",
    "razao_social": "SOLUCOES DE PGMENTO PASCHOALOTTO ADV INOVA SIMPLES (I.S.)",
    "nome_fantasia": null,
    "situacao_cadastral": "01",
    "email": "adsbha@gmail.com",
    "email_dominio_raiz": "gmail.com",
    "email_eh_pessoal_provider": true,
    "cnae_principal": "7319002",
    "tipo_logradouro": "PRACA",
    "logradouro": "DA SE",
    "numero": "14478"
  },
  {
    "uf": "SP",
    "cep5": "01008",
    "cep8": "01008904",
    "endereco_norm": "rua li bero badaro 158 158",
    "cnpj14": "57521040000104",
    "cnpj_basico": "57521040",
    "razao_social": "DEP RECEBIMENTOS LTDA",
    "nome_fantasia": null,
    "situacao_cadastral": "01",
    "email": "raylan.lopes2020@gmail.com",
    "email_dominio_raiz": "gmail.com",
    "email_eh_pessoal_provider": true,
    "cnae_principal": "5611201",
    "tipo_logradouro": "RUA",
    "logradouro": "RUA LÍBERO BADARÓ, 158",
    "numero": "158"
  },
  {
    "uf": "SP",
    "cep5": "01013",
    "cep8": "01013000",
    "endereco_norm": "quinze de novembro lado par 827",
    "cnpj14": "49823805000124",
    "cnpj_basico": "49823805",
    "razao_social": "49.823.805 BRUNNO LOPES FERNANDES",
    "nome_fantasia": null,
    "situacao_cadastral": "01",
    "email": "brunnolopes2703@gmail.com",
    "email_dominio_raiz": "gmail.com",
    "email_eh_pessoal_provider": true,
    "cnae_principal": "4754701",
    "tipo_logradouro": "RUA",
    "logradouro": "QUINZE DE NOVEMBRO - LADO PAR",
    "numero": "827"
  },
  {
    "uf": "SP",
    "cep5": "01021",
    "cep8": "01021200",
    "endereco_norm": "vinte e cinco de marco 111",
    "cnpj14": "65659709000149",
    "cnpj_basico": "65659709",
    "razao_social": "ELKTRO NEO INOVA SIMPLES (I.S.)",
    "nome_fantasia": null,
    "situacao_cadastral": "01",
    "email": "elek@gmail.com",
    "email_dominio_raiz": "gmail.com",
    "email_eh_pessoal_provider": true,
    "cnae_principal": "3511501",
    "tipo_logradouro": "RUA",
    "logradouro": "VINTE E CINCO DE MARCO",
    "numero": "111"
  },
  {
    "uf": "SP",
    "cep5": "01022",
    "cep8": "01022970",
    "endereco_norm": "rua cavalheiro basi lio jafet 191 191",
    "cnpj14": "56980731000103",
    "cnpj_basico": "56980731",
    "razao_social": "ASSESSORIA DE RECEBIMENTOS LTDA",
    "nome_fantasia": null,
    "situacao_cadastral": "01",
    "email": "victor1727722@gmail.com",
    "email_dominio_raiz": "gmail.com",
    "email_eh_pessoal_provider": true,
    "cnae_principal": "5611201",
    "tipo_logradouro": "RUA",
    "logradouro": "RUA CAVALHEIRO BASÍLIO JAFET, 191",
    "numero": "191"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.empresas_por_endereco\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.empresas_por_endereco`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
