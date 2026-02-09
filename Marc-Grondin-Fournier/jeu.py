import random
import jeux_repertoire
menu=""
while menu != "Q":
    print("Menu jeux", "\n", "A: Roulette russe", "\n","B: Pile ou face", "\n", "C: Courte paille", "\n","D: Roche, papier, ciseau","\n", "Q: Quitter","\n" )
    menu=input("Sélectionner un jeu!\n")
    menu=menu.upper()
    match menu:
        case "A":               
            jeux_repertoire.roulette_russe() 

