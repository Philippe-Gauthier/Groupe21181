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
            
            elif choix3 == "2":


        elif choix2 == "2":



    elif choix1 == "2":
