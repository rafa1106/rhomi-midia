# TESTE da ponte (17/11).
from render import *

LEGENDA = """teste"""

S = [vitrine("o15-horizontal-e-vertical-tela-desligada-1200", "OrbitaComet · tela touch", "Horizontal ou vertical.<br><em>Você escolhe.</em>",
             topo=20, alt=1010, pos="50% 50%", larg=680, pena=26)]

if __name__ == "__main__":
    for p in build(S, "p0101y_teste"): print(p)
