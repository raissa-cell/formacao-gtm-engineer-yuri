# `gold_energia.estabelecimentos_consumo_certo` — Consumo elétrico BDGD ↔ CNPJ (match certeza)

**Tipo:** TABLE
**Camada:** gold
**Granularidade:** 1 linha por **UC (Unidade Consumidora)** ANEEL/BDGD com match certeza ao CNPJ. **N:1 com `cnpj_basico`** — 1 empresa pode ter várias UCs (matriz + filiais + endereços terceiros).
**Linhas (~):** 1,259,040
**Chave:** `cod_id_encr` (UC criptografado ANEEL); `cnpj` 14d agrupa UCs do mesmo estabelecimento; `cnpj_basico` 8d agrupa o grupo
**Cluster BY:** `cnae`, `classe_consumo`, `tensao`
**Refresh:** sob demanda (BDGD anual ANEEL). Build: `python -m scripts.aneel.silver_consumo_certo --build`. Doc: [`docs/aneel/16-consumo-certo.md`](../../../../docs/aneel/16-consumo-certo.md).
**Origem:** Match deterministico BDGD (BT/MT/AT) ↔ bronze_cnpj.estabelecimentos via 3 tiers de confiança: A (cep_cnae_unico, conf 1.0), B (numero desambigua, conf 0.9), S (sócios em comum, conf 0.85/0.70).

**Descrição BQ:** Match deterministico BDGD <-> CNPJ em 3 tiers: A=cep_cnae_unico (1 PJ no CEP+CNAE, conf 1.0), B=cep_cnae_numero_unico (n=2 desambiguado por numero, conf 0.9), S=cep_cnae_socios_unico (n=2 com socios em comum, conf 0.85 strict / 0.70 loose). Filtra Adm Publica (NJ 1xxx) e classes BDGD PP/IP/CPR. Para esses CNPJs o consumo medido pela distribuidora e atribuivel com confianca alta. Doc: docs/aneel/16-consumo-certo.md. Build: scripts.aneel.silver_consumo_certo --build.

---

## Quando usar

⭐ **Pra perguntas sobre consumo elétrico de empresa**: kWh medio mensal, distribuidora atendente, classe consumo, ACL/GD elegibilidade, top consumidores por UF/CNAE/setor.

⭐ **Pra cruzar com `gold_cnpj.empresas`**: agregar por `cnpj_basico` (SUM kwh, COUNT UCs) e fazer JOIN. Exemplo: "empresas em Maricá/RJ ordenadas por consumo".

**ATENÇÃO** — granularidade é UC (1 empresa pode ter N UCs):
- Pra consumo TOTAL do grupo: `SUM(kwh_medio_mensal)` agrupado por `cnpj_basico`
- Pra consumo POR ESTABELECIMENTO (matriz + filial individual): `SUM(...)` agrupado por `cnpj` (14d)
- Pra UCs individuais (drill-down): direto sem agg

**NÃO use** quando precisar de:
- TODAS empresas com consumo (mesmo Tier C, sem certeza) → ainda não existe; este gold cobre só matches **certeza**
- Histórico mês-a-mês detalhado → use `ene_12_meses_kwh` (array com 12 valores) — granularidade UC apenas
- Consumo de pequenas UCs sem CNPJ associado → fora do escopo; este gold só tem UCs com match deterministico

## Schema

