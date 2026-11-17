# rhomi-midia

Artes, geradores e automação do Instagram **@rhomi.tech**. Gerido pelo Claude para a RHOMI.

- `estrategia/guia_conteudo.md` — regras de conteúdo e imagem (leitura obrigatória antes de criar posts).
- `estrategia/automacao.md` — como a fila do Make, a GitHub Action e a rotina se conectam.
- `gerador/` — um arquivo por post (`pMMDD_tema.py`), com a legenda; `render.py` é o motor (Playwright).
- `fontes/img/` + `fontes/inventario.json` — imagens-base permitidas e o estado da tela do totem em cada uma.
- `artes/` — JPEGs publicados (as URLs raw daqui são as que o Instagram baixa).
- `destaques/` — stories dos destaques fixados, capas e foto de perfil.
