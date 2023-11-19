class Hotelzimmer:
    def __init__(self, zimmernummer, kapazitaet, preisProNacht) -> None:
        self.zimmernummer = zimmernummer
        self.kapazitaet = kapazitaet
        self.preisProNacht = preisProNacht

    def zeige_details(self):
        return f"Zimmernummer: {self.zimmernummer}, Kapazitaet: {self.kapazitaet}, Preis Pro Nacht: {self.preisProNacht} Euro"
    
class Einzelnzimmer(Hotelzimmer):
    def __init__(self, zimmernummer, kapazitaet, preisProNacht, tier) -> None:
        super().__init__(zimmernummer, kapazitaet, preisProNacht)
        self.tier = tier

    def zeige_details(self):
        return super().zeige_details() + f", Tier erlaubt: {self.tier}"
    
class Hotel:
    def __init__(self):
        self.hotel = []

    def zimmer_einfuegen(self, zimmer):
        return self.hotel.append(zimmer)
    
    def zimmer_loeschen(self, zimmernummer):
            zimmerGefunden = False
            for zimmer in self.hotel:
                if zimmer.zimmernummer == zimmernummer:
                    self.hotel.remove(zimmer)
                    zimmerGefunden = True
                    print(f"Das Zimmer mit der Nummer: {zimmernummer} wurde erfolgreich entfernt")
                    break
            if not zimmerGefunden:
                print(f"Zimmer mit der Nummer: {zimmernummer} nicht gefunden")

    def hotel_anzeigen(self):
        for zimmer in self.hotel:
            print(zimmer.zeige_details())

hotel = Hotel()
einzehnZimmer = Einzelnzimmer(2,14,45,"Nein")
einzehnZimmer1 = Einzelnzimmer(4,44,85,"Ja")
hotel.zimmer_einfuegen(einzehnZimmer)
hotel.zimmer_einfuegen(einzehnZimmer1)
hotel.hotel_anzeigen()
hotel.zimmer_loeschen(2)
hotel.hotel_anzeigen()
