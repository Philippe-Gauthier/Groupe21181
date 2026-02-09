# lib des fonctions de jeux
import random
import message
def roulette_russe():
    reset="N"

    while reset == "O":
                    #Sélection entre les 6 positionnements possibles du barrilet
                    choix =int(input(message.roulette_bienvenu))
                    #Le barrilet spin pour atteindre une position au hasard
                    roll=random.randint(1, 6)
                    #Addition pour obtenir le nombre maximal de tour avant la munition
                    roll=choix+roll                   
                    
                    reset=input("Premier tour! Prêt? O/N\n")
                    for choix in range(roll):
                        tour_adv=choix+1       
                        if(tour_adv==roll):
                            reset=input(message.roulette_next())
                            reset=reset.upper()
                            reset=input(message.roulette_win)
                            reset=reset.upper()
                            if(reset=="N"):break                           
                            else:choix=roll                            

                    while choix != roll:

                                    

                        for choix in range(roll):                    
                                                       

                            if(tour_adv+1==roll):
                                reset=input("Votre adversaire est mort! Rejouer? O/N\n")
                                reset=reset.upper()
                                if(reset=="O"):break                               
                            elif(tour_adv==roll):
                                reset=input("Votre adversaire a survécu! À votre tour! Prêt? O/N\n")
                                reset=reset.upper()
                                tour_adv=choix+1  

                            if(choix+1==roll):

                                reset=input()
                                reset=reset.upper()  
                            else:
                                  reset=input("Vous avez survécu! Au tour de l'adversaire!")
                            