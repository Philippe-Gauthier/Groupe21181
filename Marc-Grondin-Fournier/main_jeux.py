"""
**********************************************
Projet: 1
Auteur: Marc-André Grondin-Fournier
But du projet: Jeux à arbres multiples
Date: 2026/02/25
Nom du fichier: main_jeux.py
**********************************************
"""
import jeux_repertoire
import jeux_message
menu="O"
while menu != "Q":
    menu=jeux_message.menu()
    match menu:
        case "A":
            jeux_repertoire.roulette_russe() 

        case "B":
            jeux_repertoire.pile_face()    

        case "C":            
            jeux_repertoire.courte_paille()

