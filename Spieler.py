import random






class Spieler:

    name = ""

    hat_double_down = False

    hat_split = False

    gesammt_wert = 0

    computer = 0

    geld = 0

    ass_zaehler = 0

    einsatz_momentan = 0

    verloren = False

    kartenwert_bankier = 0

    totale_siege = 0

    def __init__(self, geld, name):
        self.geld = geld
        self.name = name




    def neues_spiel(self, start_einsatz, momentane_karten):
        return "Fehler"

    def bekomme_karte(self, wert):
        return "Fehler"

    def weitere_karte(self):
        return "True/False"

    def erhoehen(self):
        return "Fehler"
    #Überprüft ob gesammt kartenwert grösser als 21
    def ausgeschieden(self):
        return self.gesammt_wert > 21

    #sein Gewinnn wird ihm ausgezahlt
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

    def dealer_bekommt_karte(self):
        return "Fehler"

    def pleite(self):
        return "Fehler"

    def definiere_computer(self, computer):
        self.computer = computer


    def double_down(self):

        self.geld_setzen(self.einsatz_momentan)

        self.hat_double_down = True

        return True



class Konsolenspieler(Spieler):

    def neues_spiel(self, start_einsatz, momentane_karten):

        print("------------------------------------------------------------------")
        print("")
        print("------------------------------------------------------------------")

        self.hat_double_down = False

        self.gesammt_wert = 0

        self.ass_zaehler = 0

        self.verloren = False

        self.einsatz_momentan = 0

        self.kartenwert_bankier = 0

        hat_genug_geld = self.geld_setzen(start_einsatz)

        return hat_genug_geld

    def bekomme_karte(self, wert):

        if wert == 11:
            self.ass_zaehler = self.ass_zaehler + 1

        print("Sie haben eine " + str(wert) + " bekommen")

        self.gesammt_wert = self.gesammt_wert + wert

        while self.gesammt_wert > 21 and self.ass_zaehler > 0:
            self.gesammt_wert = self.gesammt_wert - 10
            self.ass_zaehler = self.ass_zaehler - 1


        print("Ihr gesammt Wert ist " + str(self.gesammt_wert) + "\n")


    def weitere_karte(self):

        neue_karte_bekommen = input("Wollen sie eine weitere Karte?")

        while True:

            neue_karte_bekommen.lower()

            if neue_karte_bekommen == "ja":
                return True

            elif neue_karte_bekommen == "nein":
                return False

            elif neue_karte_bekommen == "dd":
                return self.double_down()

            neue_karte_bekommen = input("Keine valide Antwort. Geben sie Ja/Nein ein.")


    def erhoehen(self):
        erhöhungs_wert = int(input("Um wieviel wollen sie den Einsatz erhöhen?"))
        erhöhungs_wert = abs(erhöhungs_wert)
        noch_genug_geld = False


        while not noch_genug_geld:

            noch_genug_geld = self.geld_setzen(erhöhungs_wert)

            if noch_genug_geld:
                print("Ihr Einsatz ist: " + str(self.einsatz_momentan) + "\n")

            else:
                print("Sie haben nicht genug Geld. Ihr verfügbares Geld ist: " + str(self.geld))
                erhöhungs_wert = int(input("Wählen sie einen neuen Betrag: "))


    def bekomme_geld(self, gewinn):

        super().bekomme_geld(gewinn)
        print("Sie haben " + str(gewinn) + " erhalten. Ihr neues Total ist " + str(self.geld))

    def dealer_bekommt_karte(self, dealer_wert):

        self.kartenwert_bankier = dealer_wert
        print("Der Dealer hat eine " + str(self.kartenwert_bankier) + "\n")

    def pleite(self):
        print("Sie haben kein Geld mehr und sind somit ausgeschieden.")




