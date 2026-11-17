# -*- coding: utf-8 -*-
"""Renderizador do feed @rhomi.tech: HTML -> JPEG (Chromium/Playwright).

Uso num gerador:  from render import *  ->  build([slides...], "pMMDD_tema")
Gera ../artes/<prefixo>_NN.jpg (1080x1350). Stories: build(..., formato="story") -> 1080x1920.
Regras de conteúdo e visual: ../estrategia/guia_conteudo.md
"""
import os, html as _h
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MARCA = ROOT / "marca"
IMG = ROOT / "fontes" / "img"
OUT = Path(os.environ.get("ARTES_DIR") or (ROOT / "artes"))
OUT.mkdir(parents=True, exist_ok=True)
HANDLE = "@rhomi.tech"
SITE = "rhomi.com.br"
W, H = 1080, 1350

C = dict(g950="#0C0C0E", g900="#161619", g800="#232327", g700="#2B2B2F", g600="#3A3A40",
         c500="#8A8782", c400="#B9B6B1", c300="#D0CDC8", areia="#F4F2EE",
         lar="#F7A600", lar_c="#FBCB68", verde="#A7D26C", azul="#3E86A8")


USADAS = []  # imagens-base usadas no slide em renderização (para a página de revisão)


def img(nome):
    """Caminho file:// de uma imagem de fontes/img (com ou sem extensão)."""
    USADAS.append(nome)
    p = IMG / nome
    if not p.suffix:
        p = next(IMG.glob(nome + ".*"))
    if not p.exists():
        raise FileNotFoundError(p)
    return p.as_uri()


def marca(nome):
    return (MARCA / nome).as_uri()


def icone(nome, cor=None, tam=44):
    svg = (MARCA / "icones" / f"{nome}.svg").read_text(encoding="utf-8")
    svg = svg.replace("<svg ", f'<svg width="{tam}" height="{tam}" style="color:{cor or C["lar"]}" ', 1)
    return svg


