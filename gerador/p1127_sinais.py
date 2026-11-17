# Post 9: atendimento na prática (a). 5 sinais. Carrossel 8.
from render import *

LEGENDA = """A sua recepção dá sinais quando o sistema de senhas ficou para trás.

Fila que se forma no balcão, cliente perguntando se ainda falta muito, prioridade que depende de quem está atendendo. Se você reconheceu mais de um desses sinais, vale conhecer uma forma nova de organizar o atendimento.

Salve e mostre para quem cuida da recepção. Fale com a gente no WhatsApp: link na bio.

#gestaodeatendimento #gestaodefilas #recepcao #experienciadocliente #atendimentoaocliente"""

S = [
    capa_foto("lp15", "Atendimento na prática", "5 sinais de que<br>a sua recepção<br><em>pede um sistema novo.</em>", "",
              pos="50% 50%", tam="tl"),
    texto("Sinal 1", "A fila se forma<br><em>no balcão</em>,<br>não no sistema.",
          "Quem chega precisa esperar alguém livre só para pegar a senha.", num="01"),
    texto("Sinal 2", "O cliente pergunta<br><em>toda hora</em> se ainda<br>falta muito.",
          "Sem ver a fila, ele não sabe quando vai ser chamado.", num="02"),
    texto("Sinal 3", "A prioridade depende<br><em>de quem está atendendo.</em>",
          "Preferenciais e idosos deveriam ser chamados pela regra, não pela boa vontade.", num="03"),
    texto("Sinal 4", "Ninguém sabe<br><em>quanto tempo</em><br>o cliente esperou.",
          "Sem números, cada reclamação vira opinião contra opinião.", num="04"),
    texto("Sinal 5", "Quando o sistema trava,<br><em>o atendimento para.</em>",
          "E a recepção volta para o papel e para o grito.", num="05"),
    texto("Reconheceu algum?", "Se marcou mais de um,<br><em>vale conhecer o PHILA.</em>",
          "Senha, fila, chamada e gestão num só sistema, em nuvem, com o totem OrbitaComet.", foto="lp16", pos="50% 60%"),
    final(phila=True),
]

if __name__ == "__main__":
    for p in build(S, "p1127_sinais"): print(p)