class Dealer(Spieler):


    def neues_spiel(self, start_einsatz, momentane_karten):

        self.gesammt_wert = 0

        self.ass_zaehler = 0

        self.verloren = False

    def bekomme_karte(self, wert):

        if wert == 11:
            self.ass_zaehler = self.ass_zaehler + 1

        self.gesammt_wert = self.gesammt_wert + wert

        while self.gesammt_wert > 21 and self.ass_zaehler > 0:
            self.gesammt_wert = self.gesammt_wert - 10
            self.ass_zaehler = self.ass_zaehler - 1


    def weitere_karte(self):
        return self.gesammt_wert < 17



    def erhoehen(self):
        print("Fehler: Dealer hat keinen Einsatz")









class HiLoSpieler(Spieler):

    einsatz_unit = 0

    karte_1 = 0

    karte_2 = 0

    running_count = 0

    real_count = 0

    uebrige_karten = []

    def neues_spiel(self, start_einsatz, momentane_karten):

        self.hat_double_down = False

        self.running_count = 0

        for i in momentane_karten:
            if i > 9:
                self.running_count = self.running_count + 1

            elif i > 6:
                self.running_count = self.running_count + 0

            else:
                self.running_count = self.running_count - 1



        self.gesammt_wert = 0

        self.einsatz_unit = self.geld / 10000

        self.ass_zaehler = 0

        self.verloren = False

        self.uebrige_karten = momentane_karten

        self.einsatz_momentan = 0

        self.kartenwert_bankier = 0

        hat_genug_geld = self.geld_setzen(start_einsatz)

        return hat_genug_geld

    def bekomme_karte(self, wert):

        if self.karte_1 == 0:
            self.karte_1 = wert
        elif self.karte_2 == 0:
            self.karte_2 = wert

        if wert > 9:
            self.running_count = self.running_count - 1

        elif wert > 6:
            self.running_count = self.running_count + 0

        else:
            self.running_count = self.running_count + 1



        if wert == 11:
            self.ass_zaehler = self.ass_zaehler + 1

        self.gesammt_wert = self.gesammt_wert + wert

        while self.gesammt_wert > 21 and self.ass_zaehler > 0:
            self.gesammt_wert = self.gesammt_wert - 10
            self.ass_zaehler = self.ass_zaehler - 1


    def weitere_karte(self):





        if self.ass_zaehler > 0 or self.karte_1 == 10 and self.karte_2 == 10:

            if self.gesammt_wert > 18:

                return False


            elif self.gesammt_wert == 13 or self.gesammt_wert == 14:

                if self.kartenwert_bankier < 5 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 15 or self.gesammt_wert == 16:

                if self.kartenwert_bankier < 4 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 17:

                if self.kartenwert_bankier < 3 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            #self.karte_1 == 18
            else:

                if self.kartenwert_bankier < 9:

                    return False

                else:

                    return True

        #self.ass_counter < 1 and not self.karte_1 == self.karte_2
        else:

            if self.gesammt_wert < 9:

                return True

            elif self.gesammt_wert == 9:

                if self.kartenwert_bankier < 3 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 10:

                if self.kartenwert_bankier > 10:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 11:

                if not self.kartenwert_bankier == 11:

                    return self.double_down()

                else:

                    return True

            elif self.gesammt_wert == 12:

                if self.kartenwert_bankier < 4 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return False

            elif self.gesammt_wert < 17:

                if self.kartenwert_bankier > 6:

                    return True

                else:

                    return False

            else:

                return False






    def erhoehen(self):

        anzahl_decks = len(self.uebrige_karten) / 52

        self.real_count = self.running_count / anzahl_decks

        if self.real_count < 2:
            self.geld_setzen(self.einsatz_unit)

        else:
            self.geld_setzen(self.einsatz_unit * (self.real_count - 1))




    def bekomme_geld(self, gewinn):

        super().bekomme_geld(gewinn)


    def dealer_bekommt_karte(self, dealer_wert):

        self.kartenwert_bankier = dealer_wert
        if dealer_wert > 9:
            self.running_count = self.running_count - 1

        elif dealer_wert > 6:
            self.running_count = self.running_count + 0

        else:
            self.running_count = self.running_count + 1



    def pleite(self):

        print("HiLoSpieler ist ausgeschieden")






