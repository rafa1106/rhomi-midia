# Post 8: tela horizontal ou vertical. Post único.
from render import *

LEGENDA = """Horizontal ou vertical: você escolhe.

O OrbitaComet tem a mesma estrutura nas duas versões. Muda só a posição da tela touch, para combinar com o espaço da recepção e com o jeito que as suas telas foram pensadas. A inclinação também se ajusta.

Fale com a gente no WhatsApp: link na bio.

#totemdeautoatendimento #recepcao #design #experienciadocliente #orbitacomet"""

S = [vitrine("o15-horizontal-e-vertical-tela-desligada-1200", "OrbitaComet · tela touch", "Horizontal ou vertical.<br><em>Você escolhe.</em>",
             topo=20, alt=1010, pos="50% 50%", larg=680, pena=26)]

if __name__ == "__main__":
    for p in build(S, "p1126_horizontal"): print(p)
