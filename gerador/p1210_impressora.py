# Quinta 10/12: OrbitaComet, impressora com corte automático. Post único.
from render import *

LEGENDA = """A senha sai cortada e pronta para levar.

O OrbitaComet tem impressora térmica com corte automático. O cliente toca na tela, escolhe o serviço e pega a senha na hora, sem rasgar papel e sem depender de alguém no balcão. A senha impressa também pode levar a sua logo e um QR code.

É um detalhe pequeno, mas é o primeiro contato do cliente com o seu atendimento.

Fale com a gente no WhatsApp: link na bio.

Marca fictícia, criada para demonstração.

#totemdeautoatendimento #gestaodefilas #experienciadocliente #recepcao #orbitacomet"""

S = [unico("h08-close-senha-2560", "OrbitaComet · impressora térmica",
           "A senha sai<br><em>pronta para levar.</em>", pos="56% 50%", alt_txt=80)]

if __name__ == "__main__":
    for p in build(S, "p1210_impressora"): print(p)