| Coluna | Tipo BQ | Modo | Descrição |
|---|---|---|---|
| `cnpj` | STRING |  | CNPJ completo (14 digitos) do estabelecimento atribuido. Em Tiers B/S e o vencedor da desambiguacao (Tier B = numero igual UC; Tier S = lex menor cnpj_basico). |
| `cnpj_basico` | STRING |  | Raiz do CNPJ (8 primeiros digitos). Identifica grupo economico. Use para JOIN com bronze_cnpj.empresas / silver_cnpj.dim_empresa. |
| `nome_fantasia` | STRING |  | Nome fantasia declarado na RFB. Frequentemente vazio (~50% dos estabelecimentos) — preferir RAZAO_SOCIAL via JOIN com bronze_cnpj.empresas. |
| `cnaes_secundarios` | STRING |  | Lista de CNAEs secundarios separados por virgula. Indica atividades adicionais alem do CNAE principal. |
| `tipo_logradouro_rfb` | STRING |  | Tipo do logradouro RFB (AVENIDA, RUA, RODOVIA, etc.). Armazenado SEPARADO de logradouro_raw_rfb na fonte RFB. |
| `logradouro_raw_rfb` | STRING |  | Logradouro RFB SEM tipo concatenado (apenas o nome). Para texto completo: CONCAT(tipo_logradouro_rfb, ' ', logradouro_raw_rfb). |
| `numero_rfb` | STRING |  | Numero do estabelecimento na RFB. Texto livre — pode conter sufixos ('100A'), separadores ('2.942') ou marcadores ('SN', 'S/N'). |
| `bairro_rfb` | STRING |  | Bairro cadastrado na RFB. Pode divergir do bairro BDGD em ~30% dos casos. |
| `municipio_rfb` | STRING |  | Codigo IBGE 4-dig do municipio (RFB). |
| `uf_rfb` | STRING |  | UF cadastrada na RFB (sigla 2 letras). |
| `cod_id_encr` | STRING |  | Hash SHA-256 da Unidade Consumidora (chave anonimizada ANEEL). Identifica UC fisica unica no BDGD. Nao joinavel com .gdb legado. |
| `tensao` | STRING |  | Tensao de fornecimento: BT (baixa <2.3kV) \| MT (media) \| AT (alta >=69kV). Apenas MT/AT sao elegiveis a ACL direto pre-Lei 14.300/22. |
| `cnae` | STRING |  | CNAE da UC declarado pela distribuidora (7 digitos). Foi a chave de match. |
| `cnae_grupo` | STRING |  | CNAE de grupo (5 primeiros digitos do cnae). Categoria de atividade mais ampla. |
| `classe_consumo` | STRING |  | Classe de consumo BDGD: CO* (comercial), IN (industrial), RU* (rural), SP* (servico publico). PP/IP/CPR sao FILTRADOS desta tabela. |
| `grupo_tensao` | STRING |  | Subgrupo de tensao detalhado: A1, A2, A3, A3a, A4, AS, B1, B2, B3, B4. |
| `grupo_tarifario` | STRING |  | Modalidade tarifaria: Convencional, Verde (THS-V), Azul (THS-A), Branca. |
| `distribuidora_sigla` | STRING |  | Sigla da distribuidora responsavel pela UC (ex: ENEL-SP, CEMIG-D). |
| `distribuidora_cnpj` | STRING |  | CNPJ da distribuidora (resolvido via dim_distribuidoras_bdgd). |
| `distribuidora_nome` | STRING |  | Nome completo da distribuidora. |
| `ponto_conexao` | STRING |  | Ponto de conexao na rede (PN_CON do BDGD). Identifica rede/transformador. |
| `cep` | STRING |  | CEP normalizado 8 digitos. Foi a chave de match com a RFB. |
| `cep_formatado` | STRING |  | CEP no formato XXXXX-XXX (apresentacao). |
| `logradouro` | STRING |  | Logradouro normalizado do BDGD (lowercase, sem acentos, alfanum). Inclui o tipo (ex: 'av paulista'), diferente do RFB que separa em 2 campos. |
| `numero_bdgd` | STRING |  | Numero do imovel conforme BDGD (extraido de LGRD via parse_lgrd.py). |
| `bairro_bdgd` | STRING |  | Bairro conforme BDGD. Pode divergir de bairro_rfb. |
| `municipio_ibge` | STRING |  | Codigo IBGE 7-dig do municipio (BDGD/MUN). |
| `uf` | STRING |  | UF derivada dos 2 primeiros digitos do municipio_ibge. |
| `lat` | FLOAT |  | Latitude SIRGAS2000 da UC (declarada pela distribuidora). Usavel para validacao geo. |
| `lon` | FLOAT |  | Longitude SIRGAS2000 da UC. |
| `kwh_medio_mensal` | FLOAT |  | Consumo medio mensal medido pela distribuidora. Valor REAL (nao estimado) atribuivel ao CNPJ via match deterministico do tier informado em metodo_match. |
| `kwh_total_12m` | FLOAT |  | Soma do consumo dos 12 meses mais recentes da safra BDGD. Real. |
| `ene_12_meses_kwh` | FLOAT | REPEATED | ARRAY com 12 valores de consumo mensal (ENE_01..12). Para AT: soma de ENE_P (ponta) + ENE_F (fora-ponta). |
| `porte_consumo` | STRING |  | Bucket por kWh/mes: baixo (<500), medio (<2k), alto (<10k), muito_alto (>=10k). Diferente do PORTE da RFB (que e cadastral, nao consumo real). |
| `carga_instalada_kw` | FLOAT |  | Carga instalada declarada (CAR_INST do BDGD). ATENCAO: alguns valores sao absurdos (>1 GW) — bug de unidade upstream do BDGD. |
| `dem_contratada_kw` | FLOAT |  | Demanda contratada em kW (apenas MT/AT). NULL para BT (Grupo B nao contrata demanda). |
| `uc_tem_ceg_gd` | BOOLEAN |  | TRUE se a UC fisica tem GD vinculada via CEG_GD do BDGD. |
| `ceg_gd` | STRING |  | Codigo CEG da usina de GD vinculada a esta UC (NULL se nao tem). |
| `cnpj_tem_gd` | BOOLEAN |  | TRUE se o CNPJ atribuido tem alguma UC com GD em qualquer lugar (via JOIN com bronze_aneel.geracao_distribuida). |
| `gd_potencia_kw` | FLOAT |  | Potencia maxima de GD do CNPJ (soma de todas as usinas vinculadas). |
| `elegivel_acl` | BOOLEAN |  | TRUE se tensao IN ('MT','AT'). Pos Lei 14.300/22 qualquer Grupo A pode migrar. Use junto com NOT no_acl_livre AND NOT no_acl_especial para identificar leads. |
| `no_acl_livre` | BOOLEAN |  | TRUE se o CNPJ exato esta como Consumidor Livre ATIVO na CCEE. Usa fonte bronze_ccee.lista_perfil_v1. |
| `no_acl_especial` | BOOLEAN |  | TRUE se o CNPJ exato esta como Consumidor Especial ATIVO na CCEE. |
| `grupo_no_acl_livre` | BOOLEAN |  | TRUE se algum CNPJ raiz (8 digitos) do grupo economico esta como Livre. Mais permissivo que no_acl_livre — pega quando matriz migrou e filiais ainda nao. |
| `grupo_no_acl_especial` | BOOLEAN |  | Idem grupo_no_acl_livre, mas para Consumidor Especial. |
| `cnpj_eh_consumidor_acl` | BOOLEAN |  | CNPJ aparece em lista_agente_associado como classe Consumidor Livre/Especial. Sinal mais conservador que no_acl_*. |
| `cnpj_eh_comercializador` | BOOLEAN |  | CNPJ e Comercializador na CCEE — exclui da prospeccao (seria competidor, nao cliente). |
| `cnpj_eh_gerador` | BOOLEAN |  | CNPJ e Gerador / Produtor Independente / Autoprodutor na CCEE. |
| `cnpj_eh_distribuidor` | BOOLEAN |  | CNPJ e Distribuidor — exclui da prospeccao. |
| `cnpj_eh_varejista` | BOOLEAN |  | CNPJ e Varejista (Lei 14.300/22) — pode ser canal ou competidor. |
| `metodo_match` | STRING |  | Tier do match: cep_cnae_unico (A, conf 1.00) \| cep_cnae_numero_unico (B, conf 0.90) \| cep_cnae_socios_unico (S, conf 0.85 strict / 0.70 loose). Filtre por este campo para escolher nivel de confianca. |
| `n_pjs_no_grupo` | INTEGER |  | Quantos PJs ATIVOS existiam no (CEP, CNAE) antes da desambiguacao. 1=Tier A (unico). 2=Tier B/S (havia ambiguidade resolvida). |
| `cnpj_alternativo` | STRING |  | Para Tier B/S: CNPJ do outro PJ do grupo (transparencia). NULL para Tier A. No Tier B = perdedor (numero diferente da UC). No Tier S = outro CNPJ do mesmo grupo economico. |
| `socios_modalidade` | STRING |  | Apenas Tier S. strict=socios EXATAMENTE iguais nos 2 CNPJs (alta confianca). loose=interseccao parcial >= 1 socio em comum. NULL para Tier A/B. |
| `confianca_score` | FLOAT |  | Score numerico de confianca [0.7-1.0]. 1.00=Tier A (determinismo absoluto). 0.90=Tier B (desambiguacao por numero). 0.85=Tier S strict (mesmos socios). 0.70=Tier S loose (interseccao parcial socios). |
| `n_ucs_para_este_cnpj` | INTEGER |  | Quantas UCs do BDGD foram atribuidas a este mesmo CNPJ. Util para reagregar consumo total do CNPJ (matriz com varias UCs no mesmo terreno). |
| `_data_carga` | TIMESTAMP |  | Timestamp UTC do build desta linha. Util para auditoria de safra. |
| `uf_part` | INTEGER |  | Coluna tecnica de particionamento (RANGE_BUCKET 0-28, 1 INT por UF). Filtro por UF deve usar 'uf' (STRING), nao esta coluna. |

