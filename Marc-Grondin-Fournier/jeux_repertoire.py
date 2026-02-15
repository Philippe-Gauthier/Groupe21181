# lib des fonctions de jeux
import random
import jeux_message
def roulette_russe():
    reset=""
    while reset != "N":                                        
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
                    reset=jeux_message.roulette_next()
                    if(reset=="N"):break
                elif(choix+k==roll):
                    reset=jeux_message.roulette_lose()      
            else:
                if(choix+k<roll):                                     
                    reset=jeux_message.roulette_adv_survi()
                    if(reset=="N"):break
                elif(choix+k==roll):
                    reset=jeux_message.roulette_win()

def pile_face():
    choix=""
    while choix != "Q":
        choix=input(jeux_message.pile_face_bienvenu())
        if(choix=="P"):choix=0
        elif(choix=="F"):choix=1
# pile ou face lancé        
        result=random.randint(0,1)
# message gagnant ou perdant selon le choix
        if(choix==result):jeux_message.pile_face_win(choix)
        else:jeux_message.pile_face_lose(choix)

def courte_paille():
    exit=""
    while exit != "Q":
        choix=jeux_message.courte_paille_bienvenu()
        total=int(choix)
        joueur=[]
        for nb_joueur in joueur:
            joueur[nb_joueur]=nb_joueur
        for nb_joueur in range(len(joueur)):
            joueur[nb_joueur] =nb_joueur
        
        choix=jeux_message.courte_paille_select(total)       
        paille_loser=random.randint(1,total)

        for k in range(len(joueur)):
            if(joueur[k]==choix):
                exit=jeux_message.courte_paille_user()                
            else:             
                exit=jeux_message.courte_paille_next(k)                    

        if(choix==paille_loser):
            exit=jeux_message.courte_paille_loser()
        else:
            exit=jeux_message.courte_paille_winner(joueur[paille_loser])



        