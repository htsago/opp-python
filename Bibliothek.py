class Buch:
    def __init__(self, titel, autor,isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn

    def zeige_info(self):
        return f"Titel: {self.titel}, Autor: {self.autor}, ISBN: {self.isbn}"

class Bibliothek:
    
    def __init__(self):
        self.buecher = []
        
    def buch_hinzufuegen(self,buch):
        self.buecher.append(buch)

    def zeige_buecher(self):
        for buch in self.buecher:
            print(buch.zeige_info())
    
buch1 = Buch("Python Grundlagen", "Herman Tsago", "123456789")
buch2 = Buch("Fortgeschrittenes Python", "Marie Kenne", "987654321")

obj = Bibliothek()
obj.buch_hinzufuegen(buch1)
obj.buch_hinzufuegen(buch2)
obj.zeige_buecher()    