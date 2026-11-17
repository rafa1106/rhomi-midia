# Guia de conteúdo — Instagram @rhomi.tech

Versão 1 · 17/11/2026 · aprovado pelo Rafael. Toda peça (arte + legenda) obedece a este guia. Na dúvida, a regra mais restritiva vence.
Versão para leitura: https://claude.ai/artifact/GNzC2q6LoJzNqeXUzZApSN

## 1. Papel do perfil
Vitrine de credibilidade, não canal de aquisição. Quem chega pela mala direta, pelo site, pelo Google ou pelo WhatsApp abre o perfil para ver se a empresa é séria e está ativa. O perfil precisa parecer atual, de alto padrão e coerente com o site (rhomi.com.br), o folder e os vídeos, e levar ao WhatsApp.

## 2. Marca e posicionamento
- RHOMI é a marca central: "Tecnologia que transforma experiências". Mais de 12 anos.
- Três frentes: **PHILA** (gestão de filas e atendimento, do início ao fim, em nuvem), **OrbitaComet** (o totem do PHILA) e **engenharia sob medida** (hardware e software, do protótipo à produção).
- O PHILA é vendido como solução completa; o OrbitaComet é sempre "o totem do PHILA", nunca um segundo produto. **Nunca escrever "OrbitaComet + PHILA".**
- Público: gestores e donos de lugares onde as pessoas esperam atendimento — clínicas, laboratórios, hospitais, cartórios, bancos, órgãos públicos, instituições de ensino (todos podem aparecer). Secundários: comércio e eventos.
- Dores (palavras deles): "a recepção vira bagunça no horário de pico", "o cliente reclama da espera e eu não sei quanto ele esperou", "o sistema de senha é antigo e trava", "não sei quem atendeu quantos", "trocar parece complicado".

## 3. Rodízio semanal (3 posts, 11h00 de São Paulo = 14:00Z)
| Dia | Pilar | Formato | Conteúdo |
|---|---|---|---|
| **Ter** | PHILA, a solução | Carrossel 6–8 | Um recurso ou etapa por post: emissão (totem, computador, máquina portátil, WhatsApp), filas e prioridades, painel de chamada com voz, painel do atendente, atendimento pelo celular, gestão em tempo real, relatório com IA, Phila Score, personalização |
| **Qui** | OrbitaComet e ambientes | Post único (alternar) ou carrossel 3–5 | Design, LED RGB, tela horizontal ou vertical, impressora com corte, boas-vindas por voz, Wi-Fi e bivolt, frente personalizada, totem em recepções de cada segmento |
| **Sex** | Atendimento na prática | Carrossel 5–7, girando a → b → c | (a) recepção melhor: ideias para organizar a espera, sem número inventado; (b) por segmento: como fica numa clínica, laboratório, cartório, banco, órgão público, ensino; (c) Rhomi: engenharia sob medida, como funciona a implantação |
- Nenhum recurso do PHILA e nenhum segmento se repete em menos de 4 semanas.
- Sem datas comemorativas e sem post genérico de motivação.

## 4. Identidade visual (o `gerador/render.py` já aplica)
- 1080 × 1350, JPEG. Fundo grafite #161619 com grão sutil. Laranja #F7A600 só como acento (uma palavra, número, fio ou ponto). Nunca fundo laranja chapado, nunca texto branco sobre laranja.
- Títulos Poppins 300 com destaque `<em>` em laranja; rótulo em Inter 500 caixa alta com ponto laranja; corpo Inter.
- Logos contorno B. Capa: logo RHOMI (ou PHILA nos posts do PHILA). Slides internos: símbolo + @rhomi.tech + "NN / NN". Slide final: `final()` ou `final(phila=True)`.
- Quebras de linha à mão com `<br>`: nenhuma palavra sozinha na última linha.
- Layouts disponíveis: `capa_foto`, `capa_texto`, `foto_texto`, `foto_cheia`, `tela` (captura num monitor, com `zoom`), `celular`, `texto` (com `num` grande ou `foto` de fundo), `lista`, `final`, `unico`, `vitrine`, `html_livre`. Modelos: os geradores `p1124*` a `p1208*`.

