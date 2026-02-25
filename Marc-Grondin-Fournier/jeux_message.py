# lib messages
import random
#message main
def menu():
    tracer=0
    message=input("Menu jeux \nSélectionner un jeu! \nA: Roulette russe \nB: Pile ou face \nC: Courte paille \nD: Roche, papier, ciseau \nQ: Quitter \n" )
    message=message.upper()
    while tracer==0:

        if message==("A")or("B")or("C")or("D")or("Q"):
            tracer=1
        else:
            message=input("Entré inconnue! \nMenu jeux \nA: Roulette russe \nB: Pile ou face \nC: Courte paille \nD: Roche, papier, ciseau \nQ: Quitter \n" )
            message=message.upper()    
    return message

#messages roulette russe
def roulette_bienvenu(tracker):
    check=0
    while check==False:

        if(tracker):        
            message=input("Sélectionner la chambre du barrilet à 6 coups pour y insérer la munition! (1,2,3,4,5,6)\n")
        else:    
            message=input("Bienvenu au jeu de la roulette russe! \nSélectionner la chambre du barrilet à 6 coups pour y insérer la munition! (1,2,3,4,5,6)\n")
        
        intSearch=message.isdigit()                   
        
        if intSearch==True: 

            message=int(message)
            if message <1 or message>6: 
                check=0
                tracker=1
                print("Entré inconnue! \n")
            else:check=1

        else:
            print("Entré inconnue! \n") 
            tracker=1
    message=int(message)
    return message

def roulette_next():
    message=input("Vous avez survécu! Au tour de l'adversaire! Prêt ? O/N\n")
    message=message.upper()
    return message
def roulette_adv_survi():
    message=input("Votre adversaire a survécu! À votre tour! Prêt? O/N\n")
    message=message.upper()
    return message  
def roulette_win():
    message=input("Votre adversaire est mort et vous avez des couilles d'acier!! Rejouer? O/N\n")
    message=message.upper()
    return message
def roulette_lose():
    message=input("Oh non! Vous êtes mort! Voulez-vous réssuciter? O/N\n")
    message=message.upper()
    return message
def roulette_false():
    message=input("Entré inconnu! \nContinuer ?O/N")
    message=message.upper()
    return message

#messages pile ou face
def pile_face_bienvenu(tracer):

    if(tracer==0): message=input("Bienvenu à pile ou face! Quelle côté choisissez-vous? P/F\n")              
    else: message=input("Quelle côté choisissez-vous? P/F\n")

    message=message.upper()         
    return message    
    
def pile_face_false():
            
    choix=input("Côté non-reconnu, appuyer sur toutes touches pour recommencer ou Q pour quitter\n")
    choix=choix.upper()
    return choix

def pile_face_win(choix):
        
    if(choix==0):
        message=input("Pile! Vous avez gagné! Voulez-vous rejouer(O) ou quitter(Q)?")
    else:
        message=input("Face! Vous avez gagné! Voulez-vous rejouer(O) ou quitter(Q)?")

    message=message.upper()            
    return message        
    
def pile_face_lose(choix):
    
    if(choix==0):
        message=input("Face! Vous avez perdu! Voulez-vous rejouer(O) ou quitter(Q)?")
    else:
        message=input("Pile! Vous avez perdu! Voulez-vous rejouer(O) ou quitter(Q)?")

    message=message.upper()            
    return message

#messages courte paille
def courte_paille_bienvenu():
    message=input("Bienvenu au jeu de la courte paille! \nCombien de joueurs y participent?:\n")
    while (message.isdigit()==False):               
        message=input("Quantité de joueurs inconnus! \nCombien de joueurs y participent?:\n")
    message=int(message)
    return message
def courte_paille_select(total):
    message=input(F"Choisir parmi les {total+1} pailles!\n")
    while (message.isdigit()==False):               
        message=input(F"Paille inexistante! \nChoisir parmi les {total+1} pailles!:\n")
    message=int(message)
    return message
def courte_paille_loser():
    message=input("Vous avez la plus petite paille! Voulez-vous rejouer(Toutes touches) ou quitter(Q)?")
    message=message.upper()
    return message   
def courte_paille_user(k):
    message=input(F"Vous avez tiré la paille numéro {k+1}! Enter pour continuer ou Q pour quitter.")
    message=message.upper()
    return message   
def courte_paille_next(k):
    message=input(F"Le joueur numéro {k+1} a tiré une paille! Enter pour continuer ou Q pour quitter.")       
    message=message.upper()
    return message      
def courte_paille_winner(a):
    message=input(F"Le joueur numéro {a+1} la mauvaise paille! Voulez-vous rejouer(Toutes touches) ou quitter(Q)?")
    message=message.upper()
    return message 

def rpCiseaux_bienvenu():
    message=input("Bienvenu à roche papier ciseau! \nChoisissez entre(A,B,C,Q): \nA:Roche \nB:Papier \nC:Ciseau \nQ:Quitter")
    message=message.upper()
    return message
def rpCiseaux_loser():
    message=input("Votre adversaire a choisi papier, vous avez perdu! Voulez vous rejouer?(O/N)")
    message=message.upper()
    return message
def rpCiseaux_win():
    message=input("Votre adversaire a choisi ciseau, vous avez gagné! Voulez vous rejouer?(O/N)")
    message=message.upper()
    return message
def rpCiseaux_egal():
    message=input("Votre adversaire a choisi roche, égalité! Voulez vous un prochain round?(O/N)")
    message=message.upper()
    return message
def rpCiseaux_egal_choix(a):
    message=input(F"Round {a+1}! \nChoisissez entre(A,B,C,Q): \nA:Roche \nB:Papier \nC:Ciseau \nQ:Quitter")
    message=message.upper()
    return message
