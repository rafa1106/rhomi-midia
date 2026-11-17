# Post 10: gestão em tempo real. Carrossel 6.
from render import *

LEGENDA = """O que a gestão enxerga quando o atendimento passa pelo PHILA.

Senhas emitidas, tempo de espera, filas por serviço e desempenho de cada atendente, tudo em tempo real. E um relatório com IA que resume o período e aponta o que pode melhorar. Em nuvem: abre no computador ou no celular.

Fale com a gente no WhatsApp: link na bio.

Imagens ilustrativas.

#gestaodeatendimento #gestaodefilas #indicadores #inteligenciaartificial #phila"""

S = [
    capa_foto("p11-gestao-foto-2560", "PHILA · Gestão", "O que a gestão<br><em>enxerga em tempo real.</em>", "", pos="55% 40%", phila=True),
    tela("p14-gestao-1-visao-geral", "Visão geral", "O dia inteiro <em>num só painel.</em>",
         "Senhas, espera, atendimentos e filas, atualizados na hora.", alt=518),
    tela("p14-gestao-2-desempenho-atendentes", "Equipe", "O desempenho de cada<br>atendente <em>e de cada serviço.</em>", "", zoom=1.7),
    tela("p14-gestao-3-relatorio-ia", "Relatório com IA", "O que aconteceu <em>e o que melhorar.</em>",
         "A IA resume o período e sugere ajustes.", zoom=1.8),
    texto("De onde você estiver", "Em nuvem:<br>no computador<br><em>ou no celular.</em>",
          "Sem servidor na empresa para manter.", foto="p11-gestao-painel-1920", pos="50% 40%"),
    final(phila=True),
]

if __name__ == "__main__":
    for p in build(S, "p1208_gestao"): print(p)
