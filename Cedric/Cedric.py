"""Nom Prenom: ATTIEPO N'GBA JEAN MICHEL CEDRIC"""
"""Tritre du projet1: jeu de quiz éducatif""" 

score = 0

def réponse (choixA, choixB, choixC, vrai_reponse) :
 """But: Poser une question de quiz et vérifier la réponse de l'utilisateur. """
 """Entrées: choixA, choixB et choixC sont les choix proposés et vrai réponse estle numéro de la vrai réponse"""
 """Sorties: retourne 1 point si la réponse est correct sinon 0 piont et s'il écrit n'importe quoi qui n'est pas 1,2,3 retourne 0  """
 print(f"1: {choixA}")
 print(f"2: {choixB}")
 print(f"3: {choixC}")
 decision = input("veuiller saisir votre reponse :")

 if decision == vrai_reponse :
     print("bonne réponse")
     return 1  
 elif decision in ["1", "2", "3"]: 
    print("mauvais réponse")
    return 0
 else:
    print("Erreur, Choix invalide")
    return 0
 
 #Niveau 1 du jeu de quiz educatif: Capitales des pays""" 
print("niveau_1 Capital des pays")
print("---------------------------")

print ("1- Quelle est la capital du Canada ?")
score += réponse ("Otawa", "Toronto", "Vancouver", "1")
print ("score actuel :", score)

print ("2- Quelle est la capitale de la France ?")
score += réponse ("Lyon", "Paris", "Marseille", "2")
print ("score actuel :", score)

print ("3- Quelle est la capitale du Japon ?")
score += réponse ("Kyoto", "Osaka", "Tokyo", "3")
print ("score actuel :", score)

print ("4- Quelle est la capitale de l'Italie ?")
score += réponse ("Vénise", "Rome", "Milan", "2")
print ("score actuel :", score)

print ("5- Quelle est la capitale de l'Allemagne ?")
score += réponse ("Berlin", "Hambourg", "Munich", "3")
print ("score actuel :", score)

print ("6- Quelle est la capitale de l'Espagne ?")
score += réponse ("Madrid", "Barcelone", "Valence", "1")
print ("score actuel :", score)

print ("7- Quelle est la capitale du portugal ?")
score += réponse ("Porto", "Lisbonne", "Faro", "2")
print ("score actuel :", score)

print ("8- Quelle est la capitale du Brésil ?")
score += réponse ("Brasilia", "Sao paulo", "Rio de janeiro", "1")
print ("score actuel :", score)

print ("9- Quelle est la capitale de l'Anglterre ?")
score += réponse ("Manchester", "Liverpool", "Londres", "3" )
print ("score actuel :", score)

print ("10- Quelle est la capitale de la Cote - d'Ivoire")
score += réponse ("Abidjan","Yamoussoukro", "Abobo Doumé", "2")
print ("score actuel :", score)

print ("11- Quelle est la capitale du Maroc ?")
score += réponse ("Casablanca", "Marraketch", "Rabat", "3")
print ("score actuel :", score)

print ("12- Quelle est la capitale de la Chine ?")
score += réponse ("Shanghai","Pékin","Hong Kong", "2")
print ("score actuel :", score)
 

print ("13- Quelle est la capitale de la Russie ?")
score += réponse ("Moscou", "Kazan", "Saint-Pétersbourg", "1")
print ("score actuel :", score)

print ("14- Quelle est la capitale du Mexique ?")
score += réponse ("Cancun", "Yopougon", "Mexico", "3")
print ("score actuel :", score)

print ("15- Quelle est la capitale de l'Argentine ?")
score += réponse ("Koumassi", "Buenos Aires", "Treichville", "2")
print ("score actuel :", score)

print ("16- Quelle est la capitale du Sénégal ?")
score += réponse ("Saint-Louis", "Dakar", "Yopougon(Ghandi)", "2")
print ("score actuel :", score)

print ("17- Quelle est la capitale de la Suisse ?")
score += réponse ("Zurich", "Génève", "Berne", "3")
print ("score actuel :", score)

print ("18- Quelle est la capitale de la Norvège ?")
score += réponse ("Olso", "Bergen", "Trondheim", "1")
print ("score actuel :", score)

print ("19- Quelle est la capitale de la Belgique ?")
score += réponse ("Bruxelle", "Anvers", "Liège", "1")
print ("score actuel :", score)

print ("20- Quelle est la capitale du Ghana ?")
score += réponse ("Port Bouet", "Abobo Doumé", "Accra", "3")
print ("score actuel :", score)

#Niveau 2 du jeu de quiz educatif: Mathématiques et Physique 

print("niveau_2 Mathématiques et Physique")
print("---------------------------")

print ("1-Combien font 5*6 ?")
score += réponse ("30", "25", "√100", "1")
print ("score actuel :", score)

print ("2-Comnien font 100/4 ?")
score += réponse ("100", "25", "2AB", "2")
print ("score actuel :", score)

