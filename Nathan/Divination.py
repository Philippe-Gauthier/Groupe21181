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
niveau1_1 = [1, variable_4]
variable_4 = 4
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

print(loop_niveaux(niveau1))

#if every variable is a list, I can call the text, or the next set of variables for the level



