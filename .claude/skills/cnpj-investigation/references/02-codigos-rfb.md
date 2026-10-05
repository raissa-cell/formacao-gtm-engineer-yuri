# Códigos RFB — Tabela de Referência

Volumes medidos no snapshot atual de `bronze_cnpj`.

---

## SITUACAO_CADASTRAL (em `estabelecimentos`)

| Código | Significado | % da base |
|---|---|---:|
| `01` | Nula | 0,2% |
| **`02`** | **ATIVA** ← filtro padrão | **40,6%** |
| `03` | Suspensa | 0,4% |
| `04` | Inapta | 12,0% |
| `08` | Baixada | 46,9% |

> **Quase metade da base é BAIXADA.** Sempre filtrar `SITUACAO_CADASTRAL = '02'` para análise de empresas em operação.

---

## ID_MATRIZ_FILIAL (em `estabelecimentos`)

| Código | Significado |
|---|---|
| `1` | Matriz (~67M linhas) |
| `2` | Filial (~3,2M linhas) |

---

## PORTE (em `empresas`)

| Código | Significado | % |
|---|---|---:|
| `01` | **ME** (Microempresa, genérico — inclui MEI e não-MEI) | 75,1% |
| `03` | **EPP** (Empresa de Pequeno Porte) | 3,0% |
| `05` | Demais (médias/grandes) | 21,9% |
| `00`/`NULL` | Não informado | <0,01% |

> ⚠️ **`PORTE='01'` NÃO é MEI.** MEI é identificado por `simples.OPCAO_MEI='S'` ou `empresas.NATUREZA_JURIDICA='2135'`.

---

## NATUREZA_JURIDICA (em `empresas`) — top 10

Faixa de 4 dígitos. **`1xxx`**=Adm. Pública, **`2xxx`**=Empresariais, **`3xxx`**=Sem fins lucrativos, **`4xxx`**=Pessoas Físicas, **`5xxx`**=Organismos Internacionais.

| Código | Categoria | Linhas |
|---|---|---:|
| `2135` | **MEI** | 43,7M |
| `2062` | Sociedade Empresária Ltda | 16,1M |
| `4090` | Empresário Individual | 2,9M |
| `3999` | Outras OSC | 1,4M |
| `2240` | Sociedade Simples Limitada | 810K |
| `4120` | Produtor Rural (PF) | 633K |
| `3085` | Cooperativa | 333K |
| `4014` | Microempreendedor Rural | 215K |
| `2305` | EIRELI | 213K |
| `2321` | Sociedade Unipessoal de Advocacia | 157K |

Outros úteis:
- `2046` S.A. Fechada
- `2054` S.A. Aberta
- `2240` Sociedade Simples Limitada
- `1244` Município
- `1031` Órgão Executivo Municipal

---

## OPCAO_SIMPLES e OPCAO_MEI (em `simples`)

| Coluna | `S` (Sim) | `N` (Não) |
|---|---:|---:|
| `OPCAO_SIMPLES` | 24,7M | 23,4M |
| `OPCAO_MEI` | 16,8M | 31,3M |

**Identificar MEI ATIVO** (combinar 3 filtros):
```sql
WHERE e.SITUACAO_CADASTRAL = '02'
  AND emp.NATUREZA_JURIDICA = '2135'
  AND s.OPCAO_MEI = 'S'
```

---

## QUALIFICACAO_SOCIO (em `socios`) — códigos comuns

A tabela `qualificacoes` tem 68 entradas. Mais frequentes:

| Código | Descrição |
|---|---|
| `05` | Administrador |
| `10` | Diretor |
| `16` | Presidente |
| `22` | Sócio |
| `28` | Sócio-Gerente |
| `49` | Sócio-Administrador |
| `52` | Sócio com Capital |
| `54` | Fundador |
| `65` | Titular Pessoa Física Residente ou Domiciliado no Brasil |

Para descrição completa, sempre faça JOIN com `bronze_cnpj.qualificacoes ON QUALIFICACAO_SOCIO = CODIGO`.

---

## ID_SOCIO (em `socios`)

| Código | Tipo |
|---|---|
| `1` | Pessoa Jurídica |
| `2` | Pessoa Física |
| `3` | Estrangeiro |

---

## FAIXA_ETARIA (em `socios`)

| Código | Idade | Janela de nascimento (referência: 2026) |
|---|---|---|
| `0` | Não se aplica (PJ) | — |
| `1` | 0–12 | 2014–2026 |
| `2` | 13–20 | 2006–2013 |
| `3` | 21–30 | 1996–2005 |
| `4` | 31–40 | 1986–1995 |
| `5` | 41–50 | 1976–1985 |
| `6` | 51–60 | 1966–1975 |
| `7` | 61–70 | 1956–1965 |
| `8` | 71–80 | 1946–1955 |
| `9` | >80 | até 1945 |

**Sempre recalcule a janela com base na data atual** — a tabela acima é referência para 2026.

---

## MOTIVO_SITUACAO_CADASTRAL (em `estabelecimentos`)

Tabela `motivos` tem 63 códigos. Principais:

| Código | Descrição |
|---|---|
| `00` | Sem motivo (CNPJ ativo) |
| `01` | Extinção por encerramento liquidação voluntária |
| `21` | Pedido de baixa pelo titular |
| `63` | **Omissão de declarações** (mais comum em baixadas) |
| `73` | Inaptidão por inexistência de fato |

---

## SITUACAO_ESPECIAL (em `estabelecimentos`)

Quando preenchido, indica situação especial em curso. Exemplos:
- `RECUPERACAO JUDICIAL`
- `FALENCIA`
- `INTERVENCAO`
- `LIQUIDACAO EXTRAJUDICIAL`

A coluna `DATA_SITUACAO_ESPECIAL` indica quando começou.
