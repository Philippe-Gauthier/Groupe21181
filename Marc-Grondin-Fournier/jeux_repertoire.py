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
                        if(choix==roll): input(message.roulette_lose())      
                        elif(tour_adv==roll):
                            reset=input(message.roulette_next())
                            reset=reset.upper()
                            reset=input(message.roulette_win())
                            reset=reset.upper()                            
                            if(reset=="N"):break                           
                        else:
                             reset=input(message.roulette_adv_survi())
                             reset=reset.upper()
                             if(reset=="N"):break
                        