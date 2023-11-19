class Sportaktivitaet:
    def __init__(self,name,spielerzahl):
        self.name = name 
        self.spielerzahl = spielerzahl

    def aktivitaets_info(self):
        return f"Name: {self.name},  Spielerzahl: {self.spielerzahl}"
    

class Mannschaftssport(Sportaktivitaet):

    def __init__(self, name, spielerzahl, teamgroesse):
        super().__init__(name, spielerzahl)
        self.teamgroesse = teamgroesse

    def aktivitaets_info(self):
        return super().aktivitaets_info() + f" ,Teamgroesse: {self.teamgroesse}"

class EinzelnSport(Sportaktivitaet):
    def __init__(self, name, spielerzahl,ausruestung):
        super().__init__(name, spielerzahl)
        self.ausruestung = ausruestung

    def aktivitaets_info(self):
         return super().aktivitaets_info() + f", Ausruestung: {self.ausruestung}"
      




manschaftssport = Mannschaftssport("Fußball", 22, 4)
einzelnsport = EinzelnSport("Joga", 1, "Jogateppich,ruhiges Zimmer")

print(manschaftssport.aktivitaets_info())
print(einzelnsport.aktivitaets_info())