class Elektronikprodukt:
    def __init__(self,produktID, marke, modell, preis) -> None:
        self.produktID = produktID
        self.marke = marke
        self.modell = modell
        self.preis = preis

    def zeige_details(self):
        return f"ProduktID: {self.produktID}, Marke: {self.marke}, Modell: {self.modell}, Preis (in Euro): {self.preis}"


class Laptop(Elektronikprodukt):
    def __init__(self, produktID, marke, modell, preis, betriebssystem):
        super().__init__(produktID, marke, modell, preis)
        self.betriebsystem = betriebssystem

    def zeige_details(self):
        return super().zeige_details() + f", Betriebssystem: {self.betriebsystem}"
    
class Elektronikgeschaeft:
    def __init__(self) -> None:
        self.geraete = []
    
    def geraet_einfuegen(self, geraet):
        self.geraete.append(geraet)
        print (f"Das Produkt {geraet.produktID} wurde erfolgreih eingefügt!")  

    def geraet_entfernen(self, produktID):
        is_geraet = False
        for geraet in self.geraete:
            if geraet.produktID == produktID:
                self.geraete.remove(geraet)
                is_geraet = True
                print(f"Das Produkt {produktID} wurde erfolgreich entfernt!")
                break

        if not is_geraet:
            print (f"Das Geraet {produktID} wurde nicht gefunden")


    def produkt_anzeigen(self):
        for produkt in self.geraete:
            print(produkt.zeige_details())



electro = Elektronikgeschaeft()

laptop1 = Laptop(12345,"Macbook Pro", 2023, 1500, "IOS")
laptop2 = Laptop(56789,"Macbook", 2000, 1200, "IOS")
electro.geraet_einfuegen(laptop1)
electro.geraet_einfuegen(laptop2)
electro.produkt_anzeigen()
electro.geraet_entfernen(12345)
electro.produkt_anzeigen()