# `tabelas/` — docs por tabela BQ

Cada arquivo `<dataset>.<tabela>.md` é **auto-contido**: schema completo, sample real (5 linhas), descrição, quirks, templates SQL. Pra carregamento granular do contexto pelo agente.

**Total:** 37 docs (Tier 1+2). Foco: análise comercial de empresas brasileiras (CNPJ + PAT + Energia). Fora do escopo: ANEEL detalhado (`bronze_aneel`/`silver_aneel`).

## Convenção

- Naming: `<dataset>.<tabela>.md` (flat, não em subdiretórios — facilita grep)
- Schema completo + sample real são **gerados** via `python -m scripts.cnpj._gen_table_doc`
- Seções "Quando usar", "Quirks", "Templates SQL", "Tabelas relacionadas" são **curadas manualmente**

## Índice — Tier 1 (essenciais)

| Doc | Camada | Linhas | Usar pra |
|---|---|---:|---|
| [gold_cnpj.empresas](gold_cnpj.empresas.md) ⭐ | gold | 27,4M | **Fonte canônica** comercial — 1 doc/CNPJ_BASICO ATIVO com 8 clusters semânticos |
| [gold_cnpj.pessoas](gold_cnpj.pessoas.md) ⭐ | gold | 10,2M | Pessoa PF deduplicada → array de empresas onde aparece |
| [gold_pat.empresas](gold_pat.empresas.md) ⭐ | gold | 288k | Beneficiárias PAT — total trabalhadores, folha estimada, cobertura |
| [gold_pat.empresas_unidades](gold_pat.empresas_unidades.md) | gold | 407k | PAT unidades flat (1/CNPJ 14d) — pra mapas/distribuição |
| [gold_pat.servicos_alimentacao](gold_pat.servicos_alimentacao.md) | gold | 20k | Facilitadoras (cartões) + fornecedoras (refeição direta) |
| [gold_energia.estabelecimentos_consumo_certo](gold_energia.estabelecimentos_consumo_certo.md) ⭐ | gold | 1,26M | Consumo elétrico BDGD/ANEEL — 1/UC, agregar por cnpj_basico |

## Índice — Tier 1 (CNPJ bronze base)

| Doc | Camada | Linhas | Usar pra |
|---|---|---:|---|
| [bronze_cnpj.empresas](bronze_cnpj.empresas.md) | bronze | 67M | Razão social, NJ, porte, capital social (cru) |
| [bronze_cnpj.estabelecimentos](bronze_cnpj.estabelecimentos.md) | bronze | 70M | Endereço, situação, CNAE (cru) |
| [bronze_cnpj.socios](bronze_cnpj.socios.md) | bronze | 27,5M | QSA cru (cotistas + admins misturados) |
| [bronze_cnpj.simples](bronze_cnpj.simples.md) | bronze | 48M | OPCAO_SIMPLES, OPCAO_MEI |

## Índice — Tier 2 (silver_cnpj derivado)

| Doc | Tipo | Usar pra |
|---|---|---|
| [silver_cnpj.dim_empresa](silver_cnpj.dim_empresa.md) | TABLE | Dimensão empresa dedupada |
| [silver_cnpj.estabelecimentos_dominios](silver_cnpj.estabelecimentos_dominios.md) | TABLE | Email parseado, dominio_raiz, endereco_norm |
| [silver_cnpj.socios](silver_cnpj.socios.md) | TABLE | Sócios denormalizados, qualificacao_nome resolvido |
| [silver_cnpj.domains](silver_cnpj.domains.md) | TABLE | 1 linha por domínio classificado (seed > Explorium) |
| [silver_cnpj.grupos_por_dominio](silver_cnpj.grupos_por_dominio.md) | VIEW | Empresas que usam o mesmo domínio (grupo) |
| [silver_cnpj.empresas_por_endereco](silver_cnpj.empresas_por_endereco.md) | VIEW | Empresas no mesmo endereço |
| [silver_cnpj.empresas_por_socio_pj](silver_cnpj.empresas_por_socio_pj.md) | VIEW | Holding → controladas |
| [silver_cnpj.grupos_via_socios](silver_cnpj.grupos_via_socios.md) | VIEW | CNPJs com sócio PJ em comum |
| [silver_cnpj.rede_executivos](silver_cnpj.rede_executivos.md) | VIEW | Top sócios PF por # empresas (board members serial) |
| [silver_cnpj.socios_por_pessoa](silver_cnpj.socios_por_pessoa.md) | VIEW | Empresas onde a pessoa aparece |

