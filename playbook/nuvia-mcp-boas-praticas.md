# Nuvia MCP — Boas Práticas

Aprendizados operacionais de uso do MCP da Nuvia (CRM), consolidados em campanhas reais. Consultar antes de qualquer upload em massa de contatos/listas.

## Antes de qualquer operação de escrita

- Rodar `whoami` primeiro pra confirmar o tenant autenticado (userId/companyId/companyName) — evita escrever na conta errada.
- `create_list` **não deduplica por nome**: chamar duas vezes com o mesmo nome cria duas listas. Sempre confirmar com o usuário antes de criar (nome, `object_type`, colunas) — não há como desfazer criando de novo com o nome certo, fica lista duplicada.
- Antes de `add_records`, rodar `get_list` pra pegar as **chaves (UUID) das colunas** — `add_records` espera `data` por chave de coluna, não por nome.

## Campo `phone_number` é obrigatório

`create_contact`/`create_contacts` exigem `phone_number`, mas boa parte dos leads enriquecidos via scraping/Apify não tem telefone real (só e-mail). Convenção acordada com o usuário: usar **IDs sequenciais placeholder** a partir de `990001123` (não é um número real, é só pra satisfazer o schema) — leads que já tinham telefone real do enriquecimento mantiveram o valor verdadeiro. Documentar esse padrão sempre que a base não tiver telefone confiável; não inventar número plausível (evita futuro disparo acidental de WhatsApp/SMS pra número real de terceiro).

## Limites de lote

- `create_contacts`: máximo 100 contatos por chamada. Falha é parcial (`failed: [{index, reason}]`) — só re-tentar os que falharam, não o lote inteiro.
- `add_records` em listas: o limite formal é 100, mas quando a coluna carrega texto longo (ex: copy de outbound de 3 mensagens por lead), o payload por chamada fica grande — preferir lotes de **~25** pra evitar timeout. É idempotente por `contact_id`/`business_id`: registros já presentes voltam em `skipped`, então é seguro re-tentar uma chamada que falhou.

## Capturar IDs da resposta, não inferir

Ao criar contatos em massa e precisar depois vincular cada um a um registro de lista (ex: contato → suas 3 mensagens), **sempre extrair o `id` direto da resposta de `create_contacts`** (o array `created` preserva a ordem do input). Não inferir/reconstruir IDs por incremento hexadecimal sobre o primeiro ID retornado — MongoDB ObjectId não garante incremento estritamente sequencial por item em todos os cenários; funcionou nesta sessão porque as chamadas foram sequenciais e de baixa concorrência, mas é uma prática frágil e não deve virar padrão. O jeito certo é sempre mapear pelo campo estável do input (ex: `phone_number` ou `linkedin_identifier`) contra o `id` retornado na mesma resposta.

## Trabalho em escala (centenas de registros)

Para volumes grandes (centenas de contatos + registros com payload grande), dividir em lotes e processar com subagentes em paralelo (via Workflow) acelera bastante — mas cada subagente precisa carregar a ferramenta certa via `ToolSearch` (`select:mcp__.../add_records` etc.) antes de chamar, já que as ferramentas MCP chegam deferridas por padrão.
