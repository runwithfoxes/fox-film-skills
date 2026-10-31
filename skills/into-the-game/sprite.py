# Our chunky game fox, traced from our reference picture so he keeps his own head, ears and proportions.
# It is here as a worked example. Read the points off your own character and change them.
# Points are read off that picture (1500 x 2000). The eyes, nose and mouth are placed by hand, pixel by pixel.
from PIL import Image, ImageDraw
import numpy as np
C=dict(line=(44,20,20),o=(228,92,26),oh=(248,140,54),od=(170,56,20),cream=(255,240,222),creamd=(226,194,168),
 ear=(232,204,192),eard=(120,62,44),y=(255,200,24),yd=(214,140,14),pupil=(30,14,12),white=(255,255,255),
 hood=(78,76,84),hoodh=(104,102,112),hoodd=(52,50,58),str=(206,204,200),jean=(44,62,108),jeand=(30,42,78),cuff=(116,122,136),
 paw=(84,38,28),pawh=(122,62,44),pad=(204,104,56))
HS=1.18  # his head is drawn a touch bigger than the reference, as game characters are, which gives the eyes room
def hs(p): return (750+(p[0]-750)*HS,900+(p[1]-900)*HS)
def build(HT=70,PAD=3):
    X0,Y0,X1,Y1=90,-115,1440,1895; sc=HT/(Y1-Y0); W=round((X1-X0)*sc)+PAD*2; H=HT+PAD*2; SS=8
    def g(p): return ((p[0]-X0)*sc+PAD,(p[1]-Y0)*sc+PAD)
    def spline(pts,n=10):
        P=[np.array(p,float) for p in pts]; L=len(P); out=[]
        for i in range(L):
            a,b,c,d=P[(i-1)%L],P[i],P[(i+1)%L],P[(i+2)%L]
            for t in np.linspace(0,1,n,endpoint=False): out.append(tuple(0.5*((2*b)+(-a+c)*t+(2*a-5*b+4*c-d)*t*t+(-a+3*b-3*c+d)*t*t*t)))
        return out
    def mask(pts,smooth=True):
        pp=[g(p) for p in pts]; pp=spline(pp) if smooth else pp
        im=Image.new("L",(W*SS,H*SS),0); ImageDraw.Draw(im).polygon([(x*SS,y*SS) for x,y in pp],fill=255)
        return np.array(im.resize((W,H),Image.BOX))>127
    def ell(cx,cy,rx,ry): return mask([(cx+rx*np.cos(t),cy+ry*np.sin(t)) for t in np.linspace(0,6.283,36,endpoint=False)],False)
    im=np.zeros((H,W,4),"uint8")
    def put(m,c): im[m,:3]=C[c]; im[m,3]=255
    def sh(m,dx,dy):
        o=np.zeros_like(m); ys,xs=np.where(m); y2,x2=ys+dy,xs+dx; k=(y2>=0)&(y2<H)&(x2>=0)&(x2<W); o[y2[k],x2[k]]=True; return o
    def part(m,b,s=None,sd=(-1,-1),h=None,hd=(1,1)):
        put(m,b)
        if s: put(m&~sh(m,*sd),s)
        if h: put(m&~sh(m,*hd),h)
    tail=mask([(1000,1640),(1170,1525),(1330,1515),(1436,1590),(1425,1705),(1300,1800),(1150,1868),(1030,1840)])
    part(tail,"o","od",(-1,-2)); put(tail&mask([(1255,1500),(1450,1500),(1450,1760),(1290,1800)],False),"cream")
    legL=mask([(465,1470),(700,1470),(690,1745),(468,1745)],False); legR=mask([(800,1470),(1035,1470),(1035,1745),(808,1745)],False)
    part(legL,"jean","jeand",(-1,0)); part(legR,"jean","jeand",(1,0))
    put(mask([(462,1735),(694,1735),(692,1808),(462,1808)],False),"cuff"); put(mask([(804,1735),(1036,1735),(1034,1808),(806,1808)],False),"cuff")
    fL=ell(515,1825,152,72); fR=ell(975,1825,150,72); part(fL,"paw","line",(0,-1)); part(fR,"paw","line",(0,-1))
    body=mask([(405,925),(1060,925),(1200,1250),(1205,1365),(1050,1400),(1040,1500),(460,1500),(450,1400),(295,1370),(290,1270)])
    part(body,"hood","hoodd",(-1,-2),"hoodh",(0,1))
    for x0,x1 in ((438,452),(1040,1056)):
        put(mask([(x0,1120),(x1,1120),(x1,1395),(x0,1395)],False)&body,"hoodd")
    pk=mask([(520,1375),(632,1225),(875,1220),(985,1375)],False); put(pk&~sh(pk,0,1),"hoodd")
    put(mask([(460,1440),(1040,1440),(1040,1456),(460,1456)],False),"hoodd")
    put(mask([(530,905),(970,905),(750,1015)],False),"cream")
    for x in (660,840):
        a0=int(round(g((x,0))[0])); put(np.array([[a0==xx and g((0,1000))[1]<=yy<=g((0,1150))[1] for xx in range(W)] for yy in range(H)]),"str")
    pL=mask([(306,1395),(450,1395),(452,1500),(425,1575),(345,1580),(310,1500)]); pR=mask([(1052,1395),(1196,1395),(1190,1500),(1150,1578),(1075,1575),(1048,1500)])
    part(pL,"paw","line",(0,-1)); part(pR,"paw","line",(0,-1))
    mhead=lambda pts,smooth=True: mask([hs(p) for p in pts],smooth)
    # ears: big, with brown backs running down the outer edge
    eL=mhead([(300,50),(430,95),(600,235),(420,320),(330,430),(278,300),(268,130)]); eR=mhead([(1200,45),(1075,90),(895,235),(1080,320),(1172,430),(1226,300),(1236,130)])
    put(eL,"eard"); put(eR,"eard")
    put(mhead([(322,120),(520,250),(400,350),(330,360),(312,240)]),"ear"); put(mhead([(1178,115),(985,250),(1105,350),(1172,360),(1192,240)]),"ear")
    put(mhead([(470,190),(600,235),(470,330),(420,250)],False),"o"); put(mhead([(1030,190),(895,235),(1030,330),(1080,250)],False),"o")
    head=mhead([(330,400),(420,300),(600,205),(750,190),(900,205),(1080,300),(1180,400),(1235,530),(1305,682),(1245,725),(1190,805),(1040,875),(750,905),(460,875),(310,805),(255,725),(196,695),(268,530)])
    part(head,"o","od",(0,-1),"oh",(0,2))
    ck=mhead([(205,697),(390,668),(590,650),(690,612),(810,612),(910,650),(1110,668),(1296,684),(1245,725),(1190,805),(1040,875),(750,905),(460,875),(310,805),(255,725)])
    put(ck,"cream"); put(ck&~sh(ck,0,-1),"creamd")
    # face, by hand. L line, y yellow, d dark yellow, P pupil, W catch light, . leave
    def stamp(x0,y0,rows):
        for j,r in enumerate(rows):
            for i,c in enumerate(r):
                k={"L":"line","y":"y","d":"yd","P":"pupil","W":"white","b":"od","n":"line","h":"pawh","m":"line","c":"creamd"}.get(c)
                if k: im[y0+j,x0+i,:3]=C[k]; im[y0+j,x0+i,3]=255
    L=[".bbbbbbbbb.",
       "LLLLLLLLLLL",
       ".yyyyPPWPy.",
       ".yyyyPPPPy.",
       "..yyyPPPy..",
       "...ddddd..."]
    R=[".bbbbbbbbb.",
       "LLLLLLLLLLL",
       ".yPPWPyyyy.",
       ".yPPPPyyyy.",
       "..yPPPyyy..",
       "...ddddd..."]
    gx=lambda x:int(round(g((x,0))[0])); gy=lambda y:int(round(g((0,y))[1]))
    stamp(gx(337),gy(469),L); stamp(gx(842),gy(469),R)
    nx=gx(750)-2; ny=gy(582)
    stamp(nx,ny,[".nnn.","nhnnn",".nnn.","..n..","..m..",".m.m."])
    # toes
    for cx in (515,975):
        for dx in (-50,0,50):
            a=gx(cx+dx); b=gy(1800)
            im[b+1:b+3,a,:3]=C["line"]
    for cx in (440,515,590,900,975,1050):
        a=gx(cx); b=gy(1870); im[b,a:a+2,:3]=C["pad"]
    # outline
    a=im[...,3]>0; b=a|sh(a,1,0)|sh(a,-1,0)|sh(a,0,1)|sh(a,0,-1); o=b&~a; im[o,:3]=C["line"]; im[o,3]=255
    return Image.fromarray(im,"RGBA")
if __name__=="__main__":
    f=build(HT=72); f.save("fox-sprite.png"); print(f.size)
