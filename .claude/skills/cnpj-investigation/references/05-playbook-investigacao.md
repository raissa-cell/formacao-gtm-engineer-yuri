# Playbook de Investigação

Cenários comuns de exploração na base CNPJ, com a abordagem que funciona bem.

---

## Cenário 1 — "Existe empresa do CNAE X com sócio chamado Y?"

**Estratégia em 3 passos**:

1. Descubra os códigos CNAE relevantes via `bronze_cnpj.cnaes` (busca textual).
2. Filtre `estabelecimentos` ATIVOS pelo CNAE OU palavra-chave no nome (cobre os dois casos).
3. JOIN com `socios` filtrando o nome.

**Sempre cubra grafia com e sem acento** (`ACOUGUE` e `AÇOUGUE`, `MEDICO` e `MÉDICO`).

**Reporte separadamente**:
- Total de matches
- Subgrupo específico se o usuário citar nome composto (ex.: "225 com Bruno, dos quais 3 com Bruno Cardoso")

---

## Cenário 2 — "Esse telefone pertence a alguma dessas empresas?"

1. Normalize o número de input removendo não-dígitos.
2. Compare contra `DDD1+TELEFONE1` E `DDD2+TELEFONE2` (também normalizados).
3. **Avise o usuário** que a RFB armazena fixo comercial — celulares pessoais e WhatsApp raramente aparecem.
4. Se não bater exato, sugira: (a) verificar se o DDD bate com a região da empresa; (b) buscar por prefixo (`LIKE '94%'`) para ver se o DDD é da mesma região.

---

## Cenário 3 — "Esse e-mail pertence a alguma dessas empresas?"

1. Busca exata primeiro (`LOWER(CORREIO_ELETRONICO) = '...'`).
2. Se zero match, busca fuzzy (`LIKE '%parte_local%'`) para encontrar variações.
3. **Lembre** que a RFB cadastra **um e-mail por estabelecimento** — frequentemente é do contador, não do sócio. Falsa-negativa é comum.

---

## Cenário 4 — "Essa pessoa pode ter nascido em [ano X]?"

1. Pegue o `FAIXA_ETARIA` do registro em `socios`.
2. Calcule a janela de nascimento usando a data atual: `nascimento_max = ano_atual - idade_min` e `nascimento_min = ano_atual - idade_max`.
3. Confronte com o ano que o usuário citou.
4. Responda em uma linha: "**Sim, é compatível**" ou "Não, a faixa N indica nascimento entre X e Y, fora do ano que você sugeriu."

---

## Cenário 5 — "Existe vínculo entre [empresa/lugar] e [pessoa/sobrenome]?"

Teste **duas hipóteses** em paralelo:

1. **Vínculo nominal**: pessoa é sócia em empresa cujo nome contém o termo (`razão social` ou `nome fantasia`).
2. **Vínculo geográfico**: pessoa é sócia em empresa **localizada** no município/região mencionada.

Se ambos zerarem, declare "**Nenhum vínculo direto encontrado**" e mostre os dois testes em uma tabela curta. Se houver match em apenas um, destaque.

**Não** especule sobre vínculos indiretos (parentesco com outro sócio, sócio em comum em terceira empresa) sem o usuário pedir explicitamente.

---

## Cenário 6 — "Quais empresas estão na cidade/região X?"

1. Use `municipios.DESCRICAO` para resolver o nome (em maiúsculo).
2. **Sempre adicione `e.UF = 'XX'`** porque há municípios homônimos (ex.: 16 cidades chamadas "Boa Vista" no Brasil).
3. Filtre `SITUACAO_CADASTRAL = '02'`.
4. Limite por CNAE ou tamanho se a região for grande.

---

## Cenário 7 — "Quem são os sócios dessa empresa?"

1. Filtre `socios` por `CNPJ_BASICO` (8 dígitos).
2. JOIN com `qualificacoes` para o cargo.
3. Marque tipo (PF/PJ/Estrangeiro) via `ID_SOCIO`.
4. Mostre `DATA_ENTRADA_SOCIEDADE` formatada.
5. Se houver `NOME_REPRESENTANTE`, exiba também (caso de sócio PJ ou menor de idade).

---

## Cenário 8 — "Quais empresas essa pessoa abriu? (rede de sócio)"

Como CPF é mascarado (`***123456**`), tem risco de homônimo:

1. Busque por `NOME_SOCIO` exato + `CNPJ_CPF_SOCIO` igual à máscara conhecida.
2. **Se houver mais de um CPF mascarado distinto** com o mesmo nome, há homônimos — separe os grupos e reporte.
3. Liste todas as empresas (ativas + baixadas), ordenadas por data de entrada decrescente.
4. Acrescente `SITUACAO_CADASTRAL` para o usuário ver o status de cada uma.

---

## Cenário 9 — "Análise setorial / quantas empresas no CNAE X?"

```sql
SELECT
  e.UF,
  COUNT(DISTINCT e.CNPJ_BASICO) AS empresas
FROM `data-hacker-488115.bronze_cnpj.estabelecimentos` e
WHERE e.SITUACAO_CADASTRAL = '02'
  AND e.CNAE_FISCAL_PRINCIPAL = '4722901'
  AND e.ID_MATRIZ_FILIAL = '1'  -- evitar contar matriz+filiais como duas
GROUP BY 1
ORDER BY empresas DESC
```

---

## Cenário 10 — "Existe empresa com site/domínio X (e sócio Y)?"

**Estratégia**:

1. Extraia o domínio do `CORREIO_ELETRONICO`: `SPLIT(LOWER(CORREIO_ELETRONICO), '@')[SAFE_OFFSET(1)]`.
2. Filtre por domínio com `LIKE '%@dominio.com.br'` (com `@` no início — evita falso positivo tipo `naogabriel.com.br`).
3. Se houver nome de sócio, faça `JOIN socios` filtrando o nome.
4. Reporte o e-mail completo cadastrado para o usuário ver o contexto (pode ser `contato@`, `comercial@`, etc.).

**Importante avisar o usuário**:
- A RFB armazena **1 e-mail por estabelecimento**, frequentemente do contador.
- Domínio próprio cadastrado **não garante** que o site está ativo hoje.
- Empresa cuja fantasia bate com domínio (ex.: fantasia "Padaria Gabriel" + e-mail `@gabriel.com.br`) é match forte.
- Se o e-mail é genérico (`@gmail.com`), não há informação de site para reportar.

**Heurísticas adicionais quando o domínio bate**:
- Conte quantos CNPJs ativos compartilham aquele domínio. Se 3+, é grupo econômico provável.
- Verifique se o domínio aparece em escritório de contabilidade (parte local com `contabil`, `fiscal`, `escrita`).
- Cruze com sócios em comum entre os CNPJs que compartilham o domínio.

Detalhes técnicos completos em `references/06-analise-dominios.md`. SQL pronto em `references/04-padroes-query.md` (queries 12, 13, 14, 15).

---

## Postura analítica geral

- **Conservador na inferência**: dois Fulanos com mesmo nome **podem** ser a mesma pessoa, mas não afirme. Use a faixa etária, CPF mascarado e qualificação para corroborar.
- **Confirme E desconfirme**: se respondeu "sim" a algo, mostre também o que não bateu (ex.: "está em PA mas o telefone não é o que você buscou").
- **Vazio é um resultado válido**: declare-o explicitamente, não tente forçar matches inflando critério.
- **Responda em camadas**: total → subgrupo → detalhe. Deixe o usuário pedir mais profundidade.
