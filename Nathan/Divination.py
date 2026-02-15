#pour pouvoir utiliser time.sleep plus loin dans le code
import time


#definition des variables

regles_instructions = "placeholder instructions (Au moment de choisir, entrez 0 si vous voulez retourner au début de la journée)"

choix_retour = "retour au début de la journée..."
choix_fail = "Cela ne fesait pas partie des choix, réessayez"







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

#module d'extraction d'information de niveau
def level_extractor(niveau_selectionne):
    variable_test0 = niveau_selectionne[0]
    variable_test1 = niveau_selectionne[1]
    variable_test2 = niveau_selectionne[2]
    variable_test3 = niveau_selectionne[3]
    return variable_test0, variable_test1, variable_test2, variable_test3


#module de présentation des choix
def presentation_choix(situation0, choix_1, choix_2, choix_3):
    time.sleep(0.5)
    print(f"{situation0}\n")
    time.sleep(1.5)
    print(f"1: {choix_1}\n")
    time.sleep(0.5)
    print(f"2: {choix_2}\n")
    time.sleep(0.5)
    print(f"3: {choix_3}\n")
    time.sleep(0.5)
    reponse = int(input("Quel est votre choix? "))
    return reponse


#module d'assignation de valeur au résultat du choix
def resultat_choix(reponse):
    if reponse == 1:
        choix_final = 1
    elif reponse == 2:
        choix_final = 2
    elif reponse == 3:
        choix_final = 3
    elif reponse == 0:
        choix_final = 0
    else:
        choix_final = 4
    
    return choix_final


#fonction de "looping" du code au cas ou la réponse n'est pas valide
def loop_niveau(input_niveau):
    while True:

        situation0, description1, description2, description3 = level_extractor(input_niveau)
        reponse_user = presentation_choix(situation0, description1, description2, description3)

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
                print("continuons alors...")
                time.sleep(1.5) #retour aux choix
            else:
                print("Bon, tu parles chinois maintenant, j'imagine qu'on continue alors...")
                time.sleep(1.5) #retour aux choix
        elif verif_reponse != 4:
            prochain_niveau = verif_reponse #passer au prochain niveau
            break

    return prochain_niveau





#début du code du jeu (i have to nest everything under one single if statement)


print(regles_instructions)
time.sleep(1.5)
while True:
    start_confirmation = input("Pret a jouer? (y/n) ")
    if start_confirmation == "y":
        print("Alors c'est parti!")
        time.sleep(0.5)
        print(f"\r.", end="")
        time.sleep(0.7)
        print(f"\r..", end="")
        time.sleep(0.9)
        print(f"\r...", end="")
        time.sleep(1.2)
        print("\n")
        break
    elif start_confirmation == "n":
        print("Ah bon, au revoir alors")
        time.sleep(1.5)
    else:
        print("Bon.. ca commence bien la journée ca...")
        time.sleep(1.5)
        

niveau = loop_niveau(lvl1)

if niveau == 1:
    prochain_niveau = lvl1_1
    niveau2 = loop_niveau(prochain_niveau)
    if niveau2 == 1:
        prochain_niveau = lvl1_1
    elif niveau2 == 2:
        prochain_niveau = lvl1_2
    elif niveau2 == 3:
        prochain_niveau = lvl1_3


elif niveau == 2:
    prochain_niveau = lvl1_2
    niveau2 = loop_niveau(prochain_niveau)
    if niveau2 == 1:
        prochain_niveau = lvl1_1
    elif niveau2 == 2:
        prochain_niveau = lvl1_2
    elif niveau2 == 3:
        prochain_niveau = lvl1_3


elif niveau == 3:
    prochain_niveau = lvl1_3
    niveau2 = loop_niveau(prochain_niveau)
    if niveau2 == 1:
        prochain_niveau = lvl1_1
    elif niveau2 == 2:
        prochain_niveau = lvl1_2
    elif niveau2 == 3:
        prochain_niveau = lvl1_3





