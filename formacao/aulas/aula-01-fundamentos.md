# Aula 01 — Fundamentos, skills e loops

**Data:** 05/10/2026  
**Duração:** aproximadamente 2h47  
**Tipo:** aula inaugural, com teoria e prática  
**Fonte:** síntese de transcrição automática, revisada para corrigir termos e remover dados pessoais.

## Objetivo da aula

Apresentar o papel do GTM Engineer, explicar a arquitetura básica de uma máquina de GTM operada por IA e conduzir a turma da execução de um prompt isolado até a criação de uma skill reutilizável e de um loop de melhoria.

Ao final da aula, o aluno deveria compreender a progressão:

```text
prompt isolado
  -> prompt estruturado
  -> processo repetível
  -> skill
  -> loop com controle de qualidade
```

## Principais aprendizados

### 1. Distribuição é uma vantagem competitiva

Produtos e funcionalidades estão cada vez mais fáceis de reproduzir. O diferencial tende a migrar para capacidades menos copiáveis:

- dados proprietários;
- pessoas e conhecimento operacional;
- estratégia e execução de go-to-market;
- distribuição previsível;
- sistemas que aprendem com os resultados.

O produto continua importante, mas construir deixou de ser suficiente. É necessário criar uma máquina capaz de encontrar o mercado, priorizar oportunidades e distribuir a oferta de forma consistente.

### 2. O GTM Engineer trabalha sobre o sistema inteiro

GTM Engineering reúne competências que antes ficavam separadas entre marketing, vendas, produto, RevOps e dados.

| Disciplina | Unidade de atenção mais comum |
|---|---|
| Outbound | lead e mensagem |
| ABM | conta e stakeholders |
| RevOps | processo, CRM e saúde do funil |
| GTM Engineering | sistema de ponta a ponta |

O GTM Engineer não cuida apenas de uma sequência ou de um dashboard. Ele conecta dados, sinais, automações, IA, copy e canais para responder à pergunta: **como fazer esse sistema operar, aprender e escalar?**

### 3. O fluxo de GTM começa no ICP

O processo apresentado na aula segue esta lógica:

```text
hipótese de ICP
  -> sourcing
  -> enriquecimento
  -> sinais e contexto
  -> qualificação e priorização
  -> mensagem personalizada
  -> execução por canal
  -> medição
  -> aprendizado e nova iteração
```

O ICP precisa ser traduzido em critérios verificáveis. Campanhas também servem como experimentos para descobrir se o problema está no público, no momento, no canal, na oferta ou na mensagem.

Fontes de sourcing citadas incluem LinkedIn, Google Maps, comunidades, grupos, fóruns e eventos. O enriquecimento adiciona contexto sobre empresa e pessoa, como expansão, troca de liderança, captação, mudança de emprego e adoção de ferramentas.

### 4. O modelo é apenas o motor

Um modelo potente, sozinho, não constitui um bom sistema. O conjunto que envolve o modelo foi apresentado como o **harness**.

Componentes relevantes:

- **Instruções:** regras gerais e prompts do projeto.
- **Memória:** contexto da sessão e informações preservadas entre conversas.
- **RAG:** recuperação seletiva de trechos de documentos, evitando carregar tudo no contexto.
- **Tools:** ferramentas que permitem à IA agir, e não apenas responder.
- **MCP:** protocolo usado para conectar o agente a ferramentas e contas externas.
- **Conectores de dados:** acesso a bancos e fontes estruturadas.
- **Guardrails:** limites de entrada, saída e comportamento.
- **Skills:** processos empacotados e reutilizáveis.
- **Subagentes:** papéis especializados que podem executar skills.
- **Hooks:** ações disparadas automaticamente por eventos.

Uma ideia central da aula foi que um modelo menor, envolvido por um harness bem construído, pode superar um modelo mais potente sem contexto, ferramentas ou processos adequados.

### 5. Contexto precisa ser administrado

Conversas longas acumulam instruções, respostas e arquivos. Excesso de contexto pode aumentar consumo e reduzir a precisão.

Práticas recomendadas apresentadas:

- manter as instruções do projeto em arquivos Markdown;
- separar referências grandes em documentos específicos;
- usar recuperação seletiva quando possível;
- compactar conversas longas;
- configurar um limite para compactação automática;
- iniciar uma conversa limpa ao comparar prompts, evitando contaminação pelo histórico;
- revisar o plano antes de liberar tarefas complexas ou autônomas.

### 6. Prompts estruturados são mais previsíveis

A turma comparou uma instrução simples com versões progressivamente mais estruturadas.

Blocos recomendados:

- papel;
- contexto;
- dados de entrada;
- tarefa;
- regras;
- restrições;
- exemplos;
- formato de saída;
- critério de qualidade.

Markdown funciona bem para instruções curtas e médias. XML pode ser útil em prompts longos, pois deixa explícito onde cada bloco começa e termina.

Para proibições, a recomendação foi não depender apenas de frases como “não faça”. É mais eficaz mostrar a substituição desejada:

```text
Em vez de: “Admiro sua trajetória...”
Use: um sinal concreto do perfil e uma pergunta natural sobre aquele contexto.
```

