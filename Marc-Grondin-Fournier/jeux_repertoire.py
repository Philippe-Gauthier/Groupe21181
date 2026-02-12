# lib des fonctions de jeux
import random
import jeux_message
def roulette_russe():
    reset="O"  

    while reset == "O":                                        
                    #Sélection entre les 6 positionnements possibles du barrilet
                    choix =int(input(jeux_message.roulette_bienvenu()))
                    k=choix
                    #Le barrilet spin pour atteindre une position au hasard
                    roll=random.randint(1, 6)
                    #Addition pour obtenir le nombre maximal de tour avant la munition
                    roll=roll+choix
                    #Identification bool du joueur
                    modu_player=choix%2
                     
                    reset=input("Premier tour! Prêt?\n")
                    reset=reset.upper()

                    if(reset=="N"):break
                    for k in range(choix,roll+1):
                            if(choix+k %2 == modu_player):                                    
                                if(choix+k<roll):                                      
                                    reset=input(jeux_message.roulette_next())
                                    reset=reset.upper()
                                    if(reset=="N"):break
                                elif(choix+k==roll):
                                    reset=input(jeux_message.roulette_lose()) 
                                    reset=reset.upper()           
                            else:
                                if(choix+k<roll):                                     
                                    reset=input(jeux_message.roulette_adv_survi())
                                    reset=reset.upper()
                                    if(reset=="N"):break
                                elif(choix+k==roll):
                                    reset=input(jeux_message.roulette_win())
                                    reset=reset.upper()                            
                         