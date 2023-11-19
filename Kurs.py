class Kurs:
    def __init__(self,kursname,dozent,teilnehmerzahl):
        self.kursname = kursname
        self.dozent = dozent
        self.teilnehmerzahl = teilnehmerzahl
    
    def kurs_info(self):
        return f"Kursname: {self.kursname},Dozent: {self.dozent}, Teinehmerzahl: {self.teilnehmerzahl}"

class OnlineKurs(Kurs):
    def __init__(self, kursname, dozent, teilnehmerzahl, plattform):
        super().__init__(kursname, dozent, teilnehmerzahl)
        self.plattform = plattform

    def kurs_info(self):
        return super().kurs_info() + f", Plattform: {self.plattform}"

class PraesenzKurs(Kurs):
    def __init__(self, kursname, dozent, teilnehmerzahl,raumnummer):
        super().__init__(kursname, dozent, teilnehmerzahl)
        self.raumnummer = raumnummer

    def kurs_info(self):
        return super().kurs_info() + f", raumnummer: {self.raumnummer}"

    
onlinekurs1 = OnlineKurs("Deutsch", "Dr. Tsago", 3,"Zoom")
onlinekurs2 = OnlineKurs("Englisch", "Dr. Kenne", 20,"WhatsApp")
presenzkurs1 = PraesenzKurs("Mathe", "Dr. Dimou", 10,5)

print(onlinekurs1.kurs_info())
print(onlinekurs2.kurs_info())
print(presenzkurs1.kurs_info())