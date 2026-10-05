# `gold_pat.empresas` — Beneficiárias PAT agregadas por grupo (CNPJ_BASICO)

**Tipo:** TABLE
**Camada:** gold
**Granularidade:** 1 linha por **CNPJ_BASICO** com pelo menos 1 unidade PAT ATIVA. Inclui ARRAY top 50 unidades aninhadas.
**Linhas (~):** 288,376
**Chave:** `cnpj_basico` (8d)
**Cluster BY:** `cnpj_basico`, `porte`, `uf_matriz`
**Refresh:** sob demanda (snapshot PAT é semestral/anual). Build: `python -m scripts.pat.gold_empresas --build`. Doc: [`docs/pat/gold-pipeline.md`](../../../../docs/pat/gold-pipeline.md).
**Origem:** `silver_pat.empresas_beneficiarias_grupo` (filtros zumbis/divergentes aplicados) + endereço RFB-first + `folha_mensal_estimada_brl` (heurística 3SM/8SM × trabalhadores, SM=R$1.518). Município/UF sempre **UPPERCASE** RFB.

**Descrição BQ:** Camada limpa PAT pra consumo direto. Use por padrão pra análise comercial PAT — silver só pra investigação/auditoria.

---

## Quando usar

⭐ **Default pra perguntas PAT**: "Quantas empresas têm PAT em X cidade", "Top empregadores com PAT", "Folha estimada agregada", "Cobertura PAT por UF/setor".

⭐ **Pra cruzar com `gold_cnpj.empresas`**: JOIN simples por `cnpj_basico` traz `total_trabalhadores`, `folha_mensal_estimada_brl`, `qtd_unidades_pat_ativas`.

