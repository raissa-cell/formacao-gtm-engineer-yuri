# AutoDM keepalive

## Causa raiz

A Upload Post documenta os monitores de AutoDM (`POST /api/uploadposts/autodms/start`)
como "run in the background 24/7 — no need to keep polling manually". Isso não bate com
o observado: a thread do monitor morre e o `status` fica em `resuming`, que a própria
doc define como *"monitor was active in DB but no live thread; one was just started"*.

Ou seja: sem uma chamada externa periódica pra API deles, comentários com a
palavra-gatilho ficam sem resposta por horas (confirmado em produção: comentário às
27/08 20:11, DM só saiu às 28/08 11:40, quando alguém finalmente chamou `GET
/autodms/status` — 15h30 de atraso, bem acima do `monitoring_interval` de 15 min
configurado).

## Fix

`ping_autodm_monitors.py` chama `GET /api/uploadposts/autodms/status` a cada 15 min via
launchd (`com.exemplo.autodm-keepalive.plist`, `StartInterval=900`), forçando a Upload Post a
religar a thread do monitor sempre que ela cair. Roda 100% independente do Claude Code
ou de qualquer app aberto — mesma lógica do `com.exemplo.comment-to-dm.*` (runtime vive em `~/gtm-automation`, nunca no Desktop: o macOS bloqueia o launchd em `~/Desktop`).

Log: `~/gtm-automation/autodm_keepalive.log`.

## Deploy

```bash
cp ping_autodm_monitors.py ~/gtm-automation/
cp com.exemplo.autodm-keepalive.plist ~/Library/LaunchAgents/
launchctl unload ~/Library/LaunchAgents/com.exemplo.autodm-keepalive.plist 2>/dev/null
launchctl load ~/Library/LaunchAgents/com.exemplo.autodm-keepalive.plist
```

Chave `UPLOAD_POST_API_KEY` lida do `.env` já existente em `~/gtm-automation/.env`.

Isso cobre **todos** os monitores AutoDM ativos da conta de uma vez (não é por post) —
não precisa duplicar a automação a cada novo comment-gate no Instagram.
