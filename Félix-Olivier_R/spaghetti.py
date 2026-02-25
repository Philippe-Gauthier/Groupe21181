"""
Projet 1: Histoire intéractive
Félx-Olivier Rioux
"""
import sys
from time import sleep
JOUER=True

court=0 # Variable de constantes pour les time.sleep, facilite le changement de tout les délais
long=0  # Variable de constantes pour les time.sleep, facilite le changement de tout les délais

choix_temps=2
nb_lecture=0   # Permet de garder le nombre de lectures plus tard 
char_1=0 

def choice_user2(choix1,choix2):
    """
    Entrées: Choix de réponse pour l'utilisateur.
    Sortie: La réponse de l'utilisateur en INT.
    But: Optimizer les choix de réponose et limiter les risques d'erreurs.
    """
    result=0
    print(f"\n"+"_"*40)
    print(f"|     1 = {choix1}")
    print(f"|     2 = {choix2}")
    while(result!=1 and result!=2):
        decision=input("       Choix: ")
        while True:
            try:
                result=int(decision)
                break
            except ValueError:
                decision=input("Veuillez entrer un nombre: ")
    return result

def choice_user3(choix1,choix2,choix3): 
    """
    Entrées: Choix de réponse pour l'utilisateur.
    Sortie: La réponse de l'utilisateur en INT.
    But: Optimizer les choix de réponose et limiter les risques d'erreurs.
    """
    result=0
    print(f"\n"+"_"*40)
    print(f"|     1 = {choix1}")
    print(f"|     2 = {choix2}")
    print(f"|     3 = {choix3}")
    while(result!=1 and result!=2 and result!=3):
        decision=input("       Choix: ")
        while True:
            try: 
                result=int(decision)
                break
            except ValueError:
                decision=input("\nVeuillez entrer un nombre: ")
    return result

