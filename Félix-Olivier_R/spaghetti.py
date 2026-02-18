# Félx-Olivier Rioux        Projet 1: histoire intéractive

import time, sys
JOUER=True

rejouer=("0") # Défénir les variable qui décide si le jeu fonctionne ou non. Pour pas que le jeu break 
nb_lecture=0   # Permet de garder le nombre de 

def choice_user2(choix1,choix2): # Fonction de question à 2 options
    result=0
    print("\n______________________________________________")
    print(f"|     1 = {choix1}")
    print(f"|     2 = {choix2}")
    while(result!=1 and result!=2):
        decision=input("       Entrée: ")
        while True:
            try:
                result=int(decision)
                break
            except ValueError:
                decision=input("Veuillez entrer un nombre: ")
    return result

def choice_user3(choix1,choix2,choix3):   # Fonction de question à 3 options
    result=0
    print("\n______________________________________________")
    print(f"|     1 = {choix1}")
    print(f"|     2 = {choix2}")
    print(f"|     3 = {choix3}")
    while(result!=1 and result!=2 and result!=3):
        decision=input("       Entrée: ")
        while True:
            try:
                result=int(decision)
                break
            except ValueError:
                decision=input("\nVeuillez entrer un nombre: ")
    return result

def choice_num(question): # Permet à la fonction de looper jusqu'à ce que l'utilisateur ait rentré un nombre entier
    while True: 
        number=input(f"{question} : ") 
        try:
            result=int(number)
            break
        except ValueError:
            print("\nVeuillez entrer un nombre.")
    return result

def texte_delai(text, delay=0.05, newline=True): # Code emprunté de monsieur copilot. Permet d'écrire une lettre à la fois
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()   
            time.sleep(delay)
        if newline:
            sys.stdout.write("\n")
            sys.stdout.flush()