class Wahrscheinlichkeits_Spieler(Spieler):

    karte_1 = 0

    karte_2 = 0


    uebrige_karten = []


    def neues_spiel(self, start_einsatz, momentane_karten):
        self.hat_double_down = False

        self.gesammt_wert = 0

        self.ass_zaehler = 0

        self.verloren = False

        self.uebrige_karten = momentane_karten

        self.einsatz_momentan = 0

        self.kartenwert_bankier = 0

        hat_genug_geld = self.geld_setzen(start_einsatz)

        return hat_genug_geld


    def bekomme_karte(self, wert):

        if wert == 11:
            self.ass_zaehler = self.ass_zaehler + 1

        self.gesammt_wert = self.gesammt_wert + wert

        while self.gesammt_wert > 21 and self.ass_zaehler > 0:
            self.gesammt_wert = self.gesammt_wert - 10
            self.ass_zaehler = self.ass_zaehler - 1


    def weitere_karte(self):

        wie_oft = []
        for h in range(12):
            wie_oft.append(0)

        for i in self.uebrige_karten:
            wie_oft[i - 1] = wie_oft[i - 1] + 1

        for i in range(len(wie_oft)):
            wie_oft[i - 1] = wie_oft[i - 1] / len(self.uebrige_karten)

        #print("Debug wie_oft: " + str(wie_oft))

        differenz = 21 - self.gesammt_wert

        if differenz >= 11:
            return True

        wkeit_true = 0
        counter = 0
        while counter <= differenz:
            wkeit_true = wkeit_true + wie_oft[counter]
            counter = counter + 1

        return wkeit_true > 0.5







    def erhoehen(self):

        wkeit_spieler_total = 0

        wkeit_sieg_spieler = 0

        wie_oft = []

        wkeit_spieler = []

        wkeit_dealer = []

        for i in range(22):
            wkeit_dealer.append(0)


        for i in range(12):
            wie_oft.append(0)


        for i in self.uebrige_karten:
            wie_oft[i] = wie_oft[i] + 1


        for i in range(len(wie_oft)):
            wie_oft[i] = wie_oft[i] / len(self.uebrige_karten)


        for i in range(len(wie_oft)):

            if self.kartenwert_bankier + i > 21:
                wkeit_dealer[21] = wkeit_dealer[21] + wie_oft[i]

            else:

                wkeit_dealer[self.kartenwert_bankier + i - 1] = wkeit_dealer[self.kartenwert_bankier + i - 1] + wie_oft[i]

        for i in range(17):
            for j in range(len(wie_oft)):
                if i + j > 21:
                    wkeit_dealer[21] = wkeit_dealer[21] + wkeit_dealer[i] * wie_oft[j]

                else:

                    wkeit_dealer[i + j] = wkeit_dealer[i + j] + wkeit_dealer[i] * wie_oft[j]

        #print("Debug wkeit_dealer: " + str(wkeit_dealer))






        for i in range(22):
            wkeit_spieler.append(0)


        for i in range(len(wie_oft)):

            if self.gesammt_wert + i > 21:
                wkeit_spieler[21] = wkeit_spieler[21] + wie_oft[i]

            else:

                wkeit_spieler[self.gesammt_wert + i - 1] = wkeit_spieler[self.gesammt_wert + i - 1] + wie_oft[i]

        for i in range(17):
            for j in range(len(wie_oft)):
                if i + j > 21:
                    wkeit_spieler[21] = wkeit_spieler[21] + wkeit_spieler[i] * wie_oft[j]

                else:

                    wkeit_spieler[i + j] = wkeit_spieler[i + j] + wkeit_spieler[i] * wie_oft[j]

        n = 16
        while n < 22:

            wkeit_spieler_total = wkeit_spieler_total + wkeit_spieler[n]

            n = n + 1

        #print("Debug wkeit_spieler: " + str(wkeit_spieler))


        wkeit_sieg_spieler = wkeit_sieg_spieler + wkeit_dealer[16] * (wkeit_spieler[17] + wkeit_spieler[18] + wkeit_spieler[19] + wkeit_spieler[20]) + wkeit_dealer[17] * (wkeit_spieler[18] + wkeit_spieler[19] + wkeit_spieler[20] + wkeit_dealer[18]) * (wkeit_spieler[19] + wkeit_spieler[20]) + wkeit_dealer[19] * wkeit_spieler[20] + wkeit_dealer[21] * (wkeit_spieler_total - wkeit_spieler[21])
        #print("Debug wkeit_siege_spieler: " + str(wkeit_sieg_spieler))
        if wkeit_sieg_spieler < 0.25:

            self.geld_setzen(0)


        else:
            if wkeit_sieg_spieler < 0.50:
                self.geld_setzen(0)

            elif wkeit_sieg_spieler < 0.75:
                self.geld_setzen(self.einsatz_momentan * 5)

            else:
                self.geld_setzen(self.einsatz_momentan * 10)





    def bekomme_geld(self, gewinn):
        super().bekomme_geld(gewinn)



    def dealer_bekommt_karte(self, dealer_wert):
        self.kartenwert_bankier = dealer_wert


    def pleite(self):
        print("WahrscheinlichkeitsSpieler ist ausgeschieden")