**NÃO use** quando precisar de:
- Detalhe por unidade (filial individual) → `gold_pat.empresas_unidades`
- Auditoria de divergências PAT × RFB → `silver_pat.empresas_beneficiarias` (com flag `pat_rfb_divergente`)
- Histórico bruto → `bronze_pat.empresas_beneficiarias`
- Operadoras de cartão / fornecedoras de refeição → `gold_pat.servicos_alimentacao`

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj_basico` | STRING |  | CNPJ raiz (8 dígitos) — chave do grupo econômico. |
| `razao_social` | STRING |  | Razão social RFB (UPPERCASE sem acento). Fallback: PAT normalizado se grupo não está na RFB. |
| `nome_fantasia` | STRING |  |  |
| `cod_natureza_juridica` | STRING |  |  |
| `natureza_juridica` | STRING |  |  |
| `cod_porte` | STRING |  |  |
| `porte` | STRING |  | Porte RFB (MICRO EMPRESA / EPP / DEMAIS). Maioria do PAT em DEMAIS por viés de adesão. |
| `capital_social` | NUMERIC |  | Capital social registrado na RFB (NUMERIC, em BRL). |
| `cnae_principal_codigo` | STRING |  |  |
| `cnae_principal_descricao` | STRING |  |  |
| `data_abertura` | DATE |  |  |
| `idade_anos` | INTEGER |  |  |
| `optante_simples` | BOOLEAN |  |  |
| `optante_mei` | BOOLEAN |  |  |
| `uf_matriz` | STRING |  |  |
| `municipio_matriz` | STRING |  |  |
| `qtd_unidades_pat_ativas` | INTEGER |  | Filiais cadastradas no PAT com situacao=Ativo E não-divergentes (RFB também ativa). |
| `qtd_unidades_pat_matriz` | INTEGER |  |  |
| `qtd_unidades_pat_filial` | INTEGER |  |  |
| `total_trabalhadores` | INTEGER |  | Soma de trabalhadores das unidades ATIVAS PAT do grupo. Não inclui zumbis (silver tem isso em total_trabalhadores_grupo). |
| `trabalhadores_ate_5sm` | INTEGER |  | Trabalhadores ganhando até 5 salários mínimos (faixa baixa). |
| `trabalhadores_acima_5sm` | INTEGER |  | Trabalhadores ganhando acima de 5 SM. |
| `pct_baixa_renda` | FLOAT |  | Percentual de trabalhadores na faixa ≤5SM. Alto = operação fabril/varejo; baixo = escritório/HQ. |
| `folha_mensal_estimada_brl` | NUMERIC |  | ESTIMATIVA GROSSEIRA pra ranking, NÃO valor absoluto. Heurística: ≤5SM × 3 SM médio + >5SM × 8 SM médio (SM 2025 = R$ 1518). Pra precisão, cruzar com BDC employees_count ou RAIS/CAGED. |
| `ufs_atuacao` | STRING | REPEATED | ARRAY de UFs distintas onde o grupo tem unidade ativa no PAT (endereço RFB). |
| `qtd_ufs_atuacao` | INTEGER |  |  |
| `qtd_municipios_atuacao` | INTEGER |  | Municípios distintos onde o grupo tem unidade ativa (endereço RFB, não cadastro PAT centralizado). |
| `qtd_filiais_rfb_ativas` | INTEGER |  | Filiais ativas no CNPJ-RFB (universo total). Compare com qtd_unidades_pat_ativas pra ver cobertura PAT. |
| `qtd_filiais_rfb_total` | INTEGER |  |  |
| `cobertura_pat_pct` | FLOAT |  | qtd_unidades_pat_ativas ÷ qtd_filiais_rfb_ativas × 100. Bradesco: 9999 RFB / 3521 PAT = 35%. |
| `unidades` | RECORD | REPEATED | ARRAY<STRUCT> top 50 unidades ATIVAS por nº de trabalhadores. Pra grupos com >50 filiais (Correios, BB, Bradesco), use gold_pat.empresas_unidades (flat) pra ver tudo. |
| `unidades.cnpj` | STRING |  |  |
| `unidades.matriz_ou_filial` | STRING |  |  |
| `unidades.uf` | STRING |  |  |
| `unidades.municipio` | STRING |  |  |
| `unidades.bairro` | STRING |  |  |
| `unidades.cep` | STRING |  |  |
| `unidades.endereco_completo` | STRING |  |  |
| `unidades.cnae_principal_descricao` | STRING |  |  |
| `unidades.trabalhadores` | INTEGER |  |  |
| `unidades.trabalhadores_ate_5sm` | INTEGER |  |  |
| `unidades.trabalhadores_acima_5sm` | INTEGER |  |  |
| `unidades.folha_mensal_estimada_brl` | NUMERIC |  |  |
| `unidades.data_inicio_atividade` | DATE |  |  |
| `_periodo` | STRING |  |  |
| `_data_carga` | TIMESTAMP |  |  |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj_basico": "07002627",
    "razao_social": "UNIDOS AGRO INDUSTRIAL LTDA",
    "nome_fantasia": null,
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": "2046000",
    "cnae_principal_codigo": "4623102",
    "cnae_principal_descricao": "Comércio atacadista de couros, lãs, peles e outros subprodutos não-comestíveis de origem animal",
    "data_abertura": "2004-09-10",
    "idade_anos": 22,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz": "SP",
    "municipio_matriz": "JALES",
    "qtd_unidades_pat_ativas": 1,
    "qtd_unidades_pat_matriz": 1,
    "qtd_unidades_pat_filial": 0,
    "total_trabalhadores": 0,
    "trabalhadores_ate_5sm": 0,
    "trabalhadores_acima_5sm": 0,
    "pct_baixa_renda": null,
    "folha_mensal_estimada_brl": "0",
    "ufs_atuacao": [
      "SP"
    ],
    "qtd_ufs_atuacao": 1,
    "qtd_municipios_atuacao": 1,
    "qtd_filiais_rfb_ativas": 1,
    "qtd_filiais_rfb_total": 5,
    "cobertura_pat_pct": 100.0,
    "unidades": [
      {
        "cnpj": "07002627000120",
        "matriz_ou_filial": "Matriz",
        "uf": "SP",
        "municipio": "JALES",
        "bairro": "PARQUE INDUSTRIAL III",
        "cep": "15700598",
        "endereco_completo": "RUA AFFONSO MEROTTI, 464, PARQUE INDUSTRIAL III",
        "cnae_principal_descricao": "Comércio atacadista de couros, lãs, peles e outros subprodutos não-comestíveis de origem animal",
        "trabalhadores": 0,
        "trabalhadores_ate_5sm": 0,
        "trabalhadores_acima_5sm": 0,
        "folha_mensal_estimada_brl": "0",
        "data_inicio_atividade": "2004-09-10"
      }
    ],
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:54.123650+00:00"
  },
  {
    "cnpj_basico": "61416624",
    "razao_social": "MACAUBA MAQUINAS AGRICOLAS LTDA",
    "nome_fantasia": "MACAUBA MAQUINAS AGRICOLAS",
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": "1240932",
    "cnae_principal_codigo": "4661300",
    "cnae_principal_descricao": "Comércio atacadista de máquinas, aparelhos e equipamentos para uso agropecuário; partes e peças",
    "data_abertura": "1989-09-01",
    "idade_anos": 37,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz": "SP",
    "municipio_matriz": "ARTUR NOGUEIRA",
    "qtd_unidades_pat_ativas": 1,
    "qtd_unidades_pat_matriz": 1,
    "qtd_unidades_pat_filial": 0,
    "total_trabalhadores": 0,
    "trabalhadores_ate_5sm": 0,
    "trabalhadores_acima_5sm": 0,
    "pct_baixa_renda": null,
    "folha_mensal_estimada_brl": "0",
    "ufs_atuacao": [
      "SP"
    ],
    "qtd_ufs_atuacao": 1,
    "qtd_municipios_atuacao": 1,
    "qtd_filiais_rfb_ativas": 1,
    "qtd_filiais_rfb_total": 2,
    "cobertura_pat_pct": 100.0,
    "unidades": [
      {
        "cnpj": "61416624000189",
        "matriz_ou_filial": "Matriz",
        "uf": "SP",
        "municipio": "ARTUR NOGUEIRA",
        "bairro": "JD WADA",
        "cep": "13167150",
        "endereco_completo": "RUA MARIA MARSON SIA, 475, JD WADA",
        "cnae_principal_descricao": "Comércio atacadista de máquinas, aparelhos e equipamentos para uso agropecuário; partes e peças",
        "trabalhadores": 0,
        "trabalhadores_ate_5sm": 0,
        "trabalhadores_acima_5sm": 0,
        "folha_mensal_estimada_brl": "0",
        "data_inicio_atividade": "1989-09-01"
      }
    ],
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:54.123650+00:00"
  },
  {
    "cnpj_basico": "03523839",
    "razao_social": "MOVEIS BENETTI LTDA",
    "nome_fantasia": null,
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "cod_porte": "03",
    "porte": "EMPRESA DE PEQUENO PORTE",
    "capital_social": "237286",
    "cnae_principal_codigo": "4754701",
    "cnae_principal_descricao": "Comércio varejista de móveis",
    "data_abertura": "1999-11-05",
    "idade_anos": 27,
    "optante_simples": false,
    "optante_mei": false,
    "uf_matriz": "PE",
    "municipio_matriz": "RECIFE",
    "qtd_unidades_pat_ativas": 1,
    "qtd_unidades_pat_matriz": 1,
    "qtd_unidades_pat_filial": 0,
    "total_trabalhadores": 0,
    "trabalhadores_ate_5sm": 0,
    "trabalhadores_acima_5sm": 0,
    "pct_baixa_renda": null,
    "folha_mensal_estimada_brl": "0",
    "ufs_atuacao": [
      "PE"
    ],
    "qtd_ufs_atuacao": 1,
    "qtd_municipios_atuacao": 1,
    "qtd_filiais_rfb_ativas": 1,
    "qtd_filiais_rfb_total": 2,
    "cobertura_pat_pct": 100.0,
    "unidades": [
      {
        "cnpj": "03523839000100",
        "matriz_ou_filial": "Matriz",
        "uf": "PE",
        "municipio": "RECIFE",
        "bairro": "BOA VIAGEM",
        "cep": "51011050",
        "endereco_completo": "AVENIDA ENGENHEIRO DOMINGOS FERREIRA, 1450, BOA VIAGEM",
        "cnae_principal_descricao": "Comércio varejista de móveis",
        "trabalhadores": 0,
        "trabalhadores_ate_5sm": 0,
        "trabalhadores_acima_5sm": 0,
        "folha_mensal_estimada_brl": "0",
        "data_inicio_atividade": "1999-11-05"
      }
    ],
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:54.123650+00:00"
  },
  {
    "cnpj_basico": "66822537",
    "razao_social": "WAL VIAGENS E TURISMO S.A",
    "nome_fantasia": "ALATUR VIAGENS E TURISMO",
    "cod_natureza_juridica": "2054",
    "natureza_juridica": "Sociedade Anônima Fechada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": "2750000",
    "cnae_principal_codigo": "7911200",
    "cnae_principal_descricao": "Agências de viagens",
    "data_abertura": "1991-09-03",
    "idade_anos": 35,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz": "SP",
    "municipio_matriz": "SAO PAULO",
    "qtd_unidades_pat_ativas": 1,
    "qtd_unidades_pat_matriz": 1,
    "qtd_unidades_pat_filial": 0,
    "total_trabalhadores": 0,
    "trabalhadores_ate_5sm": 0,
    "trabalhadores_acima_5sm": 0,
    "pct_baixa_renda": null,
    "folha_mensal_estimada_brl": "0",
    "ufs_atuacao": [
      "SP"
    ],
    "qtd_ufs_atuacao": 1,
    "qtd_municipios_atuacao": 1,
    "qtd_filiais_rfb_ativas": 3,
    "qtd_filiais_rfb_total": 15,
    "cobertura_pat_pct": 33.33,
    "unidades": [
      {
        "cnpj": "66822537000145",
        "matriz_ou_filial": "Matriz",
        "uf": "SP",
        "municipio": "SAO PAULO",
        "bairro": "REPUBLICA",
        "cep": "01047020",
        "endereco_completo": "RUA DR BRAULIO GOMES, 141 - ANDAR 10, REPUBLICA",
        "cnae_principal_descricao": "Agências de viagens",
        "trabalhadores": 0,
        "trabalhadores_ate_5sm": 0,
        "trabalhadores_acima_5sm": 0,
        "folha_mensal_estimada_brl": "0",
        "data_inicio_atividade": "1991-09-03"
      }
    ],
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:54.123650+00:00"
  },
  {
    "cnpj_basico": "04426565",
    "razao_social": "T-SYSTEMS DO BRASIL LTDA.",
    "nome_fantasia": null,
    "cod_natureza_juridica": "2062",
    "natureza_juridica": "Sociedade Empresária Limitada",
    "cod_porte": "05",
    "porte": "DEMAIS",
    "capital_social": "30000000",
    "cnae_principal_codigo": "6201501",
    "cnae_principal_descricao": "Desenvolvimento de programas de computador sob encomenda",
    "data_abertura": "1975-12-03",
    "idade_anos": 51,
    "optante_simples": null,
    "optante_mei": null,
    "uf_matriz": "SP",
    "municipio_matriz": "SAO PAULO",
    "qtd_unidades_pat_ativas": 1,
    "qtd_unidades_pat_matriz": 1,
    "qtd_unidades_pat_filial": 0,
    "total_trabalhadores": 1354,
    "trabalhadores_ate_5sm": 656,
    "trabalhadores_acima_5sm": 698,
    "pct_baixa_renda": 48.45,
    "folha_mensal_estimada_brl": "11463936",
    "ufs_atuacao": [
      "SP"
    ],
    "qtd_ufs_atuacao": 1,
    "qtd_municipios_atuacao": 1,
    "qtd_filiais_rfb_ativas": 7,
    "qtd_filiais_rfb_total": 18,
    "cobertura_pat_pct": 14.29,
    "unidades": [
      {
        "cnpj": "04426565000196",
        "matriz_ou_filial": "Matriz",
        "uf": "SP",
        "municipio": "SAO PAULO",
        "bairro": "VILA OLIMPIA",
        "cep": "04551000",
        "endereco_completo": "RUA OLIMPIADAS, 205 - ANDAR 3, VILA OLIMPIA",
        "cnae_principal_descricao": "Desenvolvimento de programas de computador sob encomenda",
        "trabalhadores": 1354,
        "trabalhadores_ate_5sm": 656,
        "trabalhadores_acima_5sm": 698,
        "folha_mensal_estimada_brl": "11463936",
        "data_inicio_atividade": "1975-12-03"
      }
    ],
    "_periodo": "2025-12-31",
    "_data_carga": "2026-05-02T21:37:54.123650+00:00"
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_pat.empresas\` LIMIT 5'`

