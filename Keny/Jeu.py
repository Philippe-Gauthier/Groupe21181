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

    choix = int(input("Vous pouvez entrez votre choix svp (`{choix_1} ou {choix_2})"))
    print("-" * 50)
    print(f"Joseph est un étudiant en électronique programmable")
    print(f"Joseph a pour ambition de réussir sa session")
    print(f"{choix_1}- joseph gere bien son horaire")
    print(f"{choix_2}- joseph néglige son horaire")
    if choix == choix_1:
        print("Joseph gere bien son horaire")
    elif choix == choix_2:
        print("Joseph néglige son horaire")
    else:
        print("choix invalid")
    return choix  

demander_choix(1,2)

print(f"Joseph gere bien son horaire")
if demander_choix == 3:
        print(f" joseph arrive a l'heure")
else:
        print(f"Joseph arrive souvent en retard")
