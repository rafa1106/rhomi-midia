import json, os, re, html
R='rhomi-midia'; E='entrega/06_instagram'
NOTAS=[('frente_','Simulador do site: arte aprovada da frente; tela desligada.','ok'),
 ('o15-horizontal-e-vertical-tela-desligada','Render: tela desligada.','ok'),
 ('p01-abertura','Render: tela desligada.','ok'),
 ('o02-abertura','Render: tela COM interface (boas-vindas do vídeo 1).','tela'),
 ('lp07','Render: 4 telas COM interfaces.','tela'), ('h08-close-led','Render: telas COM interfaces.','tela'),
 ('o08-tela-touch','Render: close da tela COM interface Lumivida (vacinação).','tela'),
 ('p19-ecossistema','Composição: totem e telas COM interfaces reais do PHILA.','tela'),
 ('lp06','Close da impressora: tela não aparece.','ok'),
 ('p03-chegada','Foto de IA: tela do totem com a interface H06 composta (aprovada no vídeo 3).','tela'),
 ('p16-emissao-computador','Foto de IA: totem pequeno ao fundo, à direita.','ia'),
 ('p16-emissao-totem','Foto de IA: tela do totem com interface. Conferir de perto.','ia'),
 ('lp09','Foto de IA: tela do totem com interface composta. Conferir de perto.','ia'),
 ('lp15','Foto de IA: totem ao fundo com tela gerada pela IA.','ia'),
 ('lp16','Foto de IA: tela do totem gerada pela IA (texto pode estar deformado).','ia'),
 ('lp17','Foto de IA: tela do totem gerada pela IA (texto pode estar deformado).','ia'),
 ('lp18','Foto de IA: tela do totem gerada pela IA (texto pode estar deformado).','ia'),
 ('lp19','Foto de IA: tela do totem gerada pela IA (texto pode estar deformado).','ia'),
 ('a02-','Foto de IA: tela do totem gerada pela IA (texto pode estar deformado).','ia'),
 ('a08-','Foto de IA: tela do totem gerada pela IA (texto pode estar deformado).','ia'),
 ('o05-','Foto de IA: tela do totem gerada pela IA (texto pode estar deformado).','ia')]
def nota(srcs):
    out=[]
    for s in srcs:
        for p,t,c in NOTAS:
            if s.startswith(p): out.append((t,c)); break
    return out
plano=[('01','24/11 · 09h00','p1124a_rhomi'),('02','24/11 · 09h30','p1124b_orbitacomet'),('03','24/11 · 10h00','p1124c_jornada'),('04','24/11 · 10h30','p1124d_led'),
       ('05','24/11 · 11h00','p1124e_emissao'),('06','24/11 · 11h30','REEL'),('07','qui 26/11 · 11h00','p1126_horizontal'),('08','sex 27/11 · 11h00','p1127_sinais'),
       ('09','ter 01/12 · 11h00','p1201_chamada'),('10','qui 03/12 · 11h00','p1203_frente'),('11','sex 04/12 · 11h00','p1204_clinica'),('12','ter 08/12 · 11h00','p1208_gestao')]
F=json.load(open(f'{R}/artes/_fontes.json'))
pastas={d.split('_')[0]:d for d in os.listdir(f'{E}/primeira_leva') if os.path.isdir(f'{E}/primeira_leva/'+d)}
cards=''
for n,quando,k in plano:
    pasta=pastas[n]; leg=open(f'{E}/primeira_leva/{pasta}/legenda.txt').read()
    if k=='REEL':
        slides=f'<figure><video src="primeira_leva/{pasta}/reel.mp4" controls preload="metadata" poster="primeira_leva/{pasta}/capa.jpg"></video><figcaption><span class="tela">Vídeo 4b (aprovado em 13/11): telas COM interface; letreiro "OrbitaComet + PHILA".</span></figcaption></figure>'
        tit='Reel: A evolução do seu atendimento'
    else:
        tit=open(f'{R}/gerador/{k}.py').read().splitlines()[0].lstrip('# ')
        slides=''
        for f in sorted(x for x in os.listdir(f'{E}/primeira_leva/{pasta}') if x.endswith('.jpg')):
            nn=f[6:8]; ns=nota(F.get(f'{k}_{nn}',[]))
            cap=''.join(f'<span class="{c}">{html.escape(t)}</span>' for t,c in ns) or '<span class="ok">Sem totem com tela.</span>'
            slides+=f'<figure><a href="primeira_leva/{pasta}/{f}" target="_blank"><img src="primeira_leva/{pasta}/{f}" loading="lazy"></a><figcaption><b>{nn}</b>{cap}</figcaption></figure>'
    cards+=f'<section><h2><span>{n}</span> {html.escape(tit)}</h2><p class="q">{quando}</p><div class="sl">{slides}</div><details><summary>Legenda</summary><pre>{html.escape(leg)}</pre></details></section>'