while(JOUER==True): # Permet de looper le jeu selon l'input de l'user après sa lecture
    
    if(nb_lecture>0):
        input("\nContinuer?   -Suite") # Permet d'afficher un message différent selon le nombre de fois que l'utilisateur a joué
    else:
        input("\nCommencer?   -Suite")

    print("\nLa création, la musique, l'art en général, j'ai jamais réussi à trouver une bonne raison, \nou je dirais que j'ai pas encore trouvé l'occasion d'abandonner tout et de m'y mettre pour de bon.\nJ'ai 21 ans, en ce moment je travail dans le provigo du coin. Chu, comme, zéro populaire,\npar contre c'est plus par choix que pas résultat de mes actions ou whatever.\nJe dirais pas que j'ai beaucoup d'argent, mais j'ai quand même un ford raptor 2017.   -Suite") 
    input()
    print("Très bon prix d'ailleurs. Ça me rappele l'interaction que j'ai eu avec le vendeur, c'était quand même vraiment mongole.\nAprès avoir démontré mon intérêt sur l'annonce facebook le gars m'avais donné un coup de fil.     -Suite")
    input() # Permet d'attendre l'input de l'utilisateur avant de continuer

    print("     -Bonjour, est-ce que je parle à Nicolas?\n")
    time.sleep(0)
    print("   **Regardez le README s'il y a confusion.** ")
    phone_1=choice_user2("Oui","Non")  # Évènement 1 - phone_1 appel pour la voiture

    if(phone_1==1): # phone_1 OUI
        print("\n-Oui c'est bien moi.")
        time.sleep(0)
        print("-Je m'adresse à qui?")
        time.sleep(0)
        print("     -C'est George, voyons criss tu sonne bin jeune, c'est tu vraiment toi sur facebook?")
        time.sleep(0)
        texte_delai("ouch" , delay=(0))

        char_1=choice_user3("Oui c'est moi","Racrocher","Es-tu sérieux pour le truck ou non?") # char_1 réponse - Évènement 2

        if(char_1==1): #char_1 option 1
            print("\n-Oui c'est moi, on me le dit souvent, toé t'as quel age? Tu sonnes crissement vieux.")
            time.sleep(0)
            print("J'ai pas pu me retenir sa voix criait la vieillesse.")
            time.sleep(0)
            print("Au final il m'avait offert de passer chez eux la même journée.")
            time.sleep(0)

        elif(char_1==2): #char_1 option 2
            print("\nBon.. J'ai racroché.")
            time.sleep(0)

        elif(char_1==3): #char_1 option 3
            print("\n-Scuse moi, mais es-tu sérieux avec le truck ou tu va perdre mon temps?")
            time.sleep(0)
            print("     -Pardonne moi, tu souhaites le voir? Viens à l'adresse indiqué sur l'annonce ajourd'hui à partir de 3h si tu peux.      -Suite")
            input()
            print("C'est bon, on va se voir.")  
            time.sleep(0)

    elif(phone_1==2): # phone_1 NON
        print("n-Non scuse moi lgros, tu dois avoir le mauvais numéro.") 
        time.sleep(0)
        print("J'étais sûr c'était un foutu spam, j'ai pas réfléchi..   -Suite")
        input()
        print("     -Ah je suis désolé. C'est pas toi qui m'avait envoyé un message pour le ford ce matin?")
        time.sleep(0)
        texte_delai("Ah, shit.",delay=(0)) # Effet type writter
        time.sleep(0)
        print("Je ne pouvais pas retourner la situation, je sais pas si j'avais simplement pas allumé, mais j'ai choké.\nJ'avais 18 ans je sais pas trop quoi te dire. Compte-tenu qu'il savait pas j'étais qui je ne me suis pas retenue..       -Suite")
        input()

        print("-Non désolé. Je te souhaite une bonne journée.")
        time.sleep(0)
        print("     -Ah pardon, bonne journée à toi aussi.")
        time.sleep(0)

    print("Je dois l'admettre j'étais un peu impuslif..\nAu moins j'ai le char.       -Suite")
    input()

    if(char_1==2 or phone_1==2): 
        print("Au final chu juste aller voir le gars sans m'annoncer. Quand même content que tout ait fonctionné.")
        time.sleep(0)

    print("     -Chérie? T'avais tu fais la lessive ou pas encore? Moi et ton père on a du linge à laver pour la semaine prochaine.")
    time.sleep(0)
    print("Ouaip, j'habite encore chez mes parents, tu serais fou de croire que je peux me permettre un chez moi dans cette économie.    -Suite")
    input()

    print("Ils s'en vont en vacances la semaine prochaine, j'ai quand même hâte ça va me donner tellement de temps pour moi. ")
    time.sleep(0)
    print("-Ouais je m'en vais justement sortir mon stock tu va pouvoir y aller.")
    time.sleep(0)
    print("-Vous partez quand déjà?")
    time.sleep(0)
    print("     -Dimanche vers 11 heures. Dit moi, il fait combien dehors aujourd'hui?\n")
    time.sleep(0)
    
    num_temp_1=choice_num("Température: ") # Commande pour défénire la saison pour le reste de l'histoire
    if(num_temp_1 >= 30):
        saison="+été" 
    elif(num_temp_1 > 15): 
        saison = "été"
    elif(num_temp_1>=-5):
        saison = "automne"
    elif(num_temp_1 > -30): 
        saison = "hiver"
    elif(num_temp_1 <= -30):
        saison="+hiver"


    print(f"Il fait {num_temp_1} avec du soleil dehors. Au plus chaud {num_temp_1+8}.")        # Définir la saison selon la température entrée par l'utilisateur.
    time.sleep(0)
    if(saison=="+été"): 
        print("     -Sérieux?? Cibole, je penses que je me suis trop habillé ce matin.")
    elif(saison=="été"):
        print("     -Parfait comme température, je vais pouvoir manger dehors. Bonne journée.")
    elif(saison=="automne"):
        print("     -Ok, merci, je penses que je vais me mettre une veste.")
    elif(saison=="hiver"):
        print("     -Merci chérie. On se revoit tantôt.")
    elif(saison=="+hiver"):
        print("     -C'est sûr tu me niaise. Ok merci, je vais prendre ma tuque. À tantôt.")
    

    time.sleep(0)
    print("-Bonne journée et à ce soir.")
    time.sleep(0)
    print("Ce matin je dois aller porter ma soeur à son cégep, sa voiture a eu un pépin. Au moins c'est vendredi j'ai pas besoin d'y aller demain.       -Suite")
    input()
    print("Je dois me rendre à la job pour un shift de 8 heures après. Trop long si tu me demandes mais au moins mon buddy Alex va être là.")

    if(saison=="été" or saison=="automne" or saison=="+été"): 
        print("Il fait beau la route va être plaisante je crois. Je vais pouvoir blaster ma musique.     -Suite")
        input()
        print("Fallait je m'ouvre la geule, il y a un accident sur le coin de ma rue, je suis dans un foutu cul de sac.\nOn peut même pas sortir de notre rue.\nJe suis encore content que ma soeur commence ses cours aussi tôt j'ai du buffer ce matin.\nMoins cool pour elle par contre, mais moi je suis sur le point de me faire virer donc je veux pas jouer avec le feu.       -Suite")

        police_1=choice_user2("Aller voir les policiers","Attendre") # Évènement policiers
        if(police_1==1):
            print("J'étais sortie du char pour aller voir c'était quoi le deal. Rendu à la auteur de leur voiture,\nj'ai vu leur char complètement détruit, y'avait une bmw sur le side qui était rentré dans une pole.\nTypique. Chépa trop comment ils ont fait mais c'était pas beau à voir.     -Suite")
            input()
            print("Ils m'ont dit que d'ici une vingtaines ils allait être en route. Au final moi et ma soeur on est rentré chez nous.\nPuis, enfin, 1 heure plus tard, de chez nous on les avait vu parir.")
        elif(police_1==2):
            print("On doit avoir attendu une bonne heure avant que les ambulances puis tout soit arrivé. C'était pénible. Au moins on avait l'AC dans le char.     -Suite")
            input()
    elif(saison=="hiver" or saison=="+hiver"): 
        print("Pas hâte de conduire, on va pas se mentir c'est vraiment laid sur les routes ce matin. \nEncore une chance que c'est supposé de réchauffer cette semaine.      -Suite")
        input()
        print("J'embarquais sur l'autoroute et là... mon truck fait un gros 'CLANK', vraiment pas rassurant.\nPas rien entendu d'anormal après mais j'ai pas trippé on va pas se mentir.. Ma soeur non plus d'ailleurs, le bruit était de son bord.     -Suite")
        input()
    print("Après avoir déposé ma soeur je repartais avant d'avoir reçu un texto d'un numéro inconnu qui me disait de ne pas venir à la job.\nJ'aurais aimé le voir avant de partir, j'ai seulement vu le message quand j'étais arrivé.      -Suite")
    input()

    print("Au final chu juste arrivé et j'ai rien vu de flagrant. Le texto disait rien.")
    time.sleep(0)
    print("     -Yo Nico comment tu vas aujourd'hui?")
    time.sleep(0)
    print("-Bien, et toi?")
    time.sleep(0)
    print("    -Ça va, le réveille était rough ce matin je l'ai poussé hier soir, deux-trois nouvelles chansons qui sont sorties autour de minuit.\nJe te les envoies plus tard.")
    time.sleep(0)
    print("-Ah ouais shit j'ai manqué ça. Cool.")
    time.sleep(0)

    texto_1=choice_user2("Lui parler du texto","Le garder pour soi")
    if(texto_1==1):
        print("- Hey, t'avais-tu reçu un texto te disant de ne pas te pointer à la job ce matin?\n-Il venait d'un numéro inconnu.       -Suite")
        input()
        print("     -Non, the fuck? J'aurais presque aimé, moi je l'aurais écouté si j'étais toi.\n      -8 heures c'est long broo.")
        time.sleep(0)
        print("-Weird, bref live je vois rien d'inabituel donc je vais pas trop y porter attention.")

    elif(texto_1==2):
        print("Prêt pour les 8 prochaines heures?")
        time.sleep(0)
        print("     -8 heures c'est long broo. Encore une chance qu'on est deux sur la même job aujourd'hui.")
    time.sleep(0)
    print("Je serais peut-être pas venu si j'avais reçu le texto avant de rembarquer sur la route.      -Suite")
        






    if(rejouer=="0"): 
        nb_lecture=nb_lecture+1
        while(rejouer != "1" and rejouer != "2"):
           
            print(f"\nCela vous fait {nb_lecture} lectures.")
            print("Souhaitez vous recommencer l'histoire?")
            print("|    1 = Oui")
            rejouer=(input("|   2 = Non : "))
        if(rejouer=="2"):
            print(rejouer)
            JOUER=False
        rejouer=str("0")
print("Fin")
time.sleep(0)
