---
name: outbound-personalization
description: >
  Escreve mensagens de prospecção ativa 1:1 no tom do usuário — nota de conexão do LinkedIn, DM,
  WhatsApp, e-mail frio e follow-up — SEMPRE personalizadas lead a lead a partir de uma base
  enriquecida. Use sempre que a tarefa for: escrever nota de conexão, DM de LinkedIn, mensagem
  de outreach, sequência de follow-up 1:1, personalizar mensagem para uma lista de leads, ou
  adaptar um template de outbound para pessoas específicas. Gatilhos: "escreve a nota de conexão",
  "mensagem de conexão pro lead", "DM pra esses leads", "personaliza a mensagem", "outreach no
  LinkedIn", "cold email pra essa lista", "mensagem 1:1", "abordagem pro lead X".
  NÃO use para copy de conteúdo (post, carrossel, ad) — isso é linkedin-post-generator /
  impact-copywriter com brand/voice.md.
---

# Outbound Personalization — mensagens 1:1 no tom do usuário

## Regra zero (não negociável)

**Carregue `brand/voice-outbound.md` ANTES de escrever uma única linha.** É o doc canônico de voz para prospecção. Ele manda sobre `brand/voice.md` em qualquer conversa 1:1.

O erro clássico, já cometido: usar `voice.md` (voz de CONTEÚDO) para escrever DM. Produz jargão de post dito a estranho — "documento o que quebra", "rodo em produção", "transformo time de dados em gerador de pipeline". Frase de deck mata a conversa antes de começar.

`impact-copywriter` é brand-blind e não substitui esta skill. Se for usado, é só como apoio de estrutura, nunca de tom.

---

## Regra um: template é BASE, não produto final

Templates por segmento (ex: `campaigns/<campanha>/Outbound/matriz-abordagem.md`) existem para dar o esqueleto e garantir consistência de registro. **Eles nunca são enviados como estão.**

Antes de escrever a mensagem de CADA lead, rode a busca de sinal abaixo. O template só entra se nada mais forte aparecer.

---

## Regra dois: hierarquia de sinal de conexão

Busque, na ordem, o elemento em comum mais forte entre o lead e o usuário. **Pare no primeiro que encontrar** e construa a mensagem em cima dele. O interesse temático ("a gente acompanha os mesmos assuntos de IA e vendas") é o ÚLTIMO da fila, o fallback quando não existe nada melhor.

| # | Sinal | Onde procurar | Por que é forte |
|---|---|---|---|
| 1 | **Mesma empresa** (mesmo em época diferente) | `empresa`, `empresas_anteriores`, `experience[]` no engagers.json | Vínculo verificável e imediato. Gera resposta quase sempre |
| 2 | **Mesma faculdade / programa** | `education[]` no engagers.json | Pertencimento tribal. Vale mesmo com anos de diferença |
| 3 | **Mesma cidade / país de vivência** | `cidade`, `pais`, `about`, `experience[].location` | a cidade ou país onde o usuário mora ou já morou |
| 4 | **Cliente ou ecossistema em comum** | `empresa`, `empresas_anteriores`, `empresa_setor` | Trabalhou em conta que o usuário atendeu, ou no mesmo ecossistema |
| 5 | **Trajetória espelhada** | `historico_gtm`, `cargos_gtm_anteriores`, `icp_origem` | Fez o mesmo movimento de carreira que o usuário |
| 6 | **Aluno / comunidade em comum** | `about`, `education[]`, `experience[]` | Passou pelo mesmo curso ou já está na comunidade do usuário |
| 7 | **Interesse temático** (fallback) | `headline`, `about`, `top_skills` | O mais fraco. É o que os templates da matriz já cobrem |

### Trajetória do usuário para bater contra o lead

