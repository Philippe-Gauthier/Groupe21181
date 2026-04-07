import json

import csv

etudiants = [
    {"id": 1, "nom": "Alice", "age": 20},
    {"id": 2, "nom": "Bob", "age": 22},
    {"id": 3, "nom": "Charlie", "age": 21},
    {"id": 4, "nom": "Diana", "age": 19},
    {"id": 5, "nom": "Eve", "age": 23},
    {"id": 6, "nom": "Frank", "age": 20},
    {"id": 7, "nom": "Grace", "age": 22},
    {"id": 8, "nom": "Henry", "age": 21},
    {"id": 9, "nom": "Ivy", "age": 20},
    {"id": 10, "nom": "Jack", "age": 22},
    {"id": 11, "nom": "Kate", "age": 19},
    {"id": 12, "nom": "Liam", "age": 23},
    {"id": 13, "nom": "Mia", "age": 21},
    {"id": 14, "nom": "Noah", "age": 20},
    {"id": 15, "nom": "Olivia", "age": 22},
    {"id": 16, "nom": "Peter", "age": 19},
    {"id": 17, "nom": "Quinn", "age": 23},
    {"id": 18, "nom": "Rachel", "age": 21},
    {"id": 19, "nom": "Steve", "age": 20},
    {"id": 20, "nom": "Tina", "age": 22} 
]

with open("etudiants.json", "w") as f:
    json.dump(etudiants, f, indent=4)

#json.load permet de lire un fichier json


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

notes_propres = {}

with open("notes_etudiants.csv", "r") as f:
    reader = csv.reader(f)  # csv.reader permet de lire un fichier csv, il prend en argument le fichier ouvert en mode lecture
    next(reader)
    for row in reader:
        notes = {
            "id": int(row[0]),
            "math": int(row[1]),
            "francais": int(row[2]),
            "anglais": int(row[3])
        }
        notes_propres[notes["id"]] = notes

print(json.dumps(notes_propres, indent=4))