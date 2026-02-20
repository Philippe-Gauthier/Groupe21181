"""
Futurs dont vous êtes l'auteur!
Par: Nathan Paradis
"""



import time #pour pouvoir utiliser time.sleep dans le code
import textwrap #pour formatter le text présenté dans le terminal





#definition des variables

mise_en_contexte = "Vous êtes la grande Yisma, voyante reconnue a travers le monde (le monde étant Longueil), mais ce matin vous avez échappé votre boule de crystal en vous faisant un bol de céréales, vous devez donc inventer de toutes pieces le futur de vos clients de la journée, en attente de voir le réparateur de boules de crystal (qui est occupé pour les 3 prochaines semaines, son service est très en demande, les boules sont devenues glissantes de nos jours)."

regles_instructions = "Instructions:\nL'aventure se joue en une journée, composée de deux parties, la mise en situation et la prise de décision.\nPour la partie mise en situation, vous allez avoir un texte unique au niveau a lire, ensuite, 3 options apparaitront sur le terminal, chacune\ndes options commencent par 1, 2, ou 3.\n\nAprès, vous aurez une décision a prendre. Pour faire cela, entrez le numéro de l'option que vous voulez choisir, soit 1, 2, ou 3, et entrez\nle dans le terminal (ce serait clairement indiqué qu'il est pret a recevoir votre décision).\n\nCa recommence ensuite avec une nouvelle mise en situation, puis une décision, et ainsi de suite jusqu'a une mise en situation finale qui\nterminera l'aventure.\n(Au moment de choisir, entrez 0 si vous voulez retourner au début de la journée)\n"

choix_retour = "\nretour au début de la journée...\n"
choix_fail = "\nCela ne faisait pas partie des choix, réessayez\n"










#---3 layer

text1_1_1 = "placeholder text"
option1_1_1_1 = "placeholder choice"
option1_1_1_2 = "placeholder choice"
option1_1_1_3 = "placeholder choice"

lvl1_1_1 = [text1_1_1, option1_1_1_1, option1_1_1_2, option1_1_1_3]






#--2 layer

text1_1 = "placeholder text"
option1_1_1 = "placeholder choice"
option1_1_2 = "placeholder choice"
option1_1_3 = "placeholder choice"

lvl1_1 = [text1_1, option1_1_1, option1_1_2, option1_1_3]

#--2 layer

text1_2 = "placeholder text"
option1_2_1 = "placeholder choice"
option1_2_2 = "placeholder choice"
option1_2_3 = "placeholder choice"

lvl1_2 = [text1_2, option1_2_1, option1_2_2, option1_2_3]

#--2 layer

text1_3 = "placeholder text"
option1_3_1 = "placeholder choice"
option1_3_2 = "placeholder choice"
option1_3_3 = "placeholder choice"

lvl1_3 = [text1_3, option1_3_1, option1_3_2, option1_3_3]





#-1 layer

text1 = "placeholder text"
option1_1 = "option1"
option1_2 = "option2"
option1_3 = "option3"

lvl1 = [text1, option1_1, option1_2, option1_3]







#definition des fonctions du jeu


#petite fonction de print, seulement utlisée pour "l'animation" de "loading" dans le jeu
def print_par_lettre(text):
    """ 
    Petite fonction pour print des caracteres les uns apres les autres
    Inputs: strings de text courts (certains problemes de formattage, seulement utiliser avec des petites strings)
    Outputs: la meme string qu'a l'input, mais écrit caractere par caractere avec un délai
    """
    for caracteres in text:
        print(f"{caracteres}", end="", flush=True)
        time.sleep(0.4) #changer a 0.008s pour des strings plus longues
    print("\n\n")



