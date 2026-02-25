choix = int(input("ecrit 1 ou 2 \n 1 addition \n 2 soustraction"))         
nombre1 = int(input("choisis un nombre"))
nombre2 = int(input("choisis un autre nombre"))
if choix == 1:
    print(nombre1 + nombre2)
elif choix == 2:
    print(nombre1 - nombre2)
else:
    print("fail")
