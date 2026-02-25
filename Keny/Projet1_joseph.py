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

# Demander un choix à l'utilisation
    try: 
     choix = int(input(f"Vous pouvez entrez votre choix svp ({choix_1} ou {choix_2})"))
    except ValueError:
     print("-" * 50)
     print("Choix invalid : veuillez entrer un nombre entier svp.")
     print("-" * 50)
     return demander_choix(choix_1, choix_2, question)
    print("-" * 50)

# Vérifier si le choix est conforme
    if choix == choix_1:
        return choix_1
    elif choix == choix_2:
        return choix_2
    else:
        print("choix invalid : veuillez faire le bon choix svp")
        print("-" * 50)
        
# Si le choix est invalid repose la question
    return demander_choix (choix_1, choix_2, question)  
print("-" * 50)

reponse = demander_choix(1,2, f"Comment Joseph gere t'il son horaire?")

# Question 1 
if reponse == 1: 
        print(f"Joseph gere bien son horaire")
        print(f"Joseph arrive a l'heure")
else:
        print(f"Joseph néglige son horaire")
        print(f"Joseph arrive toujours en retard")
print("-" * 50)

# Question 2
reponse = demander_choix(1,2, f"Comment Joseph organise t'il son travail?")

if reponse == 1:
     print("Joseph revise régulierement ses cours")
     print("Joseph remet ses travaux dans le temps")
else:
     print("Joseph ne revise pas ses cours")
     print("Joseph remet ses travaux toujours en retard")
print("-" * 50)

# Question 3
reponse = demander_choix(1,2, f"Comment Joseph se comporte t'il en classe?")
if reponse == 1:
     print("Joseph écoute attentivement l'enseignant")
     print("Joseph participe en classe")
else:
     print("Jospeh est distrait")
     print("Jospeh joue sur ordinateur pendant l'heure du cour")
print("-" * 50)

# Question 4
reponse = demander_choix(1,2, f"Comment Joseph gere t'il ses laboratoires?")
if reponse == 1:
     print("Joseph fait ses laboratoires dans le temps")
     print("Joseph travail avec diligence")
else:
     print("Joseph néglige les laboratoires")
     print("Joseph ne participe souvent pas aux laboratoires")
print("-" * 50)

# Question 5
reponse = demander_choix(1,2, f"Joseph travaille t'il en équipe?")
if reponse == 1:
     print("Joseph travail avec ses collegues")
     print("Joseph assiste souvent ses collegues dans leurs exercices")
else:
     print("Joseph travail seul à la maison")
     print("Joseph ne partage pas ces lacunes")
print("-" * 50)

# Question 6
reponse = demander_choix(1,2, f"Comment Joseph prépare t'il ses examens finaux?")
if reponse == 1:
     print("Joseph se prépare efficacement")
     print("Joseph reussit son examen")
else:
     print("Joseph ne se prepare pas comme il se doit")
     print("Joseph echoue son examen")
print("-" * 50)

# Question 7
reponse = demander_choix(1,2, f"Comment Joseph gere t'il le stress pendant la session?")
if reponse == 1:
     print("Joseph prend le temps de bien se reposer et de bien dormir")
     print("Joseph reste calme pendant les période difficile")
else:
     print("Joseph accumule beaucoup de stress")
     print("Joseph devient irritable")
print("-" * 50)

# Question 8
reponse = demander_choix(1,2, f"Joseph demande-t-il de l'aide lorsqu'il ne comprend pas?")
if reponse == 1:
     print("Joseph pose des questions à ses enseignants")
     print("Joseph améliore rapidement sa compréhension")
else:
     print("Joseph garde ses difficultés pour lui")
     print("Joseph accumule de lacunes")
print("-" * 50)

# Question 9
reponse = demander_choix(1,2, f"Comment Joseph gere ses finances étudiandes?")
if reponse == 1:
     print("Joseph planifie son budget et évite les dépenses unitile")
     print("Joseph garde toujours un peu d'argent de coté")
else:
     print("Joseph fait des dépenses inutile")
     print("Joseph est tout le temps à court d'argent")
