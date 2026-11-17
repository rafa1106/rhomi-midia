# Post 1 da primeira leva (virada 24/11): quem é a RHOMI. Carrossel 6.
from render import *

LEGENDA = """Tecnologia que transforma experiências. É isso que a RHOMI faz há mais de 12 anos.

Somos a empresa por trás do PHILA, a solução de gestão de filas e atendimento, e do OrbitaComet, o totem do PHILA. Também desenvolvemos hardware e software sob medida, do projeto à produção.

A partir de agora, este perfil mostra como tudo isso funciona na prática.

Fale com a gente no WhatsApp: link na bio.

Algumas imagens são ilustrativas.

#gestaodeatendimento #gestaodefilas #totemdeautoatendimento #experienciadocliente #tecnologia"""

S = [
    capa_foto("p01-abertura-luz-1920", "RHOMI", "Tecnologia que<br>transforma <em>experiências.</em>",
              "Do software ao equipamento, para quem atende pessoas todos os dias.", pos="62% 40%"),
    texto("Quem somos", "Há mais de 12 anos,<br>criamos tecnologia<br>para <em>organizar<br>o atendimento.</em>",
          "Projetamos e fabricamos o que entregamos: sistema, equipamento e o que liga um ao outro.",
          foto="h12-da-ideia-ao-produto-2560", pos="50% 50%"),
    foto_texto("p19-ecossistema-2560", "PHILA", "Gestão de filas e atendimento, <em>do início ao fim.</em>",
               "Senha, chamada, atendimento e gestão num só sistema, em nuvem.", alt=560),
    foto_texto("o02-abertura-2560", "OrbitaComet", "O totem do PHILA:<br><em>elegante, compacto</em><br>e com a sua marca.",
               "", pos="68% 50%", alt=680),
    foto_texto("e02-etapa-3-desenvolvimento", "Engenharia sob medida", "Hardware e software<br><em>sob medida</em>, do protótipo<br>à produção.",
               "", pos="50% 50%", alt=680),
    final(),
]

if __name__ == "__main__":
    for p in build(S, "p1124a_rhomi"): print(p)
