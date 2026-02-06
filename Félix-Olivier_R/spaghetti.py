import time, sys
JOUER=True
rejouer="0"
while(JOUER==True): 
    # Code emprunté de monsieur copilot. Effet typewritter (une lettre à la fois)
    def texte_delai(text, delay=0.05, newline=True):
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()   
            time.sleep(delay)
        if newline:
            sys.stdout.write("\n")
            sys.stdout.flush()
    print("La création, la musique, l'art en général, j'ai jamais réussi à trouver une bonne raison d'abandonner tout et de m'y mettre pour de bon. J'ai 21 ans, en ce moment je travail dans le provigo du coin. Chu, comme, zéro populaire, par contre c'est plus par choix que pas résultat de mes actions ou whatever. Je dirais pas que j'ai beaucoup d'argent, mais j'ai quand même un ford raptor 2017.   -Suite") 
    print()
    attendre=input("  **Veuillez appuyer sur ENTER pour continuer. Lisez le README s'il y a confusion.**  ")
    print("Très bon prix d'ailleurs. Ça me rappele l'interaction que j'ai eu avec le vendeur, c'était quand même vraiment mongole. Après avoir démontré mon intérêt sur l'annonce facebook le gars m'avais donné un coup de fil.     -Suite")
    attendre=input() # Permet d'attendre l'input de l'utilisateur avant de continuer

    # Premier évènement: coup de téléphone
    phone_1="0"
    print("     -Bonjour, est-ce que je parle à Nicolas?")
    while(phone_1 != "1" and phone_1 != "2") :
        print()
        print("** Insérez le NOMBRE de l'option choisie, regarder le README si vous êtes confus.**")
        print("     Option 1 = Oui")
        phone_1=input(str("     Option 2 = Non      Nombre: "))  # Options réponse Évènement 1
    char_1=("0")
    if(phone_1=="1"): # phone_1 OUI
        print("-Oui c'est bien moi.")
        time.sleep(0)
        print("-Je m'adresse à qui?")
        time.sleep(0)
        print("     -C'est George, voyons criss tu sonne bin jeune, c'est tu vraiment toi sur facebook?")
        time.sleep(0)
        texte_delai("ouch" , delay=(0))
        while(char_1 != "1" and char_1 != "2" and char_1 != "3"):  # Options réponse. Évènement 2
            print()
            print("     1 = -Ouais on me le dit souvent")
            print("     2 = Racrocher")
            char_1=input(str("     3 = -Es-tu sérieux pour le truck ou non?    : "))
            if(char_1=="1"): #char_1 option 1
                print("-Oui c'est moi, on me le dit souvent, toé t'as quel age? Tu sonnes crissement vieux.")
                time.sleep(0)
                print("J'ai pas pu me retenir sa voix criait la vieillesse.")
                time.sleep(0)
                print("Au final il m'avait offert de passer chez eux la même journée.")
                time.sleep(0)
            elif(char_1=="2"): #char_1 option 2
                print("Bon, j'ai racroché.")
                time.sleep(0)
            elif(char_1=="3"): #char_1 option 3
                print("Scuse moi, mais es-tu sérieux avec le truck ou tu va perdre mon temps?")
                time.sleep(0)
                print("Excuse moi, tu souhaites le voir? Viens à l'adresse indiqué sur l'annonce ajourd'hui à partir de 3h si tu peux.      -Suite")
                attendre=input()
                print("C'est bon, on va se voir.")
                time.sleep(0)
    else: # phone_1 NON
        if(phone_1=="2"):
            print("-Non scuse moi lgros, tu dois avoir le mauvais numéro.") 
            time.sleep(0)
            print("J'étais sûr c'était un foutu spam, j'ai pas réfléchi..   -Suite")
            attendre=input()
            print("     -Ah je suis désolé. Tu n'es pas la personne qui m'avait envoyé un message pour le ford ce matin?")
            time.sleep(0)
            texte_delai("Ah, shit." , delay=(0)) # type writter
            time.sleep(0)
            print("Je ne pouvais pas retourner la situation, je sais pas si j'avais simplement pas allumé, mais j'ai choké. J'avais 18 ans je sais pas trop quoi te dire. Compte-tenu qu'il savait pas j'étais qui je ne me suis pas retenue..       -Suite")
            attendre=input()
            print("-Non désolé. Je vous souhaite une bonne journée.")
            time.sleep(0)
            print("     -Ah pardon, bonne journée à vous aussi.")
            time.sleep(0)

    print("Je dois l'admettre j'étais un peu impuslif..")
    time.sleep(0)
    print("Un ti peu...")
    time.sleep(0)
    print("Au moins j'ai le char.       -Suite")
    attendre=input()
    if(char_1=="2" or phone_1=="2"):
        print("Au final chu juste aller voir le gars sans m'annoncer.")
        time.sleep(0)
    print("     -Chérie? T'avais tu fais la lessive ou pas encore? Moi et ton père on a du linge à laver pour la semaine prochaine.")
    time.sleep(0)
    print("Ouaip, j'habite encore chez mes parents, tu serais fou de croire que je peux me permettre un chez moi dans cette économie.    -Suite")
    attendre=input()
    print("Ils s'en vont en vacances la semaine prochaine, j'ai quand même hâte ça va me donner tellement de temps pour moi. ")
    time.sleep(0)
    print("-Ouais je m'en vais justement sortir mon stock tu va pouvoir y aller.")
    time.sleep(0)
    print("     -Merci. Il fait combien dehors aujourd'hui?")
    time.sleep(0)
    print("")

    while True: 
        choix_temp_1=input("Température: ") # Permet à la commande de looper jusqu'à ce que l'utilisateur ait rentré un INT aka nombre
        print("")
        try:
            num_temp_1=int(choix_temp_1)
            break
        except ValueError:
            print("Veuillez entrer un nombre.")
       
    if(num_temp_1 >= 20 and num_temp_1 < 40): # Commande pour défénire la saison pour le reste de l'histoire
        saison = "été"
    elif(num_temp_1 < 20 and num_temp_1 >= -5):
        saison = "automne"
    elif(num_temp_1 < -5 and num_temp_1 >-35): 
        saison = "hiver"
    elif(num_temp_1 >= 40):
        saison="+été"
    elif(num_temp_1 <= -35):
        saison="+hiver"
    pluschaud=num_temp_1+8

    print(f"Il fait {num_temp_1} avec du soleil dehors. Au plus chaud {pluschaud}.")
    if(saison=="+hiver"):
        print("     -C'est sûr tu me niaise. Ok merci, je vais prendre ma tuque. À tantôt.")
    elif(saison=="hiver"):
        print("     -Merci chérie. On se revoit tantôt.")
    elif(saison=="automne"):
        print("     -Ok, merci, je penses que je vais me mettre une veste.")
    elif(saison=="été"):
        print("     -Parfait comme température, je vais pouvoir manger dehors. Bonne journée.")
    elif(saison=="+été"): 
        print("     -Sérieux?? Cibole, je penses que je me suis trop habillé ce matin.")

    time.sleep(0)
    print("-Bonne journée à ce soir.")
    time.sleep(0)
    print("Ce matin je dois aller porter ma soeur à son cégep, sa voiture a eu un pépin. Au moins c'est vendredi pas besoin d'y aller demain.       -Suite")
    attendre=input()
    if(rejouer=="0" or rejouer=="1"): 
        while(rejouer != "1" and rejouer != "2"):
            print()
            print("Souhaitez vous recommencer l'histoire?")
            print("1: Oui")
            rejouer=input(str("2: Non : "))
        if(rejouer=="2"):
            print(rejouer)
            JOUER=False
        rejouer="0"
    
