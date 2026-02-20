"""
Félx-Olivier Rioux
Projet 1: Histoire intéractive

"""
import time, sys
JOUER=True

court=0.5 # Variable de constantes pour les time.sleep, facilite le changement de tout les délais
long=0.5  # Variable de constantes pour les time.sleep, facilite le changement de tout les délais

choix_temps=2
nb_lecture=0   # Permet de garder le nombre de lectures plus tard
char_1=0 

def choice_user2(choix1,choix2):
    """
Permet de formatter les questions toujours de la même façon. Celle-ci à 2 options
    result = 0 Pour permettre de looper dans un while lorsque l'input n'égal pas une des trois options
    Print option 1 entrée dans le re-call de la fonction
    Print option 2 entrée dans le re-call de la fonction
    While qui loop jusqu'à ce que (1) ou (2) ou (3) soit rentré
    Return le choix du l'utilisateur 
    """
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

def choice_user3(choix1,choix2,choix3): 
    """
Permet de formatter les questions toujours de la même façon. Celle-ci à 3 options
    result = 0 Pour permettre de looper dans un while lorsque l'input n'égal pas une des trois options
    Print option 1 entrée dans le re-call de la fonction
    Print option 2 entrée dans le re-call de la fonction
    Print option 3 entrée dans le re-call de la fonction
    While qui loop jusqu'à ce que (1) ou (2) ou (3) soit rentré
    Return le choix du l'utilisateur 
    """
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

def choice_num(question): 
    """
    While true = boucle sans fin.
        Print la question entrée dans le re-call de la fonction et stock la réponse dans "number"
        Le programme essaie de convertir la réponse de "number" vers "result" en un INTEGER
            Si ça break pas on continuer avec le return
        Si ça chie.
            Demande de re-rentrer un nombre et recommence d'en haut dans le while.
    Return le résultat en INTEGER
    """
    while True: 
        number=input(f"{question} : ") 
        try:
            result=int(number)
            break
        except ValueError:
            print("\nVeuillez entrer un nombre.")
    return result

def texte_delai(text, delay=0.05, newline=True): 
    """
    Code emprunté de monsieur copilot. Permet d'écrire une lettre à la fois
    Je sais pas comment il fonctionne.
    """
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()   
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

