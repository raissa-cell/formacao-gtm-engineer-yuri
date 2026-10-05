# Surface: LinkedIn  (most detailed — this is the flagship text surface)

ALSO read `references/text-style-rules.md` before generating.

## Cut point (D1 Fold Survival) — THE defining constraint
The first **180 characters** are the only thing shown in the feed before "see more."
The hook's punchline MUST land inside 180 chars. Count characters. If the surprise or
indignation arrives at char 200, the hook scores D1 ≤ 4 no matter how good it reads in full.
Aim for the punch inside the first ~90 chars when possible.

## Weights for scoring
D1 0.35 · D2 0.25 · D3 0.20 · D4 0.20

## Hook structure (mined + elaborated)
**Simple Hook (default, 2 lines):**
- Line 1 — assertive statement, max 7 words.
- Line 2 — complement to line 1, max 7 words.

**Full Hook (3 lines, only when topic complexity warrants):**
- Line 1 — assertive statement, max 7 words.
- Line 2 — complement, max 7 words.
- Line 3 — reading CTA with strong curiosity pull, OR a second complement.

Rules:
- Line 1 is always a statement (never a question opener, never a subordinate clause).
- Default to Simple Hook. Use Full Hook only when depth demands a reading CTA.
- Line breaks are rhythm tools — the white space between lines does pacing work the
  words can't. Use intentionally.
- Parenthetical asides allowed for humor/self-awareness (sparingly).

## Surface mechanics for D4 (Shareability)
On LinkedIn, reshares and "this needs to be said" comments drive reach. A hook that
stakes a clear, slightly uncomfortable professional position outperforms a safe one.
Stake an opinion a competent peer might disagree with.

## Types that over-index
Contrarian/Myth-Bust, Personal Story (Failure/Win), Exact Pain, Statistic/Number.
Identity Threat works but keep it professional, not personal-attack.

## Output formatting
Show the hook with real line breaks AND the character count of the visible-fold portion.

## Worked examples
Topic: AI adoption in SMEs. Surface: LinkedIn.
```
AI won't take your job.
A person using AI will.
```
(42 chars to punch) D1 9 · D2 7 · D3 9 · D4 8 → 8.30/10. Lands far inside the fold,
contrarian stake people repost.

```
I fired our best SDR last quarter.
The replacement doesn't sleep.
```
(35 chars to punch) D1 9 · D2 9 · D3 8 · D4 8 → 8.60/10. Personal-win + identity threat
+ unbearable gap, all before the fold.

---

# Biblioteca de fórmulas (curadoria de 79 ganchos reais)

Banco completo: `references/linkedin-hook-templates.json` — 79 ganchos deduplicados, cada um com
`slots` (os componentes que preenchem a fórmula), `exemplo`, `chars` e `porque_funciona`.
Use o JSON quando quiser variedade bruta; use as 18 fórmulas abaixo como ponto de partida.

**Como usar:** escolher 5 fórmulas de FAMÍLIAS DIFERENTES (nunca 5 variações da mesma),
preencher os slots com o material do post, e só então pontuar D1–D4.
Fórmula sem prova real vira clichê de guru — se não houver o número, o caso ou a cicatriz,
troque de fórmula em vez de inventar o dado.

**Filtro de voz (Engenheiro-Prático-Estoico):** as fontes originais são criadores de LinkedIn
em inglês, muitas em registro de guru. Marcação abaixo:
✅ usar direto · ⚠️ adaptar (tirar hype, cortar aspiracional) · ❌ evitar (colide com a voz).

## A. Contraste temporal / transformação

1. **Escape + segredo contraintuitivo** ⚠️
   `[Situação difícil que escapei] há [tempo]. Meu segredo: [abordagem contraintuitiva].`
   → "Parei de escrever proposta comercial há 8 meses. O truque foi ter menos processo, não mais."
   (Só funciona com o dado real; sem ele vira frase de coach.)

2. **Antes → depois → lições** ⚠️
   `[Ponto de partida humilde]. [Tempo] depois, [ponto de chegada]. [N] lições no caminho.`
   Risco alto de soar aspiracional. Adaptar: trocar "conquista" por "aprendizado técnico".

3. **Resultado impressionante primeiro, dificuldade depois** ✅
   `Hoje [resultado/número]. Em [ano], [condição precária].`
   Top-down puro — bate com a regra de VALOR na linha 1.

4. **Marco + sequência de decisões** ✅
   `Há [tempo] tomei [decisão]. [Ação 1], [ação 2] e [ação 3].`

## B. Expectativa quebrada

5. **Achei que era X, até que Y** ✅
   `Pensei que [expectativa alta]. Até que [ponto de virada], em [tempo curto].`

6. **Ação inconvencional + resultado** ✅
   `[Tempo] atrás, [ação que ninguém faz]. Não fiz [passo esperado]. Hoje, [resultado].`

7. **Confissão de erro** ✅ (autoironia = erro como dado — exatamente a voz)
   `[Erro que cometi]. [Expansão do erro]. Mas isso não foi o pior.`

8. **"Bem, isso aconteceu"** ✅
   `[Declaração chocante em 5 palavras]. [Contexto que reenquadra].`
   → "Passei a noite na cadeia. Última noite de férias. Cela 110."

9. **O que aconteceu foi o oposto** ✅
   `O que aconteceu quando [ação que todos recomendam]? [Resultado ruim].`

## C. Contrarian / mito

10. **Não é sobre X, é sobre Y** ✅
    `[Assunto] não é sobre [o que todo mundo acha]. É sobre [o que realmente é].`

11. **Por que [prática comum] não funciona** ✅
    `[Prática consagrada] não funciona. [Métrica que prova].` — exige o número.

12. **X é eufemismo para Y** ✅ (humor seco em uma linha)
    `"[Frase corporativa]" normalmente significa "[tradução crua]".`

13. **Pare de fazer isso** ⚠️
    `Nunca [prática comum]. [Motivo cru em uma linha].`
    Adaptar: sem exclamação, sem "sério, quem você pensa que é". Imperativo seco, uma vez só.

14. **Não é falta de informação** ✅
    `A maioria sabe exatamente [o que fazer]. O problema não é [causa presumida].`

## D. Lista / material rico (slot de quinta)

15. **Número + prova de esforço** ✅
    `Levei [tempo/esforço quantificado] para aprender estas [N] coisas.`

16. **Todos conhecem X, poucos sabem usar** ⚠️
    `Todo mundo conhece [ferramenta]. Quase ninguém [uso avançado]. Aqui vão [N] [itens].`
    Cortar percentuais inventados ("apenas 0,01%") — proibido pela voz.

17. **Processo que economiza tempo** ✅
    `Para economizar [tempo], aqui está meu processo em [N] etapas.`

## E. Diálogo / cena

18. **Fala + resposta crua** ✅
    `"[Pergunta ou objeção real]" — [resposta em uma linha que desmonta].`
    → "'Concorrente faz por R$500.' Faz mesmo. Uma vez."

## Antipadrões deste banco (não importar)

- ❌ Anúncio de conquista pessoal sem lição ("Fechamos Série A", "Cheguei a 40k seguidores").
- ❌ Aspiracional de estilo de vida (apartamento na praia, viajar o mundo, multimilionário aos 27).
- ❌ Autodepreciação sem dado ("eu era invisível", "eu não era nada").
- ❌ Percentual/estatística inventada para dar autoridade.
- ❌ Emoji como punchline, CAPS LOCK para ênfase, "NOTÍCIA GRANDE".
