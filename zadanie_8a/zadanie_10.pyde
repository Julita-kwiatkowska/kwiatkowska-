import unittest 
class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): # przejrzenie zasobu
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook):
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False


class Julita():
    book = ""
    haveBook = False
    def wypozyczKsiazka(self,ksiazka):
        print("Wybrałeś książke")
        self.ksiazka = ksiazka
        self.maszksiazke = True
        return self.ksiazka
    def returnKsiazka(self):
        print("Ksiazka, ktora zwracasz, to {}".forma(self.ksiazka))
        if self.maszksiazke:
            self.maszksiazke= False
            return self.ksiazka
        else:
            self.ksiazka = ""
            return False

def setup():
    size(220,100)
    global library, Madzia , Julita
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter","Hobbit","Lalka"]
    library = Library(books)
    Madzia = Customer()
    library = Library(books)
    Julita = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked():
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())

class Test(unittest.TestCase):
    
    def test_wypozyczenie(self):
        lib = Library([ "Lalka","Harry Potter", "Wyrok","Sens Sztuki"])
        lib.lendBook("Harry Potter")
        self.assertEqual(lib.availableBooks, ["Lalka", "Wyrok", "Sens Sztuki"])
   
    def test_oddanie(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Hobbit"]
        library = Library(books)
        Julek = Customer()
        library.addBook(Julek.returnBook())
        self.assertEqual(False, Julek.haveBook) 
    
    def test_na_spacje(self):
        s = 'sens sztuki'
        self.assertEqual(s.split(), ['sens', 'sztuki'])
        with self.assertRaises(TypeError):
            s.split(2)
        
if __name__=='__main__':
    unittest.main()
    
    
    
    
