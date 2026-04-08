from Fonctions import (
    lire_json,
    lire_csv,
    fusionner_json_csv,
    classement_etudiants,
    sauvegarder_classement,
    calculer_moyenne
)

def main():


    # 1. Lire les fichier
    etudiants = lire_json("etudiants.json")
    notes = lire_csv("notes_etudiants.csv")

    if not etudiants or not notes:
        print("Impossible de continuer : un des fichiers n'a pas été chargé.")
        return

    # 2. Fusionner les donné
    fusion = fusionner_json_csv(etudiants, notes)

    # 3. Classer les étudiant par moyennes
    classement = classement_etudiants(fusion)

    # 4. Sauvegarder le classement dans un fichier
    sauvegarder_classement(classement, "classement.txt")

    # 5. Afficher un resume de ce que fait leprograme
    print("Le classement a été sauvegardé dans 'classement.txt'.\n")
    print("Top 3 des étudiants :\n")

    for etu in classement[:3]:
        moyenne = calculer_moyenne(etu)
        print(f"{etu['nom']} — moyenne : {moyenne}")

    print("\nProgramme terminé.")

if __name__ == "__main__":
    main()