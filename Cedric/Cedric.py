#Nom Prenom: ATTIEPO N'GBA JEAN MICHEL CEDRIC
#Tritre du projet1: jeu de quiz éducatif 


def réponse (choixA, choixB, choixC, vrai_reponse) :
 print(f"1: {choixA}")
 print(f"2: {choixB}")
 print(f"3: {choixC}")
 decision = input("veuiller saisir votre reponse :")
 if decision == vrai_reponse :
     print("bonne réponse")
 else:
    print("mauvais réponse")
    return decision
 #Niveau 1 du jeu de quiz educatif: Capitales des pays 
print("niveau_1 Capital des pays")
print("---------------------------")

print ("1- Quelle est la capital du Canada")
réponse ("Otawa", "Toronto", "Vancouver", "1")

print ("2- Quelle est la capitale de la France")
réponse ("Lyon", "Paris", "Marseille", "2")

print ("3- Quelle est la capitale du Japon")
réponse ("Kyoto", "Osaka", "Tokyo", "3")

print ("4- Quelle est la capitale de l'Italie")
réponse ("Vénise", "Rome", "Milan", "2")

print ("5- Quelle est la capitale de l'Allemagne")
réponse ("Berlin", "Hambourg", "Munich", "3")

print ("6- Quelle est la capitale de l'Espagne")
réponse ("Madrid", "Barcelone", "Valence", "1")




