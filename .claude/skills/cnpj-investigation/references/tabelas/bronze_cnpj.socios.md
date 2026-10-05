# `bronze_cnpj.socios` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 27,494,742
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
| `ID_SOCIO` | STRING |  |  |
| `NOME_SOCIO` | STRING |  |  |
| `CNPJ_CPF_SOCIO` | STRING |  |  |
| `QUALIFICACAO_SOCIO` | STRING |  |  |
| `DATA_ENTRADA_SOCIEDADE` | STRING |  |  |
| `PAIS` | STRING |  |  |
| `REPRESENTANTE_LEGAL` | STRING |  |  |
| `NOME_REPRESENTANTE` | STRING |  |  |
| `QUALIFICACAO_REPRESENTANTE_LEGAL` | STRING |  |  |
| `FAIXA_ETARIA` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "CNPJ_BASICO": "04673969",
    "ID_SOCIO": "1",
    "NOME_SOCIO": "MAUBERTEC EMPREENDIMENTOS E CONSTRUCOES LTDA",
    "CNPJ_CPF_SOCIO": "51484780000123",
    "QUALIFICACAO_SOCIO": "05",
    "DATA_ENTRADA_SOCIEDADE": "20010904",
    "PAIS": null,
    "REPRESENTANTE_LEGAL": "***000000**",
    "NOME_REPRESENTANTE": null,
    "QUALIFICACAO_REPRESENTANTE_LEGAL": "05",
    "FAIXA_ETARIA": "0",
    "_arquivo_origem": "Socios0.zip",
    "_data_carga": "2026-04-22T18:22:22+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "68553957",
    "ID_SOCIO": "1",
    "NOME_SOCIO": "RBM BRASIL EMPREENDIMENTOS E PARTICIPACOES LTDA",
    "CNPJ_CPF_SOCIO": "19680087000113",
    "QUALIFICACAO_SOCIO": "05",
    "DATA_ENTRADA_SOCIEDADE": "20150714",
    "PAIS": null,
    "REPRESENTANTE_LEGAL": "***000000**",
    "NOME_REPRESENTANTE": null,
    "QUALIFICACAO_REPRESENTANTE_LEGAL": "00",
    "FAIXA_ETARIA": "0",
    "_arquivo_origem": "Socios0.zip",
    "_data_carga": "2026-04-22T18:22:22+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "00716510",
    "ID_SOCIO": "2",
    "NOME_SOCIO": "LIVIA DE FATIMA NICHELE SCHIMIDT",
    "CNPJ_CPF_SOCIO": "***721589**",
    "QUALIFICACAO_SOCIO": "05",
    "DATA_ENTRADA_SOCIEDADE": "20221110",
    "PAIS": null,
    "REPRESENTANTE_LEGAL": "***000000**",
    "NOME_REPRESENTANTE": null,
    "QUALIFICACAO_REPRESENTANTE_LEGAL": "00",
    "FAIXA_ETARIA": "2",
    "_arquivo_origem": "Socios0.zip",
    "_data_carga": "2026-04-22T18:22:22+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "39538141",
    "ID_SOCIO": "2",
    "NOME_SOCIO": "ISADORA TAROSSO BRANDAO",
    "CNPJ_CPF_SOCIO": "***846679**",
    "QUALIFICACAO_SOCIO": "05",
    "DATA_ENTRADA_SOCIEDADE": "20251029",
    "PAIS": null,
    "REPRESENTANTE_LEGAL": "***000000**",
    "NOME_REPRESENTANTE": null,
    "QUALIFICACAO_REPRESENTANTE_LEGAL": "00",
    "FAIXA_ETARIA": "2",
    "_arquivo_origem": "Socios0.zip",
    "_data_carga": "2026-04-22T18:22:22+00:00",
    "_periodo": "202604"
  },
  {
    "CNPJ_BASICO": "09151435",
    "ID_SOCIO": "2",
    "NOME_SOCIO": "BERNARDO PEREIRA DE LEMOS",
    "CNPJ_CPF_SOCIO": "***482417**",
    "QUALIFICACAO_SOCIO": "05",
    "DATA_ENTRADA_SOCIEDADE": "20220210",
    "PAIS": null,
    "REPRESENTANTE_LEGAL": "***000000**",
    "NOME_REPRESENTANTE": null,
    "QUALIFICACAO_REPRESENTANTE_LEGAL": "00",
    "FAIXA_ETARIA": "2",
    "_arquivo_origem": "Socios0.zip",
    "_data_carga": "2026-04-22T18:22:22+00:00",
    "_periodo": "202604"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_cnpj.socios\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_cnpj.socios`
WHERE ...
```

## Histórico

- 2026-04-22: última modificação BQ
- 2026-05-03: doc criado