Exemplos de entrada e saída ajudam o modelo a abstrair o padrão esperado.

## Parte prática

### Exercício 1 — Linha de base

Criar uma nota de conexão do LinkedIn a partir do print de um lead, com pouca instrução, para estabelecer o resultado inicial.

Objetivo: observar o comportamento zero-shot e guardar uma referência de comparação.

### Exercício 2 — Prompt estruturado

Repetir a tarefa em uma conversa nova, usando o mesmo lead e um prompt organizado por papel, contexto, tarefa e regras.

Regras discutidas:

- escrever como conexão, não como pitch;
- evitar linguagem robótica ou excessivamente comercial;
- usar um sinal verdadeiro do perfil;
- respeitar o limite de caracteres do LinkedIn;
- terminar com uma pergunta que valha a pena responder;
- comparar o resultado com a linha de base usando o mesmo lead.

### Exercício 3 — Template Master

Adicionar mais contexto sobre pessoa, empresa, solução e objetivo. Quando faltarem informações, instruir o modelo a fazer perguntas antes de executar.

O foco foi separar descoberta e execução: primeiro preencher o contexto necessário; depois produzir a mensagem.

### Exercício 4 — Skills fornecidas

Foram apresentadas três skills:

- `humanize-pt-br`: remove padrões comuns de texto gerado por IA;
- `brand-voice-enforcement`: cria e aplica regras de tom de voz;
- `grand-slam-offer-builder`: estrutura ofertas com base na metodologia de ofertas de alto valor.

Regra operacional: uma skill com referências deve ser distribuída como um ZIP contendo a pasta daquela skill. Não se deve agrupar várias skills diferentes dentro do mesmo ZIP.

### Exercício 5 — Criar a skill `nota-de-conexao`

Empacotar o processo desenvolvido durante a aula em uma skill reutilizável.

A versão final deve combinar:

- estrutura do prompt validado;
- regras de tom de voz;
- uso de sinais concretos do lead;
- limites do canal;
- aplicação de `humanize-pt-br` no resultado;
- exemplos positivos e negativos.

### Exercício 6 — Transformar a skill em loop

Executar a skill, avaliar o resultado e gerar uma nova versão até que os critérios de qualidade sejam atendidos.

Arquitetura sugerida:

```text
agente executor
  -> produz a nota
agente avaliador
  -> compara com os critérios
aprovado?
  -> sim: entrega
  -> não: devolve feedback e inicia nova iteração
```

O avaliador deve ser separado do executor sempre que a tarefa justificar uma auditoria independente.

Todo loop precisa de um ponto de parada explícito. Exemplo: no máximo três ou cinco iterações. Isso evita repetição infinita e consumo descontrolado.

## Critérios iniciais para a nota de conexão

1. Usa um sinal real e específico do perfil.
2. Soa como uma conexão natural, não como uma venda.
3. Explica implicitamente por que a conexão faz sentido.
4. Evita elogios genéricos e vícios de texto de IA.
5. Respeita o limite do canal.
6. Termina com uma pergunta simples e relevante, quando isso melhorar a resposta.
7. Não inventa informações sobre o lead ou a empresa.

## Ferramentas apresentadas

| Ferramenta | Papel na formação |
|---|---|
| Claude Code | Ambiente principal para operar arquivos, skills, scripts e integrações |
| GitHub | Versionamento e colaboração sobre a máquina de GTM |
| Clay | Sourcing, enriquecimento e organização de fluxos |
| Apify | Scraping e automação de coleta de dados |
| Firecrawl | Busca, scraping e extração de conteúdo web |
| Nuvia | CRM, campanhas, canais e agentes conversacionais |
| Oxygen | Infraestrutura e execução de prospecção por e-mail |

As ferramentas são meios, não o objetivo final. A arquitetura do processo deve continuar compreensível mesmo que uma ferramenta seja substituída.

## Entregáveis da Aula 01

- repositório próprio da formação criado;
- linha de base da nota de conexão;
- versão com prompt estruturado;
- skills da aula instaladas;
- documento de tom de voz iniciado;
- skill `nota-de-conexao` criada;
- desenho do loop de qualidade.

## Tarefa para casa

Prioridade principal:

- concluir o documento de tom de voz com exemplos reais e revisá-lo com cuidado.

Demais tarefas:

- criar ou revisar a skill `nota-de-conexao`;
- aplicar `humanize-pt-br` ao resultado;
- definir critérios objetivos de aprovação;
- transformar a skill em um loop com limite de iterações;
- testar com outro lead;
- manter credenciais e dados pessoais fora do GitHub.

## Situação deste repositório após a aula

- Repositório próprio criado e publicado no GitHub.
- MCPs de Nuvia, Apify e Firecrawl configurados e testados.
- Documentação evolutiva da formação iniciada.
- Documento de tom de voz, skill personalizada e loop ainda pendentes.

## Próxima aula

A Aula 02 entra em sourcing: definição operacional do ICP, conexão de ferramentas via MCP e geração da primeira lista real de leads.

