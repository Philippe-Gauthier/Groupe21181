"""Fait par Arnaud Baril TGE G.21181"""

import Texteprojet1

choix = 0

def prochainepage(texte):
    print(texte)
    choix = 0
    while choix != "1" and  choix != "2":
       choix = (input("ecrire 1 ou 2\n"))
    choix = int(choix)
    return choix

print(Texteprojet1.page1)
input("Suivant")

print(Texteprojet1.page1_1)
input("suivant")

choix = prochainepage(Texteprojet1.page1_12)
if choix == 1:
    choix = prochainepage(Texteprojet1.page2)
    if choix == 1:
        choix = prochainepage(Texteprojet1.page3)
        Choix = prochainepage(Texteprojet1.page3_1)
    elif choix == 2:
          choix = prochainepage(Texteprojet1.page4) 
if choix == 2:
    choix = prochainepage(Texteprojet1.page5)
    if choix == 1:
        choix = prochainepage(Texteprojet1.page6)
    if choix == 2:
        choix = prochainepage(Texteprojet1.page7)
        if choix == 1:
            choix = prochainepage(Texteprojet1.page8)
        if choix == 2:
            choix = prochainepage(Texteprojet1.page9)
            if choix == 1:
                choix == prochainepage(Texteprojet1.page11)
                if choix =  
            if choix == 2:
                choix = prochainepage(Texteprojet1.page10)


              
else:
    print("fail")
