import datetime 
from time import sleep

'''
Projet 2 Lecture et écriture de fichiers : FICHIER DE FONCTIONS :)
Félix-Olivier rioux
'''
def lirecours(cours):
    try: 
        listecours = open(f"{cours}.txt","r")
        fichier=listecours.readlines()
        for ligne in fichier:
            classe=ligne.split(",")
            liste=set()
            for cours in classe:
                liste.add(cours)
        listecours.close()
        try:
            print(liste)
        except:
            print("Aucun cours trouvé")
        x=0
    except FileNotFoundError:
        print("Aucun cours trouvé")
        x=1
        return x

def creationfichier(cours,log):
    delete=input("Effacer la liste de cours? Cela n'efface pas vos notes.\ny/n\n")
    if delete=="y":
        try:
            fichier=open(f"{cours}.txt","w")
            fichier.write("Liste de vos cours,")
            fichier.close()
            print("Liste effacé")
        except FileNotFoundError:
            pass
    lirecours(cours)
    while True:
        time=datetime.datetime.now()
        nom=input("Ajouter un cours? ")
        if nom=="":
            break
        while True:
            try:
                logs = open(f"{log}.txt", "x")
                logs.close()
                logs = open(f"{log}.txt", "w")
                logs.write(f"[Created file - {log} - ; {time}]\n")
                logs.close()
            except FileExistsError: 
                logs = open(f"{log}.txt", "a")
                logs.write(f"[- {nom} - was added to {cours}.txt ; {time}]\n")
                logs.close()
                try:
                    fichier=open(f"{cours}.txt","x")
                    fichier.close()
                except FileExistsError:
                    fichier=open(f"{cours}.txt","a")
                    fichier.write(f"{nom},")
                    fichier.close()
                    lirecours(cours)
                    break

def Document(append,file,log):
    '''
    Entrée: append = info choisi par l'utilisateur. file = choisir le fichier où écrire. log = choisir où logger l'info
    Sortie: Dans le fichié choisi, ajout de ligne avec l'info et le datetime
    '''
    while True:
        time=datetime.datetime.now()
        try:
            logs = open(f"{log}.txt", "x")
            logs.close
            logs = open(f"{log}.txt", "w")
            logs.write(f"[Created file - {log} - ; {time}]\n")
            logs.close
        except FileExistsError: 
            logs = open(f"{log}.txt", "a")
            logs.write(f"[- {append} - was added to {file} ; {time}]\n")
            while True:
                try:
                    fichier=open(f"{file}","x")
                    fichier.close
                except FileExistsError:
                    fichier=open(f"{file}","a")
                    fichier.write(f"{append},")
                    break
            break
    fichier.close()
    logs.close()

def dateexam(cours,date,info,log):
    '''
    Entrée: Le nom du cours pour écrire dans le fichier rattaché, la date entrée par l'user, l'information en rapport à l'exam, le fichier log pour logger l'info
    Sortie: Dans le fichier rattaché écrire l'information de la date et info, alongside rentrer les log dans le fichier log
    But: Stocker dans un fichier CSV l'information entrée par l'utilisateur pour l'utiliser comme dictionnaire quand on désire print.
    '''
    while True:
        time=datetime.datetime.now()
        try:
            logs = open(f"{log}.txt", "x")
            logs.close()
        except FileExistsError: 
            while True:
                try: 
                    fichier=open(f"{cours}.csv","x")
                    fichier.close()
                except FileExistsError:
                        logs = open(f"{log}.txt", "a")
                        logs.write(f"[In {cours}.csv added {date}, {info} ; {time}]\n")
                        logs.close()
                        fichier=open(f"{cours}.csv","a")
                        fichier.write(f"{date},{info}\n")
                        fichier.close()
                        break
        break
                

def lecture(cours):
    '''
    Entrée: le nom du cours
    Sortie: un print de l'information dans le fichier choisi
    But: Print l'information demandé par l'utilisateur
    '''
    try:
        lecturetxt=open(f"{cours}.txt","r")     
        print(f"\nNotes ----------------------------\n {lecturetxt.readlines()}")
        lecturetxt.close()
    except FileNotFoundError:
        print(f"\nNotes ----------------------------\nAucunes notes trouvées")
    try: 
        lecturecsv=open(f"{cours}.csv","r")
        csv=lecturecsv.readlines()
        dateinfo=[]
        for ligne in csv:
            ligne=ligne.strip()
            date = ligne.split(",")
            dictionnaire = {
                "jj": date[0],
                "mm": date[1],
                "aaaa": date[2],
                "info": date[3],
            }
            dateinfo.append(dictionnaire)
        print("Examens --------------------------")
        for i in dateinfo:
            print(f"{i["jj"]}/{i["mm"]}/{i["aaaa"]}. \nInfo: {i["info"]}\n")
        lecturecsv.close()
    except FileNotFoundError:
        print("Examens --------------------------\nAucun examen à venir")
        




