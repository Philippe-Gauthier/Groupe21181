# lib des fonctions de jeux
import random
import message
def roulette_russe():
    reset="O"

    while reset == "O":
                    
                    #Sélection entre les 6 positionnements possibles du barrilet
                    choix =int(input(message.roulette_bienvenu()))
                    #Le barrilet spin pour atteindre une position au hasard
                    roll=random.randint(1, 6)
                    #Addition pour obtenir le nombre maximal de tour avant la munition
                    modu_player=choix%2
                    modu_roll=roll%2
                    if(choix<=roll):roll=choix+roll  
                    elif(choix>roll):roll=choix-roll     

                    reset=input("Premier tour! Prêt? O/N\n")
                    reset=reset.upper()  
                    
                    for choix in range(roll):                       
                        reset=input(message.roulette_next())
                        reset=reset.upper()
                        tour_adv=choix+1 
                        if(choix==roll): 
                            reset=input(message.roulette_lose()) 
                            reset=reset.upper()     
                            if(reset=="N"):break
                        elif(tour_adv==roll):
                            reset=input(message.roulette_win())
                            reset=reset.upper()                            
                            if(reset=="N"):break                           
                        elif():
                             reset=input(message.roulette_adv_survi())
                             reset=reset.upper()
                             if(reset=="N"):break
                        