class Fahrzeug:
    def __init__(self, marke, model, baujahr):
        self.marke = marke
        self.model = model
        self.baujahr = baujahr

    def zeige_daten(self):
        return f"Marke: {self.marke}, Model: {self.model}, Baujahr: {self.baujahr}"
    
class Auto(Fahrzeug):
    def __init__(self, marke, model, baujahr, sitzplatze):
        super().__init__(marke, model, baujahr)
        self.sitzplatze = sitzplatze

    def zeige_daten(self):
        return super().zeige_daten() + f", Sitzplätze: {self.sitzplatze}"
    
class Motorrad(Fahrzeug):
    def __init__(self, marke, model, baujahr, helmpflicht):
        super().__init__(marke, model, baujahr)
        self.helmpflicht = helmpflicht

    def zeige_daten(self):
        return super().zeige_daten() + f", Helmpflicht: {self.helmpflicht}"

auto1 = Auto("BMW", "BMW2023", 2023, 5)
motorrad1 = Motorrad("Senke", "Senke2030", 2012, "Ja")

print(auto1.zeige_daten())
print(motorrad1.zeige_daten())
