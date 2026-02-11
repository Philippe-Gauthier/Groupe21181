"""
Histoire intéractif
Auteur: Joseph Boka
"""


def demander_choix(choix_1,choix_2):
    """
    Entrée: Deux choix (entier)
    Sortie: option choisie (texte)
    But: Demander a l'utilisateur de faire un choix
    """

    choix = input("Vous pouvez entrez votre choix svp 1(choix_1 ou choix_2)")
    print("------------------------------")
    print(f"Joseph est un étudiant en électronique programmable")
    print(f"Joseph a pour ambition de réussir sa session")
    print(f"{choix_1}- joseph gere bien son horaire")
    print(f"{choix_2}- joseph néglige son horaire")
    
    if choix == "choix_1":
        print("Joseph gere bien son horaire")
    else:
        print("Joseph néglige son horaire")
    return choix

demander_choix(1,2)

print(f"Joseph gere bien son horaire")
if demander_choix == "choix_3":
        print(f"1- joseph arrive a l'heure")
else:
        print(f"Joseph arrive souvent en retard")
