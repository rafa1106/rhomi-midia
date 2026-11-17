# Post 2 (virada 24/11): vitrine do OrbitaComet. Post único.
from render import *

LEGENDA = """Seu atendimento começa aqui.

O OrbitaComet é o totem do PHILA: design elegante e compacto, tela touch Full HD, impressora com corte automático e boas-vindas por voz para quem se aproxima. A frente, a iluminação e as telas levam a identidade da sua empresa.

Quer ver como ele fica na sua recepção? Fale com a gente no WhatsApp: link na bio.

#totemdeautoatendimento #gestaodefilas #experienciadocliente #recepcao #orbitacomet"""

S = [unico("o02-abertura-2560", "OrbitaComet · o totem do PHILA", "Seu atendimento<br><em>começa aqui.</em>", pos="66% 50%")]

if __name__ == "__main__":
    for p in build(S, "p1124b_orbitacomet"): print(p)
