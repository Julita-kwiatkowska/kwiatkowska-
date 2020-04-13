def setup():
    size(500,500)
    textSize(100)
    background(0)

def draw():
    clear()
    fill(0,255,0,255)
    text("J", width/2-100,height/3)
    text("K", width/2-50, height/3)

    if keyPressed:
        if key == 'k':
            fill(255,0,0,255)
            text("K", width/2-50, height/3)
            
    if mouseX<200 and mouseX>150 and mouseY<200 and mouseY>90:
        fill(255,0,0,255)
        text ("J" , width/2-100, height/3)
    if keyPressed:
        if key == CODED:
            if keyCode==RIGHT and mouseX<200 and mouseX>150 and mouseY<200 and mouseY>90:
                fill(255,0,0,255)
                text("K", width/2-50, height/3)
    l = createShape()
    l.beginShape()
    l.fill(255,0,0,127)
    l.stroke(0,255,0,200)
    l.vertex(50, 400)
    l.vertex(50, 200)
    l.vertex(400, 400)
    l.vertex(400, 200)
    l.endShape(CLOSE)
    shape(l, 25, 25)

                
        
    fill(0,0,255,255)
    #KSZTAŁT
#s = createShape() 
