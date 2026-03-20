import sys, time

'''
Projet 2 Lecture et écriture de fichiers FICHIER DE FONCTIONS :)
Félix-Olivier rioux
'''

'''
variable = open(" 'nom du fichier' ",   " '_' ")
r = Read
w = Write
a = Add
x = Create
'''




def logs(input):
    '''
Entrée: input à rentrer dans les logs
Sortie: Dans le fichié Projet2logs, ajout de ligne
'''
    while True:
        try:
            logs = open("Projet2logs.txt", "x")
            logs.close
        except: 
          
            logs = open("Projet2logs.txt", "a")
            logs.write(f"{input}")
            break
    logs.close

def choice_num(): 
    """
    Entrée: Nombre (ou pas) entré par lutilisateur
    Sortie: Un numéro en format INT, entrée par l'utilisateur, ou un erreur
    But: S'assurer que l'utilisateur rentre un nombre pour pouvoir l'affecter avec des maths.
    """
    while True: 
        number=input("Veuillez entrez un nombre : ") 
        try:
            result=int(number)
            break
        except ValueError:
            print("\nInvalide")
    return result

