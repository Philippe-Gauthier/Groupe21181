# lib des fonctions de jeux
import random
import jeux_message
def roulette_russe():
    reset=""
    while reset != "N":                                        
        #Sélection entre les 6 positionnements possibles du barrilet       
        choix =jeux_message.roulette_bienvenu()
        if(choix <= 6 and choix >= 0):
            k=choix
            #Le barrilet spin pour atteindre une position au hasard
            roll = random.randint(1, 6)
            #Addition pour obtenir le nombre maximal de tour avant la munition
            roll =+ choix
            #Identification bool du joueur
            modu_player = choix%2
                
            reset=input("Premier tour! Prêt?\n")
            reset=reset.upper()

            if(reset == "N"):break
            for k in range(choix,roll+1):
                if(choix+k %2 == modu_player):                                    
                    if(choix+k < roll):                                      
                        reset = jeux_message.roulette_next()
                        if(reset == "N"):break
                    elif(choix+k == roll):
                        reset=jeux_message.roulette_lose()      
                else:
                    if(choix+k < roll):                                     
                        reset = jeux_message.roulette_adv_survi()
                        if(reset == "N"):break
                    elif(choix+k == roll):
                        reset = jeux_message.roulette_win()
        else:
            reset=jeux_message.roulette_false()

def pile_face():

    exit=0
    choix="" 
    tracer=0   
    while exit != "Q":       
        choix=jeux_message.pile_face_bienvenu(tracer)               
        if(choix =="F" or choix =="P"):
            tracer=1
            # Identification bool du joueur
            if(choix =="P"):choix=0
            elif(choix =="F"):choix=1
            # pile ou face lancé
            result=random.randint(0,1)

            # message gagnant ou perdant selon le choix
            if(result == choix):exit=jeux_message.pile_face_win(choix)
            else:exit=jeux_message.pile_face_lose(choix)

        elif(choix=="Q"):break

        else:  
            choix=jeux_message.pile_face_false()
            tracer=1                   
                        
def courte_paille():
    exit=""
    while exit != "Q":
        #choix du nb de joueur
        choix=jeux_message.courte_paille_bienvenu()
        total=int(choix)
        total-=1
        joueur=[1]

        #creation d'une liste de joueurs
        for nb_joueur in range(0,total):
            new_joueur=[nb_joueur]
            joueur.extend(new_joueur)

        #nombre attribué à chaque joueur
        for nb_joueur in range(len(joueur)):
            joueur[nb_joueur] =nb_joueur

        #choix de la paille
        choix=jeux_message.courte_paille_select(total)
        #creation de la plus courte paille      
        paille_loser=random.randint(1,total)
        #début tirage
        for k in range(len(joueur)):
            if(joueur[k]==choix-1):
                exit=jeux_message.courte_paille_user(k)                
            else:             
                exit=jeux_message.courte_paille_next(k)                    
        #conclusion
        if(choix==paille_loser):
            exit=jeux_message.courte_paille_loser()
        else:
            exit=jeux_message.courte_paille_winner(joueur[paille_loser])
#incomplet
def rpCiseaux():
    choix=""
    choix=input(jeux_message.rpCiseaux_bienvenu())
    while choix != "N":
        if(egal.true):
            choix=input(jeux_message.rpCiseaux_egal_choix(egal))

        match choix:
            case"A":                   
                                 
                    choix_adv=random.randint(0,1)
                    if(choix_adv.false):
                        choix=input(jeux_message.rpCiseaux_loser()) 
                        egal=0

                    elif(choix==choix_adv):
                        choix=input(jeux_message.rpCiseaux_egal())      
                        egal+=1              
                    
                    else:
                        egal=0
                        choix=input(jeux_message.rpCiseaux_win())
                        