#fonction pour demander au jouer s'il est pret a commencer le jeu
def start_game():
    """
    Fonction pour confirmer le début du jeu avec un input du joueur
    Inputs: confirmation du joueur par un input de y ou n
    Outputs: strings de texte
    """
    while True:
        start_confirmation = input("Pret a jouer? (y/n) ")
        if start_confirmation == "y":
            print_par_lettre(".....") #fonction utilisée ici pour le "loading"
            break
        elif start_confirmation == "n":
            print("Ah bon, au revoir alors")
            time.sleep(1.5)
        else:
            print("? ? ?")
            time.sleep(1.5)



#Fonction pour detecter la fin d'une branche
def failstate_detect(niveau_selectionne):
    """
    Fonction pour vérifier si le prochain choix du joueur sera son dernier dans chaque branche de l'arbre
    Inputs: variable du niveau actuel contenant une liste de choix (ou pas)
    Outputs: retour au début du jeu ou continution du jeu
    """
    while True:
        fail_check = len(niveau_selectionne)
        if fail_check > 1:
            break
        else:
            print(niveau_selectionne[0])
            time.sleep(1.5)
            while True:
                start_confirmation = input("\nVoulez vous retourner au début de la journée? (y/n) ")
                if start_confirmation == "y":
                    print(choix_retour)
                    time.sleep(1.5)
                    loop_niveau(lvl1)
                elif start_confirmation == "n":
                    print("\nAh bon, au revoir alors (vous pouvez maintenant fermer le jeu)")
                    time.sleep(1.5)
                else:
                    print("\n? ? ?")
                    time.sleep(1)



#module d'extraction d'information de niveau + formattage pour fiter dans le terminal, à utiliser en duo avec la prochaine fonction
def level_extractor(niveau_selectionne):
    """
    Fonction d'extraction et de formattage du texte et des options possible d'une variable de niveau
    Inputs: output de la derniere fonction, soit une variable de niveau avec une liste de choix
    Outputs: variables pour chaque choix et le texte du niveau, formattés pour ne pas séparer un mot en deux
    """
    situation0 = textwrap.fill(niveau_selectionne[0], width = 140)
    choix1 = textwrap.fill(niveau_selectionne[1], width = 140)
    choix2 = textwrap.fill(niveau_selectionne[2], width = 140)
    choix3 = textwrap.fill(niveau_selectionne[3], width = 140)

    return situation0, choix1, choix2, choix3


#module de présentation des choix, utiliser avec la fonction ci dessus
def presentation_choix(situation0, choix_1, choix_2, choix_3):
    """
    Fonction qui formatte le texte et les choix d'un niveau en liste lisible et claire, puis demande une question a l'utilisateur
    Inputs: Output de la derniere fonction, soit les variables pour chaque choix et le texte formattés
    Outputs: Liste formattée de la situation et des choix possibles sur le terminal, et une variable de réponse au choix en int
    """
    time.sleep(0.5)
    print(f"\n{situation0}\n")
    time.sleep(1.5)
    print(f"1: {choix_1}\n")
    time.sleep(0.5)
    print(f"2: {choix_2}\n")
    time.sleep(0.5)
    print(f"3: {choix_3}\n")
    time.sleep(0.5)
    reponse = int(input("Quel est votre choix? "))
    return reponse


#module d'assignation de valeur au résultat du choix, prends le résultat de la fonction ci dessus et lui assigne une valeur fixe
def resultat_choix(reponse):
    """
    Fonction d'assignation de valeur au résultat du choix fait a la fonction plus haut
    Inputs: réponse en int a la question posée par la fonction ci dessus
    Output: Chiffre en int entre 0 et 4 dans une variable
    """
    if reponse == 1 or reponse == 2 or reponse == 3 or reponse == 0:
        choix_final = reponse
    else:
        choix_final = 4
    
    return choix_final


