# Post 5 (virada 24/11): quatro formas de emitir a senha. Carrossel 6.
from render import *

LEGENDA = """O totem não é a única porta de entrada.

No PHILA, a senha pode ser emitida de quatro formas: no totem, pelo computador da recepção, com a máquina portátil ou pelo WhatsApp do próprio cliente. Todas caem na mesma fila, organizada por serviço e prioridade.

Salve para mostrar para a sua equipe. Fale com a gente no WhatsApp: link na bio.

Imagens ilustrativas.

#gestaodefilas #gestaodeatendimento #senhadeatendimento #whatsapp #phila"""

S = [
    capa_texto("PHILA · Emissão de senha", "Quatro formas de <em>emitir a senha.</em>",
               "E todas caem na mesma fila.",
               fotos=["p16-emissao-totem", "p16-emissao-computador", "p16-emissao-maquina-portatil", "p16-emissao-whatsapp"], phila=True),
    foto_texto("p16-emissao-totem", "1 · Totem", "O cliente escolhe o serviço<br>e <em>retira a senha sozinho.</em>",
               "", pos="50% 35%", alt=720),
    foto_texto("p16-emissao-computador", "2 · Computador", "Na recepção, o funcionário<br><em>emite pelo sistema.</em>",
               "E entrega impressa ou envia pelo WhatsApp, sem gastar papel.", pos="50% 45%", alt=600),
    foto_texto("p16-emissao-maquina-portatil", "3 · Máquina portátil", "Em qualquer ponto,<br><em>a equipe vai até quem chega.</em>",
               "Gera e imprime a senha ali mesmo.", pos="50% 40%", alt=620),
    foto_texto("p16-emissao-whatsapp", "4 · WhatsApp", "O próprio cliente<br><em>pede a senha pelo celular.</em>",
               "", pos="50% 35%", alt=720),
    final(phila=True),
]

if __name__ == "__main__":
    for p in build(S, "p1124e_emissao"): print(p)
