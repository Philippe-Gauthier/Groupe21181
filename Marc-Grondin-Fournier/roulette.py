# lib de la fonction roulette russe
import random
def roulette_russe():
    reset="O"
    while reset == "O":
                    roll=random.randint(1, 6)
                    choix =int(input("Bienvenu au jeu de la roulette russe! Quelle trou du barrilet à 6 coups choisir pour mettre la munition? (1,2,3,4,5,6)"))
                    roll=choix+roll
                    roll=int(roll)
                  
                    
                    while choix != roll:             

                        for choix in 6:                    
                            
                            tour_adv=choix+1

                            if(tour_adv==roll):
                                reset=input("Votre adversaire est mort! Rejouer? O/N")
                                reset=reset.upper()
                                break                               
                              
                            else:
                                reset=input("Vous avez survécu, au tour de l'adversaire! Prêt? O/N")
                                  

                            