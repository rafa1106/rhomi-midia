# Post 11: personalização da frente. Carrossel 5.
from render import *

LEGENDA = """O totem pode ter a cara da sua empresa.

No OrbitaComet, a frente recebe a arte com a sua identidade e a iluminação lateral acompanha as suas cores. As telas e a senha impressa também levam a sua marca, configuradas no PHILA.

Fale com a gente no WhatsApp: link na bio.

Marcas fictícias, criadas para demonstração.

#totemdeautoatendimento #identidadevisual #personalizacao #recepcao #orbitacomet"""

S = [
    capa_foto("frente_fila4", "OrbitaComet · Personalização", "A frente do totem<br><em>com a sua identidade.</em>", "",
              pos="50% 30%", alt_foto=880, tam="tl"),
    foto_texto("frente_par_1", "Frente personalizada", "A arte acompanha<br><em>o estilo da marca.</em>", "", pos="50% 40%"),
    foto_texto("frente_par_2", "Iluminação RGB", "E a luz lateral<br><em>na mesma cor.</em>", "", pos="50% 40%"),
    foto_texto("frente_par_3", "Qualquer segmento", "Do cartório<br><em>ao banco de investimentos.</em>", "", pos="50% 40%"),
    foto_texto("o08-tela-touch-2560", "Telas", "As telas também<br><em>com a sua identidade.</em>",
               "Cores, imagens e serviços, configurados no PHILA.", pos="50% 50%"),
    final(),
]

if __name__ == "__main__":
    for p in build(S, "p1203_frente"): print(p)