print("-" * 50)

# Question 10
reponse = demander_choix(1,2, f"Joseph entretient-il de bonnes relations avec ses étudiants?")
if reponse == 1:
     print("Joseph est un éudiant respectueux")
     print("Joseph reçoit des conseils des enseignant")
else:
     print("Joseph est tres distant")
     print("Joseph manque des informations importantes")
print("-" * 50)

# Question 11
reponse = demander_choix(1,2, f"Comment Joseph utilise son temps libre?")
if reponse == 1:
     print("Joseph se repose puis révise")
     print("Joseph garde un bon équilibre entre travail et détente")
else:
     print("Joseph passe son temps libre sur les réseax sociaux")
     print("Joseph perd du temps et n'est pas productif")
print("-" * 50)

# Question 12
reponse = demander_choix(1,2, f"Joseph participe-t-il aux projets scolaire?")
if reponse == 1:
     print("Joseph s'implique activement")
     print("Joseph développe de nouvelle compétence")
else:
     print("Joseph ne participe pas aux projets")
     print("Joseph manque des occasion d'apprendre")
print("-" * 50)

# Question 13
reponse = demander_choix(1,2, f"Joseph gere t'il bien son sommeil?")
if reponse == 1:
     print("Joseph dort bien chaue nuit")
     print("Joseph reste concenté")
else:
     print("Joseph se couche tard")
     print("Joseph est souvent fatigué en classe")
print("-" * 50)

# Question 14
reponse = demander_choix(1,2, f"Joseph prend t'il soin de sa santé?")
if reponse == 1:
     print("Joseph mange bien et fait des exercices")
     print("Joseph garde une bonne énergie")
else:
     print("Joseph ne fait pas d'exercie et se nourrit mal")
     print("Joseph tombe souvent malade")
print("-" * 50)

# Question 15
reponse = demander_choix(1,2, f"Joseph demande t'il des retroactions sur ses devoirs?")
if reponse == 1:
     print("Joseph demande des commentaires et progresse")
     print("Joseph corrige ses erreurs et progresse")
else:
     print("Joseph ne demande pas de retroaction")
     print("Joseph avance avec des lacunes")
print("-" * 50)

# Question 16
reponse = demander_choix(1,2, f"Joseph respecte les regles du laboratoire?")
if reponse == 1:
     print("Joseph nettoie son environnement apres chaque maipulation")
     print("Joseph suit toutes les consigne de sécurité")
else:
     print("Joseph ne nettoie pas son environnement")
     print("Joseph ignorore les consignes de sécurité")
print("-" * 50)

# Question 17
reponse = demander_choix(1,2, f"Joseph utilise des ressources externes?")
if reponse == 1:
     print("Joseph regarde des tutoriels")
     print("Joseph se documente en allant à la bibliotheque")
else:
     print("Joseph ne fait aucune recherche")
     print("Joseph se contente juste du cour")
print("-" * 50)

# Question 18
reponse = demander_choix(1,2, f"Joseph respecte-t-il les horaires de remise de devoir?")
if reponse == 1:
     print("Joseph remet toujours son devoir à temps")
     print("Joseph demande des retroactions puis depose")
else:
     print("Joseph ne depose pas dans le temps")
     print("Joseph ne demande pas de retroaction")
print("-" * 50)

# Question 19
reponse = demander_choix(1,2, f"Joseph respecte-t-il les autres étudiants?")
if reponse == 1:
     print("Joseph est respectueux et courtois")
     print("Joseph crée un envirennement positif autour de lui")
else:
     print("Joseph se montre parfois impoli")
     print("Joseph est cource de conflit par moment")
print("-" * 50)

# Question 20
reponse = demander_choix(1,2, f"Joseph participe-t-il aux révisions de groupe?")
if reponse == 1:
     print("Joseph participe activement auxx révision")
     print("Joseph apprend beaucoup grace aux échanges")
else:
     print("Joseph ne participe pas")
     print("Joseph manque des occasions pour apprendre")
print("-" * 50)

# Fin du programme

print("Au revoir !")
