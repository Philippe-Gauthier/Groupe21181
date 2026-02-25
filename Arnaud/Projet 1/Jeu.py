"""
nom du jeu: J'avais une bonne excuse...
Auteur: Arnaud Baril TGE G.21181
Version de remise
"""

import Texteprojet1
#La variable constante NOUVEL_ESSAI sert à la boucle while permetant de recommencer le jeu après une mauvaise fin.
NOUVEL_ESSAI = True

"""
entré de la fonction: La page de texte actuelle.
sortie de la fonction: Retourne le choix de l'utilisateur.
but de la fonction: print la page actuel et prépare la prochaine selon son choix.
"""
def prochainepage(texte):
    print(texte)
    choix = 0
    while choix != "1" and  choix != "2":
       choix = (input("Votre choix:  "))
    choix = int(choix)
    return choix

"""
entré de la fonction: page actuelle.
sortie de la fonction: rien
but de la fonction: faire une pause entre deux pages se suivant et sans choix.
"""
def lire_la_suite(page):
    print(page)
    input("peser Entrer pour la suite")
    return

#Permet a l'utilisateur de recommencer après avoir atteint une fin.
while  NOUVEL_ESSAI == True:
    
    lire_la_suite(Texteprojet1.page_debut)
    lire_la_suite(Texteprojet1.page_debut1)

    choix = prochainepage(Texteprojet1.page_debut2)
    if choix == 1:
        choix = prochainepage(Texteprojet1.page_dance)
        if choix == 1:
            choix = lire_la_suite(Texteprojet1.page_dance_robot)
            Choix = lire_la_suite(Texteprojet1.page_dance_break)
        if choix == 2:
            choix = lire_la_suite(Texteprojet1.page_gigue) 
    if choix == 2:
        choix = prochainepage(Texteprojet1.page_heehee)
        if choix == 1:
            choix = lire_la_suite(Texteprojet1.page_tamiat)
        if choix == 2:
            choix = prochainepage(Texteprojet1.page_autopsie)
            if choix == 1:
                choix = lire_la_suite(Texteprojet1.page_glandis)
            if choix == 2:
                choix = prochainepage(Texteprojet1.page_kazakstan)
                if choix == 1:
                    choix = prochainepage(Texteprojet1.page_politique)
                    if choix == 1:
                        choix = lire_la_suite(Texteprojet1.page_coeur)
                        choix = prochainepage(Texteprojet1.page_reptilien)
                        if choix == 1:
                            choix = prochainepage(Texteprojet1.page_beurre)
                            if choix == 1:
                                choix = lire_la_suite(Texteprojet1.page_baba)
                            if choix == 2:
                                choix = lire_la_suite(Texteprojet1.page_again)
                        if choix == 2: 
                            choix = prochainepage(Texteprojet1.page_portal)
                            if choix == 1:
                                choix = lire_la_suite(Texteprojet1.page_beurre)
                            if choix == 2:
                                choix = prochainepage(Texteprojet1.page_double)
                                if choix == 1:
                                    choix = lire_la_suite(Texteprojet1.page_retour)
                                    choix = lire_la_suite(Texteprojet1.page_retour2)
                                if choix == 2:
                                    choix = lire_la_suite(Texteprojet1.page_dopleganger)
                            if choix == 2:
                                choix = prochainepage(Texteprojet1.page_jurassic)
                                if choix == 1:
                                    choix = prochainepage(Texteprojet1.page_explication)
                                    if choix == 1:
                                        choix = lire_la_suite(Texteprojet1.page_space_jesus)
                                        choix = prochainepage(Texteprojet1.page_nouveau_monde)
                                        if choix == 1:
                                            choix = prochainepage(Texteprojet1.page_anglais)
                                            if choix == 1:
                                                choix = lire_la_suite(Texteprojet1.page_magie)
                                                choix = prochainepage(Texteprojet1.page_magie_chat)
                                                if choix == 1:
                                                    choix = lire_la_suite(Texteprojet1.page_magie_portail)
                                                    choix = lire_la_suite(Texteprojet1.page_monologue)
                                                    choix = lire_la_suite(Texteprojet1.page_wtf)
                                            if choix == 2:
                                                choix = prochainepage(Texteprojet1.page_hero)
                                                if choix == 1:
                                                    choix = lire_la_suite(Texteprojet1.page_hero_bad_sword)
                                                if choix == 2:
                                                    choix = prochainepage(Texteprojet1.page_hero_operation)
                                                    if choix == 1:
                                                        choix = lire_la_suite(Texteprojet1.page_hero_quest)
                                                    if choix == 2:
                                                        choix = lire_la_suite(Texteprojet1.page_glandalf)
                                                if choix == 2:
                                                    choix = lire_la_suite(Texteprojet1.page_magie_combat)
                                            if choix == 2:
                                                choix = lire_la_suite(Texteprojet1.page_hero)
                                        if choix == 2:
                                            choix = lire_la_suite(Texteprojet1.page_boude)
                                    if choix == 2: 
                                        choix = prochainepage(Texteprojet1.page_nobel)
                                        if choix == 1:
                                            choix = prochainepage(Texteprojet1.page_noel)
                                            if choix == 1:
                                                choix = lire_la_suite(Texteprojet1.page_nomnom_divin)
                                            if choix == 2:
                                                choix = lire_la_suite(Texteprojet1.page_retour_space_jesus)
                                        if choix == 2:
                                            choix = lire_la_suite(Texteprojet1.page_prout)        
                                if choix == 2:
                                    choix = prochainepage(Texteprojet1.page_rein)
                                    if choix == 1:
                                        choix = prochainepage(Texteprojet1.page_dinogarou)
                                        if choix == 1:
                                            choix = lire_la_suite(Texteprojet1.page_fin_rein)
                                        if choix == 2: 
                                            choix = lire_la_suite(Texteprojet1.page_rein_garou)
                                    if choix == 2:
                                        choix = lire_la_suite(Texteprojet1.page_boom_dino)
                    if choix == 2:
                        choix = lire_la_suite(Texteprojet1.page_oeil)
                        
                    if choix == 2:
                        choix = lire_la_suite(Texteprojet1.page_borat)
                if choix == 2:
                    choix = lire_la_suite(Texteprojet1.page_borat)
