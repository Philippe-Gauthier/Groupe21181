import random
import jeux_repertoire
import message
menu=""
while menu != "Q":
    menu=input(message.menu())
    menu=menu.upper()
    match menu:
        case "A":

            jeux_repertoire.roulette_russe() 

