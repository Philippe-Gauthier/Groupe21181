import random
import roulette
menu=""
while menu != "Q":
    print("Menu jeux", "/n", "A: Roulette russe", "/n", "B: Pile ou face", "/n", "C: Courte paille", "/n", "Q: Quitter" )
    menu=input("Sélectionner un jeu!")
    menu=menu.upper()
    match menu:
        case "A":
                
            roulette.roulette_russe() 

