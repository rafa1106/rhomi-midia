# -*- coding: utf-8 -*-
"""Destaques fixados (stories 1080x1920), capas dos destaques e foto de perfil do @rhomi.tech.
Uso: python3 destaques.py  ->  ../destaques/<destaque>/NN.jpg, ../destaques/capas/*.jpg, ../destaques/perfil.jpg
Zonas seguras do story: nada importante nos 250 px de cima e de baixo.
"""
from pathlib import Path
import os
from render import *

DEST = ROOT / "destaques"
SW, SH = 1080, 1920


def _rs(i, n):
    return (f'<div class="rod" style="bottom:200px"><span class="m"><img src="{marca("rhomi-simbolo-fundo-escuro.svg")}">{HANDLE}</span>'
            f'<span>{i:02d} / {n:02d}</span></div>')


def st_foto(foto, lbl, titulo, corpo="", pos="50% 50%", alt=1080):
    def f(i, n):
        return f"""<div class="s"><div class="bleed" style="height:{alt}px"><img src="{img(foto)}" style="object-position:{pos}"></div>
  <div style="position:absolute;left:0;right:0;top:0;height:330px;z-index:1;background:linear-gradient(180deg,rgba(12,12,14,.7),transparent)"></div>
  <div style="position:absolute;left:0;right:0;top:{alt - 480}px;height:480px;z-index:1;background:linear-gradient(180deg,transparent,{C['g900']} 90%)"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:{alt - 60}px">
    <div class="lbl">{lbl}</div>
    <div class="t tl" style="margin-top:26px">{titulo}</div>
    {f'<div class="bd" style="margin-top:26px">{corpo}</div>' if corpo else ''}
  </div>{_rs(i, n)}</div>"""
    return f


def st_tela(foto, lbl, titulo, corpo="", celular=False, pos="top left"):
    def f(i, n):
        if celular:
            dev = (f'<div class="cel" style="left:{(SW - 470) / 2}px;top:300px;width:470px;height:990px">'
                   f'<img src="{img(foto)}" style="object-position:top"></div>')
            ttop = 1360
        else:
            dev = (f'<div class="bez" style="left:60px;width:960px;top:420px;height:{round(932 * 9 / 16 + 28)}px">'
                   f'<img src="{img(foto)}" style="object-position:{pos}"></div>')
            ttop = 1060
        return f"""<div class="s"><div class="grao"></div>{dev}
  <div class="z" style="position:absolute;left:80px;right:80px;top:{ttop}px">
    <div class="lbl">{lbl}</div>
    <div class="t tl" style="margin-top:26px">{titulo}</div>
    {f'<div class="bd" style="margin-top:26px">{corpo}</div>' if corpo else ''}
  </div>{_rs(i, n)}</div>"""
    return f


def st_texto(lbl, titulo, corpo="", itens=None, topo_logo=True, phila=False):
    def f(i, n):
        li = ""
        if itens:
            li = '<div style="display:flex;flex-direction:column;gap:46px;margin-top:80px">' + "".join(
                f'<div class="item"><div class="ic">{icone(ic)}</div><div><div class="it">{t}</div><div class="id">{d}</div></div></div>'
                for ic, t, d in itens) + "</div>"
        lg = f'<div style="margin-bottom:90px">{logo(64, phila)}</div>' if topo_logo else ""
        return f"""<div class="s"><div class="grao"></div>
  <div style="position:absolute;width:1100px;height:1100px;border-radius:50%;right:-560px;top:-420px;z-index:0;
       background:radial-gradient(circle, rgba(247,166,0,.12), transparent 62%)"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
    {lg}<div class="lbl">{lbl}</div>
    <div class="t tl" style="margin-top:28px">{titulo}</div>
    {f'<div class="bd" style="margin-top:30px">{corpo}</div>' if corpo else ''}{li}
  </div>{_rs(i, n)}</div>"""
    return f


def st_contato():
    def f(i, n):
        return f"""<div class="s"><div class="grao"></div>
  <div style="position:absolute;width:1100px;height:1100px;border-radius:50%;right:-560px;top:-420px;z-index:0;
       background:radial-gradient(circle, rgba(247,166,0,.14), transparent 62%)"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:330px">
    {logo(64)}
    <div class="lbl" style="margin-top:110px">Contato</div>
    <div class="t txl" style="margin-top:28px">Fale com<br>a gente.</div>
    <div class="bd" style="margin-top:34px">Conte como é a sua recepção e a gente mostra o PHILA funcionando.</div>
  </div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:1130px">
    <div class="item"><div class="ic">{icone('mensagem')}</div><div><div class="it">WhatsApp</div><div class="id">(37) 99932-2040</div></div></div>
    <div class="item" style="margin-top:44px"><div class="ic">{icone('email')}</div><div><div class="it">E-mail</div><div class="id">comercial@rhomi.com.br</div></div></div>
    <div class="item" style="margin-top:44px"><div class="ic">{icone('externo')}</div><div><div class="it">Site</div><div class="id">rhomi.com.br</div></div></div>
  </div>{_rs(i, n)}</div>"""
    return f


