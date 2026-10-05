# `gold_cnpj.pessoas` — Pessoas físicas deduplicadas (cross-empresas)

**Tipo:** TABLE
**Camada:** gold
**Granularidade:** 1 linha por **pessoa PF deduplicada** por `(nome_norm, cpf_visivel)`. Cada pessoa traz array com TODOS os CNPJ_BASICOs onde aparece (cotista OU diretor).
**Linhas (~):** 10,204,292
**Chave:** `id` = `nome_norm + '_' + cpf_visivel`
**Cluster BY:** `nome_norm`, `cpf_visivel`
**Refresh:** semanal — mesmo Cloud Run Job de `gold_cnpj.empresas` (segunda 08:00 BRT). Build: `python -m scripts.cnpj.gold_pessoas --build`.
**Origem:** `bronze_cnpj.socios` filtrado por `ID_SOCIO='2'` (PF) + agregação por `(nome_norm, cpf_visivel)`. Spec: [`docs/cnpj/arquitetura-comercial-v2.md`](../../../../docs/cnpj/arquitetura-comercial-v2.md).

**Descrição BQ:** Card de pessoa PF deduplicado, sem referenciar empresas detalhadamente (apenas array de CNPJs). Permite cross-empresa: "em quais empresas a pessoa X aparece?".

---

## Quando usar

⭐ **Pra busca cross-empresas por pessoa**: dado um nome/CPF, retornar TODAS as empresas onde aparece como sócio/diretor. Sem precisar abrir cada doc empresa.

⭐ **Pra perfil de pessoa**: idade aproximada (faixa_etaria), tempo de vínculo societário (primeiro_vinculo / ultimo_vinculo), perfil de papel (sócio cotista vs diretor estatutário via `qualificacoes_aparece`).

**NÃO use** quando precisar de:
- **Detalhe da empresa onde aparece** → usar `empresas_cnpj_basicos[]` como lookup pra fazer `WHERE cnpj_basico IN UNNEST(...)` em `gold_cnpj.empresas`
- **Pessoa PJ** (sócio PJ) → essas estão em `gold_cnpj.empresas.socios.pessoas_juridicas_*` (não há doc próprio pra PJ porque PJ já é uma empresa)
- **Histórico cronológico** de quando entrou/saiu de cada empresa → ainda não tem; usar `bronze_cnpj.socios.DATA_ENTRADA_SOCIEDADE` cru

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `id` | STRING |  |  |
| `nome` | STRING |  |  |
| `nome_norm` | STRING |  |  |
| `cpf_visivel` | STRING |  |  |
| `faixa_etaria` | RECORD |  |  |
| `faixa_etaria.codigo` | STRING |  |  |
| `faixa_etaria.descricao` | STRING |  |  |
| `qtd_empresas` | INTEGER |  |  |
| `primeiro_vinculo_data` | DATE |  |  |
| `ultimo_vinculo_data` | DATE |  |  |
| `qualificacoes_aparece` | RECORD | REPEATED |  |
| `qualificacoes_aparece.codigo` | STRING |  |  |
| `qualificacoes_aparece.descricao` | STRING |  |  |
| `qualificacoes_aparece.qtd` | INTEGER |  |  |
| `empresas_cnpj_basicos` | STRING | REPEATED |  |
| `contato` | RECORD |  |  |
| `contato.email` | STRING |  |  |
| `contato.telefone` | STRING |  |  |
| `contato.linkedin` | STRING |  |  |
| `biografia` | STRING |  |  |
| `links_publicos` | STRING | REPEATED |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |
| `_fontes` | STRING | REPEATED |  |

## Sample (5 linhas reais)