## Índice — Tier 1 (CNPJ dimensões)

| Doc | Linhas | Usar pra |
|---|---:|---|
| [bronze_cnpj.cnaes](bronze_cnpj.cnaes.md) | 1,4k | CODIGO → DESCRICAO CNAE 7d |
| [bronze_cnpj.municipios](bronze_cnpj.municipios.md) | 5,6k | CODIGO RFB → nome município |
| [bronze_cnpj.naturezas](bronze_cnpj.naturezas.md) | ~90 | CODIGO → DESCRICAO natureza jurídica |
| [bronze_cnpj.paises](bronze_cnpj.paises.md) | ~255 | CODIGO RFB → nome país |
| [bronze_cnpj.qualificacoes](bronze_cnpj.qualificacoes.md) | ~70 | CODIGO → DESCRICAO qualificação sócio |
| [bronze_cnpj.motivos](bronze_cnpj.motivos.md) | ~65 | CODIGO → DESCRICAO motivo baixa/suspensão |

## Índice — Tier 2 (PAT)

| Doc | Camada | Linhas | Usar pra |
|---|---|---:|---|
| [bronze_pat.empresas_beneficiarias](bronze_pat.empresas_beneficiarias.md) | bronze | 521k unid | Empresas que oferecem PAT (cru, com unidades) |
| [bronze_pat.empresas_facilitadoras](bronze_pat.empresas_facilitadoras.md) | bronze | ~10k | Operadoras de cartão-refeição (Sodexo etc.) |
| [bronze_pat.empresas_fornecedoras](bronze_pat.empresas_fornecedoras.md) | bronze | ~12k | Refeições coletivas/cozinha industrial |
| [bronze_pat.nutricionistas](bronze_pat.nutricionistas.md) | bronze | ~38k | Nutricionistas registrados PAT |
| [silver_pat.empresas_beneficiarias](silver_pat.empresas_beneficiarias.md) | silver | 521k | + flag `pat_rfb_divergente` |
| [silver_pat.empresas_beneficiarias_grupo](silver_pat.empresas_beneficiarias_grupo.md) | silver | 345k | Agrupado por CNPJ_BASICO |
| [silver_pat.empresas_servicos_alimentacao](silver_pat.empresas_servicos_alimentacao.md) | silver | ~28k | Facilitadoras ∪ fornecedoras |
| [gold_pat.empresas_outliers_suspeitos](gold_pat.empresas_outliers_suspeitos.md) | view | — | Empresas com sinais suspeitos (folha enorme com 1 unidade etc.) |

## Índice — Tier 2 (Energia views)

| Doc | Tipo | Usar pra |
|---|---|---|
| [gold_energia.dim_consumidor_acl_full](gold_energia.dim_consumidor_acl_full.md) | VIEW | Consumidores ACL (Mercado Livre) |
| [gold_energia.estabelecimentos_360](gold_energia.estabelecimentos_360.md) | VIEW | Empresa enriquecida 360° (RFB + PAT + energia) |
| [gold_energia.tam_acl_elegivel](gold_energia.tam_acl_elegivel.md) | VIEW | TAM (mercado endereçável) ACL |

## Como atualizar

```bash
# 1. Re-gerar esqueleto de uma tabela específica (atualiza schema + sample)
python -m scripts.cnpj._gen_table_doc --dataset gold_cnpj --table empresas

# 2. Re-gerar todas as 37 tabelas Tier 1+2
python -m scripts.cnpj._gen_table_doc --all

# 3. Editar manualmente as seções "Quando usar / Quirks / Templates SQL / Tabelas relacionadas"
```

> **O gerador sobrescreve schema e sample mas APAGA as seções qualitativas** — sempre re-aplique a curadoria após regenerar. (TODO: gerador idempotente que preserva sections curadas).

## Mirror

Os mesmos arquivos existem em `skills/cnpj-investigation/references/tabelas/` (publicado pela skill). O `_gen_table_doc.py` mantém os 2 sincronizados.
