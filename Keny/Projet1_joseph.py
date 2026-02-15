"""
Histoire intéractif
Auteur: Joseph Boka
"""


def demander_choix(choix_1,choix_2, question):
    """
    Entrée: Deux choix (entier) et une question (texte)
    Sortie: choisir une option (1 ou 2)
    But: Demander a l'utilisateur de faire un choix
    """

    print(question)
    choix = int(input(f"Vous pouvez entrez votre choix svp ({choix_1} ou {choix_2})"))
    print("-" * 50)

    
    if choix == choix_1:
        return choix_1
    elif choix == choix_2:
        return choix_2
    else:
        print("choix invalid")
    return demander_choix (choix_1, choix_2, question)  
print("-" * 50)

reponse = demander_choix(1,2, f"comment Joseph gere t'il son horaire?")

if reponse == 1: 
        print(f" joseph gere bien son horaire")
        print(f"Joseph arrive a l'heure")
else:
        print(f"Joseph néglige son horaire")
        print(f"joseph arrive en retard")
print("-" * 50)

reponse = demander_choix(1,2, f"comment Joseph travail-il?")

if reponse == 1:
     print("joseph revise régulierement ses cours")
     print("Joseph remet ses travaux dans le temps")
else:
     print("Joseph ne revise pas ses cours")
     print("Joseph remet ses travaux toujours en retard")
