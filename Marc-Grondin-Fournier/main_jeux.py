import random
import jeux_repertoire
import jeux_message
menu="O"
while menu != "Q":
    menu=jeux_message.menu()
    menu=menu.upper()
    match menu:
        case "A":
            jeux_repertoire.roulette_russe() 

        case "B":
            jeux_repertoire.pile_face()    

        case "C":
            jeux_repertoire.courte_paille()
