# Automação do Instagram @rhomi.tech — como funciona (v1 · 17/11/2026)

Mesmo desenho do @pontua.club (repo `rafa1106/pontua-midia`), dividindo a fila e o publicador do Make com ele.
Tudo roda na nuvem; não depende do PC do Rafael.

```
Rotina do Claude (seg e qui 07:51 SP)           GitHub Action "renderizar fila"           Make "publicar fila" (compartilhado)
 cria o post, renderiza, faz QA ──► Make ──►   pede pendentes (fila=renderizar_rhomi),  ──►  publica ter/qui/sex 11:00 SP
 grava status "renderizar_rhomi"   data store  renderiza, commita, confere as URLs,          na conta @rhomi.tech (campo conta)
 + código do gerador               (154610)    avisa a ponte → status "agendado"
```

| Peça | Onde | O que faz |
|---|---|---|
| Rotina de conteúdo | Tarefa programada do Claude "rhomi · conteúdo do Instagram", **seg e qui 07:51 SP** | Mantém posts para os **próximos 15 dias** nos dias ter/qui/sex 11:00 SP (14:00Z). Cria, renderiza, faz QA visual e grava no Make. Se tiver permissão de push, publica direto e grava `agendado`; senão grava `renderizar_rhomi` + código no campo `gerador`. Envia ao Rafael o resumo e a página de revisão. |
| Fila | Make · data store `pontua_fila_instagram` (154610), **compartilhado** | Registros da Rhomi têm `conta: "rhomi"`. Sem `conta` = pontua. Status: `renderizar_rhomi → agendado → publicado`, ou `erro_render` / `erro` / `pausado` / `removido`. `_rotina_log_rhomi` = log da última execução da rotina. |
| Ponte | Make · cenário 6780455 (webhook) | `acao=pendentes&fila=renderizar_rhomi` devolve o próximo post da Rhomi; `acao=pronto` → `agendado`; `acao=falhou` → `erro_render`. Sem `fila`, atende o pontua como antes. |
| Renderização/hospedagem | `.github/workflows/renderizar.yml` + `automacao/render_fila.py` (todo dia 06:27 SP e seg/qui 08:47, 10:47, 14:47 SP) | Renderiza com o mesmo código, commita `artes/`, `gerador/`, `fontes/inventario.json`, espera as URLs `raw.githubusercontent.com` e avisa a ponte. |
| Publicador | Make · cenário 6350969 (a cada 30 min, 08h–13h SP), **compartilhado** | Publica 1 post vencido por execução. Rotas separadas por `tipo` (carrossel, imagem, reel) e por `conta` (rhomi → conta 17841462846161056; demais → pontua). |
| Vídeos de Reels | Branch órfã `reels` | `https://raw.githubusercontent.com/rafa1106/rhomi-midia/reels/reel_NN.mp4` (H.264 ≤4,5 Mbps, AAC 128k 48 kHz, faststart). |

## Regras da fila compartilhada
- Toda escrita da Rhomi leva `conta: "rhomi"` e key começando com `p` (posts) ou `r` (reels). A rotina da Rhomi **nunca** altera registros sem `conta: "rhomi"`; a do pontua ignora os que têm.
- O publicador pega 1 post por execução (a cada 30 min). Em dia com post do pontua (09:00) e da Rhomi (11:00) não há conflito.

## Limites e custos
- Make Free: 2 cenários e 1 data store (por isso tudo é compartilhado), 1.000 operações/mês. A Rhomi soma cerca de 40–60 operações/mês.
- Conexão do Instagram no Make (`pontua-instagram`, id 11223462) vale para as duas contas e **vence a cada ~60 dias** (atual: 16/01/2027). Renovar: make.com → Credentials → Connections → pontua-instagram → Reauthorize, mantendo as duas contas marcadas.

## O que só o Rafael faz
- Renovar a conexão (a rotina avisa 15 dias antes).
- Segurar um post: no data store, mudar `status` para `pausado` antes das 11h do dia.
- Responder comentários e direct (a conexão não tem permissão de ler comentários).
- Destaques fixados e figurinha de link: só pelo app.
