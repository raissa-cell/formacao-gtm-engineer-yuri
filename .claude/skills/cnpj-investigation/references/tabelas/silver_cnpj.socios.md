# `silver_cnpj.socios` — _TODO: título curto_

**Tipo:** TABLE
**Camada:** silver
**Granularidade:** _TODO_
**Linhas (~):** 27,494,742
**Chave:** _TODO_
**Cluster BY:** `socio_nome_norm`, `socio_cnpj_basico`
**Refresh:** _TODO_ (mensal | semanal | sob demanda)
**Origem:** _TODO_

**Descrição BQ:** _(sem descrição na tabela BQ — preencher)_

---

## Quando usar

_TODO: 1-2 frases. Quando essa tabela é a melhor escolha. Quando NÃO usar._

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `empresa_cnpj_basico` | STRING |  |  |
| `empresa_razao_social` | STRING |  |  |
| `empresa_natureza_juridica` | STRING |  |  |
| `socio_tipo` | STRING |  |  |
| `socio_nome` | STRING |  |  |
| `socio_nome_norm` | STRING |  |  |
| `socio_documento` | STRING |  |  |
| `socio_cnpj_basico` | STRING |  |  |
| `socio_razao_social` | STRING |  |  |
| `socio_cpf_visible` | STRING |  |  |
| `qualificacao_codigo` | STRING |  |  |
| `qualificacao_nome` | STRING |  |  |
| `data_entrada_sociedade` | DATE |  |  |
| `representante_legal_documento` | STRING |  |  |
| `representante_legal_nome` | STRING |  |  |
| `representante_legal_qualificacao_codigo` | STRING |  |  |
| `representante_legal_qualificacao_nome` | STRING |  |  |
| `pais_codigo` | STRING |  |  |
| `pais_nome` | STRING |  |  |
| `faixa_etaria` | STRING |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "empresa_cnpj_basico": "22328691",
    "empresa_razao_social": "MAYLU PARTICIPACOES S.A",
    "empresa_natureza_juridica": "2054",
    "socio_tipo": "PJ",
    "socio_nome": "PEREIRA E SAMPAIO PARTICIPACOES LTDA",
    "socio_nome_norm": "pereira e sampaio participacoes ltda",
    "socio_documento": "21632570000174",
    "socio_cnpj_basico": "21632570",
    "socio_razao_social": "PEREIRA E SAMPAIO PARTICIPACOES LTDA",
    "socio_cpf_visible": null,
    "qualificacao_codigo": "08",
    "qualificacao_nome": "Conselheiro de Administração",
    "data_entrada_sociedade": "2015-10-15",
    "representante_legal_documento": "***000000**",
    "representante_legal_nome": null,
    "representante_legal_qualificacao_codigo": "00",
    "representante_legal_qualificacao_nome": "Não informada",
    "pais_codigo": null,
    "pais_nome": null,
    "faixa_etaria": "0",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:43.369965+00:00"
  },
  {
    "empresa_cnpj_basico": "01988795",
    "empresa_razao_social": "PREUSSAG TRADE SUDAMERICA SA",
    "empresa_natureza_juridica": "2054",
    "socio_tipo": "PJ",
    "socio_nome": "PDB DO BRASIL LTDA",
    "socio_nome_norm": "pdb do brasil ltda",
    "socio_documento": "42587642000189",
    "socio_cnpj_basico": "42587642",
    "socio_razao_social": "PDB DO BRASIL LTDA",
    "socio_cpf_visible": null,
    "qualificacao_codigo": "10",
    "qualificacao_nome": "Diretor",
    "data_entrada_sociedade": "1997-07-23",
    "representante_legal_documento": "***000000**",
    "representante_legal_nome": null,
    "representante_legal_qualificacao_codigo": "00",
    "representante_legal_qualificacao_nome": "Não informada",
    "pais_codigo": null,
    "pais_nome": null,
    "faixa_etaria": "0",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:43.369965+00:00"
  },
  {
    "empresa_cnpj_basico": "01978759",
    "empresa_razao_social": "SALZGITTER TRADE SUDAMERICA S/A",
    "empresa_natureza_juridica": "2054",
    "socio_tipo": "PJ",
    "socio_nome": "PDB DO BRASIL LTDA",
    "socio_nome_norm": "pdb do brasil ltda",
    "socio_documento": "42587642000189",
    "socio_cnpj_basico": "42587642",
    "socio_razao_social": "PDB DO BRASIL LTDA",
    "socio_cpf_visible": null,
    "qualificacao_codigo": "10",
    "qualificacao_nome": "Diretor",
    "data_entrada_sociedade": "1997-07-09",
    "representante_legal_documento": "***000000**",
    "representante_legal_nome": null,
    "representante_legal_qualificacao_codigo": "00",
    "representante_legal_qualificacao_nome": "Não informada",
    "pais_codigo": null,
    "pais_nome": null,
    "faixa_etaria": "0",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:43.369965+00:00"
  },
  {
    "empresa_cnpj_basico": "30866068",
    "empresa_razao_social": "CONSORCIO ALSOLAR",
    "empresa_natureza_juridica": "2151",
    "socio_tipo": "PJ",
    "socio_nome": "PEIXARIA REAL LTDA",
    "socio_nome_norm": "peixaria real ltda",
    "socio_documento": "39915968000183",
    "socio_cnpj_basico": "39915968",
    "socio_razao_social": "PEIXARIA REAL LTDA",
    "socio_cpf_visible": null,
    "qualificacao_codigo": "20",
    "qualificacao_nome": "Sociedade Consorciada",
    "data_entrada_sociedade": "2022-11-18",
    "representante_legal_documento": "***000000**",
    "representante_legal_nome": null,
    "representante_legal_qualificacao_codigo": "00",
    "representante_legal_qualificacao_nome": "Não informada",
    "pais_codigo": null,
    "pais_nome": null,
    "faixa_etaria": "0",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:43.369965+00:00"
  },
  {
    "empresa_cnpj_basico": "04285783",
    "empresa_razao_social": "CONSORCIO RODOVIAS DO OESTE",
    "empresa_natureza_juridica": "2151",
    "socio_tipo": "PJ",
    "socio_nome": "PAVISERVICE SERVICOS DE PAVIMENTACAO LTDA",
    "socio_nome_norm": "paviservice servicos de pavimentacao ltda",
    "socio_documento": "01397753000145",
    "socio_cnpj_basico": "01397753",
    "socio_razao_social": "PAVISERVICE SERVICOS DE PAVIMENTACAO LTDA",
    "socio_cpf_visible": null,
    "qualificacao_codigo": "20",
    "qualificacao_nome": "Sociedade Consorciada",
    "data_entrada_sociedade": "2001-02-12",
    "representante_legal_documento": "***000000**",
    "representante_legal_nome": null,
    "representante_legal_qualificacao_codigo": "00",
    "representante_legal_qualificacao_nome": "Não informada",
    "pais_codigo": null,
    "pais_nome": null,
    "faixa_etaria": "0",
    "_periodo": "202604",
    "_data_carga": "2026-04-29T17:40:43.369965+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`silver_cnpj.socios\` LIMIT 5'`

## Quirks e armadilhas

- _TODO_

## Tabelas relacionadas

- _TODO_

## Templates SQL

### Caso A: _TODO_
```sql
SELECT ...
FROM `data-hacker-488115.silver_cnpj.socios`
WHERE ...
```

## Histórico

- 2026-04-29: última modificação BQ
- 2026-05-03: doc criado
