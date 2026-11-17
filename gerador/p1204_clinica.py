# Post 12: por segmento (b) clínicas. Carrossel 7.
from render import *

LEGENDA = """Recepção de clínica sem fila no balcão.

Consultas, exames e retornos, cada um na sua fila. Preferenciais e idosos chamados na ordem certa. O paciente acompanha pelo WhatsApp, é chamado no painel e avalia o atendimento na saída. É assim que o PHILA organiza a recepção de uma clínica.

Fale com a gente no WhatsApp: link na bio.

Imagens ilustrativas.

#clinicas #gestaodeatendimento #recepcao #gestaodefilas #phila"""

S = [
    capa_foto("lp16", "PHILA · Clínicas", "Recepção de clínica<br><em>sem fila no balcão.</em>", "", pos="55% 50%", phila=True),
    tela("p14-totem-escolha-do-servico", "Serviços", "Consultas, exames e retornos,<br><em>cada um na sua fila.</em>",
         "O paciente escolhe o serviço no totem.", alt=518, pos="center"),
    texto("Prioridades", "Preferenciais e idosos<br><em>chamados na ordem certa.</em>",
          "As regras de prioridade ficam no sistema, e não na memória da recepção.", foto="p03-chegada-2560", pos="50% 45%"),
    celular("p14-whatsapp-acompanhamento-nr004", "Espera", "O paciente acompanha <em>pelo WhatsApp.</em>",
            "Posição na fila e aviso quando chega a vez."),
    foto_texto("p07-chamada-2560", "Chamada", "Chamado no painel,<br><em>sem gritar nomes.</em>", "", pos="60% 40%", alt=680),
    foto_texto("p10-avaliacao-2560", "Avaliação", "E a opinião dele<br><em>chega na hora.</em>", "", pos="50% 50%", alt=680),
    final(phila=True),
]

if __name__ == "__main__":
    for p in build(S, "p1204_clinica"): print(p)
