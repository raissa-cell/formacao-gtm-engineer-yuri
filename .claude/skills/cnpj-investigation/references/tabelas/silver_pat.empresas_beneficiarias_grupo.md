# `silver_pat.empresas_beneficiarias_grupo` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** 345,726
**Chave:** _TODO_
**Cluster BY:** `cnpj_basico`, `porte`
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj_basico` | STRING |  |  |
| `razao_social_grupo` | STRING |  |  |
| `razao_social_pat` | STRING |  |  |
| `cod_natureza_juridica` | STRING |  |  |
| `natureza_juridica_descricao` | STRING |  |  |
| `cod_porte` | STRING |  |  |
| `porte` | STRING |  |  |
| `capital_social` | NUMERIC |  |  |
| `cnae_principal_codigo` | STRING |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `data_inicio_atividade` | DATE |  |  |
| `idade_anos` | INTEGER |  |  |
| `optante_simples` | BOOLEAN |  |  |
| `optante_mei` | BOOLEAN |  |  |
| `uf_matriz_rfb` | STRING |  |  |
| `municipio_matriz_rfb` | STRING |  |  |
| `situacao_grupo_descricao` | STRING |  |  |
| `unidades_pat` | INTEGER |  |  |
| `unidades_pat_matriz` | INTEGER |  |  |
| `unidades_pat_filial` | INTEGER |  |  |
| `unidades_pat_ativas` | INTEGER |  |  |
| `unidades_pat_inativas` | INTEGER |  |  |
| `total_trabalhadores_grupo` | INTEGER |  |  |
| `total_trabalhadores_ativos` | INTEGER |  |  |
| `total_trabalhadores_inativos` | INTEGER |  |  |
| `trabalhadores_ate_5sm_grupo` | INTEGER |  |  |
| `trabalhadores_ate_5sm_ativos` | INTEGER |  |  |
| `trabalhadores_acima_5sm_grupo` | INTEGER |  |  |
| `trabalhadores_acima_5sm_ativos` | INTEGER |  |  |
| `pct_baixa_renda` | FLOAT |  |  |
| `pct_baixa_renda_ativos` | FLOAT |  |  |
| `ufs_atuacao` | STRING | REPEATED |  |
| `qtd_ufs_atuacao` | INTEGER |  |  |
| `municipios_atuacao_top20` | RECORD | REPEATED |  |
| `municipios_atuacao_top20.value` | STRING |  |  |
| `municipios_atuacao_top20.count` | INTEGER |  |  |
| `qtd_filiais_ativas_rfb` | INTEGER |  |  |
| `qtd_filiais_total_rfb` | INTEGER |  |  |
| `cobertura_pat_pct` | FLOAT |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj_basico": "67215555",
    "razao_social_grupo": "ALPHA DISPLAY INDUSTRIA E COMERCIO LTDA",
    "razao_social_pat": "ALPHA DISPLAY INDUSTRIA E COMERCIO LTDA",
    "cod_natureza_juridica": null,
    "natureza_juridica_descricao": null,
    "cod_porte": null,
    "porte": null,
    "capital_social": null,
    "cnae_principal_codigo": null,
    "cnae_principal_descricao": null,
    "data_inicio_atividade": null,
    "idade_anos": null,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz_rfb": null,
    "municipio_matriz_rfb": null,
    "situacao_grupo_descricao": null,
    "unidades_pat": 1,
    "unidades_pat_matriz": 1,
    "unidades_pat_filial": 0,
    "unidades_pat_ativas": 0,
    "unidades_pat_inativas": 1,
    "total_trabalhadores_grupo": 188,
    "total_trabalhadores_ativos": 0,
    "total_trabalhadores_inativos": 188,
    "trabalhadores_ate_5sm_grupo": 178,
    "trabalhadores_ate_5sm_ativos": 0,
    "trabalhadores_acima_5sm_grupo": 10,
    "trabalhadores_acima_5sm_ativos": 0,
    "pct_baixa_renda": 94.68,
    "pct_baixa_renda_ativos": null,
    "ufs_atuacao": [
      "SP"
    ],
    "qtd_ufs_atuacao": 1,
    "municipios_atuacao_top20": [
      {
        "value": "São Paulo",
        "count": 1
      }
    ],
    "qtd_filiais_ativas_rfb": null,
    "qtd_filiais_total_rfb": null,
    "cobertura_pat_pct": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:24.625979+00:00"
  },
  {
    "cnpj_basico": "81260429",
    "razao_social_grupo": "COMERCIO DE BICICLETAS J J LTDA",
    "razao_social_pat": "COMERCIO DE BICICLETAS J J LTDA",
    "cod_natureza_juridica": null,
    "natureza_juridica_descricao": null,
    "cod_porte": null,
    "porte": null,
    "capital_social": null,
    "cnae_principal_codigo": null,
    "cnae_principal_descricao": null,
    "data_inicio_atividade": null,
    "idade_anos": null,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz_rfb": null,
    "municipio_matriz_rfb": null,
    "situacao_grupo_descricao": null,
    "unidades_pat": 1,
    "unidades_pat_matriz": 1,
    "unidades_pat_filial": 0,
    "unidades_pat_ativas": 0,
    "unidades_pat_inativas": 1,
    "total_trabalhadores_grupo": 3,
    "total_trabalhadores_ativos": 0,
    "total_trabalhadores_inativos": 3,
    "trabalhadores_ate_5sm_grupo": 3,
    "trabalhadores_ate_5sm_ativos": 0,
    "trabalhadores_acima_5sm_grupo": 0,
    "trabalhadores_acima_5sm_ativos": 0,
    "pct_baixa_renda": 100.0,
    "pct_baixa_renda_ativos": null,
    "ufs_atuacao": [
      "PR"
    ],
    "qtd_ufs_atuacao": 1,
    "municipios_atuacao_top20": [
      {
        "value": "Curitiba",
        "count": 1
      }
    ],
    "qtd_filiais_ativas_rfb": null,
    "qtd_filiais_total_rfb": null,
    "cobertura_pat_pct": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:24.625979+00:00"
  },
  {
    "cnpj_basico": "92982993",
    "razao_social_grupo": "ASSEMP ASSESSORIA EMPRESARIAL LTDA",
    "razao_social_pat": "ASSEMP ASSESSORIA EMPRESARIAL LTDA",
    "cod_natureza_juridica": null,
    "natureza_juridica_descricao": null,
    "cod_porte": null,
    "porte": null,
    "capital_social": null,
    "cnae_principal_codigo": null,
    "cnae_principal_descricao": null,
    "data_inicio_atividade": null,
    "idade_anos": null,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz_rfb": null,
    "municipio_matriz_rfb": null,
    "situacao_grupo_descricao": null,
    "unidades_pat": 1,
    "unidades_pat_matriz": 1,
    "unidades_pat_filial": 0,
    "unidades_pat_ativas": 0,
    "unidades_pat_inativas": 1,
    "total_trabalhadores_grupo": 3,
    "total_trabalhadores_ativos": 0,
    "total_trabalhadores_inativos": 3,
    "trabalhadores_ate_5sm_grupo": 3,
    "trabalhadores_ate_5sm_ativos": 0,
    "trabalhadores_acima_5sm_grupo": 0,
    "trabalhadores_acima_5sm_ativos": 0,
    "pct_baixa_renda": 100.0,
    "pct_baixa_renda_ativos": null,
    "ufs_atuacao": [
      "RS"
    ],
    "qtd_ufs_atuacao": 1,
    "municipios_atuacao_top20": [
      {
        "value": "Porto Alegre",
        "count": 1
      }
    ],
    "qtd_filiais_ativas_rfb": null,
    "qtd_filiais_total_rfb": null,
    "cobertura_pat_pct": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:24.625979+00:00"
  },
  {
    "cnpj_basico": "78209196",
    "razao_social_grupo": "FRANCINE MÓVEIS LTDA",
    "razao_social_pat": "FRANCINE MÓVEIS LTDA",
    "cod_natureza_juridica": null,
    "natureza_juridica_descricao": null,
    "cod_porte": null,
    "porte": null,
    "capital_social": null,
    "cnae_principal_codigo": null,
    "cnae_principal_descricao": null,
    "data_inicio_atividade": null,
    "idade_anos": null,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz_rfb": null,
    "municipio_matriz_rfb": null,
    "situacao_grupo_descricao": null,
    "unidades_pat": 1,
    "unidades_pat_matriz": 1,
    "unidades_pat_filial": 0,
    "unidades_pat_ativas": 0,
    "unidades_pat_inativas": 1,
    "total_trabalhadores_grupo": 77,
    "total_trabalhadores_ativos": 0,
    "total_trabalhadores_inativos": 77,
    "trabalhadores_ate_5sm_grupo": 77,
    "trabalhadores_ate_5sm_ativos": 0,
    "trabalhadores_acima_5sm_grupo": 0,
    "trabalhadores_acima_5sm_ativos": 0,
    "pct_baixa_renda": 100.0,
    "pct_baixa_renda_ativos": null,
    "ufs_atuacao": [
      "SC"
    ],
    "qtd_ufs_atuacao": 1,
    "municipios_atuacao_top20": [
      {
        "value": "São Bento do Sul",
        "count": 1
      }
    ],
    "qtd_filiais_ativas_rfb": null,
    "qtd_filiais_total_rfb": null,
    "cobertura_pat_pct": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:24.625979+00:00"
  },
  {
    "cnpj_basico": "70912963",
    "razao_social_grupo": "JOSE CABELLO",
    "razao_social_pat": "JOSE CABELLO",
    "cod_natureza_juridica": null,
    "natureza_juridica_descricao": null,
    "cod_porte": null,
    "porte": null,
    "capital_social": null,
    "cnae_principal_codigo": null,
    "cnae_principal_descricao": null,
    "data_inicio_atividade": null,
    "idade_anos": null,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz_rfb": null,
    "municipio_matriz_rfb": null,
    "situacao_grupo_descricao": null,
    "unidades_pat": 1,
    "unidades_pat_matriz": 1,
    "unidades_pat_filial": 0,
    "unidades_pat_ativas": 0,
    "unidades_pat_inativas": 1,
    "total_trabalhadores_grupo": 4,
    "total_trabalhadores_ativos": 0,
    "total_trabalhadores_inativos": 4,
    "trabalhadores_ate_5sm_grupo": 4,
    "trabalhadores_ate_5sm_ativos": 0,
    "trabalhadores_acima_5sm_grupo": 0,
    "trabalhadores_acima_5sm_ativos": 0,
    "pct_baixa_renda": 100.0,
    "pct_baixa_renda_ativos": null,
    "ufs_atuacao": [
      "SP"
    ],
    "qtd_ufs_atuacao": 1,
    "municipios_atuacao_top20": [
      {
        "value": "São José dos Campos",
        "count": 1
      }
    ],
    "qtd_filiais_ativas_rfb": null,
    "qtd_filiais_total_rfb": null,
    "cobertura_pat_pct": null,
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:05:24.625979+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_pat.empresas_beneficiarias_grupo\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_pat.empresas_beneficiarias_grupo`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