## Quirks e armadilhas

- **`total_trabalhadores` vs `total_trabalhadores_ativos`**: gold_pat usa `total_trabalhadores` que **já é só ATIVOS** (filtro upstream). Coluna sem sufixo, soma de unidades ATIVAS.
- **Município é UPPERCASE sem acento** (RFB-first): `municipio_matriz = 'BELO HORIZONTE'`.
- **`folha_mensal_estimada_brl` é heurística**: 3SM (≤5 SM) + 8SM (>5SM) × trabalhadores, SM=R$1.518 (2025). NÃO é folha real — pra análise de mercado/ranking.
- **`pat_rfb_divergente=TRUE` já foi filtrado** (zumbis OUT). 13,8% das beneficiárias raw eram divergentes.
- **Granularidade é GRUPO** (CNPJ_BASICO). Pra ver unidade individual (CNPJ 14d) → use `gold_pat.empresas_unidades` ou abrir o ARRAY `unidades` desta tabela (top 50).
- **Sem MEI**: PAT só vale pra empregadores formais com CLT.

## Tabelas relacionadas

- [`gold_pat.empresas_unidades`](gold_pat.empresas_unidades.md) — 407k unidades flat (1/CNPJ 14d) — pra mapas e drill-down
- [`gold_pat.servicos_alimentacao`](gold_pat.servicos_alimentacao.md) — facilitadoras (cartões) + fornecedoras (cozinha)
- [`silver_pat.empresas_beneficiarias_grupo`](silver_pat.empresas_beneficiarias_grupo.md) — versão silver (com zumbis/divergentes)
- [`gold_cnpj.empresas`](gold_cnpj.empresas.md) — JOIN por `cnpj_basico` pra ICP composto

