# `bronze_pat.nutricionistas` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 37,676
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
| `numero_crn` | STRING |  |  |
| `num_registro_pat` | STRING |  |  |
| `municipio` | STRING |  |  |
| `uf` | STRING |  |  |
| `data_de_cadastro` | STRING |  |  |
| `_sheet_origem` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "numero_crn": "3809      ",
    "num_registro_pat": "080007458 ",
    "municipio": null,
    "uf": null,
    "data_de_cadastro": "18-01-2008",
    "_sheet_origem": "Nutricionistas_Ativos",
    "_arquivo_origem": "relacao-nutricionistas-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:12.418584+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "numero_crn": "3704      ",
    "num_registro_pat": "080020541 ",
    "municipio": null,
    "uf": null,
    "data_de_cadastro": "22-02-2008",
    "_sheet_origem": "Nutricionistas_Ativos",
    "_arquivo_origem": "relacao-nutricionistas-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:12.418584+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "numero_crn": "22365     ",
    "num_registro_pat": "080031743 ",
    "municipio": null,
    "uf": null,
    "data_de_cadastro": "19-03-2008",
    "_sheet_origem": "Nutricionistas_Ativos",
    "_arquivo_origem": "relacao-nutricionistas-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:12.418584+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "numero_crn": "1447      ",
    "num_registro_pat": "080043399 ",
    "municipio": null,
    "uf": null,
    "data_de_cadastro": "31-03-2008",
    "_sheet_origem": "Nutricionistas_Ativos",
    "_arquivo_origem": "relacao-nutricionistas-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:12.418584+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "numero_crn": "3902      ",
    "num_registro_pat": "080045981 ",
    "municipio": null,
    "uf": null,
    "data_de_cadastro": "01-04-2008",
    "_sheet_origem": "Nutricionistas_Ativos",
    "_arquivo_origem": "relacao-nutricionistas-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:12.418584+00:00",
    "_periodo": "2025-12-31"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_pat.nutricionistas\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_pat.nutricionistas`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
