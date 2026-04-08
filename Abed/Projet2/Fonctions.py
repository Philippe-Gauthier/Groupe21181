###Les Imports###
import json
import csv
from Fichiers import notes_propres
from Fichiers import notes 




###les Fonctions de lecture###
def lire_json(path):
    """
    Lit un fichier JSON contenant un dictionnaire d'étudiants
    Args:
        path (str): Le chemin vers le fichier JSON.
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
           



def lire_csv(path):
    """
    Lit un fichier CSV et retourne une liste de dictionnaires.
    Args:
        path (str): Le chemin vers le fichier CSV.
    """
    try:
        with open(path, "r") as f:
            lecteur = csv.reader(f)
            return list(lecteur)
        

    except FileNotFoundError:
        print("Erreur : Le fichier CSV n'a pas été trouvé.")
        return {}
    





def calculer_moyenne(notes):
    """
    Calcule la moyenne des notes pour chaque étudiant.
    Args:
        notes (dict): Un dictionnaire contenant les notes d'un étudiant.
    """
    return (notes["math"] + notes["francais"] + notes["anglais"]) / 3


def classement_etudiants(notes_dict):
    """Classe les étudiants en fonction de leur moyenne.
    Args:
        notes_dict (dict): Un dictionnaire contenant les notes des étudiants."""

    # On transforme le dictionnaire en liste pour pouvoir trier parce que le dictionnaire n'est pas ordonné et on veut trier les étudiants selon leur moyenne
    liste = list(notes_dict.values())

    # trier la liste selon la moyenne de chaque étudiant et il les classe du plus fort au moins fort
    liste_trie = sorted(
        liste,
        key = calculer_moyenne,
        reverse = True  # du plus fort au moins fort
        )
    
  


    return liste_trie


def fusionner_json_csv(etudiant_json, notes_csv):
    """
    Fusionne les données d'un fichier JSON et d'un fichier CSV en un seul dictionnaire.
    Args:
        etudiant_json (dict): Un dictionnaire contenant les informations des étudiants.
        notes_csv (list): Une liste de listes contenant les notes des étudiants.
    
    """
    fusion = {}

    #cette boucle c'est pour ajouter les infos du json
    for id, etu in etudiant_json.items():
        id_int = int(id)  # Convertir l'ID de chaîne de caractères en entier pour correspondre à l'ID dans le CSV car tois mes clé sont des entiers dans le CSV et des chaînes de caractères dans le JSON
        fusion[id_int] = etu.copy()  # Copier les données de l'étudiant du JSON pour ne pas modifier l'originale
 
    #cette boucle sert a ajouter les notes du csv
    for ligne in notes_csv[1:]:#on commence à partir de 1 pour sauter la ligne d'entête du csv parce que dans ma fonction lire csv il ne prend pas en compte la ligne d'entête du csv
        id = int(ligne[0])  # sassurer d'avoir le json et le csv en entier pour pouvoir les fusionner
        math = int(ligne[1])
        francais = int(ligne[2])
        anglais = int(ligne[3])
        if id in fusion:  # Vérifier si l'ID de l'étudiant existe déjà dans le dictionnaire de fusion
            fusion[id]["math"] = math
            fusion[id]["francais"] = francais
            fusion[id]["anglais"] = anglais

    return fusion


def sauvegarder_classement(classement, chemin):
    """
    Sauvegarde le classement des étudiants dans un fichier texte.
    Args:
        classement (list): La liste triée des étudiants.
        chemin (str): Le nom du fichier où écrire le classement.
    """
    with open(chemin, "w") as f:
        for rang, etu in enumerate(classement, start=1):
            moyenne = calculer_moyenne(etu)
            ligne = f"{rang}. {etu['nom']} — moyenne : {moyenne:.2f}\n"
            f.write(ligne)





