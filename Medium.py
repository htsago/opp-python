class Medium:
    def __init__(self,titel, autor , Jahr) -> None:
        self.titel = titel
        self.autor = autor
        self.jahr = Jahr

    def zeige_details(self):
        return f"Titel: {self.titel},Autor: {self.autor}, Jahr:{self.jahr}"

class Buch (Medium):
    def __init__(self, titel, autor, Jahr, seitenzahl) -> None:
        super().__init__(titel, autor, Jahr)
        self.seitenzahl = seitenzahl 

    def zeige_details(self):
        return super().zeige_details() +  f", Seitenzahl: {self.seitenzahl}"    



class DVD (Medium):
    def __init__(self, titel, autor, Jahr, spieldauer) -> None:
        super().__init__(titel, autor, Jahr)
        self.spieldauer = spieldauer 

    def zeige_details(self):
        return super().zeige_details() +  f", Spieldauer: {self.spieldauer}"     


class Bibliothek:

    def __init__(self) -> None:
        self.medien= []

    def medium_einfuegen(self, medium):
        return self.medien.append(medium)
    
    def medium_entfernen(self, titel):
        for medium in self.medien:
            if medium.titel == titel:
                self.medien.remove(medium)
                print("Das medium wurde aus der Liste entfernt")
                break

    def zeige_medien(self):
        for medium in self.medien:
            print(medium.zeige_details())


bibliothek = Bibliothek()
buch = Buch ("The Vengeance", "Herman Tsago", 2023, 300)
bibliothek.medium_einfuegen(buch)
bibliothek.zeige_medien()
bibliothek.medium_entfernen("The Vengeance")
bibliothek.zeige_medien()