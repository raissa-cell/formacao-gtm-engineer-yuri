# `silver_cnpj.socios_por_pessoa` — _TODO: título curto_

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
| `socio_nome_norm` | STRING |  |  |
| `socio_cpf_visible` | STRING |  |  |
| `socio_nome` | STRING |  |  |
| `empresas` | RECORD | REPEATED |  |
| `empresas.empresa_cnpj_basico` | STRING |  |  |
| `empresas.empresa_razao_social` | STRING |  |  |
| `empresas.qualificacao_nome` | STRING |  |  |
| `empresas.data_entrada_sociedade` | DATE |  |  |
| `n_empresas` | INTEGER |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "socio_nome_norm": "benedito jesus de gusmao",
    "socio_cpf_visible": "***782358**",
    "socio_nome": "BENEDITO JESUS DE GUSMAO",
    "empresas": [
      {
        "empresa_cnpj_basico": "03839903",
        "empresa_razao_social": "GUSMAO & FERREIRA SJ DOS CAMPOS LTDA",
        "qualificacao_nome": "Sócio-Administrador",
        "data_entrada_sociedade": "2000-05-19"
      }
    ],
    "n_empresas": 1
  },
  {
    "socio_nome_norm": "benedito paulo de almeida avila",
    "socio_cpf_visible": "***782486**",
    "socio_nome": "BENEDITO PAULO DE ALMEIDA AVILA",
    "empresas": [
      {
        "empresa_cnpj_basico": "23593778",
        "empresa_razao_social": "ALMEIDA CARVALHO ALIMENTOS LTDA",
        "qualificacao_nome": "Sócio-Administrador",
        "data_entrada_sociedade": "2015-11-04"
      }
    ],
    "n_empresas": 1
  },
  {
    "socio_nome_norm": "bruna becker",
    "socio_cpf_visible": "***782840**",
    "socio_nome": "BRUNA BECKER",
    "empresas": [
      {
        "empresa_cnpj_basico": "08043206",
        "empresa_razao_social": "BECKER & BERTONI COMERCIO DE AREIA LTDA",
        "qualificacao_nome": "Sócio-Administrador",
        "data_entrada_sociedade": "2012-10-09"
      }
    ],
    "n_empresas": 1
  },
  {
    "socio_nome_norm": "bruna alves dos santos",
    "socio_cpf_visible": "***782856**",
    "socio_nome": "BRUNA ALVES DOS SANTOS",
    "empresas": [
      {
        "empresa_cnpj_basico": "60693123",
        "empresa_razao_social": "BA SANTOS SERVICOS MEDICOS LTDA",
        "qualificacao_nome": "Sócio-Administrador",
        "data_entrada_sociedade": "2025-05-06"
      },
      {
        "empresa_cnpj_basico": "43247127",
        "empresa_razao_social": "ALOR SERVICOS MEDICOS LTDA",
        "qualificacao_nome": "Sócio-Administrador",
        "data_entrada_sociedade": "2021-08-24"
      }
    ],
    "n_empresas": 2
  },
  {
    "socio_nome_norm": "brena ceila oliveira corado dos santos",
    "socio_cpf_visible": "***785051**",
    "socio_nome": "BRENA CEILA OLIVEIRA CORADO DOS SANTOS",
    "empresas": [
      {
        "empresa_cnpj_basico": "52160912",
        "empresa_razao_social": "AGROAMBIENTAL SERVICOS DE AGRONOMIA LTDA",
        "qualificacao_nome": "Sócio-Administrador",
        "data_entrada_sociedade": "2023-09-13"
      }
    ],
    "n_empresas": 1
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.socios_por_pessoa\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.socios_por_pessoa`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
