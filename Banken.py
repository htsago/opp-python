class Bankkonto:
    def __init__(self, kontonummer, kontostand):
        self.kontonummer = kontonummer
        self.kontostand = kontostand

    def einzahlen(self, beitrag):
        self.kontostand += beitrag
    
    def abheben(self, beitrag):
        self.kontostand -= beitrag
    
    def zeige_kontostand(self):
        return f"Kontonummer: {self.kontonummer}, Kontostand: {self.kontostand}"

class Girokonto(Bankkonto):
    def __init__(self, kontonummer, kontostand, zinssatz):
        super().__init__(kontonummer, kontostand)
        self.zinssatz = zinssatz

    def berechne_zinsen(self, jahrzeit):
        return self.kontostand * jahrzeit * self.zinssatz

class Bank:
    def __init__(self):
        self.konten = []

    def konto_einfuegen(self, konto):
        self.konten.append(konto)

    def konto_loeschen(self, kontonummer):
        for konto in self.konten:
            if konto.kontonummer == kontonummer:
                self.konten.remove(konto)
                break

    def konten_anzeigen(self):
        for konto in self.konten:
            print(konto.zeige_kontostand())

girokonto = Girokonto(12345, 1000, 0.02)
bank = Bank()
bank.konto_einfuegen(girokonto)
bank.konten_anzeigen()

zinsen = girokonto.berechne_zinsen(1)  # 1 Jahr
print(f"Zinsen: {zinsen}")
