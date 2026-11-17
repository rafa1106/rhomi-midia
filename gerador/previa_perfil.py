# Prévia do perfil (cabeçalho + destaques + grid 3:4, mais novo primeiro). Uso: python3 previa_perfil.py
from pathlib import Path
R = Path(__file__).resolve().parent.parent
def u(p): return Path(p).as_uri()
ORDEM = [('p1208_gestao','08/12'),('p1204_clinica','04/12'),('p1203_frente','03/12'),('p1201_chamada','01/12'),('p1127_sinais','27/11'),
         ('p1126_horizontal','26/11'),('REEL','24/11'),('p1124e_emissao','24/11'),('p1124d_led','24/11'),('p1124c_jornada','24/11'),
         ('p1124b_orbitacomet','24/11'),('p1124a_rhomi','24/11')]
cells = ''
for k, d in ORDEM:
    src = R/'reels/reel_01_capa.jpg' if k == 'REEL' else R/f'artes/{k}_01.jpg'
    multi = len(list((R/'artes').glob(k+'_*.jpg'))) > 1
    badge = '<span class="bd">▶</span>' if k == 'REEL' else ('<span class="bd">❐</span>' if multi else '')
    cells += f'<div class="c"><img src="{u(src)}">{badge}<span class="dt">{d}</span></div>'
hl = [('1_rhomi','RHOMI'),('2_phila','PHILA'),('3_orbitacomet','OrbitaComet'),('4_aplicacoes','Aplicações'),('5_contato','Contato')]
hls = ''.join(f'<div class="h"><div class="o"><img src="{u(R/f"destaques/capas/capa_{k}_01.jpg")}"></div><span>{n}</span></div>' for k, n in hl)
F = R/'marca'
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Inter;src:url({u(F/"inter-400-regular.woff2")})}}@font-face{{font-family:Inter;font-weight:600;src:url({u(F/"inter-600-semibold.woff2")})}}
body{{margin:0;background:#000;color:#F5F5F5;font-family:Inter;width:900px}}
.top{{display:flex;gap:56px;padding:40px 48px 10px;align-items:center}}
.av{{width:170px;height:170px;border-radius:50%;overflow:hidden;flex:0 0 170px;box-shadow:0 0 0 2px #333}} .av img{{width:100%}}
.u{{font-size:24px;font-weight:600}} .st{{display:flex;gap:34px;margin:16px 0;font-size:18px}} .st b{{font-weight:600}}
.bio{{padding:6px 48px 0;font-size:17px;line-height:1.45}} .bio b{{font-weight:600}} .lk{{color:#E0F1FF;font-weight:600}}
.hl{{display:flex;gap:34px;padding:30px 48px 26px}} .h{{text-align:center;font-size:14px}} .o{{width:96px;height:96px;border-radius:50%;overflow:hidden;box-shadow:0 0 0 2px #000,0 0 0 3.5px #444;margin-bottom:8px}}
.o img{{width:100%;height:100%;object-fit:cover}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}} .c{{position:relative;aspect-ratio:3/4;overflow:hidden}} .c img{{width:100%;height:100%;object-fit:cover}}
.bd{{position:absolute;top:8px;right:10px;font-size:20px;color:#fff;text-shadow:0 1px 4px #000}} .dt{{position:absolute;left:8px;bottom:6px;font-size:13px;background:rgba(0,0,0,.6);padding:2px 7px;border-radius:6px}}
</style></head><body>
<div class="top"><div class="av"><img src="{u(R/"destaques/perfil.jpg")}"></div><div><div class="u">rhomi.tech</div>
<div class="st"><span><b>12</b> posts</span><span><b>89</b> seguidores</span><span><b>114</b> seguindo</span></div></div></div>
<div class="bio"><b>Rhomi | Gestão de atendimento</b><br>Tecnologia que transforma experiências.<br>PHILA: gestão de filas e atendimento.<br>Totem OrbitaComet · Engenharia sob medida<br>Fale com a gente 👇<br><span class="lk">🔗 wa.me/5537999322040 e mais 1</span></div>
<div class="hl">{hls}</div><div class="g">{cells}</div></body></html>'''
p = R/'gerador/.tmp/previa.html'; p.parent.mkdir(exist_ok=True); p.write_text(html, encoding='utf-8')
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 900, 'height': 800}); pg.goto(p.as_uri()); pg.wait_for_timeout(800)
    pg.screenshot(path=str(R/'previa_perfil.png'), full_page=True); b.close()
from PIL import Image
Image.open(R/'previa_perfil.png').convert('RGB').save(R/'previa_perfil.jpg', quality=90); (R/'previa_perfil.png').unlink()
