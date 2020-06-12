import random 
add_library('pdf')
def setup():
    global zdjecie
    global ramka
    global ramka2
    textSize(20)
    size(400,400)
    
    zdjecie = loadImage("pie.jpg")
    ramka = loadImage("ramka.png")
    ramka2 = loadImage("ramka niebieska.png")
    
    print(random.random())
    print(type(zdjecie))
    print(type(ramka))
    print(type(ramka2))

def draw():
    global zdjecie
    global ramka
    global ramka2



    try:
        image(zdjecie, 0, 0, height, width)
    except:
        fill(128,0,128)
        text ("Pies jest na spacerze" ,100,200)
        image(ramka,0,0, height , width)
    else:
        image(ramka2,0,0, height, width)

def mouseClicked():
    exit()
        
    
