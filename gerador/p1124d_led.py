# Post 4 (virada 24/11): iluminação RGB. Post único.
from render import *

LEGENDA = """Nas cores da sua marca.

A iluminação lateral do OrbitaComet é RGB: você escolhe a cor no sistema e o totem passa a combinar com a recepção, a fachada e a identidade da sua empresa. Um detalhe que faz o equipamento parecer parte do ambiente, e não um aparelho a mais.

Fale com a gente no WhatsApp: link na bio.

#totemdeautoatendimento #identidadevisual #experienciadocliente #recepcao #orbitacomet"""

S = [vitrine("lp07", "OrbitaComet · iluminação RGB", "Nas cores<br>da <em>sua marca.</em>", topo=170, alt=660, pos="50% 55%", larg=1180)]

if __name__ == "__main__":
    for p in build(S, "p1124d_led"): print(p)
