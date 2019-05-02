import random



karten_eines_deckes = (2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11)
alle_karten = (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, )


class Spieler:

    gesammt_wert = 0

    geld = 0

    einsatz_momentan = 0

    verloren = False

    kartenwert_bankier = 0

    def neues_spiel(self, start_einsatz):
        return "Fehler"

    def bekomme_karte(self, wert):
        return "Fehler"

    def weitere_karte(self):
        return "True/False"

    def erhoehen(self):
        return "Fehler"

    def ausgeschieden(self):
        return self.gesammt_wert > 21


    def bekomme_geld(self, gewinn):
        self.geld = self.geld + gewinn

    #setzt Geld und prüft ob genug vorhanden ist. Falls nicht genug vorhanden returnt es False
    def geld_setzen(self, wert):

        if self.geld >= wert:
            self.einsatz_momentan = self.einsatz_momentan + wert

            self.geld = self.geld - wert

            return True
        else:
            return False

class Konsolenspieler(Spieler):

    def neues_spiel(self, start_einsatz):

        self.gesammt_wert = 0

        self.verloren = False

        self.kartenwert_bankier = 0

        hat_genug_geld = self.geld_setzen(start_einsatz)

        return hat_genug_geld

    def bekomme_karte(self, wert):

        print("Sie haben eine " + wert + " bekommen")

        self.gesammt_wert = self.gesammt_wert + wert

        print("Ihr gesammt Wert ist " + self.gesammt_wert)


    def weitere_karte(self):
        neue_karte_bekommen = input("Wollen sie eine weitere Karte?")

        while True:

            neue_karte_bekommen.lower()

            if neue_karte_bekommen == "ja":
                return True

            elif neue_karte_bekommen == "nein":
                return False

            neue_karte_bekommen = input("Keine valide Antwort. Geben sie Ja/Nein ein.")



    def erhoehen(self):
        erhöhungs_wert = int(input("Um wieviel wollen sie den Einsatz erhöhen?"))
        noch_genug_geld = False

        while not noch_genug_geld:

            noch_genug_geld = self.geld_setzen(erhöhungs_wert)

            if noch_genug_geld:
                print("Ihr Einsatz ist: " + self.einsatz_momentan)

            else:
                print("Sie haben nicht genug Geld. Ihr verfügbares Geld ist: " + self.geld)
                erhöhungs_wert = input("Wählen sie einen neuen Betrag: ")


    def bekomme_geld(self, gewinn):

        super().bekomme_geld(gewinn)
        print("Sie haben " + gewinn + " erhalten. Ihr neues Total ist " + self.geld)


