class Veranstaltung:
    def __init__(self, titel, datum, ort):
        self.titel = titel
        self.datum = datum
        self.ort = ort

    def zeige_details(self):
        return f"Titel: {self.titel}, Datum: {self.datum}, Ort: {self.ort}"
    
class Konzert(Veranstaltung):
    def __init__(self, titel, datum, ort, kuenstler):
        super().__init__(titel, datum, ort)
        self.kuenstler = kuenstler

    def zeige_details(self):
        return super().zeige_details() + f", Kuenstler: {self.kuenstler}"

class VeranstaltungsManager:
    def __init__(self):
        self.veranstaltungen = []

    def veranstaltung_hinzufuegen(self, veranstaltung):
        self.veranstaltungen.append(veranstaltung)

    def veranstaltung_entfernen(self, titel):
        for veranstaltung in self.veranstaltungen:
            if veranstaltung.titel == titel:
                self.veranstaltungen.remove(veranstaltung)
                print(f"Veranstaltung '{titel}' wurde entfernt.")
                break
        else:
            print(f"Veranstaltung mit dem Titel '{titel}' wurde nicht gefunden.")

    def zeige_alle_veranstaltungen(self):
        for veranstaltung in self.veranstaltungen:
            print(veranstaltung.zeige_details())


manager = VeranstaltungsManager()
konzert = Konzert("Rockkonzert", "2023-07-01", "Berlin", "Die Ärzte")

manager.veranstaltung_hinzufuegen(konzert)
manager.zeige_alle_veranstaltungen()
manager.veranstaltung_entfernen("Rockkonzert")
manager.zeige_alle_veranstaltungen()