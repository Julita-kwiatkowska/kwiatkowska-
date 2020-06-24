import random
class Kwadrat():
    def __init__(self, bok): # konstruktor jak się dowiedzieliśmy jest metodą prywatną, nie można go wywołać na obiekcie klasy po kropce, ani po za klasą
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)

class KolorowyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y): # chyba kolorowy?
        fill(243,20,20,50)   # to nadaje kolor
        Kwadrat.sketch(self, x, y) # korzystamy z metody klasy bazowej

class PasiastyKwadrat(Kwadrat): # dziedziczymy po klasie Kwadrat aby móć skorzystać z jej funkcjonalności
    def sketchPasiasty(self, x, y, paski): # dodajemy ilość pasków, w które ma być kwadrat
        Kwadrat.sketch(self, x, y) # korzystamy z metody klasy bazowej
        space = self.bok/paski # wyliczamy przerwęmiędzy paskami
        _xLinii_ = 0 # to jest pole chronione, nie powinno się go używać w kodzie po za klaą i klasami po niej dziedziczącymi 
        for pasek in range(0, paski): # dorysowujemy paski
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
        # zamiast powtarzać warunek dodajemy wytabowaną pod nim linię - dalej tam obowiązuje
        #    _xLinii_ = fill(243,20,20,50) # przypisujesz do zmiennej kolor, po czym jej nie używasz i przypisujesz w następnej klatce znów wartość liczbową? działąnie nie ma sensu, a zajmuje programowi czas procesora


        
            
def setup():
    size(500, 500)
    kolorowyKwadrat = Kwadrat(50.0)
    kolorowyKwadrat.sketch(100,100)
    #kolorowyKwadrat.sketchKolorowy(500,200,10)
    malyKwadrat = Kwadrat(50.0) # obiekt typu kwardrat o wielkości 50
    malyKwadrat.sketch(200, 300) # rysujemy go w podanych wsółrzędnych
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyKwadrat.sketch(100, 200) # rysujemy kwadrat wielkości 50 również w innych współrzędnych
    malyPasiastyKwadrat = PasiastyKwadrat(30.0) # tu tworzymy obiekt typu pasiasty kwadrat korzystając z konstruktora klasy bazowej
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5) # umieszczamy stworzony kwadrat w 5 pasków w tych współrzędnych
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) # a teraz w 8 pasów w innych współrzędnych
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(300, 50, 12)
    duzyPasiastyKwadrat.sketch(350, 300) # na obiekcie typu klasy pochodnej można wywołać metodę klasy bazowej ( rysujemy kwadrat bez pasków )
    
    kolorowy = KolorowyKwadrat(50) # to dopiero jest obiekt Twojej klasy
    kolorowy.sketchPasiasty(50,50) # a to jego narysowanie w podanej pozycji
    
# 0,5 pkt
