import random




class Computer:

    karten_eines_deckes = (2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11)

    momentane_karten = []

    gewinn_faktor = 0

    alle_spieler = []

    dealer = None

    start_einsatz = 0

    def __init__(self, dealer, gewinn_faktor, alle_spieler, start_einsatz):

        self.dealer = dealer

        self.alle_spieler = alle_spieler

        self.gewinn_faktor = gewinn_faktor

        self.start_einsatz = start_einsatz


    def ein_spiel(self):
        #Alle Spieler setzen den start einsatz. Wenn zu wenig Geld sind sie ausgeschieden
        for spieler in self.alle_spieler:
            spieler.geld_setzen(self.start_einsatz)

            if not spieler.geld_setzen(self.start_einsatz):
                spieler.pleite()

                self.alle_spieler.remove(spieler)


        #Überprüft ob noch spieler vorhanden sind
        if len(self.alle_spieler) == 0:
            return True

        #Alle spieler bekommen 2 Karten
        for spieler in self.alle_spieler:
            for i in range(0, 2):

                index = random.randint(0, len(self.momentane_karten) - 1)

                karte = self.momentane_karten[index]

                del self.momentane_karten[index]

                spieler.bekomme_karte(karte)

        #Dealer bekommt eine Karte
        index = random.randint(0, len(self.momentane_karten) - 1)

        karte = self.momentane_karten[index]

        del self.momentane_karten[index]

        self.dealer.bekomme_karte(karte)

        #Spieler erfahren die erste Karte des Dealers
        for spieler in self.alle_spieler:
            spieler.dealer_bekommt_karte(karte)

        #Dealer bekommt die zweite Karte
        index = random.randint(0, len(self.momentane_karten) - 1)

        karte = self.momentane_karten[index]

        del self.momentane_karten[index]

        self.dealer.bekomme_karte(karte)