```json
[
  {
    "id": "hiram ayres monteiro neto_***033958**",
    "nome": "HIRAM AYRES MONTEIRO NETO",
    "nome_norm": "hiram ayres monteiro neto",
    "cpf_visivel": "***033958**",
    "faixa_etaria": {
      "codigo": "1",
      "descricao": null
    },
    "qtd_empresas": 1,
    "primeiro_vinculo_data": "2013-11-07",
    "ultimo_vinculo_data": "2013-11-07",
    "qualificacoes_aparece": [
      {
        "codigo": "30",
        "descricao": "Sócio Menor (Assistido/Representado)",
        "qtd": 1
      }
    ],
    "empresas_cnpj_basicos": [
      "19219316"
    ],
    "contato": null,
    "biografia": null,
    "links_publicos": [],
    "_periodo": "2026-05",
    "_data_carga": "2026-05-02T23:18:58.956466+00:00",
    "_fontes": [
      "rfb_bronze"
    ]
  },
  {
    "id": "helena bertoi caleffi_***151980**",
    "nome": "HELENA BERTOI CALEFFI",
    "nome_norm": "helena bertoi caleffi",
    "cpf_visivel": "***151980**",
    "faixa_etaria": {
      "codigo": "1",
      "descricao": null
    },
    "qtd_empresas": 1,
    "primeiro_vinculo_data": "2014-07-24",
    "ultimo_vinculo_data": "2014-07-24",
    "qualificacoes_aparece": [
      {
        "codigo": "30",
        "descricao": "Sócio Menor (Assistido/Representado)",
        "qtd": 1
      }
    ],
    "empresas_cnpj_basicos": [
      "20718991"
    ],
    "contato": null,
    "biografia": null,
    "links_publicos": [],
    "_periodo": "2026-05",
    "_data_carga": "2026-05-02T23:18:58.956466+00:00",
    "_fontes": [
      "rfb_bronze"
    ]
  },
  {
    "id": "henry oliveira piornedo_***596749**",
    "nome": "HENRY OLIVEIRA PIORNEDO",
    "nome_norm": "henry oliveira piornedo",
    "cpf_visivel": "***596749**",
    "faixa_etaria": {
      "codigo": "1",
      "descricao": null
    },
    "qtd_empresas": 1,
    "primeiro_vinculo_data": "2014-08-29",
    "ultimo_vinculo_data": "2014-08-29",
    "qualificacoes_aparece": [
      {
        "codigo": "30",
        "descricao": "Sócio Menor (Assistido/Representado)",
        "qtd": 1
      }
    ],
    "empresas_cnpj_basicos": [
      "17226078"
    ],
    "contato": null,
    "biografia": null,
    "links_publicos": [],
    "_periodo": "2026-05",
    "_data_carga": "2026-05-02T23:18:58.956466+00:00",
    "_fontes": [
      "rfb_bronze"
    ]
  },
  {
    "id": "heitor ladeia rodrigues_***759596**",
    "nome": "HEITOR LADEIA RODRIGUES",
    "nome_norm": "heitor ladeia rodrigues",
    "cpf_visivel": "***759596**",
    "faixa_etaria": {
      "codigo": "1",
      "descricao": null
    },
    "qtd_empresas": 2,
    "primeiro_vinculo_data": "2014-11-04",
    "ultimo_vinculo_data": "2021-01-13",
    "qualificacoes_aparece": [
      {
        "codigo": "30",
        "descricao": "Sócio Menor (Assistido/Representado)",
        "qtd": 2
      }
    ],
    "empresas_cnpj_basicos": [
      "21339946",
      "40384961"
    ],
    "contato": null,
    "biografia": null,
    "links_publicos": [],
    "_periodo": "2026-05",
    "_data_carga": "2026-05-02T23:18:58.956466+00:00",
    "_fontes": [
      "rfb_bronze"
    ]
  },
  {
    "id": "henrique bonito goncalves_***710108**",
    "nome": "HENRIQUE BONITO GONCALVES",
    "nome_norm": "henrique bonito goncalves",
    "cpf_visivel": "***710108**",
    "faixa_etaria": {
      "codigo": "1",
      "descricao": null
    },
    "qtd_empresas": 1,
    "primeiro_vinculo_data": "2015-01-26",
    "ultimo_vinculo_data": "2015-01-26",
    "qualificacoes_aparece": [
      {
        "codigo": "30",
        "descricao": "Sócio Menor (Assistido/Representado)",
        "qtd": 1
      }
    ],
    "empresas_cnpj_basicos": [
      "19198062"
    ],
    "contato": null,
    "biografia": null,
    "links_publicos": [],
    "_periodo": "2026-05",
    "_data_carga": "2026-05-02T23:18:58.956466+00:00",
    "_fontes": [
      "rfb_bronze"
    ]
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_cnpj.pessoas\` LIMIT 5'`

