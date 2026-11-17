# Post 3 (virada 24/11): a jornada do PHILA em 7 etapas. Carrossel 9.
from render import *

LEGENDA = """Da chegada ao atendimento, cada etapa passa pelo PHILA.

O cliente retira a senha no totem, acompanha a fila pelo WhatsApp e é chamado no painel, com alerta sonoro e voz. O atendente chama a próxima com um clique, a avaliação chega na hora e a gestão vê tudo em tempo real.

Salve para mostrar para a sua equipe. Para conhecer o PHILA, fale com a gente no WhatsApp: link na bio.

Imagens ilustrativas.

#gestaodeatendimento #gestaodefilas #experienciadocliente #totemdeautoatendimento #phila"""

S = [
    capa_foto("p03-chegada-toque-2560", "PHILA · Na prática", "Da chegada ao atendimento, <em>tudo no PHILA.</em>",
              "Veja, em 7 etapas, como o atendimento flui.", pos="70% 50%", phila=True),
    foto_texto("p16-emissao-totem", "1 · Chegada", "O cliente escolhe<br>o serviço <em>no totem.</em>",
               "Sem fila no balcão para pegar senha.", pos="50% 35%", alt=640),
    foto_texto("lp06", "2 · Senha", "A senha sai na hora,<br><em>com a sua marca.</em>",
               "Logo, serviço e QR code no papel. Ou direto no WhatsApp.", pos="60% 50%", alt=600),
    celular("p14-whatsapp-acompanhamento-nr004", "3 · Espera", "A fila se organiza <em>sozinha.</em>",
            "Por serviço e prioridade. O cliente acompanha a posição pelo WhatsApp."),
    foto_texto("p07-chamada-2560", "4 · Chamada", "A senha aparece no painel,<br><em>com alerta e voz.</em>",
               "", pos="60% 40%", alt=680),
    tela("p14-atendente-2-chamando-nr004", "5 · Atendimento", "O atendente chama<br>a próxima <em>com um clique.</em>",
         "Também chama de novo, pausa ou marca quem não compareceu.", alt=500),
    foto_texto("p10-avaliacao-2560", "6 · Avaliação", "A opinião do cliente<br><em>chega na hora.</em>",
               "Com o Phila Score, integrado ao sistema.", pos="50% 50%", alt=600),
    foto_texto("p11-gestao-foto-2560", "7 · Gestão", "E a gestão acompanha<br>tudo <em>em tempo real.</em>",
               "", pos="55% 40%", alt=680),
    final(phila=True),
]

if __name__ == "__main__":
    for p in build(S, "p1124c_jornada"): print(p)
