# `gold_pat.empresas_outliers_suspeitos` — _TODO: título curto_

**Tipo:** VIEW
**Camada:** gold
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
| `cnpj_basico` | STRING |  |  |
| `razao_social` | STRING |  |  |
| `cod_natureza_juridica` | STRING |  |  |
| `natureza_juridica` | STRING |  |  |
| `porte` | STRING |  |  |
| `capital_social` | NUMERIC |  |  |
| `total_trabalhadores` | INTEGER |  |  |
| `trabalhadores_ate_5sm` | INTEGER |  |  |
| `trabalhadores_acima_5sm` | INTEGER |  |  |
| `qtd_unidades_pat_ativas` | INTEGER |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `uf_matriz` | STRING |  |  |
| `municipio_matriz` | STRING |  |  |
| `razao_suspeita` | STRING |  |  |
| `score_suspeita` | INTEGER |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj_basico": "33041260",
    "razao_social": "GRUPO CASAS BAHIA S.A.",
    "cod_natureza_juridica": "2046",
    "natureza_juridica": "Sociedade Anônima Aberta",
    "porte": "DEMAIS",
    "capital_social": "7108560498.390000343",
    "total_trabalhadores": 26390,
    "trabalhadores_ate_5sm": 2057,
    "trabalhadores_acima_5sm": 24333,
    "qtd_unidades_pat_ativas": 1072,
    "cnae_principal_descricao": "Comércio varejista especializado de eletrodomésticos e equipamentos de áudio e vídeo",
    "uf_matriz": "SP",
    "municipio_matriz": "SAO PAULO",
    "razao_suspeita": "PROPORCAO_ALTA_RENDA_IMPLAUSIVEL",
    "score_suspeita": 0
  },
  {
    "cnpj_basico": "29212545",
    "razao_social": "NOVA RIO SERVICOS GERAIS LTDA",
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "porte": "DEMAIS",
    "capital_social": "35000000",
    "total_trabalhadores": 25228,
    "trabalhadores_ate_5sm": 1713,
    "trabalhadores_acima_5sm": 23515,
    "qtd_unidades_pat_ativas": 3,
    "cnae_principal_descricao": "Serviços combinados de escritório e apoio administrativo",
    "uf_matriz": "RJ",
    "municipio_matriz": "RIO DE JANEIRO",
    "razao_suspeita": "PROPORCAO_ALTA_RENDA_IMPLAUSIVEL",
    "score_suspeita": 0
  },
  {
    "cnpj_basico": "93015006",
    "razao_social": "COMPANHIA ZAFFARI COMERCIO E INDUSTRIA",
    "cod_natureza_juridica": "2054",
    "natureza_juridica": "Sociedade Anônima Fechada",
    "porte": "DEMAIS",
    "capital_social": "0",
    "total_trabalhadores": 12857,
    "trabalhadores_ate_5sm": 12557,
    "trabalhadores_acima_5sm": 300,
    "qtd_unidades_pat_ativas": 50,
    "cnae_principal_descricao": "Comércio varejista de mercadorias em geral, com predominância de produtos alimentícios - hipermercados",
    "uf_matriz": "RS",
    "municipio_matriz": "PORTO ALEGRE",
    "razao_suspeita": "CAPITAL_INCOERENTE_GRAVE",
    "score_suspeita": 2
  },
  {
    "cnpj_basico": "08744139",
    "razao_social": "G&E SERVICOS TERCEIRIZADOS LTDA",
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "porte": "DEMAIS",
    "capital_social": "20000000",
    "total_trabalhadores": 11060,
    "trabalhadores_ate_5sm": 16,
    "trabalhadores_acima_5sm": 11044,
    "qtd_unidades_pat_ativas": 1,
    "cnae_principal_descricao": "Serviços combinados de escritório e apoio administrativo",
    "uf_matriz": "DF",
    "municipio_matriz": "BRASILIA",
    "razao_suspeita": "PROPORCAO_ALTA_RENDA_IMPLAUSIVEL",
    "score_suspeita": 1
  },
  {
    "cnpj_basico": "02182621",
    "razao_social": "LOCANTY COM SERVICOS LTDA - EM RECUPERACAO JUDICIAL",
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "porte": "DEMAIS",
    "capital_social": "0",
    "total_trabalhadores": 8018,
    "trabalhadores_ate_5sm": 7937,
    "trabalhadores_acima_5sm": 81,
    "qtd_unidades_pat_ativas": 1,
    "cnae_principal_descricao": "Transporte rodoviário de carga, exceto produtos perigosos e mudanças, intermunicipal, interestadual e internacional",
    "uf_matriz": "RJ",
    "municipio_matriz": "RIO DE JANEIRO",
    "razao_suspeita": "CAPITAL_INCOERENTE_GRAVE",
    "score_suspeita": 3
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_pat.empresas_outliers_suspeitos\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.gold_pat.empresas_outliers_suspeitos`
WHERE ...
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
