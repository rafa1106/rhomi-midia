# Compõe o OrbitaComet com uma frente aprovada (camadas do simulador do site): base + frente (multiply) + tela opcional + LED (screen).
# Uso: python3 automacao/compor_frente.py  -> fontes/img/frente_<arte>.jpg (864x1080, tela desligada)
import numpy as np, sys, os
from PIL import Image
SIM=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'fontes','simulador')
OUT=os.path.join(os.path.dirname(SIM),'img')
B=np.asarray(Image.open(f'{SIM}/o12-simulador-led/o12-sim-base-1920.jpg').convert('RGB'),dtype=np.float32)/255
LUZ=np.asarray(Image.open(f'{SIM}/o12-simulador-led/o12-sim-led-luz-1920.png').convert('L'),dtype=np.float32)/255
MIO=np.asarray(Image.open(f'{SIM}/o12-simulador-led/o12-sim-led-miolo-1920.png').convert('L'),dtype=np.float32)/255
def cores(hexc):
    r,g,b=[int(hexc[i:i+2],16)/255 for i in (1,3,5)]
    rgb=np.array([r,g,b]); k=0.75/np.sqrt(max(0.2126*r+0.7152*g+0.0722*b,0.25)); c=rgb**2.2*k
    luz=np.minimum(c/1.5,1)**(1/2.2); mio=np.minimum(0.75+0.25*c/c.max(),1)**(1/2.2); return luz,mio
def comp(frente=None, led=None, tela=None):
    o=B.copy()
    if frente:
        F=np.asarray(Image.open(f'{SIM}/o13-simulador-frente/o13-sim-frente-{frente}-1920.png').convert('RGBA'),dtype=np.float32)/255
        a=F[...,3:]; o=o*(1-a)+o*F[...,:3]*a
    if tela:
        T=np.asarray(Image.open(f'{SIM}/o14-simulador-tela/o14-sim-tela-{tela}-1920.png').convert('RGBA'),dtype=np.float32)/255
        a=T[...,3:]; o=o*(1-a)+T[...,:3]*a
    if led:
        luz,mio=cores(led)
        for L,cc in ((LUZ,luz),(MIO,mio)):
            s=L[...,None]*cc; o=1-(1-o)*(1-s)
    return Image.fromarray((np.clip(o,0,1)*255+.5).astype(np.uint8))
COMBOS=[('21-lumivida','#18D2C4','Lumivida','turquesa'),('22-ourela','#FFB000','Ourela','âmbar'),('23-aguas-serenas','#2F6BFF','Águas Serenas','azul'),
        ('24-essenza','#8A3FFC','Essenza','violeta'),('25-valoren','#8A3FFC','Valoren','violeta'),('26-cartorio','#FFFFFF','Cartório','branco'),
        ('27-phila','#36D45A','PHILA','verde'),('28-bem-vindo','#FFB000','Bem-vindo','âmbar')]
if __name__=='__main__':
    for fid,hx,n,c in COMBOS:
        im=comp(fid,hx); im.crop((518,0,1382,1080)).save(f'{OUT}/frente_{fid}.jpg',quality=93)
