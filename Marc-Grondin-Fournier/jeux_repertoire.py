"""
**********************************************
Auteur: Marc-André Grondin-Fournier
But des fonctions: Répertoire des fonctions principales pour les jeux
Nom du fichier: jeux_repertoire.py
**********************************************
"""
import random
import jeux_message

"""
Fonction principale du jeu roulette russe
Entré:Aucune
Sortie:Aucune
"""
def roulette_russe():    
    reset = ""
    tracker = 0
    while reset != "N":  
        roll=0
        choix=0                                      
        #Sélection entre les 6 
        #positionnements possibles du barrilet       
        choix = jeux_message.roulette_bienvenu(tracker)
        tracker = 1
        choix=choix-1
        #Le barrilet spin pour atteindre une position au hasard
        roll = random.randint(1, 6)
        #Addition pour obtenir le nombre maximal de tour avant la munition
        roll = roll + choix
        tour=choix

        #Identification bool du joueur
        modu_player = choix%2           
        #porte de sortie
        reset = input("Premier tour! Prêt?\n")
        reset = reset.upper()       
        if(reset == "N"):break

        for k in range(choix,roll+1):       
            #position selon le choix, l'incrementation et la position de la mutinion     
            if(tour==choix):tour=choix+1
            else:tour=tour+1            
            tour_modulo=tour%2
            #Le perdant sera identifié 1 si on choisi nombre pair
            if(tour_modulo == modu_player): 

                if(tour < roll): 
                    reset = jeux_message.roulette_next()
                    if(reset == "N"):break

                elif(tour == roll):
                    reset = jeux_message.roulette_lose()      
            else:
                if(tour < roll):                                     
                    reset = jeux_message.roulette_adv_survi()
                    if(reset == "N"):break

                elif(tour == roll):
                    reset = jeux_message.roulette_win()
"""
Fonction principale du jeu pile ou face
Entré:Aucune
Sortie:Aucune
"""
def pile_face():
    exit=0
    choix="" 
    tracer=0   
    while exit != "Q":       
        choix=jeux_message.pile_face_bienvenu(tracer)               
        if(choix =="F" or choix =="P"):
            tracer = 1
            # Identification bool du joueur
            if(choix == "P"):choix=0
            elif(choix == "F"):choix=1
            # pile ou face lancé
            result = random.randint(0,1)

            # message gagnant ou perdant selon le choix
            if(result == choix):exit = jeux_message.pile_face_win(choix)
            else:exit = jeux_message.pile_face_lose(choix)
        else:  
            exit = jeux_message.pile_face_false()
            tracer = 1                   
"""
Fonction principale du jeu de la courte paille
Entré:Aucune
Sortie:Aucune
"""                        
def courte_paille():
    exit=""
    while exit != "Q":
        #choix du nb de joueur
        choix = jeux_message.courte_paille_bienvenu()
        total = int(choix)
        total -= 1
        joueur = [1]

        #creation d'une liste de joueurs
        for nb_joueur in range(0,total):
            new_joueur = [nb_joueur]
            joueur.extend(new_joueur)

        #nombre attribué à chaque joueur
        for nb_joueur in range(len(joueur)):
            joueur[nb_joueur] = nb_joueur

        #choix de la paille
        choix = jeux_message.courte_paille_select(total)
        #creation de la plus courte paille      
        paille_loser = random.randint(1,total)
        #début tirage
        for k in range(len(joueur)):
            if(joueur[k] == choix-1):
                exit = jeux_message.courte_paille_user(k)                
            else:             
                exit = jeux_message.courte_paille_next(k)                    
        #conclusion
        if(choix==paille_loser):
            exit = jeux_message.courte_paille_loser()
        else:
            exit = jeux_message.courte_paille_winner(joueur[paille_loser])