## Quirks e armadilhas

- **CPF mascarado tem 6 dígitos visíveis** (`***123456**`). Dedupe por `(nome_norm, cpf_visivel)` é forte mas não 100% — dois homônimos com mesmo CPF mascarado podem colidir (probabilidade baixa, ~1 em 1M).
- **`nome_norm` é a chave de busca**: `LOWER + sem acento + espaços únicos`. Use `WHERE nome_norm = 'pedro zinner'` (não `WHERE nome = 'Pedro Zinner'`).
- **`empresas_cnpj_basicos` mistura papéis**: cotista, diretor, procurador — todos. Pra distinguir, ver `qualificacoes_aparece[].descricao`.
- **`contato`, `biografia`, `links_publicos` sempre `null`** — placeholders pra enrichment futuro (LinkedIn, etc.).
- **Não tem PJ** — só pessoa física. PJ sócia é "uma empresa", então vive em `gold_cnpj.empresas.socios.pessoas_juridicas_*`.
- **Faixa etária aproximada** (codigo: 1=0-12, 2=13-20, 3=21-30, 4=31-40, 5=41-50, 6=51-60, 7=61-70, 8=71-80, 9=>80, 0=desconhecida). Da RFB (sem precisão de aniversário).

## Tabelas relacionadas

- [`gold_cnpj.empresas`](gold_cnpj.empresas.md) — JOIN reverso via `WHERE cnpj_basico IN UNNEST(empresas_cnpj_basicos)` pra trazer detalhe das empresas
- [`silver_cnpj.socios_por_pessoa`](silver_cnpj.socios_por_pessoa.md) — view alternativa com mesma intenção (legado)
- [`silver_cnpj.rede_executivos`](silver_cnpj.rede_executivos.md) — top pessoas por # empresas (board members serial)
- [`bronze_cnpj.socios`](bronze_cnpj.socios.md) — fonte cru com cada vínculo separado

## Templates SQL

### Caso A: empresas onde "Andre Street de Aguiar" aparece
```sql
WITH pessoa AS (
  SELECT empresas_cnpj_basicos AS cnpjs, qualificacoes_aparece
  FROM `data-hacker-488115.gold_cnpj.pessoas`
  WHERE nome_norm = 'andre street de aguiar'
)
SELECT e.cnpj_basico, e.nome, e.industria.setor, e.local.matriz.uf
FROM `data-hacker-488115.gold_cnpj.empresas` e, pessoa
WHERE e.cnpj_basico IN UNNEST(pessoa.cnpjs)
ORDER BY e.financeiro.capital_social_brl DESC;
```

### Caso B: top board members (pessoas em ≥10 empresas)
```sql
SELECT nome, cpf_visivel, qtd_empresas,
       ARRAY(SELECT q.descricao FROM UNNEST(qualificacoes_aparece) q LIMIT 3) AS top_qualif
FROM `data-hacker-488115.gold_cnpj.pessoas`
WHERE qtd_empresas >= 10
ORDER BY qtd_empresas DESC
LIMIT 50;
```

### Caso C: pessoas mais novas (sócios <30 anos) com >5 empresas
```sql
SELECT nome, faixa_etaria.descricao AS faixa, qtd_empresas
FROM `data-hacker-488115.gold_cnpj.pessoas`
WHERE faixa_etaria.codigo IN ('2', '3')   -- 13-30 anos
  AND qtd_empresas >= 5
ORDER BY qtd_empresas DESC;
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