print ("3-Quelle est l'unité de la masse ?")
score += réponse ("Le litre", "Le kilogramme", "Le mètre", "2")
print ("score actuel :", score)

print ("4- Quelle source d'énergie est renouvelable ?")
score += réponse ("Le pétrole", "Le charbon", "Le soleil", "3")
print ("score actuel :", score)

print ("5- Quel est le périmètre d'un carré de côté de 5cm ?")
score += réponse ("20cm", "25cm", "10cm", "1")
print ("score actuel :", score)

print ("6- Quand un objet tombe, quelle force agit principalement sur lui ?")
score += réponse ("La force de gravité", "La force magnétique", "La force électrique", "1")
print ("score actuel :", score)

print ("7- Quel est l'aire d'un rectangle de longueur 6cm et de largeur 4cm ?")
score += réponse ("10cm²", "24cm²", "20cm²", "2")
print ("score actuel :", score)

print ("8- Quel matériau est un bon conducteur électrique ?")
score += réponse ("Le plastique", "Le bois", "Le cuivre", "3")
print ("score actuel :", score)

print ("9- Que se passe-t-il quand on augmente la vitesse d'un objet ?")
score += réponse ("Son énergie cinétique diminue ", "Sa masse augmente", "Son énergie cinétique augmente", "3")
print ("score actuel :", score)

print ("10- Quel est le résultat de 3² ?")
score += réponse ("41", "9", "3,14", "2")
print ("score actuel :", score)

print ("11- Que se passe-t-il quand un objet flotte sur l'eau ?")
score += réponse ("Il est moins dense que l'eau", "Il est lourd que l'eau", "il a meme masse que l'air", "1")
print ("score actuel :", score)

print ("12- Quelle est la valeur de x dans l'équation: x+4= 10")
score += réponse ("6", "4", "14", "1")
print ("score actuel :", score)

print ("13- Quel changement d'état correspond au passage de solide à liquide ?")
score += réponse ("La fusion","La solidification", "La vaporisation", "3")
print ("score actuel :", score)


print ("14- Que mésure un volmètre ?")
score += réponse ("L'intensité du courant", "La tension électrique", "La résistance", "2")
print ("score actuel :", score)

print ("15- Quel fraction est équivalente à 1/2 ?")
score += réponse ("3/2", "1/4", "2/4", "3")
print ("score actuel :", score)

#Niveau 3 du jeu de quiz educatif: Culture générale  

print("niveau_3 Culture générale")
print("---------------------------") 

print ("1- Qui a découvert l'Amérique en 1492 ?")
score += réponse("Napoléon Bonaparte", "Christophe Colomb", "Marco Polo", "2")
print ("score actuel :", score)

print ("2- Combient y a-t-il de continents sur la terre ?")
score += réponse("5", "6", "7", "3")
print ("score actuel :", score)

print ("3- Quelle est la couleur du ciel par temps clair ?")
score += réponse("Bleu", "Vert", "Gris", "1")
print ("score actuel :", score)

print ("4- Quel animal est appelé le roi de la jungle ?")
score += réponse("Puma", "Lion", "Panthère", "2")
print ("score actuel :", score)

print ("5- Quelle planète est la plus proche du soleil ?")
score += réponse("Mercure", "Vécus", "Mars", "1")
print ("score actuel :", score)

print ("6- Quelle langue est parlée au brésil ?")
score += réponse("Espagnol", "Portugais", "Fraçais", "1")
print ("score actuel :", score)

print ("7- Qui est associé à l'invention de l'ampoule électrique ?")
score += réponse("Albert Einstein", "Thomas Edison", "Isaac Newton", "2")
print ("score actuel :", score)

print ("8- Quel est le plus grand océan au monde ?")
score += réponse("Atlantique", "indien", "Pacifique", "3")
print ("score actuel :", score)

print ("9- Quelle couleur attribue t-on au feu ?")
score += réponse("Orange", "Vert", "Rouge", "3")
print ("score actuel :", score)

print ("10- Quelle est la saison la plus froide ?")
score += réponse("Printemps", "Hiver", "Ete", "2")
print ("score actuel :", score)

print ("11- Quelle est la langue principale parler par les ivoiriens ?")
score += réponse("Français", "Espagnole", "Anglais", "1")
print ("score actuel :", score)

print ("12- Quelle est la seconde langue parler par les ivoiriens ?")
score += réponse("Noussi", "Anglais", "Français", "1")
print ("score actuel :", score)

print ("13- Quel objet sert à écrire ?")
score += réponse("La poutine", "Multimètre", "Crayon", "3")
print ("score actuel :", score)

print ("14- Combient y a t-il de jours dans la semaine ?")
score += réponse("90", "7", "20", "2")
print ("score actuel :", score)

print ("15- Dans quel pays se trouve la plus grande Basilique au monde ?")
score += réponse("Canada", "Italie", "Cote-d'Ivoire", "3")
print ("score actuel :", score)

if score >= 40 :
   print("Félicitation")
else: 
   print("Désolé, vous avez perdu le jeu")

print ("END")