DESTAQUES = {
    "1_rhomi": [
        st_foto("p01-abertura-luz-1920", "RHOMI", "Tecnologia que<br>transforma <em>experiências.</em>",
                "Do software ao equipamento, para quem atende pessoas todos os dias.", pos="62% 40%", alt=1180),
        st_texto("Quem somos", "Há mais de 12 anos,<br>criamos tecnologia<br>para <em>organizar<br>o atendimento.</em>",
                 "Projetamos e fabricamos o que entregamos."),
        st_texto("O que fazemos", "Três frentes,<br><em>uma só empresa.</em>", "", topo_logo=False, itens=[
            ("fila", "PHILA", "Gestão de filas e atendimento, do início ao fim."),
            ("tela-touch", "OrbitaComet", "O totem do PHILA, com a sua marca."),
            ("engenharia", "Engenharia sob medida", "Hardware e software, do protótipo à produção."),
        ]),
        st_texto("Saiba mais", "Conheça tudo<br>em <em>rhomi.com.br</em>", "Ou fale com a gente pelo WhatsApp: o link está na bio."),
    ],
    "2_phila": [
        st_foto("p03-chegada-toque-2560", "PHILA · 1 Chegada", "O cliente escolhe<br>o serviço <em>no totem.</em>", "", pos="72% 50%"),
        st_foto("lp06", "PHILA · 2 Senha", "A senha sai na hora,<br><em>com a sua marca.</em>", "Ou vai direto para o WhatsApp.", pos="62% 50%"),
        st_tela("p14-whatsapp-acompanhamento-nr004", "PHILA · 3 Espera", "A fila se organiza<br><em>sozinha.</em>", "", celular=True),
        st_foto("p07-chamada-2560", "PHILA · 4 Chamada", "No painel,<br><em>com alerta e voz.</em>", "", pos="58% 40%"),
        st_tela("p14-atendente-2-chamando-nr004", "PHILA · 5 Atendimento", "A próxima senha<br><em>com um clique.</em>"),
        st_foto("p11-gestao-foto-2560", "PHILA · 6 Gestão", "Tudo acompanhado<br><em>em tempo real.</em>", "", pos="58% 40%"),
    ],
    "3_orbitacomet": [
        st_foto("o02-abertura-2560", "OrbitaComet", "O totem do PHILA:<br><em>elegante e compacto.</em>", "", pos="66% 50%", alt=1200),
        st_foto("lp07", "Iluminação RGB", "Nas cores<br><em>da sua marca.</em>", "", pos="38% 50%"),
        st_foto("o15-horizontal-e-vertical-tela-desligada-1200", "Tela touch Full HD", "Horizontal<br><em>ou vertical.</em>", "", pos="50% 40%", alt=1200),
        st_foto("lp06", "Impressora térmica", "Senha impressa<br><em>com corte automático.</em>", "", pos="62% 50%"),
        st_foto("lp09", "Sensor de presença", "Boas-vindas por voz<br><em>para quem se aproxima.</em>", "", pos="70% 50%"),
    ],
    "4_aplicacoes": [
        st_foto("lp16", "Aplicações · Clínicas", "Consultas, exames<br>e retornos <em>em ordem.</em>", "", pos="72% 50%"),
        st_foto("a02-laboratorio-abertura-2560", "Aplicações · Laboratórios", "Coleta e resultados<br><em>sem fila no balcão.</em>", "", pos="78% 50%"),
        st_foto("lp18", "Aplicações · Cartórios", "Cada serviço<br><em>na sua fila.</em>", "", pos="22% 50%"),
        st_foto("lp17", "Aplicações · Bancos", "Atendimento<br><em>organizado e discreto.</em>", "", pos="30% 50%"),
        st_foto("lp19", "Aplicações · Órgãos públicos", "Prioridades<br><em>respeitadas.</em>", "", pos="35% 50%"),
        st_foto("a08-ensino-cena", "Aplicações · Ensino", "Secretaria<br><em>sem fila no balcão.</em>", "", pos="85% 50%"),
    ],
    "5_contato": [st_contato()],
}

CAPAS = {"1_rhomi": None, "2_phila": "fila", "3_orbitacomet": "tela-touch", "4_aplicacoes": "localizacao", "5_contato": "mensagem"}


def capa(icone_nome):
    def f(i, n):
        meio = (f'<img src="{marca("rhomi-simbolo-fundo-escuro.svg")}" style="width:420px">' if icone_nome is None
                else icone(icone_nome, C["lar"], 400))
        return f"""<div class="s" style="background:{C['g900']}"><div style="position:absolute;left:{(SW - 640) / 2}px;top:{(SH - 640) / 2}px;width:640px;height:640px;
  border-radius:50%;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle,#232327,#161619 70%)">{meio}</div></div>"""
    return f


def perfil():
    def f(i, n):
        return f"""<div class="s" style="background:radial-gradient(circle at 50% 40%,#26262C,{C['g900']} 70%)">
  <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">
  <img src="{marca("rhomi-simbolo-fundo-escuro.svg")}" style="width:560px"></div></div>"""
    return f


if __name__ == "__main__":
    import render
    for nome, slides in DESTAQUES.items():
        render.OUT = DEST / nome; render.OUT.mkdir(parents=True, exist_ok=True)
        for p in build(slides, "story", formato="story"): print(p)
    render.OUT = DEST / "capas"; render.OUT.mkdir(parents=True, exist_ok=True)
    for nome, ic in CAPAS.items():
        for p in build([capa(ic)], f"capa_{nome}", formato="story"): print(p)
    # foto de perfil 1080x1080
    from playwright.sync_api import sync_playwright
    render.OUT = DEST
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1080})
        hp = HERE / ".tmp" / "perfil.html"; hp.write_text(render._page(perfil()(1, 1), 1080, 1080), encoding="utf-8")
        pg.goto(hp.as_uri()); pg.wait_for_timeout(300); pg.screenshot(path=str(DEST / "perfil.png")); b.close()
    from PIL import Image
    Image.open(DEST / "perfil.png").convert("RGB").save(DEST / "perfil.jpg", quality=95); os.remove(DEST / "perfil.png")
    print(DEST / "perfil.jpg")
