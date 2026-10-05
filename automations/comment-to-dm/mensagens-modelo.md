# Modelo das 3 mensagens de DM (comment-gate → Nuvia)

Base canônica pra escrever a sequência de qualquer post comment-gate. Adaptar material, palavra-gatilho e oferta; **manter a anatomia**.

Config padrão: LinkedIn DM, sem connection request, sender = sua inbox, stop-on-reply ligado. Variável de primeiro nome da Nuvia: `{{var_contact_f_name}}`.

---

## Mensagem 1 — D0, entrega

**Anatomia:** saudação curta → referência ao comentário → link → o que tem lá dentro → **dica de uso acionável** → pedido de feedback → "Abs".

```
Opa {{var_contact_f_name}}! Tudo bem?
Vi que vc comentou lá no meu post.

Segue o material completo, como prometido: {{link}}

{{uma frase densa listando o que a pessoa vai encontrar, concreto: números, seções, o passo a passo}}

Ahh, {{dica de uso que faz o material render mais: um ajuste, um input que a pessoa pode dar, um jeito de testar}}. Testa aí e me avisa se fez diferença pro seu conteúdo!

Abs
```

Regras aprendidas:
- **Não repetir a palavra-gatilho.** "Vi que vc comentou lá no meu post" > "Vi que vc comentou PALAVRA". A palavra é mecânica da automação, não assunto da conversa.
- "Segue o material" > "Aqui está o material". Menos cerimônia.
- A dica de uso é o que separa entrega de relacionamento. Ela dá um motivo real pra pessoa responder, e a resposta é o que interessa.
- Fechar com pergunta de feedback, nunca com "espero que ajude" sozinho.

## Mensagem 2 — D+1, follow-up + comunidade (só se não respondeu)

**Anatomia:** pergunta sobre o uso → **erro/experiência sua** → convite pra comunidade em forma de pergunta → link.

```
E aí, conseguiu {{usar/rodar/aplicar}} em algum texto seu?

Curioso pra saber {{pergunta específica sobre o resultado}}. No meu é sempre {{o seu próprio tropeço, concreto}}.

Vc já está lá na nossa comunidade? Se quiser trocar ideia de alto nível com quem tá nas trincheiras construindo com IA de verdade, é só chegar:

{{LINK_COMUNIDADE}}
```

Regras aprendidas:
- **Perguntar "vc já está lá na nossa comunidade?" antes de jogar o link.** Não assumir que a pessoa está de fora.
- O erro próprio ("no meu é sempre {{erro seu}}") baixa a guarda e convida à resposta. É o pilar de autoironia aplicado ao outbound.
- Sem "Te vejo lá!" no fim. O link fecha sozinho.

## Mensagem 3 — D+3, oferta (só se não respondeu)

**Anatomia:** "Última coisa:" → ponte do material pro sistema maior → a oferta → **os dois lados que ela serve** → pergunta fechada de baixo atrito.

```
Oi {{var_contact_f_name}}!

Última coisa: {{o material}} é uma peça de um sistema maior que eu uso pra {{o que o sistema faz}}.

{{descreva sua oferta em uma frase: o que é, formato, o que a pessoa constrói}}

Serve pros dois lados: {{benefício A}}, ou {{benefício B}}.

Quer que eu te mande mais informações?
```

Regras aprendidas:
- **Uma ideia por parágrafo.** A versão encadeada ("um sistema maior que... que faz parte de... onde ensino...") perde o leitor no meio.
- "Serve pros dois lados: X, ou Y" em vez de "não só X mas também Y". Paralelismo negativo é um dos padrões que a própria skill de humanização caça. Não escorregar nele.
- Fechar com pergunta de sim/não, nunca com pedido de decisão grande.
- A oferta precisa de ponte com o material que a pessoa acabou de receber. Pitch solto no D+3 queima a sequência inteira.

---

## Filtro antes de mandar pra Nuvia

1. Tem travessão em alguma mensagem? Tira.
2. Tem "não só X, mas Y" / "não é sobre X, é sobre Y"? Reescreve.
3. Tem palavra de vocabulário de IA (essencial, jornada, robusto, potencializar, protagonismo)? Troca.
4. A mensagem 1 tem dica de uso acionável, ou é só entrega?
5. A mensagem 3 faz ponte com o material, ou é pitch solto?
6. Um CTA por mensagem. Nunca empilhar comunidade + oferta no mesmo texto.
