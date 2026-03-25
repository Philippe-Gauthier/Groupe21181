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
        except FileExistsError: 
            logs = open(f"{log}.txt", "a")
            logs.write(f"[Try create file - {log} - : {time}]\n")
            logs.write(f"[ERROR: Fichier existant - {log} - : {time}]\n")
            logs.close
            logs = open(f"{log}.txt", "a")
            logs.write(f"[- {append} - was added to {file} : {time}]\n")
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
                        logs.write(f"[In {cours} added {date},{info} {time}]\n")
                        logs.close
                        fichier=open(f"{cours}.csv","a")
                        fichier.write(f"{date},{info}")
                        fichier.close
                        break
        break
                

def lecture(cours):
    try:
        lecturetxt=open(f"{cours}.txt","r")
        lecturecsv=open(f"{cours}.csv","r")
        print(f"\nNotes -------------------\n {lecturetxt.readlines()}")
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
        for i in dateinfo:
            print(f"Examen le {i["jj"]}/y:{i["mm"]}/{i["aaaa"]}. Info: {i["info"]}")
        lecturetxt.close
        lecturecsv.close
    except FileNotFoundError:
        print("Fichiers non trouvé")
        