## 5. Regras de imagem (do Rafael, 17/11) — obrigatórias
- **Use só imagens de `fontes/img/` e consulte `fontes/inventario.json`** (campo `tela`): `ok` = sem tela ou tela desligada; `tela` = interface de render ou composição; `ia` = tela feita por IA, use só com o totem pequeno no quadro ou corte que não mostre o texto da tela; `nao_usar` = proibido.
- **Horizontal × vertical:** sempre `o15-horizontal-e-vertical-tela-desligada-1200` (tela desligada). Nunca `o15-*-ourela`, `-valoren` ou `lp08`.
- **Frentes personalizadas:** só `frente_*` (as 8 artes aprovadas do site: Lumivida, Ourela, Águas Serenas, Essenza, Valoren, Cartório, PHILA, Bem-vindo), compostas por `automacao/compor_frente.py`. Nunca o mockup `adesivacao`.
- Não redesenhar nem gerar o totem. Não usar imagens de fora do repositório.
- Interfaces: usar as capturas reais (`p14-*`, `if_*`), com os dados fictícios da Clínica Lumivida. Senha da história: NR004 (Nutrição · Retorno), Guichê 1; no painel da TV também aparece CN023, Guichê 3.

## 6. Fatos permitidos
**PHILA:** em nuvem, gestão pelo computador ou celular · 4 formas de emitir senha (totem; computador da recepção, com senha impressa ou enviada pelo WhatsApp; máquina portátil; WhatsApp do próprio cliente) · filas por serviço e tipo de senha, com prioridades · painel na TV com alerta sonoro e chamada por voz (vozes Camila, Thiago, Vitória) e espaço para campanhas e avisos · painel do atendente: chamar a próxima, chamar fora da ordem, alertar de novo, não compareceu, pausar, cancelar (não existe "transferir") · atendimento pelo celular (Attend) · gestão em tempo real, desempenho por atendente e serviço, relatório com IA, alertas · Phila Score integrado em tempo real · personalização de telas, cores, voz e senha (logo, QR code).
**OrbitaComet:** tela touch Full HD 15,6", horizontal ou vertical, com ajuste de inclinação · impressora térmica com corte automático · iluminação RGB nas cores da marca · sensor de presença com boas-vindas por voz · Wi-Fi, bivolt automático, alto-falante, estrutura em aço · frente personalizável.

## 7. Proibido
- Números sem fonte ("reduz a espera em 30%"), "nº 1", prazos de implantação, preços e condições comerciais (a campanha de R$ 99 não entra no Instagram).
- Clientes, logos, depoimentos ou instalações fictícios; imagem de IA apresentada como instalação real.
- Marca/modelo do monitor, "Suporte Terminal", troca de bobina pela porta traseira, "linha Órbita", "OrbitaComet + PHILA", logos antigos, concorrentes pelo nome.
- Prometer resposta por direct ou "comente X que eu mando".

## 8. Legenda
- 380–700 caracteres. 1ª linha = gancho que funciona sozinho (o Instagram corta em ~125). Depois 2–3 frases que não repetem os slides, a chamada e as hashtags.
- Chamada: "Fale com a gente no WhatsApp: link na bio." Em carrosséis úteis: "Salve para mostrar para a sua equipe."
- Se houver cena de IA: linha "Imagens ilustrativas." (ou "Imagem ilustrativa."). Se houver marcas dos mockups: "Marcas fictícias, criadas para demonstração."
- 4–6 hashtags no fim. Base: #gestaodeatendimento #gestaodefilas #totemdeautoatendimento #experienciadocliente; +1–2 de segmento (#clinicas #laboratorio #cartorio #setorpublico) ou #phila / #orbitacomet.
- Tom: especialista calmo e seguro; benefício em linguagem de cliente leigo; sem euforia.

## 9. Checklist antes de agendar
1. Rodízio e "não repetir em 4 semanas" respeitados?
2. Toda imagem tem `tela` = ok/tela no inventário (ou `ia` com a tela fora de foco/pequena)? Nenhuma `nao_usar`?
3. Texto sem corte, sem sobreposição, sem palavra órfã, contraste bom (folha de contato vista)?
4. Só fatos da seção 6? Nada da seção 7?
5. Legenda no tamanho, com gancho, chamada, avisos de IA/marcas e hashtags?