Use SOMENTE o que estiver na seção "Sobre você" de `brand/voice-outbound.md` (empresas, clientes atendidos, formação, geografia, comunidades). Nunca inventar experiência, cliente ou número que não esteja lá.
**Cuidado:** não afirme profissão ou formação que você não tem. Se o usuário não é da mesma área do lead, o terreno comum verdadeiro é o tema (dados, IA, vendas) e a trajetória, não a profissão.

### Como usar o sinal encontrado

Ele substitui a primeira frase do template, não se soma a ela. A mensagem continua de 1 a 3 linhas.

- Sinal 1: "Opa [NOME], tudo bem? Vi que vc tb passou pela [EMPRESA]. Trabalhei lá uns anos atrás. Bora conectar?"
- Sinal 2: "Opa [NOME], tudo bem? Vi que vc estudou na [FACULDADE] tb. Sempre bom achar gente da casa."
- Sinal 3: "Opa [NOME], tudo bem? Vi que vc tá em [CIDADE]. Moro aqui tb rs. Sempre bom conectar com quem curte o mesmo assunto."
- Sinal 5: "Opa [NOME], tudo bem? Vi que vc veio de vendas e hoje tá do lado técnico. Fiz um caminho parecido, só que ao contrário. Bora trocar ideia?"

Se nada de 1 a 6 aparecer, use o template da célula (origem × senioridade) sem culpa. Sinal fraco bem escrito é melhor que sinal forte inventado.

---

## Regra três: língua da mensagem

**A língua é a do PERFIL do lead, nunca a do país nem a do nome próprio.**

Detecte lendo o `about` e a `headline` no LinkedIn:

- Escrito em PT, ES, FR ou EN → escreva nessa mesma língua.
- Qualquer outra língua → escreva em EN.
- **Bio bilíngue** (metade nativa + metade em inglês, padrão comum): identifique as duas metades separadamente. Se for X + EN, use **X**, a língua nativa. Inglês na bio quase sempre é vitrine para recrutador, não preferência de conversa.

Nunca inferir por país (`pais`), por nome próprio ou por sede da empresa. Brasileiro com bio em inglês morando em Portugal pode ser qualquer uma das três coisas: quem decide é o texto que ele escreveu.

## Regra quatro: registro por interlocutor (regra de ouro operacionalizada)

Duas versões de cada mensagem, sempre. O `voice-outbound.md` diz "mais formal com mulheres e com quem for mais formal" — aqui está o que isso significa na prática.

### Registro SOLTO (padrão)

Vale "Opa", "mestre", "cara", "po", "rs" (preferir a "hahaha"), "vc", "tb", "pq", typo ocasional.

### Registro POLIDO

**Proibido: "Opa", "mestre", "cara", "po", "pow", "kkk".**

- Abrir com "Oi [NOME], tudo bem?" ou "Olá [NOME], tudo bem?"
- "rs" só se ela usar primeiro
- Contrações leves seguem valendo (vc, tb, pq). Polido não é corporativo: continua sendo WhatsApp, não e-mail de banco
- Frase um pouco mais completa, menos gíria, mesma leveza

Comparação na mesma célula (Vendas/Pleno):

| Solto | Polido |
|---|---|
| Opa [NOME], tudo bem? Vi que vc acompanha os mesmos temas... | Oi [NOME], tudo bem? Vi que vc acompanha os mesmos temas... |
| ...e curto ver como quem tá na linha de frente aplica isso. | ...e gosto de ver como quem está na linha de frente aplica isso. |

### Como escolher o registro (ordem de precedência)

1. **Nome próprio é o método primário.** Primeiro nome feminino → registro POLIDO. Primeiro nome masculino → registro SOLTO. É o sinal que existe em 100% da base, e no Brasil acerta na esmagadora maioria.
2. **Pronomes declarados no perfil sobrescrevem o nome.** Muita gente põe no campo próprio do LinkedIn, no nome ou na headline. Se declarou, o declarado manda.
3. **Nome ambíguo ou estrangeiro que você não conhece** (Alex, Darci, Ariel, nomes asiáticos e africanos que não sabe ler): POLIDO. Não chute.
4. **Depois da primeira resposta, espelhe o registro dela.** Escreveu solto, solte. Escreveu formal, mantenha formal. A partir da segunda mensagem isso vence tudo que veio antes, inclusive o nome.

