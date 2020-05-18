import random 
add_library('pdf') 
def setup():
    global zdjecie
    global czapka
    global okulary
    textSize(10)
    size(400, 400) #  to nie są proporcje zdjęcia dokumentowego
   
    zdjecie = loadImage("kobieta.jpg") 
    okulary = loadImage("okulary.png")
    czapka = loadImage("czapka.png")
    
    
    print(random.random()) 
    print(type(zdjecie)) 
    print(type(okulary))
    print(type(czapka))
    fill(20,255,200) 

def draw():
    global zdjecie
    global czapka
    global okulary
    image(zdjecie, 0,0, height, width)
    fill(0,0,0)
    text("Nacisnij strzalke \n <- oraz -> \n aby wybrac\n dodatek",10,20)
    if keyPressed:
         beginRecord(PDF, "kobieta2.pdf") # jeśi zaczniesz po napisie, to nie zarejestruje się on na pliku wyjściowym, a o to chodzi
         if keyCode==RIGHT:
            image(zdjecie, 0,0, height, width)
            image(okulary,-20,60, height/2+250, width/2+100)
            print(type(okulary))       
                    
         if keyCode==LEFT :
            image(zdjecie, 0,0, height, width)
            image(czapka, 30,-90, height/2+150, width/2+50)
            print(type(czapka)) 
         endRecord() # tu będzie logiczniej   

def mousePressed():
    exit()
    
# 1,75p
