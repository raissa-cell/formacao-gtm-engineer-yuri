# `bronze_pat.empresas_facilitadoras` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** bronze
**Granularidade:** _TODO_
**Linhas (~):** 645
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
    "cnpj": "84308980000184",
    "razao_social": "A C D A IMPORTACAO E EXPORTACAO LTDA",
    "matriz_ou_filial": null,
    "municipio": "Rio Branco",
    "uf": "AC",
    "no_registro": "090196160 ",
    "data_cadastro": "25-01-2008",
    "situacao": "Ativo",
    "_sheet_origem": "Facilitadoras-ATIVO",
    "_arquivo_origem": "relacao-facilitadoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:04.683495+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "34059178000120",
    "razao_social": "SACOLEIRO MARKET PLACE E INSTITUIÇÃO DE PAGAMENTO LTDA",
    "matriz_ou_filial": null,
    "municipio": "Rio Branco",
    "uf": "AC",
    "no_registro": "230801300 ",
    "data_cadastro": "12-05-2023",
    "situacao": "Ativo",
    "_sheet_origem": "Facilitadoras-ATIVO",
    "_arquivo_origem": "relacao-facilitadoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:04.683495+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "20077927000137",
    "razao_social": "MUSE SOLUCOES EM PAGAMENTOS LTDA",
    "matriz_ou_filial": null,
    "municipio": "Maceió",
    "uf": "AL",
    "no_registro": "220779620 ",
    "data_cadastro": "22-07-2022",
    "situacao": "Ativo",
    "_sheet_origem": "Facilitadoras-ATIVO",
    "_arquivo_origem": "relacao-facilitadoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:04.683495+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "07438697000126",
    "razao_social": "PRESTCARD ADMINISTRADORA DE CARTÃO LTDA - ME",
    "matriz_ou_filial": null,
    "municipio": "Camaçari",
    "uf": "BA",
    "no_registro": "080076212 ",
    "data_cadastro": "18-06-2008",
    "situacao": "Ativo",
    "_sheet_origem": "Facilitadoras-ATIVO",
    "_arquivo_origem": "relacao-facilitadoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:04.683495+00:00",
    "_periodo": "2025-12-31"
  },
  {
    "cnpj": "10595517000124",
    "razao_social": "PLUSCARD ADMINISTRADORA DE CARTÕES E SERVIÇOS LTDA",
    "matriz_ou_filial": null,
    "municipio": "Candeias",
    "uf": "BA",
    "no_registro": "090187423 ",
    "data_cadastro": "01-06-2009",
    "situacao": "Ativo",
    "_sheet_origem": "Facilitadoras-ATIVO",
    "_arquivo_origem": "relacao-facilitadoras-PAT-ate 31.12.2025-disponibilizar.xlsx",
    "_data_carga": "2026-05-02T20:34:04.683495+00:00",
    "_periodo": "2025-12-31"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`bronze_pat.empresas_facilitadoras\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.bronze_pat.empresas_facilitadoras`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
