#NOM: NTOM BERNARD
#PROJET1: examen de revision pour son cours d'electronique
#partie_1 de l'examen de revision en electronique

def reponse(choix1, choix2, choix3, vrai_reponse): 
    print(f"1: {choix1}") 
    print(f"2: {choix2}")
    print(f"3: {choix3}")
    decision = input("donner la reponse :")
    if decision == vrai_reponse :
        print("reponse bonne")
    else:
        print("fausse reponse")
        return decision
print("partie_1 element de base")
print("-------------------------")

print("1- quel est l'unite du courant")
reponse("voltage", "ampere", "volmetre", "2")

print("2- quel est l'unite de la tension")
reponse("volmetre", "ampere", "volt", "1")

print("3- quel est l'unite de la resistance")
reponse("faraday", "ampere", "ohm", "3")

print("quel est l'unite du condensateur")
reponse("farad", "ampere", "ohm", "1")

print("5- quel est le role d'une resistance")
reponse("tocker de l'energie", "limiter le courant", "redresser une tension", "2")

print("A quoi sert une inductance ")
reponse("iltrer les hautes frequences", "filtrer les bases frequences", "redresser un courant", "2")

print("La loi d_Ohm s_écrit")
reponse("P=U⋅IP=U⋅I", "U=R⋅IU=R⋅I", "R=P/IR=P/I", "2")

