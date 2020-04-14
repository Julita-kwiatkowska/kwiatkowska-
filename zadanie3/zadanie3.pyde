def setup():
    size(500,500)
    textSize(100)
    background(0)
    global kolor_defoultowy, kolor_zaznaczenia # oczywiście nie są niezbędne, ale dzięki wprowadzeniu zmiennych nie trzeba pamiętać wartości i kod staje się czytelniejszy
    kolor_defoultowy = (0,255,0,255)
    kolor_zaznaczenia = (255,0,0,255)
    global czyKklikniete # w jednej klatce tylko jeden klawisz na raz może być odczytany że kliknięty, więc sprawdzając, czy jedno kliknięte bezpośrednio po drugim trzeba pamiętać, czy to co nas interesuje było kliknięte poprzednio
    czyKklikniete = False
def draw():
    clear()
    global czyKklikniete
    fill(*kolor_defoultowy)
    text("J", width/2-100,height/3)
    text("K", width/2-50, height/3)
     
    if mouseX<200 and mouseX>150 and mouseY<200 and mouseY>90:
        fill(*kolor_zaznaczenia)
        text ("J" , width/2-100, height/3)
    if keyPressed:
        if key == 'k' or key =='K':
            fill(*kolor_zaznaczenia)
            text("K", width/2-50, height/3)
            czyKklikniete = True
       
        if key == CODED:
            if keyCode==RIGHT and mouseX<200 and mouseX>150 and mouseY<200 and mouseY>90:
                fill(*kolor_zaznaczenia)
                text("K", width/2-50, height/3)
                fill(*kolor_defoultowy)
                text ("J" , width/2-100, height/3)
            if keyCode==LEFT and czyKklikniete:
                fill(*kolor_defoultowy)
                text("K", width/2-50, height/3)
                fill(*kolor_zaznaczenia)
                text ("J" , width/2-100, height/3)
    else:
        czyKklikniete = False
            
    l = createShape()
    l.beginShape()
    l.fill(255,0,0,127)
    l.stroke(0,255,0,200)
    l.vertex(50, 400)
    l.vertex(50, 200)
    l.vertex(400, 400)
    l.vertex(400, 200)
    l.endShape(CLOSE)
    fill(0,0,255,255) # ostatnia linijka ten kształt rysuje, więc nadanie mu koloru powinno nastąpić wcześniej
    shape(l, 25, 25)
    
#1,75
# za to, że strzałki nie działały przy literze 'k'. Przeanalizuj, co teraz się dzieje po zmianach w Twoim kodzie i sprawdź, jak teraz działa ;)
