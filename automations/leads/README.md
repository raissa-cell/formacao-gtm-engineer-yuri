# Triagem de ICP — padrão para TODOS os leads

`triagem_icp.py` é a classificação oficial de lead deste projeto. **Todo lead que entra, de qualquer post ou campanha, passa por aqui antes de virar campanha de outbound.** O ICP não é julgamento improvisado por post: é este vocabulário, calibrado com o seu mercado e revisado à mão. Ajuste as regex de `triagem_icp.py` ao SEU ICP.

## O que ele faz

Cruza o `processed.csv` do post com o export de conexões do LinkedIn e devolve, por lead: se é conexão, desde quando, empresa, cargo, headline, **nível hierárquico**, **ICP** e o **engagement_score** vindo do ledger.

```bash
python3 "automations/leads/triagem_icp.py" \
  --pasta "campaigns/<publico>/conteudo/AAAA-MM/<post>/signals" --prefixo <xxx>
```

Saída: `<prefixo>_conectados.csv` e `<prefixo>_nao_conectados.csv` na pasta do post, ordenados por nível e depois por score.

- `--conexoes` é opcional: sem ele, usa o **export mais recente** de `Connections*.csv` na raiz do projeto. A base envelhece rápido (186 conexões novas entre 16/08 e 17/08), então exportar de novo do LinkedIn antes de campanha grande.
- `--prefixo` default vem do nome da pasta do post.

## Etapa 2 obrigatória: gravar os campos na Nuvia

A triagem só produz CSV. **Os campos não chegam na Nuvia sozinhos** — `POST /contacts` não
persiste `job_title`, só grava por PUT depois de criado. Então, logo depois da triagem:

```bash
python3 "automations/leads/preencher_campos.py" \
  --csv "<pasta>/<prefixo>_conectados.csv" --csv "<pasta>/<prefixo>_nao_conectados.csv"
```

De-para gravado (fonte: `Automations/comment-to-dm/runbook-segmentacao.md`):

| CSV | Nuvia | Tipo |
|---|---|---|
| `nome` | `name` | nativo |
| `slug` | `linkedin_identifier` | nativo |
| `headline` | `job_title` | nativo |
| `cargo` | `cargo-do-lead` | custom de contato |
| `icp` | `icp` | custom de contato |
| `score` | `engagement-score` | mantido pelo `score_engagement.py`, **não tocar** |
| — | `post-interacao` | acumula, **nunca sobrescrever** |

Escrita de campo custom é por **slug**, leitura volta por **título** (grava `icp`, lê `ICP`;
grava `cargo-do-lead`, lê `Cargo do lead`). O script limpa as duas grafias antes do PUT e
preserva `post-interacao` e `engagement-score`. É idempotente: quem já está correto volta como `ok`.

Exemplo de saída de uma rodada: 95 gravados, 10 já corretos.

## Vocabulário de ICP

Ordem importa, a primeira que casar vence:

| ICP | Pega |
|---|---|
| **Growth** | growth, demand gen, revops, aquisição, gtm, go-to-market |
| **Produto** | product manager/owner/lead, CPO, PO, gestão de produtos (PMM **não** entra: é Marketing) |
| **Dados** | data science, analytics, BI, engenheiro de dados, ML, estatística |
| **Tech** | dev, software engineer, devops, CTO, tech lead, IA, automação |
| **Vendas** | SDR, BDR, inside sales, AE, comercial, closer, new business, customer success |
| **Marketing** | marketing, mídia paga, tráfego, social media, conteúdo, branding, SEO, ads |
| **Fora** | nada acima |

Nível: C-level, Diretoria, Gerência, Consultor, Outro.

## Por que a separação conectado / não conectado importa

Muda a campanha inteira, não só a lista. Conectado recebe DM direta; não conectado precisa de connection request, e a conversa só começa depois do aceite, o que pode levar dias. As duas sequências são diferentes — a M3 da sequência de não conectados deve ser personalizada por ICP (Vendas, Marketing, Growth).

## Exclusões fixas

`{{seu-slug}}` e outros slugs seus, amigos e testes. Testes e amigos nunca entram em campanha. Editar a constante `EXCLUIR` no script.

## Revisão manual: como funciona e onde escorrega

`icp_manual()` lê os CSVs já gerados e **preserva** o que estiver na coluna `icp`, para que rodar de novo não apague correção humana. Efeito colateral: na **primeira** rodada de um post novo, o resultado do regex vira "manual" na rodada seguinte, mesmo sem ninguém ter revisado. Então a revisão do lote novo tem que acontecer logo depois da primeira execução, olhando a lista que o script imprime como `leads NOVOS (icp por regex, precisa revisao manual)`.

## Autoteste

`demo()` roda antes do main e trava os casos que já deram errado: PMM classificado como Produto, "growth product manager" caindo em Produto em vez de Growth, "sócio consultor" como C-level.

## Histórico

Nasceu como `triagem.py` dentro de `signals/` do post McKinsey Storytelling. Movido para cá em 24/08/2026 e parametrizado por `--pasta`, quando virou padrão de todos os posts.
