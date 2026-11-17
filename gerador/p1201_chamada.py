# Post 7 (ter 1/12... ajustado na fila): painel de chamada. Carrossel 6.
from render import *

LEGENDA = """Ninguém precisa gritar nomes no balcão.

No PHILA, a chamada aparece no painel da sala de espera com a senha e o guichê, um alerta sonoro e a voz que você escolher. Entre uma chamada e outra, a TV mostra os avisos e as campanhas da sua empresa.

Fale com a gente no WhatsApp: link na bio.

Imagens ilustrativas.

#gestaodefilas #paineldesenhas #saladeespera #experienciadocliente #phila"""

S = [
    capa_foto("p07-chamada-2560", "PHILA · Chamada", "A chamada que<br>o cliente <em>vê e ouve.</em>", "", pos="62% 40%", phila=True),
    texto("Na sala de espera", "Chega de chamar<br>pelo nome <em>no balcão.</em>",
          "A chamada fica clara para todo mundo, e a recepção continua trabalhando.", foto="p07-chamada-antes-2560", pos="50% 30%"),
    tela("p14-painel-tv-normal-cn023", "Painel", "Senha e guichê<br><em>à vista de toda a sala.</em>",
         "Com as últimas chamadas ao lado.", alt=518),
    tela("if_painel-tv_lumivida_2-alerta-chamada-cn023", "Alerta e voz", "Alerta sonoro<br><em>e chamada por voz.</em>",
         "Vozes Camila, Thiago ou Vitória: você escolhe.", alt=518),
    tela("if_banner_lumivida-checkup", "Avisos e campanhas", "Entre uma chamada e outra,<br><em>a TV trabalha para você.</em>",
         "Mostre campanhas, serviços e avisos da sua empresa.", alt=518, pos="center"),
    final(phila=True),
]

if __name__ == "__main__":
    for p in build(S, "p1201_chamada"): print(p)
