


class Spieler:

    def neues_spiel(self):
        return "Fehler"

    def bekomme_karte(self, wert):
        return "Fehler"

    def weitere_karte(self):
        return "True/False"

    def erhoehen(self):
        return "Fehler"

    def ausgeschieden(self):
        return "True/False"

    def bekomme_geld(self):
        return "Fehler"


class Konsolenspieler(Spieler):

    def neues_spiel(self):
        return "?"

    def bekomme_karte(self, wert):
        print("Sie haben eine " + wert + " bekommen")

    def weitere_karte(self):
        neue_karte_bekommen = input("Wollen sie eine weitere Karte?")

    def erhoehen(self):
        geld_erhoehen = input("Wollen sie den Einsatz erhoehen?")

    def ausgeschieden(self):
        return "?"

    def bekomme_geld(self):
        if