# Permet de looper le jeu selon l'input de l'utilisateur après sa lecture
while(JOUER==True): 
    
    if(nb_lecture>0):
        input("\nContinuer?   -Suite") # Permet d'afficher un message différent selon le nombre de fois que l'utilisateur a joué
    else:
        input("\nCommencer?   -Suite")

    print("\nLa création, la musique, l'art en général, j'ai jamais réussi à trouver une bonne raison, \nou je dirais que j'ai pas encore trouvé l'occasion d'abandonner tout et de m'y mettre pour de bon.\nC'est toujours juste une passion que j'ai sur le côté.\nJ'ai 21 ans, en ce moment je travail dans le provigo du coin. Chu, comme, zéro populaire,\npar contre c'est plus par choix que pas résultat de mes actions ou whatever.\nJe dirais pas que j'ai beaucoup d'argent, mais j'ai quand même un ford raptor 2017.   -Suite") 
    input()
    print("Très bon prix d'ailleurs. Ça me rappele l'interaction que j'ai eu avec le vendeur, c'était quand même vraiment mongole.\nAprès avoir démontré mon intérêt sur l'annonce facebook le gars m'avais donné un coup de fil.     -Suite")
    input() # Permet d'attendre l'input de l'utilisateur avant de continuer

    print("     -Bonjour, est-ce que je parle à Nicolas?\n")
    time.sleep(court)
    print("   **Regardez le README s'il y a confusion.** ")
    phone_1=choice_user2("-Oui","-Non")  # Évènement 1 - phone_1 appel pour la voiture

    if(phone_1==1): # phone_1 OUI
        print("\n-Oui c'est moi.")
        time.sleep(court)
        print("-Je m'adresse à qui?")
        time.sleep(court)
        print("     -C'est George, voyons criss tu sonne bin jeune, c'est tu vraiment toi sur facebook?")
        time.sleep(court)
        texte_delai("ouch" , delay=(0.4))

        char_1=choice_user3("-Oui c'est bien moi","Racrocher","-Es-tu sérieux pour le truck ou non?") # char_1 réponse - Évènement 2

        if(char_1==1): #char_1 option 1
            print("\n-Oui oui, c'est moi, on me le dit souvent, toé t'as quel age? Tu sonnes crissement vieux.")
            time.sleep(court)
            print("J'ai pas pu me retenir sa voix criait la vieillesse.")
            time.sleep(court)
            print("Au final il m'avait offert de passer chez eux la même journée.")
            time.sleep(court)

        elif(char_1==2): #char_1 option 2
            print("\nBon.. J'ai racroché.")
            time.sleep(court)

        elif(char_1==3): #char_1 option 3
            print("\n-Scuse moi, mais es-tu sérieux pour le truck ou tu va perdre mon temps?")
            time.sleep(long)
            print("     -Pardonne moi, tu souhaites le voir? Viens à l'adresse indiqué sur l'annonce ajourd'hui à partir de 3h si tu peux.      -Suite")
            input()
            print("-C'est bon, on va se voir.")  
            time.sleep(court)

    elif(phone_1==2): # phone_1 NON
        print("-Non scuse moi lgros, tu dois avoir le mauvais numéro.") 
        time.sleep(court)
        print("J'étais sûr c'était un foutu spam, j'ai pas réfléchi..   -Suite")
        input()
        print("     -Ah je suis désolé. C'est pas toi qui m'avait envoyé un message pour le ford ce matin?")
        time.sleep(long)
        texte_delai("Ah, shit.",delay=(0.2)) # Effet type writter
        time.sleep(court)
        print("Je ne pouvais pas retourner la situation, je sais pas si j'avais simplement pas allumé, mais j'ai choké.\nJ'avais 18 ans je sais pas trop quoi te dire. Compte-tenu qu'il savait pas j'étais qui je ne me suis pas retenue..       -Suite")
        input()
        print("-Non désolé. Je te souhaite une bonne journée.")
        time.sleep(court)
        print("     -Ah pardon, bonne journée à toi aussi.")
        time.sleep(court)

    print("Je dois l'admettre j'étais un peu impuslif..\nAu moins j'ai le char.       -Suite")
    input()

    if(char_1==2 or phone_1==2): 
        print("Au final chu juste aller voir le gars sans m'annoncer. Quand même content que tout ait fonctionné.")
        time.sleep(long)

    print("     -Chérie? T'avais tu fais la lessive ou pas encore? Moi et ton père on a du linge à laver pour la semaine prochaine.")
    time.sleep(long)
    print("Ouaip, j'habite encore chez mes parents, tu serais fou de croire que je peux me permettre un chez moi dans cette économie.    -Suite")
    input()

    print("Ils s'en vont en vacances la semaine prochaine, j'ai quand même hâte ça va me donner tellement de temps pour moi. ")
    time.sleep(long)
    print("-Ouais je m'en vais justement sortir mon stock tu va pouvoir y aller.")
    time.sleep(court)
    print("-Vous partez quand déjà?")
    time.sleep(court)
    print("     -Dimanche vers 11 heures. Dis moi, il fait combien dehors aujourd'hui?\n")
    time.sleep(court)
    
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

    print(f"Il fait {num_temp_1} avec du soleil dehors. Au plus chaud {num_temp_1+5}.")        # Définir la saison selon la température entrée par l'utilisateur.
    time.sleep(court)
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
    time.sleep(court)

    print("-Bonne journée et à ce soir.")
    time.sleep(court)
    print("Ce matin je dois aller porter ma soeur à son cégep, sa voiture a eu un pépin. Au moins c'est vendredi j'ai pas besoin d'y aller demain.       -Suite")
    input()
    print("Je dois me rendre à la job pour un shift de 8 heures après. Trop long si tu me demandes mais au moins mon buddy Alex va être là.")
    time.sleep(long)

    if(saison=="été" or saison=="automne" or saison=="+été"): 
        print("Il fait beau la route va être plaisante je crois. Je vais pouvoir blaster ma musique.     -Suite")
        input()
        print("Fallait je m'ouvre la geule, il y a un accident sur le coin de ma rue, je suis dans un foutu cul de sac.\nOn peut même pas sortir de notre rue.\nJe suis encore content que ma soeur commence ses cours aussi tôt j'ai du temps ce matin.        -Suite")
        input()
        print("Moins cool pour elle par contre, mais moi je suis sur le point de me faire virer donc je veux pas jouer avec le feu.")
        time.sleep(long)
        police_1=choice_user2("Aller voir les policiers","Attendre") # Évènement policiers
        if(police_1==1):
            print("J'étais sortie du char pour aller voir c'était quoi le problème. Rendu à la auteur de leur voiture,\nje l'ai vu, complètement détruite, y'avait une BMW sur le côté qui était rentré dans un poteau électrique.\nTypique. Chépa trop comment ils ont fait mais c'était pas beau à voir.     -Suite")
            input()
            print("Ils m'ont dit que d'ici une vingtaines ils allait être en route. Au final moi et ma soeur on est rentré chez nous.\nPuis, enfin, 1 heure plus tard, de chez nous on les avait vu parir.")
            time.sleep(long)
        elif(police_1==2):
            print("On doit avoir attendu un bon 45 minutes avant que les ambulances puis tout soit arrivé. C'était pénible. Au moins on avait la musique dans le char.     -Suite")
            input()
    elif(saison=="hiver" or saison=="+hiver"): 
        print("Pas hâte de conduire, on va pas se mentir c'est vraiment laid sur les routes ce matin. \nEncore une chance que c'est supposé de réchauffer le semaine prochaine.      -Suite")
        input()
        print("J'embarquais sur l'autoroute et là... mon truck fait un gros 'CLANK', vraiment pas rassurant.\nPas rien entendu d'anormal après mais j'ai pas trippé on va pas se mentir.. Ma soeur non plus d'ailleurs, le bruit était de son bord.     -Suite")
        input()
    print("Après l'avoir déposé je repartais avant d'avoir reçu un texto d'un numéro inconnu qui me disait de ne pas venir à la job.\nJ'aurais aimé le voir avant de partir, j'ai seulement vu le message quand j'étais arrivé.      -Suite")
    input()

    print("Au final j'ai rien vu de flagrant. Le texto disait rien.")
    time.sleep(court)
    print("     -Yo Nico comment tu vas aujourd'hui?")
    time.sleep(court)
    print("-Bien, et toi?")
    time.sleep(court)
    print("    -Ça va, le réveille était rough ce matin je l'ai poussé hier soir, deux ou trois nouvelles chansons qui sont sorties autour de minuit.\n    -Je te les envoies plus tard.")
    time.sleep(long)
    print("-Ah ouais shit j'ai manqué ça. Cool.")
    time.sleep(court)

    texto_1=choice_user2("Lui parler du texto","Le garder pour soi")
    if(texto_1==1):
        print("-Hey, t'avais-tu reçu un texto te disant de ne pas te pointer à la job ce matin?\n-Il venait d'un numéro inconnu.       -Suite")
        input()
        print("     -Non, the fuck? J'aurais presque aimé, moi je l'aurais écouté si j'étais toi.\n     -8 heures c'est long broo.")
        time.sleep(long)
        print("-Weird, bref, live je vois rien d'inabituel donc je vais pas trop y porter attention.     -Suite")
        input()
    elif(texto_1==2):
        print("-Prêt pour les 8 prochaines heures?")
        time.sleep(court)
        print("     -8 heures c'est long broo. Encore une chance qu'on est deux sur la même job aujourd'hui. Hâte à ce soir.")
        time.sleep(court)
    print("Je serais peut-être pas venu si j'avais reçu le texto avant de rembarquer sur la route.      -Suite")
    input()
    if(saison=="été" or saison=="automne" or saison=="+été"):
        print("-Ce matin sur ma rue il y avait un accident, une BMW avec un char de police, une Charger. On est resté pogné pendant une heures sans pouvoir passer.     -Suite")
        input()
        print("     -Ah ouin? Damn ouais c'est vraiment fort ça. Un vendredi en plus, leur journé est ruiné.")
        time.sleep(long)

    print("     -Parlant de, ce soir, t'avais reçu une invitation pour la party chez Émile ou non? Tu devrais venir, je sais que Chloé sera pas là.       -Suite")
    input()
    party_1=choice_user3("-Non j'ai rien eu","Mentir","Demander des détails sur le party")
    if(party_1==1):
        print("-Non j'ai rien reçu.")
        time.sleep(court)
        print("Si Chloé est pas là je suis peut-être preneur. C'est mon ex, il y pas plus abusive qu'elle.")
        time.sleep(long)
        print("-Tu m'enverras l'adresse, je suis pas encore allé chez Émile.        -Suite")
        input()
    elif(party_1==2):
        print("-Ouais, pas vraiment d'intérêt. Par contre si tu me dis que Chloé ne sera pas là je vais y penser.\nQuitte à arriver plus tard dans la soirée. Reste à voire si je dort là ou non si jamais.")
    else:
        print("-Dis moi plus.")
    print("     -C'est vers neuf heure. Il y aura le monde typique, venant du cégep surtout. Maxence et Yousef vont y être.")
    time.sleep(long)
    print("-Je vais voir. Merci     -Suite")
    input()
    print("Rendu dans le provigo, on a pu décider où on voulait travailler. On a choisit le comptoir à pain.\nToujours le plus calme, c'est dans le fond, pas personne qui passe, si jamais, ils savent exactement ce qu'ils veulent.     -Suite")
    input() 
    
    print("     -J'ai commencé à écouter à du nouveau stock. Tu connais Aswell?")
    time.sleep(court)
    print("-Ça me dit de quoi. Il est québécois right?")
    time.sleep(court)
    print("     -Ouaip, lui, il a droppé une nouvelle chanson justement hier soir. Vraiment bonne. Bref, je l'ai croisé récemment.")
    time.sleep(long)
    print("Si je le connais??? Je capotte dessus depuis des mois. Peux pas croire qu'il habite dans le coin.")
    time.sleep(long)
    print("-Ah ouin? Cool, vers où? Tu lui avait parlé?")
    print("     -Dernière fois, oui, je l'ai croisé deux fois. Les deux fois c'était au Tim au coin de la rue en bas.")
    time.sleep(long)
    print("Noté, j'ai mon voyage. Très clairement que je vais commencer à y aller plus souvent. J'aime pas le café remarque. \nJe vais me trouver une raison.   -Suite")
    input()
    print("Ah fuck pas monsieur Robert.")
    time.sleep(court)
    print("     -Salut mon cher, je vais te prendre 7 baguette s'il te plait.")
    print("C'est mon prof de philo, c'était. Il me donnait les pires notes à cause que ma mère c'est son ex.\nCriss que j'aurais dû le snitch. J'ai jamais passé ma philo j'ai droppé le cours.\nJe voulais vraiment pas le voir.   -Suite")
    input()

    robert=choice_user2("Lui donner une mauvaise soirée","Le charger double")
    if(robert==1):
        print("-Avec plaisir.\nJ'ai pris les baguettes de vla deux jours. C'était ma job de m'en départir, j'ai oublié deux fois.\n C'est juste parfait.        -Suite") 
    elif(robert==2):
        print("-Ça s'en vient.\nLe total devrait être de 24.50$ avant taxe, il va pas le voir venir mais il va payer pour les 4 prochaines aussi.")
        time.sleep(long)       
        print("-Cela vous fera 41.50$. Voilà la facture vous pourrez la scanner rendu à la caisse.\nSur la facture ça ne mentionne pas les baguettes d'extra, je peux ajouter le montant que je veux.    -Suite")
        input()
        print("     -41? C'est pas beaucoup?")
        time.sleep(court)
        print("-Ouais, je sais, c'est rendu cher. J'ai comme pas le contrôle sur les prix. Bonne journée.")
        time.sleep(long)
    print("     -Merci, bonne journée.")
    time.sleep(court)
    print("Là chu fier par contre. Ça fait au moins 10 fois que je le vois je me devait de faire quelque chose.")
    time.sleep(long)
    print("-Yo Alex. Tu te rapelle de Robert?")
    time.sleep(court)
    print("     -Lui qui vient de repartir?")
    time.sleep(court)
    print("-Ouaip. Faut je te montre de quoi.")
    time.sleep(court)
    if(robert==1):
        print("-Check là.\nJe lui pointe la pile des baguettes d'avant hier. Il en manque 7.     -Suite")
        input()
        print("     -Osti je peux pas croire. Pas pire, ton secret est en sécurité. Félicitation man.     -Suite")
        input()
    elif(robert==2):
        print("-Check la facture la plus récent dans le système.")    
        time.sleep(court)   
        print("     -Hahaha je peux pas croire que t'as fait passé ça.      -Suite") 
        input()
    print("-Merci haha\nReste plus qu'à voire s'il va revenir se plaindre ou non.\nHonnêtement ça me donnerait une bonne raison de me trouver une autre job.")
    time.sleep(long)



    nb_lecture=nb_lecture+1
    print(f"\n\nSouhaitez vous recommencer l'histoire? Cela vous fait {nb_lecture} lectures.")
    rejouer=choice_user2("Oui","Non")
    if(rejouer==2):
        JOUER=False
    elif(rejouer==1):
        #Si l'utilisateur a jouer au minimum 3 fois, un prompt demande s'ils veulent retirer les "time.sleep"
        if(choix_temps==2 and nb_lecture>=3):
            print("\n\n**Souhaitez vous retirer les temps d'attente? Vous n'aurez plus besoin d'attendre après les lignes de texte.**")
            choix_temps=choice_user2("Oui","Non")
            if(choix_temps==1):
                court=0
                long=0
print("Fin")
time.sleep(2.5)
