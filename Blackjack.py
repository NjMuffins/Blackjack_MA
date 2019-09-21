import random




class Computer:
    #TODO: Alles Attribute einzeln kommentieren (überall)
    #Speichern der Karten
    karten_eines_deckes = (2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11)
    momentane_karten = []

    gewinn_faktor = 0

    misch_limit = 0

    alle_spieler = []

    geister_spieler = []

    dealer = None

    start_einsatz = 0


    def __init__(self, dealer, gewinn_faktor, alle_spieler, start_einsatz, misch_limit):

        self.dealer = dealer

        self.alle_spieler = alle_spieler

        self.gewinn_faktor = gewinn_faktor

        self.start_einsatz = start_einsatz

        self.misch_limit = misch_limit

        for spieler in self.alle_spieler:
            spieler.definiere_computer(self)

    def zusaetzlicher_spieler(self, geist, aktueller_spieler):
        self.alle_spieler.append(geist)
        self.geister_spieler.append(geist)
        self.geister_spieler.append(aktueller_spieler)
        self.gib_karte(geist)
        self.gib_karte(aktueller_spieler)

    def gib_karte(self, spieler):

        index = random.randint(0, len(self.momentane_karten) - 1)

        karte = self.momentane_karten[index]

        del self.momentane_karten[index]

        spieler.bekomme_karte(karte)

        return karte
        #spieler.bekomme_karte(4)
        #return 4



    def ein_spiel(self):


        #Alle Spieler setzen den start einsatz. Wenn zu wenig Geld sind sie ausgeschieden
        for spieler in self.alle_spieler:

            if not spieler.neues_spiel(self.start_einsatz, self.momentane_karten):
                spieler.pleite()

                self.alle_spieler.remove(spieler)


        #Überprüft ob noch spieler vorhanden sind
        if len(self.alle_spieler) == 0:
            return True

        self.dealer.neues_spiel(0, self.momentane_karten)

        #Alle spieler bekommen 2 Karten
        for spieler in self.alle_spieler:
            for i in range(2):

                self.gib_karte(spieler)


        #Dealer bekommt eine Karte

        dealer_karte = self.gib_karte(self.dealer)

        #Spieler erfahren die erste Karte des Dealers
        for spieler in self.alle_spieler:
            spieler.dealer_bekommt_karte(dealer_karte)

        #Dealer bekommt die zweite Karte
        self.gib_karte(self.dealer)

        #Spieler setzen ihr Geld
        for spieler in self.alle_spieler:
            spieler.erhoehen()


        #Weitere Karten ziehen
        for spieler in self.alle_spieler:
            will_weitere_karte = True

            while will_weitere_karte:
                if spieler.weitere_karte():
                    self.gib_karte(spieler)

                else:
                    will_weitere_karte = False

                if spieler.ausgeschieden():
                    will_weitere_karte = False

                if spieler.hat_double_down:
                    will_weitere_karte = False

        #Dealer zieht weitere Karten
        while self.dealer.weitere_karte():
            self.gib_karte(self.dealer)




        print("debug: dealer karten wert: " + str(self.dealer.gesammt_wert))

        #Schaut ob Dealer oder der Spieler gewonnen hat
        for spieler in self.alle_spieler:
            if spieler.gesammt_wert < self.dealer.gesammt_wert < 22 or spieler.gesammt_wert > 22:
                spieler.bekomme_geld(0)


            elif self.dealer.gesammt_wert == spieler.gesammt_wert:
                spieler.bekomme_geld(spieler.einsatz_momentan)

            else:
                spieler.bekomme_geld(self.gewinn_faktor * spieler.einsatz_momentan)

                spieler.totale_siege = spieler.totale_siege + 1

        i = 0
        while i > len(self.geister_spieler):
            self.geister_spieler[i + 1].bekomme_geld(self.geister_spieler[i].geld)
            self.alle_spieler.remove(self.geister_spieler[i])
            i = i + 2

        self.geister_spieler = []










    def n_spiele(self, n):

        for i in range(n):
            if len(self.momentane_karten) < self.misch_limit:

                self.momentane_karten = []

                for i in range(6):
                    self.momentane_karten.extend(self.karten_eines_deckes)

            self.ein_spiel()

        for spieler in self.alle_spieler:
            print(spieler.name + " hat " + str(spieler.totale_siege) + " Siege in " + str(n) + " Spielen.")
            print(spieler.name + " hat insgesamt " + str(spieler.geld) + " Franken")















