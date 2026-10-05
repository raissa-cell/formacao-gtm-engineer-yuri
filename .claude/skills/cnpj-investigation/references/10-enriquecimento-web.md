# Enriquecimento via WebSearch / WebFetch

Quando o BigQuery sozinho não basta, use WebSearch (busca) e WebFetch (leitura de URL específica) pra adicionar contexto de fontes públicas. Útil pra: validar anomalias, encontrar nome fantasia/site/redes sociais, achar notícias, entender um setor desconhecido.

> **Regra de ouro**: BQ sempre primeiro (é a verdade jurídica). Web complementa, nunca substitui. Sempre **citar fontes** com URLs.

---

## 1. Quando ativar busca web

| Sinal na pergunta ou no resultado BQ | Ação |
|---|---|
| Anomalia estatística (ex: padaria ME com 2.412 funcionários, capital incoerente) | Buscar nome fantasia + cidade pra confirmar tamanho real |
| Resultado BQ sem `nome_fantasia` mas razão social genérica | Buscar CNPJ pra descobrir o nome comercial |
| Usuário pede "o que essa empresa faz?" / "é confiável?" / "quem é?" | Site oficial + LinkedIn + notícias |
| Empresa pequena/regional sem visibilidade pública | Instagram/Facebook/Google Maps |
| Holding/grupo desconhecido nos sócios | Buscar nome dos sócios + "sócio" / "fundador" |
| Setor que o usuário não conhece (ex: PAT facilitadora) | Buscar termo + "o que é" / "site:gov.br" |
| Empresa em recuperação judicial / baixada | Notícias com filtro temporal |

---

## 2. Padrões de query

### Encontrar empresa por nome+cidade

```
"<razao_social_ou_fantasia>" <cidade> <UF>
```

Exemplo: `"Estação do Café" padaria CPA Cuiabá MT` → encontra Instagram, diretórios locais, Google Maps.

### Encontrar CNPJ específico

```
"<razao_social>" CNPJ <primeiros 8 digitos> <cidade>
```

Sites úteis (free tier público):
- **diariocidade.com** — cobre microempresas regionais
- **brasil-empresas.com** — agregador
- **solutudo.com.br** — diretório por categoria
- **cnpj.biz** — geralmente paga, mas snippets do search ajudam
- **receitaws.com.br/v1/cnpj/<14digs>** — API pública RFB (dados básicos)

### Notícias/contexto setorial

```
"<empresa>" <ano-corrente> notícia
```

ou com filtros de domínio:

```
WebSearch query="<empresa>" allowed_domains=["valor.globo.com", "exame.com", "g1.globo.com", "infomoney.com.br"]
```

### Site oficial + redes sociais

```
"<nome fantasia>" site:linkedin.com OR site:instagram.com OR site:facebook.com
```

### Validar anomalia (capital × funcionários)

```
"<razao_social>" "número de funcionários" OR "porte" OR "faturamento"
```

---

## 3. Workflow recomendado

### Padrão "Investigação de anomalia"

```
1. [BQ] Detectei anomalia: empresa X declarou Y, mas atributo Z é incoerente
2. [Web] Vou buscar referências públicas pra entender se é real ou erro de cadastro
   → WebSearch "<razao_social ou fantasia>" <cidade>
3. [Síntese] Comparar:
   - Se web confirma BQ → registrar como caso real (raro mas possível)
   - Se web contradiz BQ → marcar como provável erro de cadastro, sugerir filtrar
4. [Saída] Mostrar dado BQ + dado web + conclusão, com **URLs como fonte**
```

### Padrão "Perfil expandido"

```
1. [BQ] Pegar tudo que tem em silver_cnpj + gold_pat:
   - razão social, fantasia, capital, idade, CNAE, endereço, sócios, email/domínio
2. [Web] Buscar:
   - Site oficial (se domínio próprio do email indica)
   - LinkedIn da empresa
   - Notícias recentes
3. [Síntese] Artifact dashboard com 2 colunas:
   - Esquerda: dados oficiais BQ (com fonte "RFB")
   - Direita: presença pública web (com URLs)
```

---

## 4. Anti-padrões

❌ **Buscar antes de checar BQ.** Sempre comece com query no BQ — o BQ tem a verdade jurídica.

❌ **Confiar cego em scrape de site.** Sites agregadores (cnpj.biz, econodata) podem ter dados desatualizados, especialmente sobre nº de funcionários.

❌ **Apresentar info web sem fonte.** Toda afirmação web precisa do URL.

❌ **Misturar sem distinguir.** Sempre marque a origem na resposta:
- ✅ *"No CNPJ-RFB: capital R$ 30k, ME · Na web (Instagram/CNN): padaria de bairro recomendada"*
- ❌ *"A empresa é uma padaria com 2.412 funcionários e R$ 30k de capital"* (mistura sem distinguir)

❌ **Buscar sem propósito.** Se o BQ já respondeu, não force uma busca web. Pergunte ao usuário se quer mais contexto.

❌ **Confiar em estimativas de receita/funcionários publicadas em sites de "consulta CNPJ" pagos.** Esses números são geralmente derivados de heurísticas próprias, não auditados.