## Sample (5 linhas reais)

```json
[
  {
    "cnpj": "59292969000126",
    "cnpj_basico": "59292969",
    "nome_fantasia": "AGROINDUSTRIAL GRAO SOLAR",
    "cnaes_secundarios": "0111302,0111399,0115600,0133499,0161003,4623199,5211799",
    "tipo_logradouro_rfb": "RODOVIA",
    "logradouro_raw_rfb": "BR 135",
    "numero_rfb": "SN",
    "bairro_rfb": "CENTRO",
    "municipio_rfb": "0901",
    "uf_rfb": "MA",
    "cod_id_encr": "6BC8BA27B2D9484E3AB919110FAB5D039B156682D248BA8F6DAB296A944565E2",
    "tensao": "BT",
    "cnae": "0111301",
    "cnae_grupo": "01113",
    "classe_consumo": "RU3",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B2RU",
    "distribuidora_sigla": "EQUATORIAL MA",
    "distribuidora_cnpj": "06272793000184",
    "distribuidora_nome": "EQUATORIAL MARANHAO DISTRIBUIDORA DE ENERGIA S.A",
    "ponto_conexao": "106785304",
    "cep": "65145000",
    "cep_formatado": "65145-000",
    "logradouro": "r nova jerusalem",
    "numero_bdgd": null,
    "bairro_bdgd": "CAJUEIRO",
    "municipio_ibge": "2110203",
    "uf": "MA",
    "lat": -3.22304743,
    "lon": -44.32019881,
    "kwh_medio_mensal": 121.59583333333332,
    "kwh_total_12m": 1459.1499999999999,
    "ene_12_meses_kwh": [
      70.14,
      143.51,
      126.98,
      116.68,
      120.61,
      127.25,
      124.87,
      117.41,
      118.24,
      126.76,
      133.13,
      133.57
    ],
    "porte_consumo": "baixo",
    "carga_instalada_kw": 1997.0,
    "dem_contratada_kw": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "metodo_match": "cep_cnae_unico",
    "n_pjs_no_grupo": 1,
    "cnpj_alternativo": null,
    "socios_modalidade": null,
    "confianca_score": 1.0,
    "n_ucs_para_este_cnpj": 1,
    "_data_carga": "2026-04-26T19:43:43.575858+00:00",
    "uf_part": 8
  },
  {
    "cnpj": "23461411000856",
    "cnpj_basico": "23461411",
    "nome_fantasia": null,
    "cnaes_secundarios": null,
    "tipo_logradouro_rfb": "FAZENDA",
    "logradouro_raw_rfb": "SAO JOAO",
    "numero_rfb": "S/N",
    "bairro_rfb": "ZONA RURAL",
    "municipio_rfb": "0741",
    "uf_rfb": "MA",
    "cod_id_encr": "5B37AA10BC403649EB0A8E7DF82775774584655D8B8361B1FC42776C1BF34005",
    "tensao": "BT",
    "cnae": "0111301",
    "cnae_grupo": "01113",
    "classe_consumo": "RU1",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B2RU",
    "distribuidora_sigla": "EQUATORIAL MA",
    "distribuidora_cnpj": "06272793000184",
    "distribuidora_nome": "EQUATORIAL MARANHAO DISTRIBUIDORA DE ENERGIA S.A",
    "ponto_conexao": "106656176",
    "cep": "65515000",
    "cep_formatado": "65515-000",
    "logradouro": "fa bacuri",
    "numero_bdgd": null,
    "bairro_bdgd": "RURAL",
    "municipio_ibge": "2102200",
    "uf": "MA",
    "lat": -3.93750043,
    "lon": -42.90427647,
    "kwh_medio_mensal": 278.7608333333333,
    "kwh_total_12m": 3345.13,
    "ene_12_meses_kwh": [
      366.19,
      382.54,
      337.93,
      360.16,
      396.72,
      381.5,
      332.58,
      310.13,
      277.8,
      111.96,
      46.87,
      40.75
    ],
    "porte_consumo": "baixo",
    "carga_instalada_kw": 5899.0,
    "dem_contratada_kw": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "metodo_match": "cep_cnae_unico",
    "n_pjs_no_grupo": 1,
    "cnpj_alternativo": null,
    "socios_modalidade": null,
    "confianca_score": 1.0,
    "n_ucs_para_este_cnpj": 2,
    "_data_carga": "2026-04-26T19:43:43.575858+00:00",
    "uf_part": 8
  },
  {
    "cnpj": "23461411000856",
    "cnpj_basico": "23461411",
    "nome_fantasia": null,
    "cnaes_secundarios": null,
    "tipo_logradouro_rfb": "FAZENDA",
    "logradouro_raw_rfb": "SAO JOAO",
    "numero_rfb": "S/N",
    "bairro_rfb": "ZONA RURAL",
    "municipio_rfb": "0741",
    "uf_rfb": "MA",
    "cod_id_encr": "76DDDEDF1EB926783220397B386E6B98D9FABA510488BE67E753306909A2969C",
    "tensao": "MT",
    "cnae": "0111301",
    "cnae_grupo": "01113",
    "classe_consumo": "RU3",
    "grupo_tensao": "MT",
    "grupo_tarifario": "B2RU",
    "distribuidora_sigla": "EQUATORIAL MA",
    "distribuidora_cnpj": "06272793000184",
    "distribuidora_nome": "EQUATORIAL MARANHAO DISTRIBUIDORA DE ENERGIA S.A",
    "ponto_conexao": "107301127",
    "cep": "65515000",
    "cep_formatado": "65515-000",
    "logradouro": "pv quebra coco",
    "numero_bdgd": null,
    "bairro_bdgd": "QUEBRA COCO",
    "municipio_ibge": "2102200",
    "uf": "MA",
    "lat": -3.9229902,
    "lon": -43.18298228,
    "kwh_medio_mensal": 5970.553333333333,
    "kwh_total_12m": 71646.64,
    "ene_12_meses_kwh": [
      2881.57,
      3845.76,
      3761.07,
      7037.47,
      16316.08,
      13930.07,
      6566.77,
      4150.63,
      3853.46,
      3340.52,
      3173.36,
      2789.88
    ],
    "porte_consumo": "alto",
    "carga_instalada_kw": 487056.0,
    "dem_contratada_kw": 2924.0,
    "uc_tem_ceg_gd": true,
    "ceg_gd": "GD.MA.001.907.238",
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "elegivel_acl": true,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "metodo_match": "cep_cnae_unico",
    "n_pjs_no_grupo": 1,
    "cnpj_alternativo": null,
    "socios_modalidade": null,
    "confianca_score": 1.0,
    "n_ucs_para_este_cnpj": 2,
    "_data_carga": "2026-04-26T19:43:43.575858+00:00",
    "uf_part": 8
  },
  {
    "cnpj": "29300412000129",
    "cnpj_basico": "29300412",
    "nome_fantasia": "CAPRPM",
    "cnaes_secundarios": "0111302,0119901,0119906,0119907,0119908,0151202,0153901,0153902,0154700,0155501,0155503,1061901,1063500,4120400",
    "tipo_logradouro_rfb": "FAZENDA",
    "logradouro_raw_rfb": "CARREIRA D`AGUA",
    "numero_rfb": "01",
    "bairro_rfb": "ZONA RURAL",
    "municipio_rfb": "0831",
    "uf_rfb": "MA",
    "cod_id_encr": "51644F8C524701C5DB47ACF986E5CA76BA758024EDBF49E2AE6342FA1DFBACDD",
    "tensao": "BT",
    "cnae": "0111301",
    "cnae_grupo": "01113",
    "classe_consumo": "RU3",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B2RU",
    "distribuidora_sigla": "EQUATORIAL MA",
    "distribuidora_cnpj": "06272793000184",
    "distribuidora_nome": "EQUATORIAL MARANHAO DISTRIBUIDORA DE ENERGIA S.A",
    "ponto_conexao": "106981026",
    "cep": "65645000",
    "cep_formatado": "65645-000",
    "logradouro": "pv mamuir",
    "numero_bdgd": null,
    "bairro_bdgd": "MAMUIR",
    "municipio_ibge": "2106607",
    "uf": "MA",
    "lat": -5.32088225,
    "lon": -43.40360143,
    "kwh_medio_mensal": 19.67833333333333,
    "kwh_total_12m": 236.14,
    "ene_12_meses_kwh": [
      16.13,
      9.61,
      27.45,
      33.77,
      8.52,
      17.23,
      22.56,
      22.51,
      19.84,
      21.09,
      19.32,
      18.11
    ],
    "porte_consumo": "baixo",
    "carga_instalada_kw": 491.0,
    "dem_contratada_kw": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "metodo_match": "cep_cnae_unico",
    "n_pjs_no_grupo": 1,
    "cnpj_alternativo": null,
    "socios_modalidade": null,
    "confianca_score": 1.0,
    "n_ucs_para_este_cnpj": 1,
    "_data_carga": "2026-04-26T19:43:43.575858+00:00",
    "uf_part": 8
  },
  {
    "cnpj": "32334810000170",
    "cnpj_basico": "32334810",
    "nome_fantasia": "COOPERAGRO",
    "cnaes_secundarios": "0111302,0111399,0115600,0162899,1066000,4611700,4617600,4631100,4632003,4634601,7490103",
    "tipo_logradouro_rfb": "RUA",
    "logradouro_raw_rfb": "SAO FRANCISCO",
    "numero_rfb": "1819",
    "bairro_rfb": "EXTREMA",
    "municipio_rfb": "0793",
    "uf_rfb": "MA",
    "cod_id_encr": "15DA50AF2A20D4AC94A8B6D838BB8784909D31DDFFF28FF93FA58FEE4DD49331",
    "tensao": "BT",
    "cnae": "0111301",
    "cnae_grupo": "01113",
    "classe_consumo": "RU3",
    "grupo_tensao": "BT",
    "grupo_tarifario": "B2RU",
    "distribuidora_sigla": "EQUATORIAL MA",
    "distribuidora_cnpj": "06272793000184",
    "distribuidora_nome": "EQUATORIAL MARANHAO DISTRIBUIDORA DE ENERGIA S.A",
    "ponto_conexao": "106296628",
    "cep": "65940000",
    "cep_formatado": "65940-000",
    "logradouro": "r velha",
    "numero_bdgd": null,
    "bairro_bdgd": "CENTRO",
    "municipio_ibge": "2104800",
    "uf": "MA",
    "lat": -5.50702105,
    "lon": -45.87406141,
    "kwh_medio_mensal": 52.31166666666667,
    "kwh_total_12m": 627.74,
    "ene_12_meses_kwh": [
      41.86,
      47.98,
      48.92,
      51.63,
      57.85,
      57.2,
      51.08,
      47.82,
      52.44,
      59.27,
      56.23,
      55.46
    ],
    "porte_consumo": "baixo",
    "carga_instalada_kw": 873.0,
    "dem_contratada_kw": null,
    "uc_tem_ceg_gd": false,
    "ceg_gd": null,
    "cnpj_tem_gd": false,
    "gd_potencia_kw": null,
    "elegivel_acl": false,
    "no_acl_livre": false,
    "no_acl_especial": false,
    "grupo_no_acl_livre": false,
    "grupo_no_acl_especial": false,
    "cnpj_eh_consumidor_acl": false,
    "cnpj_eh_comercializador": false,
    "cnpj_eh_gerador": false,
    "cnpj_eh_distribuidor": false,
    "cnpj_eh_varejista": false,
    "metodo_match": "cep_cnae_unico",
    "n_pjs_no_grupo": 1,
    "cnpj_alternativo": null,
    "socios_modalidade": null,
    "confianca_score": 1.0,
    "n_ucs_para_este_cnpj": 1,
    "_data_carga": "2026-04-26T19:43:43.575858+00:00",
    "uf_part": 8
  }
]
```

_Execução:_ `bq query --use_legacy_sql=false 'SELECT * FROM \`gold_energia.estabelecimentos_consumo_certo\` LIMIT 5'`

## Quirks e armadilhas

- **N:1 com cnpj_basico** — sempre agregue (`SUM(kwh_medio_mensal)`, `COUNT(DISTINCT cod_id_encr)`) antes de cruzar com gold_cnpj. Sem agregação, JOIN duplica linhas e inflaciona métricas comerciais.
- **Município**: prefere `municipio_ibge` (7d IBGE) sobre `municipio_rfb` (4d RFB) — IBGE é padrão. **Não use `municipio_rfb`** pra filtrar cidade (códigos diferentes).
- **`cnpj` (14d) é o estabelecimento atribuído**. Pra Tiers B/S, é o vencedor da desambiguação. Não confunda com `distribuidora_cnpj` (CNPJ da concessionária).
- **`ene_12_meses_kwh`** é ARRAY de 12 floats — consumo mensal último ano (ordem cronológica decrescente, mais recente primeiro).
- **`elegivel_acl=TRUE`**: UC com perfil pra ir ao Mercado Livre (consumo, tensão, classe). Não significa que JÁ está no ACL — pra isso `no_acl_livre` ou `no_acl_especial`.
- **`cnpj_tem_gd=TRUE`**: empresa tem geração distribuída (solar próprio etc.). Pode ter `gd_potencia_kw`.
- **Tier de confiança**: filtre por `confianca_score >= 0.85` pra alta certeza; >= 0.70 pra cobertura mais ampla com algum risco de falso positivo.
- **`location` é geo_point** (BQ GEOGRAPHY) — usar `ST_DWITHIN(location, ST_GEOGPOINT(lon,lat), <metros>)` pra raio.

## Tabelas relacionadas

- [`gold_cnpj.empresas`](gold_cnpj.empresas.md) — JOIN por `cnpj_basico` (após agg) pra trazer setor/porte/NJ
- [`gold_pat.empresas`](gold_pat.empresas.md) — JOIN tripla CNPJ × PAT × Energia (ICP composto)
- [`gold_energia.estabelecimentos_360`](gold_energia.estabelecimentos_360.md) — view 360° empresa enriquecida (RFB+PAT+energia)
- [`gold_energia.dim_consumidor_acl_full`](gold_energia.dim_consumidor_acl_full.md) — view ACL completa
- [`gold_energia.tam_acl_elegivel`](gold_energia.tam_acl_elegivel.md) — TAM mercado endereçável

## Templates SQL

### Caso A: empresas em Maricá ordenadas por consumo total do grupo
```sql
WITH energia_marica AS (
  SELECT cnpj_basico,
         SUM(kwh_medio_mensal) AS kwh_total,
         COUNT(*) AS qtd_ucs,
         ANY_VALUE(distribuidora_nome) AS distribuidora
  FROM `data-hacker-488115.gold_energia.estabelecimentos_consumo_certo`
  WHERE municipio_ibge = '3302858'   -- Maricá-RJ
  GROUP BY cnpj_basico
)
SELECT e.cnpj_basico, e.nome, e.industria.setor,
       ROUND(en.kwh_total, 0) AS kwh_total, en.qtd_ucs, en.distribuidora