#combinaison de toutes les fonctions ci dessus sauf les 2 premieres, + fonction de "looping" du code au cas ou la réponse n'est pas valide 
def loop_niveau(input_niveau):
    """
    Fonction combinant presque toutes les fonctions ci dessus afin de les mettre dans une "loop" qui valide que le choix du joueur est valide
    et répete cette boucle jusqu'a ce que le joueur entre une réponse valide.
    Inputs: Variable de niveau
    Output: Variable pour déterminer le prochain niveau
    """
    while True:
        failstate_detect(input_niveau)
        situation0, choix1, choix2, choix3 = level_extractor(input_niveau)
        reponse_user = presentation_choix(situation0, choix1, choix2, choix3)

        verif_reponse = resultat_choix(reponse_user)
        if verif_reponse == 4:
            print(choix_fail)
            time.sleep(1.5) #retour aux choix
        elif verif_reponse == 0:
            confirmation = input("Voulez vous vraiment retourner au début de la journée? (y/n) ")
            if confirmation == "y":
                print(choix_retour)
                time.sleep(1.5)
                loop_niveau(lvl1) #retour au niveau1
            elif confirmation == "n":
                print("continuons alors...\n")
                time.sleep(1.5) #retour aux choix
            else:
                print("Bon, tu parles chinois maintenant, j'imagine que ca veut dire 'on continue' alors...\n")
                time.sleep(1) #retour aux choix
        elif verif_reponse != 4:
            prochain_niveau = verif_reponse #donner l'indication pour le prochain niveau
            break

    return prochain_niveau





#début du code du jeu
fmise_en_contexte = textwrap.fill(mise_en_contexte, width = 140) #simple formattage
print(f"{fmise_en_contexte}\n\n\n")
time.sleep(1.5)

print(regles_instructions)
time.sleep(1.5)

start_game() #commencement du jeu si le joueur entre "y"

niveau = loop_niveau(lvl1) #début du niveau 1


#suite de if pour passer a chaque prochain niveau
if niveau == 1:
    niveau = loop_niveau(lvl1_1)
    if niveau == 1:
        niveau = loop_niveau(lvl1_1_1)
        if niveau == 1:
            niveau = loop_niveau(lvl1_1_1_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_1_1_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_1_1_3)
    elif niveau == 2:
        niveau = loop_niveau(lvl1_1_2)
        if niveau == 1:
            niveau = loop_niveau(lvl1_1_2_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_1_2_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_1_2_3)
    elif niveau == 3:
        niveau = loop_niveau(lvl1_1_3)
        if niveau == 1:
            niveau = loop_niveau(lvl1_1_3_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_1_3_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_1_3_3)
elif niveau == 2:
    niveau = loop_niveau(lvl1_2)
    if niveau == 1:
        niveau = loop_niveau(lvl1_2_1)
        if niveau == 1:
            niveau = loop_niveau(lvl1_2_1_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_2_1_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_2_1_3)
    elif niveau == 2:
        niveau = loop_niveau(lvl1_2_2)
        if niveau == 1:
            niveau = loop_niveau(lvl1_2_2_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_2_2_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_2_2_3)
    elif niveau == 3:
        niveau = loop_niveau(lvl1_2_3)
        if niveau == 1:
            niveau = loop_niveau(lvl1_2_3_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_2_3_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_2_3_3)
elif niveau == 3:
    niveau = loop_niveau(lvl1_3)
    if niveau == 1:
        niveau = loop_niveau(lvl1_3_1)
        if niveau == 1:
            niveau = loop_niveau(lvl1_3_1_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_3_1_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_3_1_3)
    elif niveau == 2:
        niveau = loop_niveau(lvl1_3_2)
        if niveau == 1:
            niveau = loop_niveau(lvl1_3_2_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_3_2_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_3_2_3)
    elif niveau == 3:
        niveau = loop_niveau(lvl1_3_3)
        if niveau == 1:
            niveau = loop_niveau(lvl1_3_3_1)
        elif niveau == 2:
            niveau = loop_niveau(lvl1_3_3_2)
        elif niveau == 3:
            niveau = loop_niveau(lvl1_3_3_3)




