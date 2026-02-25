"""
Histoire intéractive
Auteur: Joseph Boka
"""


def demander_choix(choix_1,choix_2, question):
    """
    Entrée: Deux choix (entier) et une question (texte)
    Sortie: choisir une option (1 ou 2)
    But: Demander a l'utilisateur de faire un choix
    """
# Présentation du personnage
    print("Joseph est un étudiant en electronique programmable")
    print("joseph a pour ambition de reussir sa session")

# Afficher la question
    print("\n" + question)

# Demander un choix à l'utilisateur
    choix = int(input(f"Vous pouvez entrez votre choix svp ({choix_1} ou {choix_2})"))
    
    print("-" * 50)

# Vérifier si le choix est valide 
    if choix == choix_1:
        return choix_1
    elif choix == choix_2:
        return choix_2
    else:
        print("choix invalid")

# Si le choix est invalid recommancer à faire un choix
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
if reponse == 1:
     print("Joseph écoute attentivement l'enseignant")
     print("Joseph participe en classe")
else:
     print("Jospeh est distrait")
     print("Jospeh joue sur ordinateur pendant l'heure du cour")
print("-" * 50)

reponse = demander_choix(1,2, f"Comment Joseph gere t'il ses laboratoires?")
if reponse == 1:
     print("Joseph fait ses laboratoires dans le temps")
     print("Joseph travail avec diligence")
else:
     print("Joseph néglige les laboratoires")
     print("Joseph ne participe souvent pas aux laboratoires")
print("-" * 50)

reponse = demander_choix(1,2, f"Joseph travaille t'il en équipe?")
if reponse == 1:
     print("Joseph travail avec ses collegues")
     print("Joseph assiste souvent ses collegues dans leurs exercices")
else:
     print("Joseph travail seul à la maison")
     print("Joseph ne partage pas ces lacunes")
print("-" * 50)

reponse = demander_choix(1,2, f"Comment Joseph prépare t'il ses examens finaux?")
if reponse == 1:
     print("Joseph se prépare efficacement")
     print("Joseph reussit son examen")
else:
     print("Joseph ne se prepare pas comme il se doit")
     print("Joseph echoue son examen")
print("-" * 50)

# Fin du programme