FROM `data-hacker-488115.gold_cnpj.empresas` e
JOIN energia_marica en USING (cnpj_basico)
WHERE e.status.operacional = 'ativa'
ORDER BY en.kwh_total DESC
LIMIT 100;
```

### Caso B: top 50 consumidores nacionais (industriais)
```sql
WITH consumo AS (
  SELECT cnpj_basico, SUM(kwh_medio_mensal) AS kwh_total
  FROM `data-hacker-488115.gold_energia.estabelecimentos_consumo_certo`
  WHERE classe_consumo IN ('IND', 'COM') AND grupo_tensao = 'AT'
  GROUP BY cnpj_basico
)
SELECT e.nome, e.industria.setor, ROUND(c.kwh_total, 0) AS kwh
FROM `data-hacker-488115.gold_cnpj.empresas` e
JOIN consumo c USING (cnpj_basico)
ORDER BY c.kwh_total DESC
LIMIT 50;
```

### Caso C: empresas elegíveis ACL com >100k kWh/mês
```sql
SELECT cnpj_basico, COUNT(*) AS ucs_elegiveis,
       SUM(kwh_medio_mensal) AS kwh_total,
       ANY_VALUE(distribuidora_nome) AS distribuidora
FROM `data-hacker-488115.gold_energia.estabelecimentos_consumo_certo`
WHERE elegivel_acl = TRUE
  AND kwh_medio_mensal >= 100000
GROUP BY cnpj_basico
HAVING ucs_elegiveis > 0
ORDER BY kwh_total DESC;
```

### Caso D: empresas com geração distribuída (GD) por UF
```sql
SELECT uf, COUNT(DISTINCT cnpj_basico) AS empresas_gd,
       SUM(gd_potencia_kw) AS gd_total_kw
FROM `data-hacker-488115.gold_energia.estabelecimentos_consumo_certo`
WHERE cnpj_tem_gd = TRUE
GROUP BY uf
ORDER BY empresas_gd DESC;
```

## Histórico

- 2026-04-26: última modificação BQ
- 2026-05-03: doc criado