FONTS = "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('{marca(f)}') format('woff2')}}"
    for fam, w, f in [("Poppins", 200, "poppins-200-extralight.woff2"), ("Poppins", 300, "poppins-300-light.woff2"),
                      ("Poppins", 400, "poppins-400-regular.woff2"), ("Poppins", 500, "poppins-500-medium.woff2"),
                      ("Inter", 400, "inter-400-regular.woff2"), ("Inter", 500, "inter-500-medium.woff2"),
                      ("Inter", 600, "inter-600-semibold.woff2")])

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:{C['g900']}}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;color:{C['areia']};text-rendering:geometricPrecision}}
.s{{position:relative;overflow:hidden;background:
   radial-gradient(90% 60% at 85% 0%, #22222A 0%, transparent 60%),
   radial-gradient(70% 50% at 0% 100%, #1C1C21 0%, transparent 65%), {C['g900']}}}
.grao{{position:absolute;inset:0;pointer-events:none;opacity:.35;z-index:1;
  background-image:radial-gradient(circle at 1px 1px, rgba(255,255,255,.035) 1px, transparent 0);background-size:6px 6px}}
.z{{position:relative;z-index:3}}
.lbl{{font-family:'Inter';font-weight:500;font-size:22px;letter-spacing:.22em;text-transform:uppercase;color:{C['c400']};
     display:flex;align-items:center;gap:16px}}
.lbl:before{{content:"";width:10px;height:10px;border-radius:50%;background:{C['lar']};flex:0 0 10px}}
.t{{font-family:'Poppins';font-weight:300;letter-spacing:-.02em;color:{C['areia']}}}
.t em{{font-style:normal;font-weight:400;color:{C['lar']}}}
.txl{{font-size:94px;line-height:1.06}} .tl{{font-size:76px;line-height:1.1}} .tm{{font-size:62px;line-height:1.14}} .ts{{font-size:50px;line-height:1.18}}
.bd{{font-family:'Inter';font-weight:400;font-size:33px;line-height:1.48;color:{C['c400']};letter-spacing:-.005em}}
.bd b{{font-weight:500;color:{C['areia']}}}
.pq{{font-family:'Inter';font-weight:400;font-size:24px;line-height:1.45;color:{C['c500']}}}
.rod{{position:absolute;left:80px;right:80px;bottom:56px;display:flex;justify-content:space-between;align-items:center;z-index:5;
     font-family:'Inter';font-weight:500;font-size:21px;letter-spacing:.04em;color:{C['c500']}}}
.rod .m{{display:flex;align-items:center;gap:14px}}
.rod .m img{{height:34px}}
.foto{{position:absolute;overflow:hidden;border-radius:28px;box-shadow:0 30px 80px rgba(0,0,0,.45);
       outline:1px solid rgba(255,255,255,.07);outline-offset:-1px;z-index:2}}
.foto img{{width:100%;height:100%;object-fit:cover;display:block}}
.bleed{{position:absolute;left:0;right:0;top:0;z-index:0}}
.bleed img{{width:100%;height:100%;object-fit:cover;display:block}}
.fio{{width:72px;height:3px;background:{C['lar']};border-radius:2px}}
.chip{{display:inline-flex;align-items:center;gap:12px;padding:14px 24px;border-radius:999px;border:1.5px solid rgba(244,242,238,.18);
      font-family:'Inter';font-weight:500;font-size:24px;color:{C['areia']};background:rgba(22,22,25,.55);backdrop-filter:blur(10px)}}
.bez{{position:absolute;background:{C['g950']};border-radius:22px;padding:14px;z-index:2;
      box-shadow:0 0 0 1.5px rgba(255,255,255,.08),0 40px 90px rgba(0,0,0,.55),0 0 120px rgba(247,166,0,.05)}}
.bez img{{width:100%;height:100%;object-fit:cover;object-position:top left;border-radius:10px;display:block}}
.cel{{position:absolute;background:#0A0A0C;border-radius:64px;padding:16px;z-index:2;
      box-shadow:0 0 0 2px rgba(255,255,255,.10),0 40px 90px rgba(0,0,0,.6)}}
.cel img{{width:100%;height:100%;object-fit:cover;object-position:top;border-radius:50px;display:block}}
.num{{font-family:'Poppins';font-weight:200;color:{C['lar']};line-height:1}}
.item{{display:flex;gap:28px;align-items:flex-start}}
.item .ic{{flex:0 0 76px;height:76px;border-radius:22px;background:{C['g800']};display:flex;align-items:center;justify-content:center;
          box-shadow:inset 0 0 0 1px rgba(255,255,255,.06)}}
.item .it{{font-family:'Poppins';font-weight:400;font-size:36px;line-height:1.2;color:{C['areia']}}}
.item .id{{font-family:'Inter';font-size:27px;line-height:1.45;color:{C['c400']};margin-top:6px}}
"""


def esc(s):
    return s  # textos são escritos à mão nos geradores; tags <em>/<b>/<br> são permitidas


def _page(inner, w, h):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FONTS}{CSS}'
            f'html,body{{width:{w}px;height:{h}px;overflow:hidden}} .s{{width:{w}px;height:{h}px}}</style></head>'
            f'<body>{inner}</body></html>')


def rod(idx=None, total=None, dica=None):
    dir_ = dica or (f"{idx:02d} / {total:02d}" if idx else "")
    return (f'<div class="rod"><span class="m"><img src="{marca("rhomi-simbolo-fundo-escuro.svg")}">{HANDLE}</span>'
            f'<span>{dir_}</span></div>')


def logo(altura=46, phila=False):
    f = "phila-logo-fundo-escuro.svg" if phila else "rhomi-logo-fundo-escuro.svg"
    return f'<img src="{marca(f)}" style="height:{altura}px;display:block">'


# ---------------------------------------------------------------- layouts
# Cada layout devolve uma função f(idx, total) -> html, para o build numerar os slides.

def capa_foto(foto, lbl, titulo, sub="", pos="50% 50%", alt_foto=820, tam="txl", phila=False, dica="Arraste →"):
    def f(i, n):
        return f"""<div class="s"><div class="bleed" style="height:{alt_foto}px"><img src="{img(foto)}" style="object-position:{pos}"></div>
  <div style="position:absolute;left:0;right:0;top:0;height:260px;z-index:1;background:linear-gradient(180deg,rgba(12,12,14,.72),transparent)"></div>
  <div style="position:absolute;left:0;right:0;top:{alt_foto-420}px;height:420px;z-index:1;background:linear-gradient(180deg,transparent,{C['g900']} 92%)"></div>
  <div class="z" style="position:absolute;left:80px;top:72px">{logo(44, phila)}</div>
  <div class="z" style="position:absolute;left:80px;right:80px;bottom:150px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:26px">{titulo}</div>
    {f'<div class="bd" style="margin-top:26px;max-width:860px">{sub}</div>' if sub else ''}
  </div>{rod(dica=dica)}</div>"""
    return f


def capa_texto(lbl, titulo, sub="", fotos=None, tam="txl", phila=False, dica="Arraste →"):
    """Capa tipográfica; fotos = lista de até 4 imagens em mosaico na parte de baixo."""
    def f(i, n):
        mos = ""
        if fotos:
            k = len(fotos); gw = (920 - 20 * (k - 1)) / k
            mos = "".join(f'<div class="foto" style="left:{80 + j * (gw + 20)}px;top:800px;width:{gw}px;height:380px">'
                          f'<img src="{img(p)}"></div>' for j, p in enumerate(fotos))
        return f"""<div class="s"><div class="grao"></div>
  <div class="z" style="position:absolute;left:80px;top:72px">{logo(44, phila)}</div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:{230 if fotos else 340}px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:30px">{titulo}</div>
    {f'<div class="bd" style="margin-top:30px;max-width:880px">{sub}</div>' if sub else ''}
  </div>{mos}{rod(dica=dica)}</div>"""
    return f


def foto_texto(foto, lbl, titulo, corpo="", pos="50% 50%", alt=None, tam="tm", topo_txt=150):
    """Texto em cima, foto arredondada ocupando o resto do slide."""
    def f(i, n):
        return f"""<div class="s"><div class="grao"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:{topo_txt}px;bottom:140px;display:flex;flex-direction:column">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:24px">{titulo}</div>
    {f'<div class="bd" style="margin-top:22px">{corpo}</div>' if corpo else ''}
    <div class="foto" style="position:relative;flex:1;margin-top:56px;min-height:300px"><img src="{img(foto)}" style="object-position:{pos}"></div>
  </div>
  {rod(i, n)}</div>"""
    return f


def foto_cheia(foto, lbl, titulo, corpo="", pos="50% 50%", tam="tm"):
    """Foto ocupando o slide, texto embaixo sobre degradê."""
    def f(i, n):
        return f"""<div class="s"><div class="bleed" style="height:{H}px"><img src="{img(foto)}" style="object-position:{pos}"></div>
  <div style="position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(22,22,25,0) 35%,rgba(22,22,25,.85) 66%,{C['g900']} 88%)"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;bottom:150px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:24px">{titulo}</div>
    {f'<div class="bd" style="margin-top:22px">{corpo}</div>' if corpo else ''}
  </div>{rod(i, n)}</div>"""
    return f


def tela(foto, lbl, titulo, corpo="", larg=920, alt=None, pos="top left", topo_txt=150, zoom=1.0):
    """Captura de tela num monitor (moldura escura), centrada no espaço abaixo do texto."""
    def f(i, n):
        a = alt or round((larg - 28) * 9 / 16 + 28)
        zs = (f"width:{zoom*100}%;height:{zoom*100}%;object-fit:cover;object-position:{pos}" if zoom != 1 else f"object-position:{pos}")
        return f"""<div class="s"><div class="grao"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:{topo_txt}px;bottom:140px;display:flex;flex-direction:column">
    <div class="lbl">{lbl}</div>
    <div class="t tm" style="margin-top:24px">{titulo}</div>
    {f'<div class="bd" style="margin-top:22px">{corpo}</div>' if corpo else ''}
    <div style="flex:1;display:flex;align-items:center;justify-content:center;margin-top:40px">
      <div class="bez" style="position:relative;width:{larg}px;height:{a}px;overflow:hidden"><div style="width:100%;height:100%;overflow:hidden;border-radius:10px"><img src="{img(foto)}" style="{zs};border-radius:0"></div></div>
    </div>
  </div>
  {rod(i, n)}</div>"""
    return f


def celular(foto, lbl, titulo, corpo="", pos="top"):
    """Captura vertical (WhatsApp, app) num celular à direita, texto à esquerda."""
    def f(i, n):
        return f"""<div class="s"><div class="grao"></div>
  <div class="z" style="position:absolute;left:80px;width:470px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;padding-bottom:40px">
    <div class="lbl">{lbl}</div>
    <div class="t ts" style="margin-top:24px">{titulo}</div>
    {f'<div class="bd" style="margin-top:22px;font-size:30px">{corpo}</div>' if corpo else ''}
  </div>
  <div class="cel" style="right:70px;top:150px;width:440px;height:930px"><img src="{img(foto)}" style="object-position:{pos}"></div>
  {rod(i, n)}</div>"""
    return f


def texto(lbl, titulo, corpo="", num=None, tam="tl", foto=None, pos="50% 50%"):
    """Slide de texto. Com num: número grande no alto e texto embaixo. Com foto: faixa de imagem escurecida embaixo."""
    def f(i, n):
        if num:
            return f"""<div class="s"><div class="grao"></div>
  <div class="num z" style="position:absolute;left:66px;top:110px;font-size:330px;letter-spacing:-.04em">{num}</div>
  <div class="z" style="position:absolute;left:80px;right:80px;bottom:170px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:28px">{titulo}</div>
    {f'<div class="bd" style="margin-top:30px;max-width:900px">{corpo}</div>' if corpo else ''}
  </div>{rod(i, n)}</div>"""
        fo = (f'<div class="bleed" style="top:auto;bottom:130px;height:520px;opacity:.5;'
              f'-webkit-mask-image:linear-gradient(180deg,transparent,#000 45%,#000 70%,transparent)"><img src="{img(foto)}" style="object-position:{pos}"></div>') if foto else ""
        return f"""<div class="s"><div class="grao"></div>{fo}
  <div class="z" style="position:absolute;left:80px;right:80px;top:{230 if foto else 0}px;{'' if foto else 'bottom:0;'}display:flex;flex-direction:column;justify-content:center;padding-bottom:{0 if foto else 60}px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:28px">{titulo}</div>
    {f'<div class="bd" style="margin-top:30px;max-width:880px">{corpo}</div>' if corpo else ''}
  </div>{rod(i, n)}</div>"""
    return f


def lista(lbl, titulo, itens, tam="tm"):
    """itens: lista de (icone, titulo, descrição)."""
    def f(i, n):
        li = "".join(f'<div class="item"><div class="ic">{icone(ic)}</div><div><div class="it">{t}</div>'
                     f'<div class="id">{d}</div></div></div>' for ic, t, d in itens)
        return f"""<div class="s"><div class="grao"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:150px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:24px">{titulo}</div>
    <div style="display:flex;flex-direction:column;gap:44px;margin-top:70px">{li}</div>
  </div>{rod(i, n)}</div>"""
    return f


def final(phila=False, titulo=None):
    def f(i, n):
        t = titulo or ("Vamos organizar<br>o atendimento<br>da sua empresa?" if not phila else
                       "Quer ver o PHILA<br>funcionando<br>na sua recepção?")
        assin = (f'<div style="display:flex;align-items:center;gap:22px">{logo(60, True)}'
                 f'<span class="pq" style="font-size:24px">Uma solução Rhomi</span></div>') if phila else logo(64)
        return f"""<div class="s"><div class="grao"></div>
  <div style="position:absolute;width:900px;height:900px;border-radius:50%;right:-420px;top:-380px;z-index:0;
       background:radial-gradient(circle, rgba(247,166,0,.13), transparent 62%)"></div>
  <div class="z" style="position:absolute;left:80px;right:80px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;padding-bottom:40px">
    {assin}
    <div class="t tl" style="margin-top:90px">{t}</div>
    <div class="fio" style="margin-top:56px"></div>
    <div class="bd" style="margin-top:40px;color:{C['areia']}">Fale com a gente no WhatsApp:<br><b style="color:{C['lar']}">link na bio</b></div>
    <div class="pq" style="margin-top:22px;font-size:28px">{SITE}</div>
  </div>{rod(i, n)}</div>"""
    return f


def unico(foto, lbl, titulo, sub="", pos="50% 50%", lado="esq", alt_txt=None, tam="tl"):
    """Post único: foto em tela cheia, texto curto embaixo."""
    def f(i, n):
        return f"""<div class="s"><div class="bleed" style="height:{H}px"><img src="{img(foto)}" style="object-position:{pos}"></div>
  <div style="position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(12,12,14,.55) 0%,rgba(12,12,14,0) 18%,rgba(12,12,14,0) 52%,rgba(12,12,14,.88) 84%)"></div>
  <div class="z" style="position:absolute;left:80px;top:72px">{logo(42)}</div>
  <div class="z" style="position:absolute;left:80px;right:80px;bottom:{alt_txt or 120}px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:22px">{titulo}</div>
    {f'<div class="bd" style="margin-top:18px">{sub}</div>' if sub else ''}
  </div></div>"""
    return f


def vitrine(foto, lbl, titulo, sub="", topo=120, alt=760, pos="50% 50%", tam="tl", larg=None, pena=8):
    """Post único: imagem larga em cima (sem cortar laterais), texto embaixo."""
    def f(i, n):
        lw = larg or W
        return f"""<div class="s"><div class="grao"></div>
  <div style="position:absolute;left:{(W - lw) / 2}px;width:{lw}px;top:{topo}px;height:{alt}px;z-index:2;
       -webkit-mask-image:linear-gradient(180deg,transparent 0,#000 {pena+4}%,#000 {92-pena}%,transparent 100%),linear-gradient(90deg,transparent 0,#000 {pena}%,#000 {100-pena}%,transparent 100%);
       -webkit-mask-composite:source-in;mask-composite:intersect">
    <img src="{img(foto)}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};display:block"></div>
  <div class="z" style="position:absolute;left:80px;top:64px">{logo(42)}</div>
  <div class="z" style="position:absolute;left:80px;right:80px;bottom:110px">
    <div class="lbl">{lbl}</div>
    <div class="t {tam}" style="margin-top:22px">{titulo}</div>
    {f'<div class="bd" style="margin-top:18px">{sub}</div>' if sub else ''}
  </div></div>"""
    return f


def html_livre(corpo_html):
    """Slide com HTML próprio (recebe idx/total no rodapé)."""
    def f(i, n):
        return f'<div class="s"><div class="grao"></div>{corpo_html}{rod(i, n)}</div>'
    return f


# ---------------------------------------------------------------- render

def build(slides, prefixo, formato="feed", qualidade=92):
    from playwright.sync_api import sync_playwright
    w, h = (1080, 1920) if formato == "story" else (W, H)
    tmp = HERE / ".tmp"; tmp.mkdir(exist_ok=True)
    saidas = []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        n = len(slides)
        fontes = {}
        for k, s in enumerate(slides, 1):
            USADAS.clear()
            html = _page(s(k, n), w, h)
            fontes[f"{prefixo}_{k:02d}"] = list(dict.fromkeys(USADAS))
            hp = tmp / f"{prefixo}_{k:02d}.html"; hp.write_text(html, encoding="utf-8")
            pg.goto(hp.as_uri()); pg.wait_for_load_state("networkidle")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            png = tmp / "shot.png"
            pg.screenshot(path=str(png), full_page=False)
            from PIL import Image
            out = OUT / f"{prefixo}_{k:02d}.jpg"
            Image.open(png).convert("RGB").save(out, quality=qualidade, optimize=True, progressive=False, subsampling=0)
            saidas.append(out)
        b.close()
    import json
    log = OUT / "_fontes.json"
    d = json.loads(log.read_text()) if log.exists() else {}
    d.update(fontes); log.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    return saidas
