class Fahrzeug:
    def __init__(self, fahrzeugnummer,marke, modell,baujahr):
        self.fahrzeugnummer = fahrzeugnummer
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
    

    def zeige_details(self):
        return f"Fahrzeugnummer: {self.fahrzeugnummer}, Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}"
    

class LKW(Fahrzeug):
    def __init__(self, fahrzeugnummer, marke, modell, baujahr,ladungskapazitaet):
        super().__init__(fahrzeugnummer, marke, modell, baujahr)
        self.ladungskapazitaet =ladungskapazitaet

    def zeige_details(self):
        return super().zeige_details() + f" Ladungkapazitaet: {self.ladungskapazitaet}"


class PKW(Fahrzeug):
    def __init__(self, fahrzeugnummer, marke, modell, baujahr,passagierkapazitaet):
        super().__init__(fahrzeugnummer, marke, modell, baujahr)
        self.passagierkapazitaet = passagierkapazitaet

    def zeige_details(self):
        return super().zeige_details() + f" Passagierkapazitaet: {self.passagierkapazitaet}"
    
    

class Autovermittlung:
    def __init__(self):
        self.fahrzeugen = []

    def fahrzeug_einfuegen(self, fahrzeug):
        self.fahrzeugen.append(fahrzeug)

    def fahrzeug_entfernen(self, fahrzeugnummer):
        for fahrzeug in self.fahrzeugen:
            if fahrzeug.fahrzeugnummer == fahrzeugnummer:
                self.fahrzeugen.remove(fahrzeug)
                print("Fahrzeug gelöscht!")
            else:
                print("Fahrzeug nicht gefunden!")
                break

    def zeige_fahrzeugen(self):
        for fahrzeug in self.fahrzeugen:
            print(fahrzeug.zeige_details())

# Verwendung
autover = Autovermittlung()
pkw = PKW(1234, "BMW", "BMW2302", 2002, 4)
autover.fahrzeug_einfuegen(pkw)

# Anzeigen aller Fahrzeuge
autover.zeige_fahrzeugen()

# Fahrzeug entfernen und erneut anzeigen
autover.fahrzeug_entfernen(1234)
autover.zeige_fahrzeugen()
