class Produkt:
    def __init__(self, name, preis):
        self.name = name 
        self.preis = preis

    def zeigInfos(self):
        return f"Name: {self.name}, Preis: {self.preis}"

class Getraenk(Produkt):
    def __init__(self, name, preis, volumen):
        super().__init__(name, preis)
        self.volumen = volumen

    def zeigInfos(self):
        return super().zeigInfos() + f", Volumen: {self.volumen}"

class Snack(Produkt):
    def __init__(self, name, preis, gewicht):
        super().__init__(name, preis)
        self.gewicht = gewicht

    def zeigInfos(self):
        return super().zeigInfos() + f", Gewicht: {self.gewicht}"
    
class Cafe:
    def __init__(self):
        self.produkte = []

    def produkt_einfuegen(self, produkt):
        self.produkte.append(produkt)

    def produkt_entfernen(self, name):
        for produkt in self.produkte:
            if produkt.name == name:
                self.produkte.remove(produkt)
                break

    def produkt_anzeigen(self):
        for produkt in self.produkte:
            print(produkt.zeigInfos())

# Verwendung
cafe = Cafe()
getr = Getraenk("Kaffee", 2.50, "200ml")
cafe.produkt_einfuegen(getr)
snack = Snack("Croissant", 1.80, "100g")
cafe.produkt_einfuegen(snack)

cafe.produkt_anzeigen()

# Ein Produkt entfernen
cafe.produkt_entfernen("Kaffee")
cafe.produkt_entfernen("Croissant")

cafe.produkt_anzeigen()
