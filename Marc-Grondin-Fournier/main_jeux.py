import random
import jeux_repertoire
import jeux_message
menu=""
while menu != "Q":
    menu=input(jeux_message.menu())
    menu=menu.upper()
    match menu:
        case "A":
            jeux_repertoire.roulette_russe() 

