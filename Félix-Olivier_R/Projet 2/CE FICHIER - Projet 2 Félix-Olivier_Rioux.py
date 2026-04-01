import FONCTIONSP2 as fonc
import sys
'''
Projet 2 Lecture et écriture de fichiers
Félix-Olivier rioux
'''
#Définir le fichier pour les logs
flogs="Projet_2_logs"
#Définir le fichier dans lesquels seront stocké le nom des cours
flist="liste_cours"


fonc.creationfichier(f"{flist}",f"{flogs}")
# Document ("texte à ajouter","nom fichier où ajouter", flogs)
while True:
    ajout=input("Que souhaitez vous ajouter dans vos notes de cours? (Laisse vide pour ignorer.)\n")
    if ajout=="":
        break
    print("Pour quel cours?\n")
    x=fonc.lirecours(flist)
    cours=input("") #Premier type de fichier : txt write and read
    fonc.Document(f"{ajout}",f"{cours}.txt",f"{flogs}")
    
while True:
    exam=input("\nAjouter une nouvelle date d'examen? (Laisse vide pour ignorer.)\njj,mm,aaaa\n") # Deuxième type de fichier : csv write and read
    if exam=="":
        break
    print("Pour quel cours?\n")
    x=fonc.lirecours(flist)
    cours=input("")
    if x==1:
        sys.exit(0)
        print("Vous n'avez aucun cours d'inscrit. Veuillez en ajouter. Programm terminé.")

    info=input("\nPécisions sur l'examen: ")
    fonc.dateexam(f"{cours}",f"{exam}",f"{info}",f"{flogs}")

while True:
    lecture=input("\nVoir vos notes et les dates d'examen pour l'un de vos cours? (Laisse vide pour ignorer. Cela va aussi terminer le programme)")
    print("Pour quel cours?\n")
    x=fonc.lirecours(flist)
    cours=input("")
    if x==1:
        sys.exit(0)
        print("Vous n'avez aucun cours d'inscrit. Veuillez en ajouter. Programm terminé.")
    if lecture=="": 
        break
    fonc.lecture(f"{lecture}")

    # Non la dernière ligne dans mon README n'est pas là pour avoir une meilleure note :)
    



