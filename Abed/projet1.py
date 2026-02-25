### Les fonctions a utiliser
"""1-une fonction qui va permettre de poser les questions
2-une fonction qui garde les choix précédent"""



def poser_question(question, option1, option2):
    """retourne le choix de l'utilisateur
    
    Args:
        question (str): texte qui pose la question a l'utilisateur
        option1 (str): premier choix
        option2 (str): deuxieme choix
    
    Returns:
        str: retourne le choix de l'utilisateur
    """
    
    print(question)
    print("1 -", option1)
    print("2 -", option2)
    
    choix = input("votre choix : ")
    return choix

def fonction_arbre():
    """Fonction qui contien l'arbre des decisions"""

    choix1 = poser_question(
        "Bobby un explorateur talentueux est perdu dans une foret sans son materielle pour l'aider a s'en sortir, que dois-t'il faire?",
        "avancer dans la foret  au hazard en esperant trouver quelque chose qui peut l'aider a s'en sortir",
        "rester la et reflechir"
    )

    if choix1 == "1":
        
        choix2 = poser_question(
            "bobby avance dans la foret et il entend un bruit",
            "aller dans la direction du bruit",
            "aller dans le sens opposé du bruit"
        )

        if choix2 == "1":

            choix3 = poser_question(
                "Bobby se dirige sur la pointe des pieds tel un ninja vers le bruit et il remarque une vielle cabanne au milieu de la foret",
                "il va vers la cabanne malgré les bruit effrayant",
                "plus il s'approche de la cabanne plus il a peur du bruit et finis par s'enfuire"
            )

            if choix3 == "1":

                choix4 = poser_question(
                    "Bobby entre dans la cabanne et le bruit effrayant est un bucheron couvert de sang qui decoupe une viande rouge a l'aide d'une tronsoneuse",
                    "à cause du bruit de la tronsonneuse le bucheron ne le remarque pas et bobby commence a parler au bucheron",
                    "à cause du bruit de la tronsonneuse le bucheron ne le remarque pas et bobby profite de l'ocasion pour assomer le bucheron par derrière"
                )

                if choix4 == "1":

                    choix5 = poser_question(
                        "le bucheron se retourne brusquement vers Bobby",
                        "Bobby le regarde et lui demande qu'est-ce qu'il fait avec la viande et la tronsonneuse",
                        "bobby lui demande est-ce qu'il peut se refugier dans sa cabanne jusqu'à ce qu'il peut partir"
                    )

                    if choix5 == "1":
                        print("Fin : LE bucheron tue Bobby parce que la viande étaitun humain. Il était un tueur en serie en cavale.")
                    
                    elif choix5 == "2":
                      print("Fin : Bobby reste un peu et pendant que le bucheron dormait il s'enfuit pendant la nuit en volant des chose utile a sa survie.")
            
                elif choix4 == "2":

                    choix9 = poser_question(
                        "Bobby assome le bucheron et il fouille la cabanne pour trouver des choses utiles pour sa survie",
                        "il trouve une carte de la foret et il decide de suivre la carte pour trouver une sortie",
                        "il trouve une carte de la foret mais il decide de ne pas la suivre et de tuer le bucheron pour prendre sa place et vivre dans la cabanne"
                    )

                    if choix9 == "1":
                        print("Fin : Bobby suit la carte et il trouve une sortie et il est sauvé")
                    elif choix9 == "2":
                        print("Fin : Bobby tue le bucheron et il prend sa place et il vit dans la cabanne mais il ne sait pas que le bucheron était un tueur en serie en cavale et il finit par se faire tuer par la police qui vient enqueter sur les meurtres du bucheron")
            
            elif choix3 == "2":

                choix8 = poser_question(
                    "Bobby s'enfuit dans la direction opposé du bruit et il se perd dans la foret",
                    "il continue a avancer dans la foret en esperant trouver une sortie",
                    "il decide de rester la et d'attendre que quelqu'un vienne le chercher"
                )
                if choix8 == "1":
                    print("Fin : Bobby continue a avancer dans la foret et il trouve une sortie et il est sauvé")
                elif choix8 == "2":        
                    print("Fin : Bobby decide de rester la et d'attendre que quelqu'un vienne le chercher, mais personne ne vient et il meurt de faim et de froid")
        
        elif choix2 == "2":
            choix7 = poser_question(
                "Bobby s'enfuit dans la direction opposé du bruit et il se perd encore plus dans la foret",
                "il continue a avancer dans la foret en esperant trouver une sortie",
                "il decide de rester la et d'attendre que quelqu'un vienne le chercher"
            )

            if choix7 == "1":
                print("Fin : Bobby continue a avancer dans la foret et il trouve une sortie et il est sauvé")
            elif choix7 == "2":        
                print("Fin : Bobby decide de rester la et d'attendre que quelqu'un vienne le chercher, mais personne ne vient et il meurt de faim et de froid")
        
    elif choix1 == "2":
        choix6 = poser_question(
            "Bobby reste la et reflechit a une solution pour s'en sortir, il se rappelle que dans sa poche il a un briquet",
            "il decide d'allumer le briquet pour faire du feu et se rechauffer",
            "il decide de garder le briquet pour plus tard"
        )      
        if choix6 == "1":
            print("Fin : Bobby allume le feu et le bruit effrayant est un ours qui s'approche de lui, le feu l'effraie et il s'enfuit dans la direction opposé a Bobby et Bobby est sauvé")
        
        elif choix6 == "2":
            print("Fin : Bobby decide de garder le briquet pour plus tard, malheureusement il se fait attaquer par un loup pendant la nuit et il n'a pas de moyen de se proteger contre le loup et il meurt")


# Lancer le jeu
fonction_arbre()