def choice_num(question): 
    """
    Entrée: La question posé à l'utilisateur.
    Sortie: Un numéro INT, entrée par l'utilisateur.
    But: S'assurer que l'utilisateur rentre un nombre pour pouvoir l'affecter avec des maths.
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
    Je sais pas comment il fonctionne pour être honnête.
    Entrée: Le temps de délai.
    Sortie: Un delai d'écriture sur le print.
    But: Ajouter un delai entre les littres à l'intérieur d'un print.
    """
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()   
        sleep(delay)
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
    input() # Attendre l'input de l'utilisateur avant de continuer. Les mettres sur une autre ligne permet de donner un line break après chaque, donnant plus d'air au texte.
    # pas ce line break. celui là c'est pour le programmeur et ses yeux seulement.
    print("Très bon prix d'ailleurs. Ça me rappele l'interaction que j'ai eu avec le vendeur, c'était quand même vraiment mongole.\nAprès avoir démontré mon intérêt sur l'annonce facebook le gars m'avais donné un coup de fil.     -Suite")
    input() 

    print("     -Bonjour, est-ce que je parle à Nicolas?\n")
    sleep(court)
    print("   **Regardez le README s'il y a confusion.** ")
    # Évènement 1 - phone_1 appel pour la voiture
    phone_1=choice_user2("-Oui","-Non")   # Réponse téléphone + 2

    if(phone_1==1): # phone_1 OUI 
        print("\n-Oui c'est moi.")
        sleep(court)
        print("-Je m'adresse à qui?")
        sleep(court)
        print("     -C'est Bruno, voyons criss tu sonne bin jeune, c'est tu vraiment toi sur facebook?")
        sleep(court)
        texte_delai("ouch" , delay=(court*0.2))

        char_1=choice_user3("-Oui c'est bien moi","Racrocher","-Es-tu sérieux pour le truck ou non?") # char_1 réponse téléphone + 3

        if(char_1==1): #char_1 option 1 
            print("\n-Oui oui, c'est moi, on me le dit souvent, toé t'as quel age? Tu sonnes crissement vieux.")
            sleep(court)
            print("J'ai pas pu me retenir sa voix criait la vieillesse.")
            sleep(court)
            print("Au final il m'avait offert de passer chez eux la même journée.")
            sleep(court)

        elif(char_1==2): #char_1 option 2 
            print("\nBon.. J'ai racroché.")
            sleep(court)

        elif(char_1==3): #char_1 option 3 
            print("\n-Scuse moi, mais es-tu sérieux pour le truck ou tu va perdre mon temps?")
            sleep(long)
            print("     -Pardonne moi, tu souhaites le voir? Viens à l'adresse indiqué sur l'annonce ajourd'hui à partir de 3h si tu peux.      -Suite")
            input()

            print("-C'est bon, on va se voir.")  
            sleep(court)

    elif(phone_1==2): # phone_1 NON 
        print("-Non scuse moi lgros, tu dois avoir le mauvais numéro.") 
        sleep(court)
        print("J'étais sûr c'était un foutu spam, j'ai pas réfléchi..   -Suite")
        input()

        print("     -Ah je suis désolé. C'est pas toi qui m'avait envoyé un message pour le ford ce matin?")
        sleep(long)
        texte_delai("Ah, shit.",delay=(court*0.1)) # Effet type writter
        sleep(court)
        print("Je ne pouvais pas retourner la situation, je sais pas si j'avais simplement pas allumé, mais j'ai choké.\nJ'avais 18 ans je sais pas trop quoi te dire. Compte-tenu qu'il savait pas j'étais qui je ne me suis pas retenue..       -Suite")
        input()

        print("-Non désolé. Je te souhaite une bonne journée.")
        sleep(court)
        print("     -Ah pardon, bonne journée à toi aussi.")
        sleep(court)

    print("Je dois l'admettre j'étais un peu impuslif..\nAu moins j'ai le char.       -Suite")
    input()

    if(char_1==2 or phone_1==2): # Si l'intéraction au téléphone s'est terminé sans conclusion else: continuer
        print("Au final chu juste aller voir le gars sans m'annoncer. Quand même content que tout ait fonctionné.")
        sleep(long)

    print("     -Chérie? T'avais tu fais la lessive ou pas encore? Moi et ton père on a du linge à laver pour la semaine prochaine.")
    sleep(long)
    print("Ouaip, j'habite encore chez mes parents, tu serais fou de croire que je peux me permettre un chez moi dans cette économie.    -Suite")
    input()

    print("Ils s'en vont en vacances la semaine prochaine, j'ai quand même hâte ça va me donner tellement de temps pour moi. ")
    sleep(long)
    print("-Ouais je m'en vais justement sortir mon stock tu va pouvoir y aller.")
    sleep(court)
    print("-Vous partez quand déjà?")
    sleep(court)
    print("     -Samedi vers 3 heures de l'aprem. Dis moi, il fait combien dehors aujourd'hui?\n")
    sleep(court)
    
    num_temp_1=choice_num("Température: ") # Commande pour défénire la saison pour le reste de l'histoire + 2
    if(num_temp_1 >= 33):
        saison="+été" 
    elif(num_temp_1 > 15): 
        saison = "été"
    elif(num_temp_1>=0):
        saison = "automne"
    elif(num_temp_1 > -30): 
        saison = "hiver"
    elif(num_temp_1 <= -30):
        saison="+hiver"

    print(f"Il fait {num_temp_1} avec du soleil dehors. Au plus chaud {num_temp_1+7}.")        # Définir la saison selon la température entrée par l'utilisateur.
    sleep(court)
    if(saison=="+été"): 
        print("     -Sérieux?? Cibole, je penses que je me suis trop habillé ce matin.")
        saison="été"
    elif(saison=="été"):
        print("     -Parfait comme température, je vais pouvoir manger dehors. Bonne journée.")
    elif(saison=="automne"):
        print("     -Ok, merci, je penses que je vais me mettre une veste.")
        saison="été"
    elif(saison=="hiver"):
        print("     -Merci chérie. On se revoit tantôt.")
    elif(saison=="+hiver"):
        print("     -C'est sûr tu me niaise. Ok merci, je vais prendre ma tuque. À tantôt.")
        saison="hiver"
    sleep(court)

    print("-Bonne journée et à ce soir.")
    sleep(court)
    print("Ce matin je dois aller porter ma soeur à son cégep, sa voiture a eu un pépin. Au moins c'est vendredi j'ai pas besoin d'y aller demain.       -Suite")
    input()

    print("Je dois me rendre à la job pour un shift de 8 heures après. Trop long si tu me demandes mais au moins mon buddy Alex va être là.")
    sleep(long)

    if(saison=="été"): 
        print("Il fait beau la route va être plaisante je crois. Je vais pouvoir blaster ma musique.     -Suite")
        input()

        print("Fallait je m'ouvre la geule, il y a un accident sur le coin de ma rue, je suis dans un foutu cul de sac.\nOn peut même pas sortir de notre rue.\nJe suis encore content que ma soeur commence ses cours aussi tôt j'ai du temps ce matin.        -Suite")
        input()

        print("Moins cool pour elle par contre, mais moi je suis sur le point de me faire virer donc je veux pas jouer avec le feu. Il y a des policiers.")
        sleep(long)
        police_1=choice_user2("Aller voir les policiers","Attendre") # Évènement policiers + 2
        if(police_1==1): # Évènement policiers aller les voir 
            print("J'étais sortie du char pour aller voir c'était quoi le problème. Rendu à la hauteur de leur voiture,\nje l'ai vu, complètement détruite, y'avait une BMW sur le côté qui était rentré dans un poteau électrique.\nTypique. Chépa trop comment ils ont fait mais c'était pas beau à voir.     -Suite")
            input()

            print("Ils m'ont dit que d'ici une vingtaines ils allait être en route. Au final moi et ma soeur on est rentré chez nous.\nPuis, enfin, 1 heure plus tard, de chez nous on les voyait parir.")
            sleep(long)
        elif(police_1==2): # Évènement policiers attendre 
            print("On doit avoir attendu un bon 45 minutes avant que les ambulances puis tout soit arrivé. C'était pénible. Au moins on avait la musique dans le char.     -Suite")
            input()

    elif(saison=="hiver"): 
        print("Pas hâte de conduire, on va pas se mentir c'est vraiment laid sur les routes ce matin. \nEncore une chance que c'est supposé de réchauffer le semaine prochaine.      -Suite")
        input()

        print("J'embarquais sur l'autoroute et là... mon truck fait un gros 'CLANK', vraiment pas rassurant.\nPas rien entendu d'anormal après mais j'ai pas trippé on va pas se mentir.. Ma soeur non plus d'ailleurs, le bruit était de son bord.     -Suite")
        input()

    print("Après l'avoir déposé je repartais avant d'avoir reçu un texto d'un numéro inconnu qui me disait de ne pas venir à la job.\nJ'aurais aimé le voir avant de partir, j'ai seulement vu le message quand j'étais arrivé.      -Suite")
    input()

    print("Au final j'ai rien vu de flagrant. Le texto disait rien.")
    sleep(court)
    print("     -Yo Nico comment tu vas aujourd'hui?")
    sleep(court)
    print("-Bien, et toi?")
    sleep(court)
    print("    -Ça va, le réveille était rough ce matin je l'ai poussé hier soir, deux ou trois nouvelles chansons qui sont sorties autour de minuit.\n    -Je te les envoies plus tard.")
    sleep(long)
    print("-Ah ouais shit j'ai manqué ça. Cool.")
    sleep(court)

    texto_1=choice_user2("Lui parler du texto","Le garder pour soi") # Parler du texto bizarre à alex + 2
    if(texto_1==1): #Texto job alex 
        print("-Hey, t'avais-tu reçu un texto te disant de ne pas te pointer à la job ce matin?\n-Il venait d'un numéro inconnu.       -Suite")
        input()

        print("     -Non, the fuck? J'aurais presque aimé, moi je l'aurais écouté si j'étais toi.\n     -8 heures c'est long broo.")
        sleep(long)
        print("-Weird, bref, live je vois rien d'inabituel donc je vais pas trop y porter attention.     -Suite")
        input()

    elif(texto_1==2): #Texto job alex
        print("-Prêt pour les 8 prochaines heures?")
        sleep(court)
        print("     -8 heures c'est long broo. Encore une chance qu'on est deux sur la même job aujourd'hui. Hâte à ce soir.")
        sleep(court)
    print("Je serais peut-être pas venu si j'avais reçu le texto avant de rembarquer sur la route.      -Suite")
    input()

    if(saison=="été"):
        print("-Ce matin sur ma rue il y avait un accident, une BMW avec un char de police, une Charger. On est resté pogné pendant une heures sans pouvoir passer.     -Suite")
        input()

        print("     -Ah ouin? Damn ouais c'est vraiment fort ça. Un vendredi en plus, leur journé est ruiné.")
        sleep(long)

    print("     -Parlant de, ce soir, t'avais reçu une invitation pour la party chez Émile ou non? Tu devrais venir, je sais que Chloé sera pas là.       -Suite")
    input()

    party_1=choice_user3("-Non j'ai rien eu","Mentir","Demander des détails sur le party") # Demander de l'info sur le party + 3
    if(party_1==1): # Info party 
        print("-Non j'ai rien reçu.")
        sleep(court)
        print("Si Chloé est pas là je suis peut-être preneur. C'est mon ex, il y pas plus abusive qu'elle.")
        sleep(long)
        print("-Tu m'enverras l'adresse, je suis pas encore allé chez Émile.        -Suite")
        input()

    elif(party_1==2): # Info party 
        print("-Ouais, pas vraiment d'intérêt. Par contre si tu me dis que Chloé ne sera pas là je vais y penser.\nQuitte à arriver plus tard dans la soirée. Reste à voire si je dort là ou non si jamais.")
    else: # Info party
        print("-Dis moi plus.")
    print("     -C'est vers neuf heure. Il y aura le monde typique, venant du cégep surtout. Maxence et Yousef vont y être.")
    sleep(long)
    print("-Je vais voir. Merci     -Suite")
    input()

    print("Rendu dans le provigo, on a pu décider où on voulait travailler. On a choisit le comptoir à pain.\nToujours le plus calme, c'est dans le fond, pas personne qui passe, si jamais, ils savent exactement ce qu'ils veulent.     -Suite")
    input() 
    
    print("     -J'ai commencé à écouter à du nouveau stock. Tu connais Aswell?")
    sleep(court)
    print("-Ça me dit de quoi. Il est québécois right?")
    sleep(court)
    print("     -Ouaip, lui, il a droppé une nouvelle chanson justement hier soir. Vraiment bonne. Bref, je l'ai croisé récemment.")
    sleep(long)
    print("Si je le connais??? Je capotte dessus depuis des mois. Peux pas croire qu'il habite dans le coin.")
    sleep(long)
    print("-Ah ouin? Cool, vers où? Tu lui avait parlé?")
    print("     -Dernière fois, oui, je l'ai croisé deux fois. Les deux fois c'était au Tim au coin de la rue en bas.\n     -Les seules fois que j'y suis allé.     -Suite")
    input()

    print("Noté, j'ai mon voyage. Très clairement que je vais commencer à y aller plus souvent. J'aime pas le café remarque. \nJe vais me trouver une raison.   -Suite")
    input()

    print("Ah fuck pas monsieur Robert.")
    sleep(court)
    print("     -Salut mon cher, je vais te prendre 7 baguette s'il te plait.")
    print("C'est mon prof de philo, c'était. Il me donnait les pires notes à cause que ma mère c'est son ex.\nCriss que j'aurais dû le snitch. J'ai jamais passé ma philo j'ai droppé le cours.\nJe voulais vraiment pas le voir.   -Suite")
    input()

    robert=choice_user2("Lui donner une mauvaise soirée","Le charger double") # incident robert + 2
    if(robert==1): # Incident robert 1
        print("-Avec plaisir.\nJ'ai pris les baguettes de vla deux jours. C'était ma job de m'en départir, j'ai oublié deux fois.\n C'est juste parfait.        -Suite") 
    elif(robert==2): # Incident robert 2
        print("-Ça s'en vient.\nLe total devrait être de 24.50$ avant taxe, il va pas le voir venir mais il va payer pour les 4 prochaines aussi.")
        sleep(long)       
        print("-Cela vous fera 41.50$. Voilà la facture vous pourrez la scanner rendu à la caisse.\nSur la facture ça ne mentionne pas les baguettes d'extra, je peux ajouter le montant que je veux.    -Suite")
        input()
        print("     -41? C'est pas beaucoup?")
        sleep(court)
        print("-Ouais, je sais, c'est rendu cher. J'ai comme pas le contrôle sur les prix. Bonne journée.")
        sleep(long)
    print("     -Merci, bonne journée.")
    sleep(court)
    print("Là chu fier par contre. Ça fait au moins 10 fois que je le vois je me devait de faire quelque chose.")
    sleep(long)
    print("-Yo Alex. Tu te rapelle de Robert?")
    sleep(court)
    print("     -Lui qui vient de repartir?")
    sleep(court)
    print("-Ouaip. Faut je te montre de quoi.")
    sleep(court)
    if(robert==1):
        print("-Check là.\nJe lui pointe la pile des baguettes d'avant hier. Il en manque 7.     -Suite")
        input()

        print("     -Osti je peux pas croire. Pas pire, ton secret est en sécurité. Félicitation man. Depuis le temps haha.     -Suite")
        input()

    elif(robert==2):
        print("-Check la facture la plus récent dans le système.")    
        sleep(court)   
        print("     -Hahaha je peux pas croire que t'as fait passé ça.      -Suite") 
        input()

    print("-Merci haha\nReste plus qu'à voire s'il va revenir se plaindre ou non.")
    sleep(court)
    print("Honnêtement ça me donnerait une bonne raison de me trouver une autre job. Ou occupation..")
    sleep(long)
    print("Bon finir mon shift c'est ma priorité en ce moment.\nRendu à la maison je vais pouvoir réfléchir pour ce party. J'ai pas d'intérêt vraiment parce que ça m'apporte pas grand chose.    -Suite")
    input()

    if robert==2:
        print("-Bonjour madame. Le monsieur qui est passé avant vous a payé pour le pain baguette des 4 prochaines personnes qui passaient.")
        sleep(long)
        print("-Souhaitez vous repartir avec une?")
        sleep(court)
        print("     -Oh mais quel ange oserait-il faire une chose telle!")
        print("Un très gentil monsieur. Très très gentil. Tellement gentil. Bon c'est bon.\nÇa c'était ma dose de sarcasme aujourd'hui.    -Suite")
        input()

        print("-Je vous souhaites une bonne journée!")
        sleep(court)
        print("     -Merci à vous!")
        sleep(court)
        print("     -Vous de même!    -Suite")
        input()

    print("-Merci encore Alex, on a été productif aujourd'hui. On se voit soon.")
    sleep(long)
    print("     -Fait plaisir. Oublie pas pour ce soir by the way.")
    sleep(court)
    print("T'inquiète mon cher. Là il me reste plus qu'à retrouver mon bolide.\nJ'ai aucune idée du là ou je me suis parké.     -Suite") 
    input()

    print("Je pourrais peut-être demander au gens au party s'ils ont déjà reçu un texto comme ce que j'ai eu ce matin.")
    sleep(court)
    print("-EILLE TOI SACRÉ-FILS REGARDE OÙ TU CONDUIS.")
    sleep(court)
    print("On a comme oubilé de savoir comment conduire ou comment ça se passe??  -Suite")
    input()

    print("Bref, j'aimerais me rendre au moins à la maison avant de penser de pouvoir aller au party.\nJe penses y aller pour m'enrichir sur ce qui s'est passé ce matin et peut-être faire de nouvelles connexions.    -Suite")
    
    texte_delai("..",delay=(court*0.1))

    print("---CHAPITRE 2---")
    sleep(court)
    print("Je crois que je serais prêt à y aller, il est 8h30.\nJ'avais reçu un message d'Alex.\n    'Tu devrais venir plus tôt que tard si tu planifiais venir. Quelqu'un souhaiterait de voir.'       -Suite")
    input()

    #Le vrai départ des "branches" ils ne retourneront plus dans la principale :) 
    party_aller=choice_user2("Ce faire à manger avant","Demander à Alex s'il va y être tôt") # Prévoir parti bientôt + 2
    if party_aller==1: # Diriger vers party après manger
        print("Je pourrais me faire réchauffer de la pizza avant d'y aller. Je commence à avoir faim. Pas sûr de rester toute la soirée.\nDe toute façon, je vais pas boire.     -Suite")
        input()

        print("La bonne pizza dominos. Je ferais mieux de regarder avec Alex ce qu'il voulait dire.     -Suite")
        print("'Je voulais te demander. Tu voulais dire quoi par quelqu'un qui veut me rencontrer?'")
        sleep(long)
        print("     'Je voulais dire que le fils de Simon, le manager de la gallerie d'art du coin, y sera, ce dit manager a zyeuter ton instagram le gros'")
        sleep(long)
        print("'Ah ouin?? Okay interessant ça. Je fini ma pizza et je m'en viens'       -Suite")
        input()

        print("---QUELQUES MINUTES PLUS TARD---")
        sleep(court)
        print("-Yo Alex, il est où celui dont tu me paprlait?")
        sleep(court)
        print("     -Je suis désolé, George est parti.")
        sleep(court)
        print("Il est just 9h45 pourtant.\n-Est-ce qu'il m'attendait moi spécifiqument?")
        sleep(long)
        print("     -Non, je savais simplement qu'il allait être là. Je les avais vu parler, les deux, quand je travaillais. \n     -Simon avait demandé à son fils s'il te connaissait puisqu'il avait fait un tour sur ton compte.     -Suite")
        input()

        if saison=="été":
            print("Ok donc je viens de perdre mon temps.")
            sleep(court)
            changement_plan=choice_user2("Rester à dormir","Repartir") # Décider de rester ou quitter le party + 2
            if changement_plan==1: # George n'est pas là: rester
                print("-Tu me passerais la bouteille de vodka?")
                sleep(court)
                print("J'ai rien à faire demain. Plutôt qu'à me faire sentir mal pour ce qui vient d'arriver je vais juste réessayer plus tard.")
                print("     -Ouais, tiens. Moi je vais aller dans la piscine avec Max et Yousef, tu viens?      -Suite")
                print("---QUELQUES HEURES PLUS TARD---")
                sleep(court)
                print("Au final je sais pas trop qu'est-ce qui s'est passé hier soir. Il est 6h20 AM. \nLe soleil est levé, je pourrais retourner chez moi je sens plus l'alcool.")
                post_drink=choice_user2("Retourner chez soi","Prendre son temps") # Après la soirée, retourner chez soi ou attendre + 2 
                if post_drink==1:
                    print("---QUELQUES MINUTES PLUS TARD---")
                    sleep(court)
                    print("Content de ne pas m'être fait arrêté. 30 minutes de routes c'est pas négligable. Je vais me coucher directement moi. ")
                    sleep(long)
                    texte_delai("..",delay=(court*0.1))
                    print("-Suite")
                    input()
                    finchap2="recherche"

            elif changement_plan==2: # George n'est pas là: repartir
                print("Après avoir fait un petit tour. J'ai pas trouvé personne.\nOn est au beau milieu de la ville, je vais préférer manger un coup avant de reprendre le volant.      -Suite")
                input()

                print("Tim it is. Passer voir si je vais être chanceux..")
                sleep(court)
                print("---QUELQUES MINUTES PLUS TARD---")
                sleep(court)
                print("Je vais m'installer dans le fond, j'ai mon déjeuner je suis bien canté.")
                sleep(long)
                texte_delai("..",delay=(court*0.1))
                print("-Suite")
                input()
                finchap2="tim"


        else: 
            print("Considérant qu'il fait froid dehors, je veux pas terminer dans mon char.")
            sleep(long)
            print("-Pardonne moi Alex, mais bonne soirée. Je pense que je vais simplement retourner chez nous.   -Suite")
            input()

            print("---QUELQUES HEURES PLUS TARD---")
            sleep(court)
            print("Je viens de me reveiller. Je suis tellement brulé je dois avoir dessiné pendant 4 heures. Je me suis endormi sur mon bureau.     -Suite")
            input()

            print("Je suis vraiment fier parcontre de celui-là. Je pense que si j'arrive à voir Simon en personne je vais l'apporter pour lui montrer.")
            sleep(long)
            texte_delai("..",delay=(court*0.1))
            print("-Suite")
            input()
            finchap2="recherche"


    elif party_aller==2: # Diriger vers party live
        print("Selon sa réponse, il va y être au plus tard à 9h05. J'ai regardé sur la map et la maison d'émile serait à 30 minutes.\nLe timing est parfait.     -Suite")
        input()

        print("Je me sens sur les tracks aujourd'hui. Tout arrive en même temps. Je re-entends le bruit métalique sur mon char.\nCette fois-ci c'est en sortant de mon driveway.    -Suite")
        input()

        print("     -Hey salut Nico. Tu es en avance.")
        sleep(court)
        print("-Ouais toute l'histoire du gérant de la gallerie d'art m'a intrigué.\n-Tu sais où je pourrais trouver son fils?")
        sleep(long)
        print("     -Ouais c'est George là bas. Chandail vert.")
        sleep(court)
        print("Ah fuck pas lui. C'est un de mes 'ex' intimidateur. Il avait vraiment les pires motifs dans le temps.\nC'était au primaire.")
        party_george=choice_user2("Aller parler à George","Trouver un autre moyen de rentrer en contact avec simon") # Parler ou non à George + 2
        if party_george==1: # Parler à George 
            print("-Hey, scuse moi de te déranger George, c'est bel et bien ton père Olivier celui qui est à la tête de la gallerie d'art du coin? ")
            sleep(long)
            print("     -Oui, oui. Il voulait te parler c'est ça?")
            sleep(court)
            print("-Je crois bien que oui. Tu sais comment je pourrais rentrer en contact avec lui?")
            sleep(court)
            texte_delai("....",delay=(court*0.25))
            print("     -Suite")
            input()

            print("-J'ai eu son numéro. Je vais pouvoir l'appeler demain.")
            sleep(court)
            print("     -Parfait ça. Check Yousef vient d'arriver.")
            sleep(court)
            print("         -Yo les gars. Avez-vous vu ce qui s'était passé dans le parking du provigo hier soir?\nAjoutais yousef    -Suite")
            input()

            print("-Ça viendrait expliquer le texto? Vas-y dit.")
            sleep(court)
            print("     -Y'avait des explosions et des feux d'artifices. C'était du monde drogués qui faisiaient de la marde. Qu'est-ce que tu veux dire le texto?")
            sleep(long)
            print("-Ce matin j'avais reçu un texto me disant de ne pas me pointer à la job. Y étant aller après j'ai rien vu de particulier.    -Suite")
            input()
            print("     -Ah ouais okay c'est ineressant. Pourquoi toi spécifiquement?")
            sleep(court)
            print("Bonne question. J'ai pas de réponse.")
            sleep(court)
            print("On est resté ensemble pendant ou bon bout. Les gars étaient trop stoned après un boute être sobre n'était plus vraiment plaisant autour d'eux.\nJ'ai plutôt priorisé le sommeil ainsi qu'appeler Simon.")
            sleep(long)
            texte_delai("..",delay=(court*0.1))
            print("-Suite")
            input()
            finchap2="appel"

            
        elif party_george==2: # Pas parler à George 
            if saison=="été":
                print("-Je vais trouver un autre moyen, je t'explique plus tard.\n-Bon, on va tu dans la piscine? J'ai pas apporté mon maillot pour rien.\nChloé est en effet pas là, je vais pas m'en empêcher.      -Suite")
                input()

                print("     -Avec plaisir.")
                sleep(court)
                print("---PLUS TARD---\nAu final je suis resté jusqu'à 11 heures et demi.")
                sleep(court)
                print("Pas trop pire, la piscine était à température parfaite. \nJe pense que je vais aller dormir et je vais regarder pour envoyer un mail à Simon demain.")
                sleep(long)
                texte_delai("..",delay=(court*0.1))
                print("-Suite")
                input()
                finchap2="mail"

            else:
                print("Tabarnak. Chloé s'est quand même pointé.")
                sleep(court)
                print("-Yo les gars, checkez dans le hall d'entrée.")
                sleep(court)
                print("     -Ah wow. Okay je suis désolé veux-tu on va ailleurs? Moi j'ai bu mais on peut prendre ton truck.")
                fini_party=choice_user2("Quitter","Rester") # Chloé arrive, rester/quitter + 2
                if fini_party==1: # Arrivé chloé - partir 
                    print("Je déteste pas l'idée.\n-Ouais venez on va passer par en arrière. Prenez vos manteau.")
                    sleep(long)
                    print("On doit avoir fait le tour de la ville. J'ai conduit toute le long, on avait de la musique, quand même forte, je l'entends encore. \nSinon on avait deux bozos qui fumaient dans le fond de mon char. La belle vie.   -Suite")
                    input()

                    print("Il y a des sacs de mcdo et des déchets qu'on a pas jeté un peu partout sur mon bed. Dont deux ou trois préservatifs apparement.") 
                    sleep(long)
                    print("Après avoir nettoyé je me suis installer puis j'ai composé une petite heure avant d'aller me coucher. ")
                    sleep(long)
                    texte_delai("..",delay=(court*0.1))
                    print("-Suite")
                    input()
                    finchap2="appel"

                elif fini_party==2: # Arrivé chloé - rester 
                    print("-Non écoute c'est good. Je veux rester voir qu'est-ce qu'elle fait ici.\nÇa risque d'être divertissant. Elle a une mauvaise réputation.      -Suite")
                    input()

                    print("Je pense qu'au moins la moitié des gars ici savent quelle genre de personne elle est.\nJ'étais le premier à voir son côté shady.      -Suite")
                    input()

                    chloe=choice_user2("Mettre de quoi dans son vers","Aller la niaiser") # Naiser chloé + 2
                    if chloe==1: # Incident chloé 
                        print("-Yo Maxence, passe ton biscuit.")
                        sleep(court)
                        print("-Je vais le mettre dans son verre quand elle va pas regarder. Après suffit juste d'attendre.")
                        sleep(long)
                        print("     -Tu vas pas faire ça pour vrai.\n           -T'es fou toi.")
                        sleep(long)
                        print("-Checkez moi ben.\nLe moment parfait est là.")
                        sleep(long)
                        print("C'est fait.")
                        sleep(court)
                        print("Le pire c'est quelle est encore avec du nouveau monde, nouvelles amies que j'ai jamais vu avant.")
                        sleep(long)
                        print("Puis c'est les bisoux, c'est la totale. Elles sont soit-disant 'proches'.")
                        sleep(long)
                        print("Elle tient son verre.\n-Moi les boys je penses que je vais y aller.")
                        sleep(long)
                        print("     -On peut venir avec toi? Le monde qui sont ici ne m'inspire pas grand chose.")
                        sleep(long)
                        print("         -Je me disais la même chose")
                        sleep(court)
                        quit_party=choice_user3("Les emmener chez soi","Refuser","Leur donner un lift") # Repartir ou non avec les gars + 3

                        if quit_party==1: # Départ du party, retourner chez nous avec les boys 
                            print("-Ouais vous voulez passer chez moi? Vous pourrez dormir si vous voulez. Demain je pourrais faire une tourné pour aller vous déposer.")
                        
                        elif  quit_party==2: # Départ du party, retourner seul 
                            print("-Non désolé les gars je vais préférer retourner chez moi seul ce soir.")
                            sleep(court)
                            print("---QUELQUES MINUTES PLUS TARD---")
                            sleep(court)
                            print("Je penses que j'ai oublié d'être fatigué, je vais faire des recherches sur ce dit Simon. \nJe dois être capable de le trouver.     -Suite")
                            print("Ouaip, Simon Lesage, trouvé. J'ai son numéro. Je vais prendre le temps de l'appeler demain. Dodo time.")
                            sleep(long)
                            texte_delai("..",delay=(court*0.1))
                            print("-Suite")
                            input()
                            finchap2="appel"

                        elif quit_party==3: # Départ du party, donner un lift aux boys 
                            print("-Le plus que je peux faire c'est que je peux vous lifter quelque part.")
                            sleep(court)
                            print("-Avez vous manger genre?")
                            sleep(court)
                            print("     -Tu pourrais nous dropper au mcdo, on va pouvoir marcher jusqu'à chez moi.\nMe disait Yousef.")
                            sleep(long)
                            print("-Ça marche")
                            sleep(court)
                            print("---QUELQUES HEURES PLUS TARD---")
                            print("Au final je suis retourer chez moi et j'ai dessiné pendant 3 heures. Je serais prêt à aller me coucher là.")
                            sleep(long)  
                            texte_delai("..",delay=(court*0.1))
                            print("-Suite")
                            input()
                            finchap2="recherche"
                          
                    elif chloe==2: # Niaiser chloé
                        print("-Donnez moi trente secondes.")
                        sleep(court)
                        print("-Salut Chloé. Je t'ai manqué?")
                        sleep(court)
                        print("     -Oui tu veux me parler?")
                        sleep(court)
                        print("     -On peut aller dehors si tu veux")
                        sleep(court)
                        print("-Non,  c'était une question réthorique. Tu sais Maxime? Celui avec la chemise là bas? Il m'avait dit qu'il te trouvait vraiment cute. Tu devrais aller lui parler.      -Suite")
                        input()

                        print("Je le connais même pas.")
                        sleep(court)
                        print("     -Ah oui? Tu sais que c'est toi que je veux right?")
                        sleep(court)
                        print("-Ouais et moi je veux que tu ailles lui parler, j'ai tourné la page ça fait longtemps.")
                        sleep(long)
                        print("Encore impressionnant qu'elle s'attarde toujours sur mon cas.        -Suite")
                        input()

                        print("Je suis retourné auprès des gars.\n-Bon moi les boys je penses que je vais aller marcher. Vous venez?")
                        sleep(long)
                        marcher=choice_user2("Partir vers le dépanneur","Partir vers le centre de trampolines") # Départ vers où + 2
                        if marcher==1:
                            print("On va partir vers en bas je penses. J'ai pas trop d'énergie, y'a un dépanneur proche.")
                            print("-Les gars je voulais vous demander. Vous savez quelque chose sur un texto ce matin venant d'un numéro inconnu me disant de ne pas venir à la job?    -Suite")
                            input()

                            print("     -De ce que j'ai entendu, ça doit être parce qu'il y avait du monde qui faisait de la marde dans le parking du provigo hier.     -Suite")
                            input()

                            print("          -ATTENDS NICOLAS!")
                            sleep(court)
                            print("Pas encore Chloé.")
                            sleep(court)
                            print("     -Je veux pas parler à Maxime. Le texto ce matin c'était moi. Je voulais pas qu'il t'arrives de malheures.")
                            sleep(long)
                            print("-Merci, mais je peux me gérer. Tu devrais vraiment lui parler. Je n'ai plus de sentiment pour toi.       -Suite")
                            input()

                            print("Elle me donnera clairement pas de break ce soir. Bonne chose qu'on soit parti.")
                            sleep(long)
                            texte_delai("..",delay=(court*0.1))
                            print("-Suite")
                            input()
                            finchap2="mail"

                        elif marcher==2:
                            print("La soirée s'est terminé dans le Volt du coin. Ben du fun. J'ai pu glisser un mot sur le truc d'Aswell. \nLes gars ont trouvé sa cool aussi, surtout Maxence.")
                            sleep(long)
                            texte_delai("..",delay=(court*0.1))
                            print("-Suite")
                            input()
                            finchap2="mail"

    print("---CHAPITRE 3---")
    sleep(court)
    if finchap2=="mail":
        print("")
    elif finchap2=="recherche":
        print("")
    elif finchap2=="tim":
        print("")
    elif finchap2=="appel":
        print("")

    nb_lecture=nb_lecture+1
    print(f"\n\nSouhaitez vous recommencer l'histoire? Cela vous fait {nb_lecture} lectures.")
    rejouer= choice_user2("Oui","Non")
    if rejouer==2:
        JOUER=False
    elif rejouer==1:
        #Si l'utilisateur a jouer au minimum 3 fois, un prompt demande s'ils veulent retirer les "time.sleep"
        if choix_temps==2 and nb_lecture>=3:
            print("\n\n**Souhaitez vous retirer les temps d'attente? Vous n'aurez plus besoin d'attendre après les lignes de texte.**")
            choix_tempssleep= choice_user2("Oui","Non")
            if choix_tempssleep==1 :
                court=0
                long=0
print("Fin")
sleep(2.5)
