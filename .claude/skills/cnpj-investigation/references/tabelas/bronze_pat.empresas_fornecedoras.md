# `bronze_pat.empresas_fornecedoras` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 27,349
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
| `situacao` | STRING |  |  |
| `_sheet_origem` | STRING |  |  |
| `_arquivo_origem` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_periodo` | STRING |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "11263481000144",
    "razao_social": "ANA FLAVIA BEGHELLI JUSTINO",
    "matriz_ou_filial": null,
    "municipio": "Abadia de Goiás",
    "uf": "GO",
    "no_registro": "100245732 ",
    "data_cadastro": "23-08-2010",
    "situacao": "Ativo",
    "_sheet_origem": "Fornecedoras-ATIVO",
    "_arquivo_origem": "relacao-fornecedoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:08.129413+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "26298762000100",
    "razao_social": "CIA BELLA EIRELI",
    "matriz_ou_filial": null,
    "municipio": "Abadia de Goiás",
    "uf": "GO",
    "no_registro": "190694940 ",
    "data_cadastro": "13-03-2017",
    "situacao": "Ativo",
    "_sheet_origem": "Fornecedoras-ATIVO",
    "_arquivo_origem": "relacao-fornecedoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:08.129413+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "17687653000193",
    "razao_social": "Premium Comercio e Empacotamento Eireli -ME",
    "matriz_ou_filial": null,
    "municipio": "Abadia dos Dourados",
    "uf": "MG",
    "no_registro": "140432876 ",
    "data_cadastro": "18-04-2013",
    "situacao": "Ativo",
    "_sheet_origem": "Fornecedoras-ATIVO",
    "_arquivo_origem": "relacao-fornecedoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:08.129413+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "08602280000209",
    "razao_social": "Fouet Serviços de Alimentação Ltda",
    "matriz_ou_filial": null,
    "municipio": "Abadia dos Dourados",
    "uf": "MG",
    "no_registro": "170575493 ",
    "data_cadastro": "13-03-2017",
    "situacao": "Ativo",
    "_sheet_origem": "Fornecedoras-ATIVO",
    "_arquivo_origem": "relacao-fornecedoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:08.129413+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "27665474000109",
    "razao_social": "CHURRASCARIA UAI TCHE GRILL EIRELI ME",
    "matriz_ou_filial": null,
    "municipio": "Abadia dos Dourados",
    "uf": "MG",
    "no_registro": "170600349 ",
    "data_cadastro": "01-09-2017",
    "situacao": "Ativo",
    "_sheet_origem": "Fornecedoras-ATIVO",
    "_arquivo_origem": "relacao-fornecedoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:08.129413+00:00",
    "_periodo": "2025-12-31"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_pat.empresas_fornecedoras\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_pat.empresas_fornecedoras`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
