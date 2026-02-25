"""
**********************************************
Auteur: Marc-André Grondin-Fournier
But générales des fonctions: messages adaptés selon la situation et retour de choix sécurisés
Nom du fichier: jeux_message.py
**********************************************

**********************************************
Fonction menu principale
Entré:Aucune
Sortie:Choix sécurisés
"""
def menu():
    tracer = 0
    message = input("Menu jeux \nSélectionner un jeu! \nA: Roulette russe \nB: Pile ou face \nC: Courte paille \nD: Roche, papier, ciseau \nQ: Quitter \n" )
    message = message.upper()
    while tracer == 0:

        if message == ("A")or("B")or("C")or("D")or("Q"):
            tracer = 1
        else:
            message = input("Entré inconnue! \nMenu jeux \nA: Roulette russe \nB: Pile ou face \nC: Courte paille \nD: Roche, papier, ciseau \nQ: Quitter \n" )
            message = message.upper()    
    return message
"""
**********************************************

**********************************************
Fonction de triage des choix input INT ou STR 
Entré: tracker, se rappeler si c'est le premier message
Sortie: Choix sécurisés et convertis
"""
#messages roulette russe
def roulette_bienvenu(tracker):
    check = 0
    while check == False:

        if(tracker):        
            message = input("Sélectionner la chambre du barrilet à 6 coups pour y insérer la munition! (1,2,3,4,5,6)\n")
        else:    
            message = input("Bienvenu au jeu de la roulette russe! \nSélectionner la chambre du barrilet à 6 coups pour y insérer la munition! (1,2,3,4,5,6)\n")
        
        intSearch = message.isdigit()                   
        # si le input est un int ou str avant la conversion
        if intSearch == True: 

            message = int(message)
            if message <1 or message > 6: 
                check = 0
                tracker = 1
                print("Entré inconnue! \n")
            else:check = 1
        else:
            print("Entré inconnue! \n") 
            tracker = 1
    message = int(message)
    return message
"""
**********************************************

**********************************************
But des fonctions: messages adaptés selon la situation et retour de choix 
Entré: Aucune
Sortie: Choix sécurisé
"""
def roulette_next():
    message = input("Vous avez survécu! Au tour de l'adversaire! Prêt ? O/N\n")
    message = message.upper()
    return message
def roulette_adv_survi():
    message = input("Votre adversaire a survécu! À votre tour! Prêt? O/N\n")
    message = message.upper()
    return message  
def roulette_win():
    message = input("Votre adversaire est mort et vous avez des couilles d'acier!! Rejouer? O/N\n")
    message = message.upper()
    return message
def roulette_lose():
    message = input("Oh non! Vous êtes mort! Voulez-vous réssuciter? O/N\n")
    message = message.upper()
    return message
def roulette_false():
    message = input("Entré inconnu! \nContinuer ?O/N")
    message = message.upper()
    return message
"""
**********************************************

**********************************************
Fonction de triage des choix input pile ou face pour des réponses adaptés aux choix
Entré: tracer, savoir si c'est le premiere fois
       choix, permet de savoir si c'est un message pour l'utilisateur ou l'adversaire
Sortie: Choix sécurisés et convertis au besoin
"""
#messages pile ou face
def pile_face_bienvenu(tracer):
    if(tracer == 0): message = input("Bienvenu à pile ou face! Quelle côté choisissez-vous? P/F\n")              
    else: message = input("Quelle côté choisissez-vous? P/F\n")
    message = message.upper()         
    return message    
    
def pile_face_false():           
    choix = input("Côté non-reconnu, appuyer sur toutes touches pour recommencer ou Q pour quitter\n")
    choix = choix.upper()
    return choix

def pile_face_win(choix):        
    if(choix == 0): message = input("Pile! Vous avez gagné! Voulez-vous rejouer(O) ou quitter(Q)?")       
    else: message = input("Face! Vous avez gagné! Voulez-vous rejouer(O) ou quitter(Q)?")    
    message = message.upper()            
    return message        
    
def pile_face_lose(choix):    
    if(choix == 0): message = input("Face! Vous avez perdu! Voulez-vous rejouer(O) ou quitter(Q)?")     
    else: message = input("Pile! Vous avez perdu! Voulez-vous rejouer(O) ou quitter(Q)?")   
    message = message.upper()            
    return message
"""
**********************************************

**********************************************
Fonctions pour éviter les entrées str causant une erreur de conversion int
Entrée: total, pour question adapté aux pailles totale
Sortie: Choix sécurisés et convertis au besoin
"""
def courte_paille_bienvenu():
    message = input("Bienvenu au jeu de la courte paille! \nCombien de joueurs y participent?:\n")
    while (message.isdigit() == False):               
        message = input("Quantité de joueurs inconnus! \nCombien de joueurs y participent?:\n")

    message = int(message)
    return message

def courte_paille_select(total):
    message = input(F"Choisir parmi les {total+1} pailles!\n")
    while (message.isdigit() == False):               
        message = input(F"Paille inexistante! \nChoisir parmi les {total+1} pailles!:\n")

    message = int(message)
    return message
"""
**********************************************

**********************************************
Fonction d'affichage de message selon le déroulement du tirage de chaque paille
Entrées: k, permet de savoir les quantités/positions dans les messages
Sortie: Choix sécurisés
"""
def courte_paille_loser():
    message = input("Vous avez la plus petite paille! Voulez-vous rejouer(Toutes touches) ou quitter(Q)?")
    message = message.upper()
    return message   
def courte_paille_user(k):
    message = input(F"Vous avez tiré la paille numéro {k+1}! Enter pour continuer ou Q pour quitter.")
    message = message.upper()
    return message   
def courte_paille_next(k):
    message = input(F"Le joueur numéro {k+1} a tiré une paille! Enter pour continuer ou Q pour quitter.")       
    message = message.upper()
    return message      
def courte_paille_winner(k):
    message = input(F"Le joueur numéro {k+1} la mauvaise paille! Voulez-vous rejouer(Toutes touches) ou quitter(Q)?")
    message = message.upper()
    return message 
"""
**********************************************
"""