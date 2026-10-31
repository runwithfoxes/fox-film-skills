# A chunky pixel character in a game level, the picture you give the model. No model and no spend: every pixel placed in code on a 213 x 120 grid,
# then blown up six times, so each game pixel is six real pixels on a 1280 x 720 frame.
from PIL import Image, ImageDraw
import numpy as np
W,H=213,120; K=6
C=dict(line=(44,20,20),o=(232,98,28),oh=(250,146,58),od=(176,60,20),cream=(255,240,222),creamd=(226,196,170),
 ear=(226,196,186),y=(255,206,28),pupil=(30,14,12),white=(255,255,255),hood=(92,96,110),hoodh=(128,132,146),hoodd=(62,64,78),
 jean=(52,86,150),jeand=(36,60,112),paw=(84,40,30),
 sky1=(10,10,30),sky2=(20,14,48),sky3=(44,16,64),cloud=(70,40,100),cloudd=(44,26,76),hill=(26,22,70),hilld=(40,30,96),
 grass=(230,30,60),grassd=(130,16,50),dirt=(30,18,44),dirtd=(52,28,72),brick=(190,30,60),brickd=(110,14,44),gold=(255,206,40),goldd=(214,146,20),goldh=(255,240,150))
g=np.zeros((H,W,3),"uint8")
def rect(x0,y0,x1,y1,c):
    g[max(y0,0):y1+1,max(x0,0):x1+1]=C[c]
# sky in hard bands, no gradient
rect(0,0,W-1,44,"sky1"); rect(0,45,W-1,70,"sky2"); rect(0,71,W-1,H-1,"sky3")
def blob(cx,cy,rx,ry,c):
    y,x=np.ogrid[:H,:W]; m=((x-cx)/rx)**2+((y-cy)/ry)**2<=1; g[m]=C[c]
for cx,cy,s in ((36,22,1.0),(150,14,.8),(196,34,.7)):
    for dx,dy,r in ((-10,2,6),(-2,-2,9),(8,1,7),(15,3,4)):
        blob(cx+dx*s,cy+dy*s+1,r*s+1,r*s*.75+1,"cloudd")
    for dx,dy,r in ((-10,2,6),(-2,-2,9),(8,1,7),(15,3,4)):
        blob(cx+dx*s,cy+dy*s,r*s+1,r*s*.75+1,"cloud")
import random
random.seed(7)
for _ in range(70):
    sx,sy=random.randrange(W),random.randrange(60)
    g[sy,sx]=random.choice([(255,255,255),(150,190,255),(255,120,150)])
# hills
y,x=np.ogrid[:H,:W]
for cx,r,c,d in ((30,44,"hilld","hill"),(120,58,"hill","hilld"),(205,40,"hilld","hill")):
    m=(x-cx)**2+((y-104)*1.5)**2<=r*r; g[m]=C[c]
    for yy in range(70,100,6):
        for xx in range(cx-20,cx+20,9):
            if 0<=xx<W and tuple(g[yy,xx])==C[c] and (xx+yy)%3==0: g[yy,xx]=C[d]; g[yy,min(xx+1,W-1)]=C[d]
# ground
GY=98
rect(0,GY,W-1,H-1,"dirt"); rect(0,GY,W-1,GY+2,"grass"); rect(0,GY+3,W-1,GY+3,"grassd")
for yy in range(GY+7,H,6):
    for xx in range((yy//6)%2*5,W,10): rect(xx,yy,xx+3,yy+1,"dirtd")
for xx in range(0,W,5):
    if xx%15==0: g[GY-1,xx]=C["grass"]; g[GY-2,xx]=C["grass"]
# floating bricks, a gold block, coins
def brick(x,y):
    rect(x,y,x+11,y+11,"brick"); rect(x,y,x+11,y,"line"); rect(x,y+11,x+11,y+11,"line"); rect(x,y,x,y+11,"line"); rect(x+11,y,x+11,y+11,"line")
    rect(x+1,y+4,x+10,y+4,"brickd"); rect(x+1,y+8,x+10,y+8,"brickd"); rect(x+5,y+1,x+5,y+3,"brickd"); rect(x+3,y+5,x+3,y+7,"brickd"); rect(x+8,y+5,x+8,y+7,"brickd"); rect(x+5,y+9,x+5,y+10,"brickd")
def gold(x,y):
    rect(x,y,x+11,y+11,"line"); rect(x+1,y+1,x+10,y+10,"gold"); rect(x+1,y+1,x+10,y+1,"goldh"); rect(x+1,y+1,x+1,y+10,"goldh"); rect(x+2,y+10,x+10,y+10,"goldd"); rect(x+10,y+2,x+10,y+10,"goldd")
    for a,b in ((3,3),(8,3),(3,8),(8,8)): g[y+b,x+a]=C["goldd"]
    rect(x+5,y+4,x+6,y+7,"line")
for i in (0,1): brick(120+i*12,52)
gold(144,52); brick(156,52)
def coin(x,y):
    rect(x+1,y,x+4,y,"line"); rect(x+1,y+7,x+4,y+7,"line"); rect(x,y+1,x,y+6,"line"); rect(x+5,y+1,x+5,y+6,"line")
    rect(x+1,y+1,x+4,y+6,"gold"); rect(x+1,y+1,x+1,y+6,"goldh"); rect(x+3,y+2,x+3,y+5,"goldd")
for i in range(4): coin(126+i*10,38)
def px(x,y,c): g[y,x]=C[c]
# THE FOX, traced from our own reference picture in sprite.py
import sprite
f=sprite.build(HT=72); FX,FY=26,GY-f.height+3
fa=np.array(f)
for y in range(f.height):
    for x in range(f.width):
        if fa[y,x,3]: g[FY+y,FX+x]=fa[y,x,:3]
# shadow under him
rect(FX+12,GY,FX+48,GY,"grassd")
# coins and hearts top left, score drawn in our own blocks
for i in range(3):
    x=8+i*10; y=7
    for (a0,b0,a1,b1) in ((1,0,2,0),(5,0,6,0),(0,1,7,3),(1,4,6,4),(2,5,5,5),(3,6,4,6)): rect(x+a0,y+b0,x+a1,y+b1,"line")
    for (a0,b0,a1,b1) in ((1,1,2,1),(5,1,6,1),(1,2,6,3),(2,4,5,4),(3,5,4,5)): rect(x+a0,y+b0,x+a1,y+b1,"od" if i==3 else "o")
coin(190,6)
Image.fromarray(g).save("level-213.png")
big=np.array(Image.fromarray(g).resize((W*K,H*K),Image.NEAREST)).astype(float)
big[::3]*=0.82   # CRT scanlines
Image.fromarray(big.astype("uint8")).save("level-1278.png")
