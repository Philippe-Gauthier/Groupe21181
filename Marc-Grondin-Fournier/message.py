# lib de la fonction pile ou face

import random

def menu():
    return "Menu jeux \nSélectionner un jeu! \nA: Roulette russe \nB: Pile ou face \nC: Courte paille \nD: Roche, papier, ciseau \nQ: Quitter \n" 

def roulette_bienvenu():
    return "Bienvenu au jeu de la roulette russe! \nSélectionner la chambre du barrilet à 6 coups pour y insérer la munition! (1,2,3,4,5,6)\n"
def roulette_next():
    return "Vous avez survécu! Au tour de l'adversaire! \n Prêt ? O/N\n"
def roulette_adv_survi():
    return "Votre adversaire a survécu! À votre tour! Prêt? O/N\n"    
def roulette_win():
    return "Votre adversaire est mort et vous avez des couilles d'acier!! Rejouer? O/N\n"
def roulette_lose():
    return "Oh non! Vous êtes mort! Voulez-vous réssuciter? O/N\n"
    
