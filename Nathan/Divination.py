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
#while True:
    reponse_user = print(presentation_choix(variables_niveau1, variables_niveau2, variables_niveau3))

    verif_reponse = print(resultat_choix(reponse_user))
    if verif_reponse != 4:
        break





#faire des loop while pour chaque niveau, fonction pour ca?

def loop_niveaux(niveau):
    while True:
        reponse_user = print(presentation_choix(variable_text1, variable_text2, variable_text3))

        verif_reponse = print(resultat_choix(reponse_user))
        if verif_reponse != 4:
            niveau + 1
            break
    
    return niveau

print(loop_niveaux(niveau1))




#trouver une facon de nest des variables dans une variable niveau, liste? ( variable = [liste1, liste2] )

niveau1_1 = 1
niveau1_2 = 2
niveau1_3 = 3
niveau1 = [niveau1_1, niveau1_2, niveau1_3]

