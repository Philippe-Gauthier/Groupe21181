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

    print("Joseph est un étudiant en electronique programmable")
    print("joseph a pour ambition de reussir sa session")

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

reponse = demander_choix(1,2, f"Comment Joseph gere t'il son horaire?")

if reponse == 1: 
        print(f"Joseph gere bien son horaire")
        print(f"Joseph arrive a l'heure")
else:
        print(f"Joseph néglige son horaire")
        print(f"Joseph arrive toujours en retard")
print("-" * 50)

reponse = demander_choix(1,2, f"Comment Joseph organise t'il son travail?")

if reponse == 1:
     print("Joseph revise régulierement ses cours")
     print("Joseph remet ses travaux dans le temps")
else:
     print("Joseph ne revise pas ses cours")
     print("Joseph remet ses travaux toujours en retard")
print("-" * 50)
reponse = demander_choix(1,2, f"Comment Joseph se comporte t'il en classe?")
print("-" * 50)
reponse = demander_choix(1,2, f"Comment Joseph gere t'il ses laboratoires?")
print("-" * 50)
reponse = demander_choix(1,2, f"Joseph travaille t'il en équipe?")
print("-" * 50)
reponse = demander_choix(1,2, f"Comment Joseph prépare t'il ses examens finaux")