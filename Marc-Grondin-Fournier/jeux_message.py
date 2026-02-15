# lib messages
import random
#message main
def menu():
    message=input("Menu jeux \nSélectionner un jeu! \nA: Roulette russe \nB: Pile ou face \nC: Courte paille \nD: Roche, papier, ciseau \nQ: Quitter \n" )
    message=message.upper()
    return message

#messages roulette russe
def roulette_bienvenu():
    message=input("Bienvenu au jeu de la roulette russe! \nSélectionner la chambre du barrilet à 6 coups pour y insérer la munition! (1,2,3,4,5,6)\n")
    message=message.upper()
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

#messages pile ou face
def pile_face_bienvenu():
    message=input("Bienvenu à pile ou face! Quelle côté choisissez-vous? P/F\n")
    message=message.upper()
    return message
def pile_face_win(choix):
    if(choix==0):
        message=input("Pile! Vous avez gagné! Voulez-vous rejouer(O) ou quitter(Q)?")
        message=message.upper()
        return message
    else:
        message=input("Face! Vous avez gagné! Voulez-vous rejouer(O) ou quitter(Q)?")
        message=message.upper()
        return message
def pile_face_lose(choix):
    if(choix==0):
        message=input("Pile! Vous avez perdu! Voulez-vous rejouer(O) ou quitter(Q)?")
        message=message.upper()
        return message
    else:
        message=input("Face! Vous avez perdu! Voulez-vous rejouer(O) ou quitter(Q)?")
        message=message.upper()
        return message

#messages courte paille
def courte_paille_bienvenu():
    message=input("Bienvenu au jeu de la courte paille! Combien de joueurs?:\n")
    message=int(message)
    return message
def courte_paille_select(total):
    message=input("Quelles pailles choisissez-vous parmi les {total} paille(s)?\n")
    message=int(message)
    return message
def courte_paille_loser():
    message=input("Vous avez choisi la mauvaise paille! Voulez-vous rejouer(O) ou quitter(Q)?")
    message=message.upper()
    return message   
def courte_paille_user(k):
    message=input("Vous avez tiré la paille numéro {k}! Enter pour continuer ou Q pour quitter.")
    message=message.upper()
    return message   
def courte_paille_next(k):
    message=input("Le joueur numéro {k} a tiré une paille! Enter pour continuer ou Q pour quitter.")       
    message=message.upper()
    return message      
def courte_paille_winner(a):
    message=input("Le joueur numéro {a} la mauvaise paille! Voulez-vous rejouer(O) ou quitter(Q)?")
    message=message.upper()
    return message 