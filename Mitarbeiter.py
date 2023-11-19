class Mitarbeiter:
    def __init__(self, name, personalnummer):
        self.name = name 
        self.personalnummer = personalnummer
    
    def zeige_info(self):
        return f"Name: {self.name}, Personalnummer: {self.personalnummer}"

class Manager (Mitarbeiter):
    def __init__(self, name, personalnummer, abteilung):
        super().__init__(name, personalnummer)
        self.abteilung = abteilung 

    def zeige_info(self):
        return super().zeige_info() + f", Abteilung: {self.abteilung}"
    
class Techniker(Mitarbeiter):
    def __init__(self,name, personalnummer, fachbereich):
        super().__init__(name, personalnummer) 
        self.fachbereich = fachbereich

    def zeige_info(self):
        return super().zeige_info() + f"Fachbereich: {self.fachbereich}"
    

techniker = Techniker("Herman", 1234, "IT")
mitarbeiter = Mitarbeiter("Marie", 9876)
manager = Manager("Dimou", 9876,"FSEH")


print(techniker.zeige_info())
print(mitarbeiter.zeige_info())
print(manager.zeige_info())