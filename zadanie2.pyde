def setup():
    size(700,700)
    stroke(256,0,0)
    global wysokosc
    wysokosc = 0
    strokeWeight(2)
    fill(0,0,255)
    global natezenie
    natezenie = 0
    global natezenie
    global szerokosc
    szerokosc = 335
    global szybkoscw
    global szybkoscs
    szybkoscw = 6
    szybkoscs = 6

def draw():
    global natezenie
    natezenie = natezenie + 1
    if natezenie==250:
        natezenie==0
    global wysokosc
    global szerokosc
    global szybkoscw
    global szybkoscs
    
    szerokosc = szerokosc + szybkoscs
    if(szerokosc> width or szerokosc <0):
        szybkoscs = szybkoscs*-1
        
    wysokosc = wysokosc + szybkoscw
    if(wysokosc > height or wysokosc <0):
        szybkoscw= szybkoscw*-1
    
    fill(0,0,natezenie,120)
    rect(szerokosc ,wysokosc,30,30)
    
    
def mousePressed():
    exit()
