# `bronze_pat.empresas_beneficiarias` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 532,088
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
| `cnpj` | STRING |  |  |
| `razao_social` | STRING |  |  |
| `matriz_ou_filial` | STRING |  |  |
| `municipio` | STRING |  |  |
| `uf` | STRING |  |  |
| `no_registro` | STRING |  |  |
| `data_cadastro` | STRING |  |  |
| `ate_5_salarios_minimos` | STRING |  |  |
| `acima_de_5_salarios_minimos` | STRING |  |  |
| `total_trabalhadores` | STRING |  |  |
| `situacao` | STRING |  |  |
| `_sheet_origem` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "75487058000100",
    "razao_social": "ARXO INDUSTRIAL DO BRASIL  SA",
    "matriz_ou_filial": "Matriz",
    "municipio": null,
    "uf": "SC",
    "no_registro": "0810363   ",
    "data_cadastro": "12-08-2008",
    "ate_5_salarios_minimos": "79",
    "acima_de_5_salarios_minimos": "9",
    "total_trabalhadores": "88",
    "situacao": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "_arquivo_origem": "relacao-beneficiarias-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:33:30.874215+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "37296449000159",
    "razao_social": "MECAT FILTRACOES INDUSTRIAIS LTDA",
    "matriz_ou_filial": "Matriz",
    "municipio": "Abadia de Goiás",
    "uf": "GO",
    "no_registro": "0056979   ",
    "data_cadastro": "16-04-2008",
    "ate_5_salarios_minimos": "47",
    "acima_de_5_salarios_minimos": "6",
    "total_trabalhadores": "53",
    "situacao": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "_arquivo_origem": "relacao-beneficiarias-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:33:30.874215+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "07468323000153",
    "razao_social": "VR ADMINISTRACAO E SERVICOS GERAIS LTDA.",
    "matriz_ou_filial": "Matriz",
    "municipio": "Abadia de Goiás",
    "uf": "GO",
    "no_registro": "1128450   ",
    "data_cadastro": "08-05-2009",
    "ate_5_salarios_minimos": "57",
    "acima_de_5_salarios_minimos": "0",
    "total_trabalhadores": "57",
    "situacao": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "_arquivo_origem": "relacao-beneficiarias-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:33:30.874215+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "08310826000169",
    "razao_social": "ESQUADRIAL VIDROS E ESQUADRIAS DE ALUMINIO LTDA",
    "matriz_ou_filial": "Matriz",
    "municipio": "Abadia de Goiás",
    "uf": "GO",
    "no_registro": "1151720   ",
    "data_cadastro": "01-07-2009",
    "ate_5_salarios_minimos": "63",
    "acima_de_5_salarios_minimos": "0",
    "total_trabalhadores": "63",
    "situacao": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "_arquivo_origem": "relacao-beneficiarias-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:33:30.874215+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "325800357283",
    "razao_social": "HELENA MARIA DO PRADO E OUTROS",
    "matriz_ou_filial": "Matriz",
    "municipio": "Abadia de Goiás",
    "uf": "GO",
    "no_registro": "2011824   ",
    "data_cadastro": "28-04-2014",
    "ate_5_salarios_minimos": "66",
    "acima_de_5_salarios_minimos": "2",
    "total_trabalhadores": "68",
    "situacao": "Ativo",
    "_sheet_origem": "Beneficiárias-ATIVO",
    "_arquivo_origem": "relacao-beneficiarias-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:33:30.874215+00:00",
    "_periodo": "2025-12-31"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_pat.empresas_beneficiarias\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_pat.empresas_beneficiarias`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
