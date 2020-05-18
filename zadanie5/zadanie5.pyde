class Trojkat():
    
    def __init__(self, n):
        self.name = n
        self.klikniety = False
    def rysuj_trojkat(self): # gdyby podać jako argumenty, możńaby kolejne trójkąty rysować w innych lokalizacjach
        triangle(100, 350, 400, 350, 250, 100)
    def kliknij_trojkat(self):
        self.klikniety = not self.klikniety 
        if self.klikniety:
            fill(255,0,0)
        else:
            fill(225,0,225)
    def nazwa_trojkata(self):
        text("trojkat",170,400)
        
def setup():
    size(500, 500)
    global trojkat
    trojkat=Trojkat("nazwa") # miało być stworzenie dwóch obiektów (wóczas by wyszło, że pewne rzeczy są tu nie do końca dopracowane..)
    background(255) 
    textSize(50)
    
def mouseClicked():
    trojkat.kliknij_trojkat()
    
def draw():
    Trojkat.rysuj_trojkat(trojkat)
    trojkat.nazwa_trojkata()

# 1pkt, mało oryginalne, metody mocno wzorowane na moich, przy większej liczbie obiektów by nie działało, przez co klasa traci sens