---

## 5. Caso de uso real — anomalia da padaria

**Pergunta**: "qual é a maior padaria do PAT por trabalhadores?"

**[BQ — gold_pat.empresas]**:
```
F. TAVARES DA COSTA VEIGA ME · CNPJ 09150946 · 1 unidade · 2.412 trabalhadores · R$ 30k capital · Cuiabá/MT
```

**Anomalia detectada**: capital R$ 30k é incompatível com 2.412 funcionários (folha estimada R$ 11M/mês × 30k de capital = empresa quebraria em dias).

**[Web]** WebSearch `"Estação do Café" padaria CPA Cuiabá MT`:
- Instagram [@estacaodocafecuiaba](https://www.instagram.com/estacaodocafecuiaba/) — pequena padaria de bairro
- [CNN Brasil V&G](https://www.cnnbrasil.com.br/viagemegastronomia/viagem/lugares-para-tomar-cafe-da-manha-em-cuiaba/) — entre os 6 melhores cafés da manhã em Cuiabá
- Diretórios locais ([Diário Cidade](https://www.diariocidade.com/mt/cuiaba/guia/estacao-do-cafe-paes-e-doces-09150946000109/amp/), [Brasil Empresas](https://cpa-ii-mato-grosso.brasil-empresas.com/cafe/estacao-do-cafe-cpa-ii)) — confirmam endereço

**Conclusão**: presença pública + porte declarado RFB (ME) + capital R$ 30k convergem pra padaria pequena. **2.412 funcionários é erro de cadastro PAT** (digitação ou confusão com outro CNPJ). Recomendação ao usuário: filtrar essa empresa em rankings, ou cruzar com BDC/CAGED se precisar dado real.

---

## 6. Output formatado

Quando integrar dado BQ + web na resposta, separe explicitamente:

```markdown
**[BQ — silver_cnpj]**
- Razão: F. TAVARES DA COSTA VEIGA ME (ME, R$ 30k, 19 anos)
- Endereço: Av. Brasil 430, CPA II, Cuiabá/MT
- Email: estacaodocafecpa02@gmail.com (gmail genérico)
- Sócios: [vazio]

**[Web]**
- Nome real: Estação do Café, Pães e Doces — pequena padaria de bairro
- Instagram: [@estacaodocafecuiaba](https://www.instagram.com/estacaodocafecuiaba/) (~ posts de pão de queijo)
- Fonte: CNN Brasil V&G recomenda como melhor café da manhã de Cuiabá

**[Síntese]**
Cadastro PAT de 2.412 funcionários é incompatível com o porte real (ME, micro). Provável erro de digitação ou confusão de CNPJ. Recomendar filtro em rankings.

**Fontes web**:
- [Instagram Estação do Café](https://www.instagram.com/estacaodocafecuiaba/)
- [CNN Brasil V&G — café da manhã em Cuiabá](https://www.cnnbrasil.com.br/viagemegastronomia/viagem/lugares-para-tomar-cafe-da-manha-em-cuiaba/)
- [Diário Cidade — Estação do Café](https://www.diariocidade.com/mt/cuiaba/guia/estacao-do-cafe-paes-e-doces-09150946000109/amp/)
```

---

## 7. Quando usar Artifact pra perfil expandido

Se a investigação resulta em **perfil completo de empresa** com BQ + web, vale construir um Artifact React (ver `09-artifacts-e-visuais.md` Template A) com:

- **Header**: razão social, CNPJ, porte, capital, idade
- **2 colunas**:
  - Esquerda — "Dados oficiais (RFB/PAT)": endereço, CNAE, sócios, métricas PAT
  - Direita — "Presença pública (web)": site, redes sociais, notícias recentes, recomendações
- **Footer**: lista de fontes com URLs clicáveis

Sempre marcar visualmente a origem (ícone 🏛️ pra RFB, 🌐 pra web).

---

## 8. Limitações do WebSearch

- **Disponível só em US** (web search restrito geograficamente).
- **Snippets curtos** — pra detalhe completo use WebFetch numa URL específica.
- **402 Payment Required** em sites pagos (cnpj.biz, econodata premium) — use só os snippets do search.
- **Cache de 15 min** no WebFetch — re-fetch da mesma URL retorna cached.
- **Não acessa redes sociais privadas** (LinkedIn requer login, Instagram pages requer login pra detalhe).
- **Resultados localizados em PT-BR** podem variar; sempre prefira nome em português + cidade.

---

## 9. Disponibilidade do WebSearch/WebFetch

Estas ferramentas **não estão sempre disponíveis** — dependem do harness Claude (ChatGPT-style web, Claude Code, API). Antes de prometer enriquecimento web ao usuário, **verifique disponibilidade** ou peça pra ele rodar a busca e colar o resultado se a tool não estiver acessível.

Se WebSearch indisponível, alternativa:
- Pedir ao usuário pra colar URL específica → usar WebFetch
- Sugerir site direto (ex: "olha em consulta-cnpj-receita-federal-da-republica-federativa-do-brasil...")
- Restringir ao que BQ tem