**Salvaguarda de escrita:** construa a frase sem concordância de gênero ("tudo bem?", "vi que vc acompanha", "sempre bom conectar"). Assim, se a inferência pelo nome errar, o efeito é só de formalidade, nunca de tratar a pessoa pelo gênero errado dentro do texto. Evite "bem-vindo/bem-vinda", "obrigado/obrigada" e adjetivos flexionados na primeira mensagem.

## Regra cinco: humanizar antes de enviar

Toda mensagem passa por humanização como último passo, depois de escrita e antes de ir pro lote:

- Mensagem em **PT-BR** → skill `humanize-pt-br`
- Mensagem em **EN** → skill `humanize-en`
- **ES / FR** → não existe skill de humanização. Revisar manualmente contra os mesmos vícios (travessão, regra de três, vocabulário de IA, paralelismo negativo) e sinalizar ao o usuário que a revisão foi manual.

Em lote isso importa mais do que em mensagem avulsa: 200 convites com a mesma estrutura sintática viram padrão detectável mesmo quando cada um foi personalizado. A humanização é o que quebra a assinatura.

Ordem completa da fabricação: buscar sinal (regra dois) → escolher língua (regra três) → escolher registro solto/polido (regra quatro) → escrever sobre o template da célula → `humanize-pt-br` / `humanize-en` → checklist.

## Checklist antes de mandar qualquer mensagem

- [ ] `voice-outbound.md` carregado
- [ ] Busca de sinal 1 a 7 feita PARA ESTE LEAD, não para o segmento
- [ ] Língua detectada do `about`/`headline` do lead, não do país nem do nome
- [ ] `humanize-pt-br` (ou `humanize-en`) rodado sobre o texto final
- [ ] Nota de conexão ≤ 300 caracteres (teto real do LinkedIn em todos os planos), **alvo de 180** — notas de 120-180 performam melhor. Contar com o nome real, testando o mais longo do lote
- [ ] 1 a 3 linhas. Máximo 600 caracteres em DM
- [ ] Uma pergunta só, aberta, nunca de sim/não
- [ ] Zero emoji, zero travessão, zero jargão de conteúdo
- [ ] Nada inventado: empresa, cliente, número, experiência
- [ ] Registro escolhido (solto/polido). Se polido: nenhum "Opa", "mestre", "cara", "po"
- [ ] Registro definido pelo primeiro nome (pronome declarado no perfil sobrescreve; nome ambíguo → polido)
- [ ] Frase sem concordância de gênero, pra erro de inferência não virar erro de tratamento
- [ ] Nenhuma menção à origem da lista (de qual post ou de quem a pessoa veio)
- [ ] Nada de venda. A cadência é conectar → contexto → valor → comunidade

## Anti-padrões que já queimaram mensagem

| Não escreva | Por quê |
|---|---|
| "Documento o que quebra" / "rodo em produção" / "os erros anotados" | Tique de voz de conteúdo. Repetido em lote, vira robô |
| "Transformo time de dados em gerador de pipeline" | Linguagem de deck. Ninguém abre conversa assim |
| "Aplico stack técnica em Go-To-Market" | Jargão que só faz sentido pra quem já comprou |
| "Seria um prazer conectar e trocar figurinhas sobre o tema" (em toda mensagem) | Vira assinatura detectável em 200 convites iguais |
| Citar de qual post ou de quem o lead veio | Entrega que ele é item de uma lista |
| Exibir senioridade sem enquadrar pertencimento | Pleno lê e pensa "por que esse cara quer falar comigo?" |
| Afirmar uma profissão que não é a sua | Falso e fácil de desmascarar. Fique no terreno comum verdadeiro |
