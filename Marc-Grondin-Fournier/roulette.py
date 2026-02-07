# lib de la fonction roulette russe
import random
def roulette_russe():
    reset="N"

    while reset == "N":
                    roll=random.randint(1, 6)
                    choix =int(input("Bienvenu au jeu de la roulette russe!", '/n' ,"Sélectionner la chambre du barrilet à 6 coups pour y insérer la munition! (1,2,3,4,5,6)"))
                    roll=choix+roll                   
                    tour_adv=choix+1                  
                    while choix != roll:
                        input("Premier tour! Prêt? O/N")             

                        for choix in range(roll):                    
                                                       

                            if(tour_adv+1==roll):
                                reset=input("Votre adversaire est mort! Rejouer? O/N")
                                reset=reset.upper()
                                if(reset=="O"):break                               
                            elif(tour_adv==roll):
                                reset=input("Votre adversaire a survécu! À votre tour! Prêt? O/N")
                                reset=reset.upper()
                                tour_adv=choix+1  

                            if(choix+1==roll):

                                reset=input("Oh non! Vous êtes mort! Voulez-vous réssuciter? O/N")
                                reset=reset.upper()  
                            else:
                                  reset=input("Vous avez survécu! Au tour de l'adversaire!")
                            