def setup():
    c=color(112,600,120)
    size(400,600)

    fill(c)

    
def draw():
    point(50,50)
    #rect(50,50, mouseX,mouseY)
    print(mouseX)
    print(mouseY)
    print(mousePressed)
    line(mouseX,mouseY,300,300)
    
    if mousePressed:
        print(mouseX)
        print(mouseY)
        rect(30,60, height, width)
    else:
        clear()
        print(300,500)

    
        
    
    
    
        
    
    
    
    