## Templates SQL

### Caso A: cidades MG com X+ empresas com PAT > 50 funcionários
```sql
SELECT
  municipio_matriz AS cidade,
  COUNT(DISTINCT cnpj_basico) AS empresas,
  SUM(total_trabalhadores) AS trabalhadores
FROM `data-hacker-488115.gold_pat.empresas`
WHERE uf_matriz = 'MG' AND total_trabalhadores > 50
GROUP BY cidade
ORDER BY empresas DESC
LIMIT 30;
```

### Caso B: top 20 empregadores nacionais (PAT)
```sql
SELECT cnpj_basico, razao_social, total_trabalhadores,
       qtd_municipios_atuacao, folha_mensal_estimada_brl
FROM `data-hacker-488115.gold_pat.empresas`
ORDER BY total_trabalhadores DESC
LIMIT 20;
```

### Caso C: cruzar PAT × CNPJ comercial (ICP)
```sql
SELECT
  e.cnpj_basico, e.nome, e.industria.setor, e.status.porte,
  pat.total_trabalhadores, pat.folha_mensal_estimada_brl
FROM `data-hacker-488115.gold_cnpj.empresas` e
JOIN `data-hacker-488115.gold_pat.empresas` pat USING (cnpj_basico)
WHERE e.industria.setor = 'Comércio'
  AND e.status.porte = 'grande'
  AND pat.total_trabalhadores >= 100
ORDER BY pat.total_trabalhadores DESC;
```

### Caso D: distribuição PAT por UF
```sql
SELECT uf_matriz,
       COUNT(*) AS empresas_pat,
       SUM(total_trabalhadores) AS trabalhadores_total,
       AVG(folha_mensal_estimada_brl) AS folha_media
FROM `data-hacker-488115.gold_pat.empresas`
GROUP BY uf_matriz
ORDER BY trabalhadores_total DESC;
```

## Histórico

- 2026-05-02: última modificação BQ
- 2026-05-03: doc criado
