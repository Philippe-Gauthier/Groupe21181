import json

def lire_json(path):
    """
    Lit un fichier JSON contenant un dictionnaire d'étudiants
    """
    try:
        # Ouvrir le fichier JSON
        with open(path, "r") as f:
            return json.load(f)  # Charger le contenu du fichier JSON et le retourner
    except FileNotFoundError:
        print("Erreur : Le fichier json n'a pas été trouvé.")
        return {}
    except json.JSONDecodeError:
        print("Erreur : Le fichier json est mal formé.")
        return {}
           


import csv

def lire_csv(path):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires.
    """
    try:
        with open(path, "r") as f:
            lecteur = csv.reader(f)
            return list(lecteur)
        

    except FileNotFoundError:
        print("Erreur : Le fichier CSV n'a pas été trouvé.")
        return {}
    


if __name__ == "__main__":
    notes = lire_csv("notes_etudiants.csv")
    print(notes)