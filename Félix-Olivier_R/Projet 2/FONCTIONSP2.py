import datetime 
from time import sleep

'''
Projet 2 Lecture et écriture de fichiers FICHIER DE FONCTIONS :)
Félix-Olivier rioux
'''


def Document(append,file,log):
    '''
    Entrée: append = info choisi par l'utilisateur. file = choisir le fichier où écrire. log = choisir où logger l'info
    Sortie: Dans le fichié chooisi, ajout de ligne avec l'info et le datetime
    '''
    time=datetime.datetime.now()
    while True:
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
                    fichier.write(f"{append}    -   ")
                    break
            break
    fichier.close
    logs.close

def dateexam(cours,date,info,log):
    '''
    Entrée: Le nom du cours pour écrire dans le fichier rattaché, la date entrée par l'user, l'information en rapport à l'exam, le fichier log pour logger l'info
    Sortie: Dans le fichier rattaché écrire l'information de la date et info, alongside rentrer les log dans le fichier log
    But: Stocker dans un fichier CSV l'information entrée par l'utilisateur pour l'utiliser comme dictionnaire quand on désire print.
    '''
    time=datetime.datetime.now()
    fichier=open(f"{cours}.csv","a")
    while True:
        try:
            logs = open(f"{log}.txt", "x")
            logs.close
        except FileExistsError: 
            while True:
                try: 
                    fichier=open(f"{cours}.csv","x")
                    fichier.close
                except FileExistsError:
                        logs = open(f"{log}.txt", "a")
                        logs.write(f"[In {cours}.csv added {date},{info} ; {time}]\n")
                        logs.close
                        fichier=open(f"{cours}.csv","a")
                        fichier.write(f"{date},{info}\n")
                        fichier.close
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
        lecturecsv=open(f"{cours}.csv","r")
        print(f"\nNotes ----------------------------\n {lecturetxt.readlines()}")
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
        lecturetxt.close
        lecturecsv.close
    except FileNotFoundError:
        print("Fichiers non trouvé")
        