class BasicStrategySpieler(Spieler):


    karte_1 = 0

    karte_2 = 0

    uebrige_karten = []

    def neues_spiel(self, start_einsatz, momentane_karten):

        self.hat_double_down = False


        self.gesammt_wert = 0

        self.ass_zaehler = 0

        self.verloren = False

        self.uebrige_karten = momentane_karten

        self.einsatz_momentan = 0

        self.kartenwert_bankier = 0

        hat_genug_geld = self.geld_setzen(start_einsatz)

        return hat_genug_geld

    def bekomme_karte(self, wert):

        if self.karte_1 == 0:
            self.karte_1 = wert
        elif self.karte_2 == 0:
            self.karte_2 = wert


        if wert == 11:
            self.ass_zaehler = self.ass_zaehler + 1

        self.gesammt_wert = self.gesammt_wert + wert

        while self.gesammt_wert > 21 and self.ass_zaehler > 0:
            self.gesammt_wert = self.gesammt_wert - 10
            self.ass_zaehler = self.ass_zaehler - 1


    def weitere_karte(self):





        if self.ass_zaehler > 0 or self.karte_1 == 10 and self.karte_2 == 10:

            if self.gesammt_wert > 18:

                return False


            elif self.gesammt_wert == 13 or self.gesammt_wert == 14:

                if self.kartenwert_bankier < 5 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 15 or self.gesammt_wert == 16:

                if self.kartenwert_bankier < 4 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 17:

                if self.kartenwert_bankier < 3 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            #self.karte_1 == 18
            else:

                if self.kartenwert_bankier < 9:

                    return False

                else:

                    return True

        #self.ass_counter < 1 and not self.karte_1 == self.karte_2
        else:

            if self.gesammt_wert < 9:

                return True

            elif self.gesammt_wert == 9:

                if self.kartenwert_bankier < 3 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 10:

                if self.kartenwert_bankier > 10:

                    return True

                else:

                    return self.double_down()

            elif self.gesammt_wert == 11:

                if not self.kartenwert_bankier == 11:

                    return self.double_down()

                else:

                    return True

            elif self.gesammt_wert == 12:

                if self.kartenwert_bankier < 4 or self.kartenwert_bankier > 6:

                    return True

                else:

                    return False

            elif self.gesammt_wert < 17:

                if self.kartenwert_bankier > 6:

                    return True

                else:

                    return False

            else:

                return False






    def erhoehen(self):

        self.geld_setzen(0)



    def bekomme_geld(self, gewinn):

        super().bekomme_geld(gewinn)


    def dealer_bekommt_karte(self, dealer_wert):

        self.kartenwert_bankier = dealer_wert




    def pleite(self):

        print("BasicStrategySpieler ist ausgeschieden")





























