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
    line(mouseX,mouseY,width/2,width/2)
    
    if mousePressed:
        print(mouseX)
        print(mouseY)
        rect(30,60, height, width)
    else:
        clear()
        print(300,500)
        
#użycie koordynatów myszy nie jest widoczne po efekcie w programie (jedynie na konsoli)
# 1,75pkt
    
        
    
    
    
        
    
    
    
    
