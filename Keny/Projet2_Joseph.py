"""
Gestion de budget
Auteur: Joseph Boka
"""
import csv 
 
def lire_liste_depense(liste_depenses.csv):
    """
    lire un fichier CSV
    afficher chaque dépense
    calculer le total
    """
    Liste_depenses = {}
    try:
        fichier = open("liste_depenses.csv", "r")
        lecteur = csv.reader(fichier)

        for element in Liste_depenses:
            print(f"{element},{Liste_depenses[element]}$")
        Liste_depenses[element]
        fichier.close()

        #calcul du montant total
        Total = 0 
        for montant in Liste_depenses.values():
            Total += montant
        print(f"montant total : {Total}$")
    except FileNotFoundError:
        print("Erreur : fichier introuvable")

    return liste_depenses


