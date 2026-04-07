import csv

notes = [
    ["id", "maths", "français", "anglais"],
    [1, 85, 78, 90],
    [2, 70, 65, 80],
    [3, 90, 88, 92],
    [4, 60, 75, 70],
    [5, 88, 82, 85],
    [6, 72, 68, 74],
    [7, 95, 90, 93],
    [8, 66, 70, 69],
    [9, 80, 77, 84],
    [10, 78, 79, 76],
    [11, 85, 83, 81],
    [12, 91, 89, 94],
    [13, 73, 75, 72],
    [14, 68, 70, 65],
    [15, 87, 85, 88],
    [16, 62, 64, 60],
    [17, 90, 92, 91],
    [18, 77, 76, 78],
    [19, 84, 82, 80],
    [20, 79, 81, 77]
]

with open("notes_etudiants.csv", "w", newline="") as f: #with ferme le fichier automatiquement apres l'ecriture
    writer = csv.writer(f) #csv.writer permet d'ecrire dans un fichier csv, il prend en argument le fichier ouvert en mode ecriture
    writer.writerows(notes) #writerows ecrit toutes les lignes du tableau notes dans le fichier csv

with open("notes_etudiants.csv", "r") as f:
    reader = csv.reader(f) #csv.reader permet de lire un fichier csv, il prend en argument le fichier ouvert en mode lecture
    for row in reader: #for permet de parcourir toutes les lignes du fichier csv, row est une liste qui contient les valeurs de chaque colonne de la ligne
        print(row) #affiche la ligne lue du fichier csv