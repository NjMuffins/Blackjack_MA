from Spieler import *
from Blackjack import *

dealer = Dealer(0, "Dealer")

alle_spieler = [
    #HiLoSpieler(10000, "HiLoSpieler"),
    #Konsolenspieler(10000, "Noah")
    #BasicStrategySpieler(10000, "BasicStrategySpieler"),
    Wahrscheinlichkeits_Spieler(10000, "Wahrscheinlichkeitsspieler")
]

gewinn_faktor = 2

misch_limit = 100

start_einsatz = 5

computer = Computer(dealer, gewinn_faktor, alle_spieler, start_einsatz, misch_limit)

computer.n_spiele(1000)