from Spieler import *
from Blackjack import *

dealer = Dealer(0, "Dealer")

alle_spieler = [
    #HiLoSpieler(1000, "HiLoSpieler")
    Konsolenspieler(1000, "Noah")
]

gewinn_faktor = 2

misch_limit = 100

start_einsatz = 5

computer = Computer(dealer, gewinn_faktor, alle_spieler, start_einsatz, misch_limit)

computer.n_spiele(1000)