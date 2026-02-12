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







# variable list
choix_retour = "retour au début de la journée..."
choix_fail = "Cela ne fesait pas partie des choix, réessayez"
the_end = "the end"

testfailure = "fail"
testagain = "blabla i guess"
otherv = "blabla" 
otherv2 = "againagian" 

text1_1_1 = "blablsa"
lvl41 = [testagain, testfailure, otherv, otherv2]
lvl42 = []
lvl43 = []

text1_1_2 = 2

text1_1_3 = 3


text1_1 = "test1_1"
lvl1_1_1 = [text1_1_1, lvl41, lvl42, lvl42]
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



#formattage variables: niveau-nombre = [text-niveau, choix1 ou "fail", choix2, choix3]




#function defining

def failstate_detector(niveau_selectionne):
    if niveau_selectionne[1] == "fail":
        print(niveau_selectionne[0])
        reponse_fin = input(f"{the_end} voulez vous recommencer? y/n ")
        if reponse_fin == "y":
            print(choix_retour)
            time.sleep(1.5)
            loop_niveaux2(lvl1) #retour au niveau1
        else:
            print("Allez toucher du gazon alors")





def level_extractor2(niveau_selectionne):
    variable_test0 = niveau_selectionne[0]
    variable_test1 = niveau_selectionne[1]
    variable_test2 = niveau_selectionne[2]
    variable_test3 = niveau_selectionne[3]
    return variable_test0, variable_test1, variable_test2, variable_test3


def presentation_choix2(situation0, choix_1, choix_2, choix_3):
    print("(A tout moment, entrez 000 pour retourner au début de la journée)")
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
    elif reponse == 000:
        choix_final = 000
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
            time.sleep(1.5) #retour aux choix
        elif verif_reponse == 000:
            confirmation = input("Voulez vous vraiment retourner au début de la journée? (y/n) ")
            if confirmation == "y":
                print(choix_retour)
                time.sleep(1.5)
                loop_niveaux2(lvl1) #retour au niveau1
            elif confirmation == "n":
                print("continuons alors...")
                time.sleep(1.5) #retour aux choix
            else:
                print("Bon, tu parles chinois maintenant, j'imagine qu'on continue alors...")
                time.sleep(1.5) #retour aux choix
        elif verif_reponse != 4:
            niveau = input_niveau[verif_reponse] #passer au prochain niveau
            break

    return niveau




#actual code
"""
next_level = loop_niveaux2(lvl1)
print(next_level)

next_level2 = loop_niveaux2(next_level)

next_level3 = loop_niveaux2(next_level2)

#seems like there is a big error in my code lol
#essayer d'identifier les variables avec des valeurs incrementales
"""


"""ce que je veux: une variable qui equivaut a du texte et une question (liste???), ensuite, je veux prendre cette variable et incrémenter
un chiffre de facon a me faire passer a la prochaine variable



lvl = text (meme methode que tantot mais avec une variable que je transforme en string et reconvertis en variable?)
lvl +_1 = text-lvl1_1?


text1 = "blibliblu"
lvl1 = text1

text2 = "blabliblo"
lvl1_1 = text2



#USE DICTIONARIES NOMDICTIONNAIRE = {
    "brand": test1
    "model": test2
}
"""







def level_extractor2(niveau_selectionne):
    lvlstr = str(niveau_selectionne)
    variable_test0 = f"{lvlstr}_1"
    
    return variable_test0




def presentation_choix2(situation0, choix_1, choix_2, choix_3):
    print("(A tout moment, entrez 000 pour retourner au début de la journée)")
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
    elif reponse == 000:
        choix_final = 000
    else:
        choix_final = 4
    
    return choix_final





dynamic_vars = {}
# Use a variable to form a key name and assign a value
name_part = "user"
full_name = f"{name_part}_1"
dynamic_vars[full_name] = "some value"

# Access the value using the dynamic key name
print(dynamic_vars["user_1"])




