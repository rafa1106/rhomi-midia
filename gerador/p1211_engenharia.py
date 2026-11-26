# Sexta 11/12: atendimento na prática (c), Rhomi: engenharia sob medida. Carrossel 7.
from render import *

LEGENDA = """Quando o equipamento que você precisa ainda não existe, ele pode ser projetado.

Na RHOMI, a engenharia sob medida trata hardware e software como um projeto só: entender o uso real, conceber a solução, desenvolver placa, firmware e sistema, testar o protótipo e levar à produção.

Tem uma ideia de produto para tirar do papel? Fale com a gente no WhatsApp: link na bio.

Imagens ilustrativas.

#engenhariaeletronica #desenvolvimentodeproduto #hardware #tecnologia #rhomi"""

S = [
    capa_foto("e01-abertura-2560", "Engenharia sob medida", "Quando o produto<br>que você precisa<br><em>ainda não existe.</em>",
              "Hardware e software sob medida,<br>do protótipo à produção.", pos="40% 50%"),
    foto_texto("e02-etapa-1-entendimento", "Etapa 1 · Entendimento", "Tudo começa pelo<br><em>uso real.</em>",
               "Antes de desenhar, entendemos onde o produto vai trabalhar e quem vai usar.", pos="50% 50%"),
    foto_texto("e02-etapa-2-esquema", "Etapa 2 · Concepção", "A ideia vira<br><em>projeto técnico.</em>",
               "Arquitetura, esquemas e escolha dos componentes.", pos="50% 50%"),
    foto_texto("e02-etapa-3-placa", "Etapa 3 · Desenvolvimento", "Placa, firmware<br>e sistema <em>juntos.</em>",
               "Hardware e software pensados como uma coisa só, e não remendados depois.", pos="50% 50%"),
    foto_texto("e02-etapa-4-prototipo", "Etapa 4 · Protótipo", "Testar antes<br><em>de fabricar.</em>",
               "O protótipo é medido e ajustado até se comportar como o produto final.", pos="40% 50%"),
    foto_texto("e02-etapa-5-fabricacao", "Etapa 5 · Produção", "Do protótipo<br><em>à produção.</em>",
               "O projeto acompanha o produto até a fabricação.", pos="50% 50%"),
    final(titulo="Tem um produto<br>para tirar<br><em>do papel?</em>"),
]

if __name__ == "__main__":
    for p in build(S, "p1211_engenharia"): print(p)