# destaques
for d,nome in [('1_rhomi','RHOMI'),('2_phila','PHILA'),('3_orbitacomet','OrbitaComet'),('4_aplicacoes','Aplicações'),('5_contato','Contato')]:
    FD=json.load(open(f'{R}/destaques/{d}/_fontes.json')); slides=''
    for f in sorted(x for x in os.listdir(f'{E}/destaques/{d}') if x.endswith('.jpg')):
        ns=nota(FD.get(f[:-4],[])); cap=''.join(f'<span class="{c}">{html.escape(t)}</span>' for t,c in ns) or '<span class="ok">Sem totem com tela.</span>'
        slides+=f'<figure class="st"><a href="destaques/{d}/{f}" target="_blank"><img src="destaques/{d}/{f}" loading="lazy"></a><figcaption><b>{f[6:8]}</b>{cap}</figcaption></figure>'
    cards+=f'<section><h2><span>D</span> Destaque {nome}</h2><div class="sl">{slides}</div></section>'
page=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Revisão · Instagram @rhomi.tech</title><style>
body{{margin:0;background:#111113;color:#eee;font:15px/1.5 system-ui,sans-serif}} header{{padding:28px 40px;border-bottom:1px solid #2b2b2f}}
h1{{font:500 26px system-ui;margin:0 0 8px}} .leg span{{margin-right:18px}} section{{padding:26px 40px;border-bottom:1px solid #2b2b2f}}
h2{{font:500 21px system-ui;margin:0}} h2 span{{color:#F7A600;margin-right:8px}} .q{{color:#999;margin:4px 0 14px}}
.sl{{display:flex;flex-wrap:wrap;gap:18px}} figure{{margin:0;width:420px}} figure.st{{width:300px}} img,video{{width:100%;border-radius:6px;display:block}} video{{max-height:640px;width:auto}}
figcaption{{font-size:13px;margin-top:6px}} figcaption b{{margin-right:6px}} figcaption span{{display:block;padding:3px 8px;border-radius:4px;margin-top:4px}}
.ok{{background:#1d2a1d;color:#9fd49f}} .tela{{background:#2e2610;color:#f5c96a}} .ia{{background:#3a1d1d;color:#ff9c9c}}
pre{{white-space:pre-wrap;background:#1b1b1e;padding:14px;border-radius:6px;max-width:860px}} summary{{cursor:pointer;color:#bbb;margin-top:14px}}
</style></head><body><header><h1>Revisão da primeira leva · Instagram @rhomi.tech</h1>
<div>Clique numa imagem para abrir em tamanho real. Cada slide mostra de onde vem a imagem e o estado da tela do totem:</div>
<div class="leg" style="margin-top:8px"><span class="ok" style="padding:2px 8px;border-radius:4px">sem tela ou tela desligada</span><span class="tela" style="padding:2px 8px;border-radius:4px">tela com interface (render ou composição)</span><span class="ia" style="padding:2px 8px;border-radius:4px">tela feita pela IA: conferir de perto</span></div></header>
{cards}</body></html>'''
open(f'{E}/REVISAO.html','w').write(page); print('ok')
