# changer le nom du fichier plus tard

variable_text1 = "1 this is a test, if you see this then it is successful"
variable_text2 = "2 this is a test, if you see this then it is successful"
variable_text3 = "3 this is a test, if you see this then it is successful"
choix_fail = "Cela ne fesait pas partie des choix, réessayez"
variable_text1_1 = "blabla test"

choix_1 = variable_text1
choix_2 = variable_text2
choix_3 = variable_text3



option_1 = variable_text1_1


#pour pouvoir utiliser time.sleep plus loin dans le code
import time


#module de présentation des choix
def presentation_choix(choix_1, choix_2, choix_3):
    print(choix_1)
    print(choix_2)
    print(choix_3)
    reponse = int(input("quel est votre choix? "))
    return reponse


#module de resultat
def resultat_choix(reponse):
    if reponse == 1:
        choix_final = 1
    elif reponse == 2:
        choix_final = 2
    elif reponse == 3:
        choix_final = 3
    else:
        choix_final = 4
    
    return choix_final



#faire sur qu'on pose les memes questions si le user entre une mauvaise valeur
"""while True:
    reponse_user = print(presentation_choix(variables_niveau1, variables_niveau2, variables_niveau3))

    verif_reponse = print(resultat_choix(reponse_user))
    if verif_reponse != 4:
        break
"""







#inserer des variables dans une variable pour essayer de faire une fonction plus bas
niveau1_1 = 1
niveau1_2 = 2
niveau1_3 = 3
niveau1 = [niveau1_1, niveau1_2, niveau1_3]




#faire des loop while pour chaque niveau, fonction pour ca?
def loop_niveaux(niveau):
    while True:
        reponse_user = presentation_choix(variable_text1, variable_text2, variable_text3)

        verif_reponse = resultat_choix(reponse_user)
        if verif_reponse == 4:
            print(choix_fail)
            time.sleep(1.5)
        elif verif_reponse != 4:
            break

    return niveau

"""print(loop_niveaux(niveau1))"""




#fonction qui prend le niveau, extract les variables specifiques de niveau, et les entre dans la variable ci dessus?




def level_extractor(niveau_selectionne):
    variable_test1 = niveau_selectionne[0]
    variable_test2 = niveau_selectionne[1]
    variable_test3 = niveau_selectionne[2]
    return variable_test1, variable_test2, variable_test3

"""
input_niveau = niveau1 #niveau precedent
print(level_extractor(input_niveau))

"""

def loop_niveaux(input_niveau):
    while True:
        description1, description2, description3 = level_extractor(input_niveau)
        reponse_user = presentation_choix(description1, description2, description3)

        verif_reponse = resultat_choix(reponse_user)
        if verif_reponse == 4:
            print(choix_fail)
            time.sleep(1.5)
        elif verif_reponse != 4:
            #passer au prochain niveau et return cela
            break

    return niveau

"""print(loop_niveaux(niveau1))"""

#if every variable is a list, I can call the text, or the next set of variables for the level


text1_1_1 = "yipee"

text1_1_2 = 2

text1_1_3 = 3


text1_1 = "test1_1"
lvl1_1_1 = [text1_1_1, 1_1_1, 0, 0]
lvl1_1_2 = [text1_1_2, 1_1_2, 0, 0]
lvl1_1_3 = [text1_1_3, 1_1_3, 0, 0]


text1_2 = "test1_2"
lvl1_2_1 = 1_2_1
lvl1_2_2 = 1_2_2
lvl1_2_3 = 1_2_3

text1_3 = "test1_3"
lvl1_3_1 = 1_3_1
lvl1_3_2 = 1_3_2
lvl1_3_3 = 1_3_3


lvl1_1 = [text1_1, lvl1_1_1, lvl1_1_2, lvl1_1_3]
lvl1_2 = [text1_2, lvl1_2_1, lvl1_2_2, lvl1_2_3]
lvl1_3 = [text1_3, lvl1_3_1, lvl1_3_2, lvl1_3_3]

text1 = "test1"
lvl1 = [text1, lvl1_1, lvl1_2, lvl1_3]



def level_extractor2(niveau_selectionne):
    variable_test0 = niveau_selectionne[0]
    variable_test1 = niveau_selectionne[1]
    variable_test2 = niveau_selectionne[2]
    variable_test3 = niveau_selectionne[3]
    return variable_test0, variable_test1, variable_test2, variable_test3


def presentation_choix2(situation0, choix_1, choix_2, choix_3):
    print(situation0)
    print(choix_1[0])
    print(choix_2[0])
    print(choix_3[0])
    reponse = int(input("quel est votre choix? "))
    return reponse


def resultat_choix2(reponse):
    if reponse == 1:
        choix_final = 1
    elif reponse == 2:
        choix_final = 2
    elif reponse == 3:
        choix_final = 3
    else:
        choix_final = 4
    
    return choix_final


def loop_niveaux2(input_niveau):
    while True:
        situation0, description1, description2, description3 = level_extractor2(input_niveau)
        reponse_user = presentation_choix2(situation0, description1, description2, description3)

        verif_reponse = resultat_choix2(reponse_user)
        if verif_reponse == 4:
            print(choix_fail)
            time.sleep(1.5)
        elif verif_reponse != 4:
            niveau = input_niveau[verif_reponse] #passer au prochain niveau et return cela
            break

    return niveau

next_level = loop_niveaux2(lvl1)

next_level2 = loop_niveaux2(next_level)