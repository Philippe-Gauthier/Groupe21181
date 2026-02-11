import os
import time
from time import sleep
import random
import keyboard
# Fonctions pour manipuler la forme et la profondeur de l'histoire 
def print_slow(text):                 
    """
    ENTRÉE : texte à afficher (string)
    SORTIE : RIEN
    BUT :    Ralentir la vitesse d'affichage de texte. Pour créer un sentiment de lecture rythmée
    """
    for i in text:
        print(i, end='', flush=True)
        sleep(0.05)
    print()

def clear_screen():                     
    """
    ENTRÉE : RIEN
    SORTIE : RIEN
    BUT :    Flusher tout élément de l'écran sans perdre mes données. Quand l'écran est trop chargé d'écriture
    """
    time.sleep(3)
    if os.name == 'nt':
        clear = os.system('cls')

#Fonctions pour tout ce qui entoure le dé à jouer
def intro():                           
    """
    ENTRÉE : réponse oui ou non de l'utilisateur
    SORTIE : choix de l'utilisateur (String majuscules)
    BUT :    Savoir si un dé numérique sera nécessaire pendant l'histoire
    """
    choice = input("Avant de commencer, as-tu un dé à 6 faces avec toi ? (Oui/Non) ")
    upper_choice = choice.upper()
    return upper_choice

def roll_dice():                        
    """
    ENTRÉE : RIEN
    SORTIE : Numéro généré au hasard
    BUT :    Rouler un dé à 6 faces (Numéro au hasard entre 1 et 6)
    """
    print("Désolé, je brasse ton dé en ce moment. Donne moi 2 sec...")
    time.sleep(2)
    resultat = random.randint(1, 6)
    print(f"Tu as eu un {resultat} ! ")
    input("Appuie sur ENTER pour continuer...")
    return resultat

def dice_Check():                      
    """
    ENTRÉE : Choix fait dans intro(), résultat de dé par utilisateur, dé numérique crée
    SORTIE : résultat final de dé.
    BUT :    Séparation de l'histoire avec le système de dés
    """
    print("Attention! Choix décisif en cours! ")
    time.sleep(2)
    if(choix == "OUI"):
    
        while True:
            result_dice = input("Brasse ton dé et donne moi ton resultat svp : (1-6) ")

            if not result_dice.isdigit():
                print("Une chance qu'il y a une sécurité contre ça ;)")
                continue
            
            result_dice = int(result_dice)
            if result_dice >= 1 and result_dice <= 6:
                break
            if result_dice == 7:
                secret_ending()
            else:
                print("Impossible, un dé a seulement 6 faces ;)")
                
    elif(choix == "NON"):
        result_dice = roll_dice()
    return result_dice

def yes_no():
    """
    ENTRÉE : input d'utilisateur (string)
    SORTIE : réponse par oui ou non (string)
    BUT :    séparer l'histoire et juger par soi-même de la situation
    """
    while True:
        choice = input("Est-ce que tu as lu ses lettres? (Oui-Non) : ")
        tempo_upper_choice = choice.upper()
        if tempo_upper_choice != "NON" and tempo_upper_choice != "OUI" :
            print("Jsuis serieux mon gars. concentre toi stp. Je te demande encore, \n\n")
            continue
        elif tempo_upper_choice == "NON" or tempo_upper_choice == "OUI":
            break
    return tempo_upper_choice

def secret_ending():
    """
    ENTRÉE : RIEN
    SORTIE : RIEN
    BUT :    FIN SECRÈTE AMUSANTE
    """
    print_slow("-Carraway! commença le détective. Je... enfin... euhmmm... \n-Je m'occupe de le faire parler cette fois? Dit Carraway pour aider à terminer la phrase de son collègue.\n\n-COUPEZ! \n-Meeeerde désolé les gars j'ai eu un p'tit blanc de mémoire." \
    "\n-Mais merde t'es sérieux? T'as gâché la prise! On doit tout recommencer maintenant! Dit le directeur de tournage\n-T'inquiète ça arrive. Dit l'acteur qui joue Carraway. T'es nouveau dans le showbiz.\n-Merci mec, désolé j'suis nerveux.\n-Ça va\n-Allez! On se prépare.\n\n" \
    "Pendant que l'acteur se répetait les lignes pour ne pas les oublier, l'acteur de Carraway se regarda pendant un instant au miroir. Il sourit à son reflet. Il ne voulait pas brimer son moral. Il savait comment tout ceci terminait et il essayait de garder une bonne humeur malgré tout\n\n" \
    "-BON ON SE PRÉPARE! Ce que l'autre a dit, Scène 2, ACTION!\n\n-Asseyez-vous droit, Elliot. Ça ira plus vite si on se parle calmement....\n\n\nFIN...?")
    
    return False

#Variables de santé mentale pour la fin
controle = 0                            #Controle de soi (Carraway)
violence = 0                            #Violence de Buchanan
lucidite = 0                            #Avoir une conscience de soi (Carraway)
mensonge = 0                            #Mensonges de Buchanan qui augmente
realite = 0                             #Il est woke sur la vraie vie (Carraway)
corruption = 0                          #Corruption de personnage de Buchanan

#Fonction temporaire pour faire le suivi de l'histoire. Sera enlevé avant la remise
def show_stats():
    print(f"Controle : {controle}\nViolence : {violence}\nLucidité : {lucidite}\nMensonge : {mensonge}\nRéalité : {realite}\nCorruption : {corruption}\n\n")


"""Début de l'histoire"""

choix = intro()
if (choix == "OUI"):
    print("Magninfique! Tu peux utiliser ton dé pour cette aventure! L'histoire commence dans 3 secondes! Bonne lecture!")

elif (choix == "NON"):
    print("T'inquiète pas! Il y a un dé qui va être roulé pendant ton histoire! Bonne lecture et bonne chance!")

clear_screen()

print_slow("Ce que l'autre a dit")
time.sleep(2)
clear_screen()

print_slow("Chapitre 1 : L'interrogatoire")
clear_screen()
print_slow("9 octobre 1936, ??H?? AM \n\n\nLa pièce était trop petite pour respirer correctement.\nUne ampoule nue pendait au plafond, oscillant lentement, projetant des ombres instables sur les murs.\n\nEliot Kramer restait immobile "\
"sur sa chaise.\nDevant lui, une table en métal et une tasse de café froide. L'odeur de cigarette s'était incrustée dans la pièce depuis longtemps\n\nIl n'avait pas touché à la tasse.\nIl n'avait pas parlé non plus.\nLa porte s'ouvrit."\
"\n\nDeux hommes entrèrent.\nIl refermèrent derrière eux.\n\n\n")
time.sleep(5)

roll_result = dice_Check()
clear_screen()

#Choix Crucial #1
if roll_result % 2 == 0:
    controle += 1 
    lucidite += 1
    show_stats()
    print_slow("\n\n-Asseyez-vous droit, Elliot.\n\nÇa ira plus vite si on se parle calmement.\n\nElliot leva les yeux vers lui.\n\n-Vous savez pourquoi vous êtes ici. N'est-ce pas?\n\nLe silence" \
    " se faisait gros.\n\nLe second détective resta près du mur, bras croisés.\n\n-Fais-le parler, Carraway.\n\nElliot esquissa un sourire nerveux. Carraway déposa le dossier sur la table.\n\n")
elif roll_result %2 != 0:
    violence += 1
    corruption += 1
    show_stats()
    print_slow("\n\n\n- Putain de merde! Mais c'est le foutu Eliot Kramer en personne! Lanca le premier détective.\n\nEliot Kramer évitait son regard.\n\n-Regarde-moi quand je te parle espèce de pourriture.\n\n" \
    "Le dossier claqua sur la table.\n\nElliot sursauta.\n\n-Trois femmes. Même quartier, même heure. Tu sais très bien qui a fait ça. Et tu vas me le dire à l'instant. Le premier détective resta debout, trop près. Le second enleva son chapeau lentement.\n\n" \
    "-Doucement, Buchanan. Il ne parlera pas si tu continue comme ça.\n\nElliot déglutit\n\n")

if controle == 1:
    print_slow("-Écoutez... Commença le suspect. Je ne suis pas plus au courant que vous. En fait je ne sais pas ce que je fait ici...\n\n-Il ment. Dit l'inspecteur aux bras croisés. Regarde ses mains, ils tremblent comme des putains de feuilles mortes.\n" \
    "L'agent Carraway baissa les yeux et vit effectivement des mains tremblantes sur la table. Eliot essayait de cacher sa nervosité... Carraway avait honte de ne pas l'avoir remarqué en premier que le détective Buchanan. ")
elif violence == 1:
    print_slow("-PARLE! Cria Buchanan en frappant du poing sur la table.\n\nL'autre détecctive se raidit d'un coup au son métallique de la table.\n\n-Calme toi, Carraway. Je ne lui ai rien fait. Pas encore. Dit Buchanan avec un sourire malicieux. Eliot ressentait " \
    "une sueur froide qui lui coulait le long du dos.\n\n-Je...je ne sais pas de quoi tu me parles...je..je..je n'ai rien à voir dans tout ça.\n\n\n-Il est nerveux, dit Carraway. Donne lui un peu d'espace. Tu l'as assez joué sur la peur.\n-Non, il ment cet enculé...\n\n")

#Choix crucial #2
roll_result = dice_Check()
clear_screen()

if roll_result <= 2:                    #Option pacifique
    controle += 1
    lucidite += 1
    if violence == 1 :
        print_slow("-Allez c'est bon je vais continuer. Dit l'agent Carraway.\nBuchanan gloussa. Il baissa la tête de déception, et recula.\n\n ")

    print_slow("-Regarde Kramer. Ici, ce que toi et moi, on veut est simple. Tu veux sortir au plus vite et moi, je veux trouver le coupable pour l'amener en justice. Mais on sait que tu as des informations utiles. Et si tu continues à éviter de répondre à la question, alors "\
               "mon collègue sera fâché. Je dois assez le supporter dans la journée. Alors ne rends pas la tâche plus difficile.\n-Quoi? Dit le suspect d'un air confus.\n-Allez. Ne perdons pas plus de temps. Le jour du meutre, on vous a vu à quelques rues de la scène de crime." \
               "Que faisiez-vous et où alliez-vous?\n\nKramer soupira un long coup")
elif roll_result <= 4:                  #Option neutre
    realite += 2
    print_slow("-Pourquoi est-ce que vous été apperçu à quelques rues des meurtres? Demanda le détective Carraway. Vous étiez loin de votre maison et vous n'êtes pas un habitué de ce coin.\n-Mais comment le saviez-vous?\n-Tu pensais qu'on ne gardait pas un oeil sur nos anciens criminels?\n" \
    "-Mais je suis devenu quelqu'un de bien, moi!\n-Et je ne dis pas le contraire, félicitations! C'est pour ça que je te demande ce que tu sais.\n\n")
elif roll_result<= 6:                   #Option violente
    violence += 2
    corruption += 1
    mensonge += 2
    print_slow("-Je ne te dirais rien, espèce de sale flic de merde. Je suis innocent moi! Tu nas pas à me garder ici.\nBuchanan gloussa sec. S'approcha d'Elliot et le pris par la nuque.\n-Dernière chance Kramer. Je ne brise aucune loi en ce moment. Je suis la loi.\n\n" \
    "La victime se contenta de cracher au visage du détectif. Le détectif Carraway s'essuya le visage. Il avait chaud car il savait ce qui allait arriver. Il détestait travailler avec Buchanan. Ils veulent la justice mais ils ont 2 visions différentes. Il ne peut pas le contrarier " \
    "non plus, car sinon, il sait qu'il passera un terrible moment.\n\nL'autre détective ne perdit pas de temps pour utiliser ses poings. Il souleva le suspect par le col, lui adressa un solide coup de tête qui le fit vasciller vers l'arrière. Il en profita alors pour lui offrir un direct " \
    "sur l'estomac pour enfin le plaquer contre le mur\n\n-Ok! Ok! Je vais vous dire! Merde! Arrêtez s'il-vous plaît! \n-Bon tu vois? C'était pas si difficile que ça pas vrai? Il assit alors Kramer sur la chaise.\n\n")

print_slow("-Vous avez deja lu les lettres? Demanda Elliot.\n-Lesquelles? Demanda sèchement Buchanan.\n-Celles qu'on ne montre pas aux journaux.\n\n-De quoi il parle encore?\n\n-Je... j'en suis pas au courant. Dit Carraway.\n\n")


#Choix crucial #3
simple_choice = yes_no()
if simple_choice == "NON":                      #Approche de Fin 4 et 5 car pas supposé
    realite += 2               
    lucidite += 3               
    print_slow("-Vous n'avez pas lu les dossiers? Alors ça c'est une première ! Vous êtes sur que vous avez fait vos devoirs?\n-Hé ho! C'est nous qui pose les questions ici. Pas toi\n-Désolé. Mais c'est ce qui a été retrouvé sur la scène." \
    " J'étais certain que vous étiez au courant...\n\n")
    roll_result = dice_Check()
    if roll_result % 2 == 0:                    #Si pair FIN 4 approche. Questionne tout

        print_slow("-Attendez... mais comment êtes-vous au courant de tout ça? C'est des données confidentielles de la police!\n\nSilence...\n\n-Contentez-vous de répondre à la question. Ordonna le détective\n-Qui parle en moment? Questionna Kramer\n"
        "-Quoi?\n-J'ai dit, qui parle en ce moment?\n\n\nQui parle? à toi de choisir...")
        roll_result = dice_Check()              #Si dé donne 4, FIN 4
        clear_screen()
        
        if roll_result == 4 : 
            lucidite += 3
            print_slow("Je, détective Carraway, parle en ce moment. Et en ce moment je te demande comment, bordel de merde, tu as cette information?\n-Information sur quoi?\n")
            roll_result = dice_Check()          #Faire croire au lecteur. mais t'es sur le chemin de non retour :(

            if roll_result <= 3:
                print_slow("L'information sur le capitaine. Comment tu sais qui a tué notre capitaine?\n")
            else:
                print_slow("L'information sur les lettres! Comment es-tu au courant??\n")

            print_slow("-Je tiens à vous dire que, depuis que vous êtes entré dans la salle, vous n'avez jamais regardé dans votre 'dossier' de police.\n-Ah ouais? Pas besoin car je le connais par coeur mon dossier, moi! Je suis avec le NYPD comme tu peux le voir sur mon badge. Dit le détective en touchant son badge de police.\n\n")
            lucidite += 3
            print_slow("En fait, il n'y avait qu'une épinglette souvenir de New York\n\n-Quoi? Je ne comprends pas. Où est mon badge?!\n\n-Vous n'êtes plus vous-même, détective.\n\nLe détective se tourna pour voir son collègue, qui était silencieux depuis un moment...\n\n")
            roll_result = dice_Check()
            if roll_result % 2 == 0:
                print_slow("Son collègue était bien là. Confus pour toute cette situation.\nMais ne disait aucun mot. ")
            else:
                print_slow("Il n'y avait personne d'autre dans la salle à part lui et le suspect. Il ne se rappelait plus du nom du suspect. Il a sûrement été drogué. Il a voulu sortir son arme pour se défendre, " \
                "mais il sortit à la place une banane.\n\n")
            print_slow("Il n'en revenait pas. La salle était devenue blanche. Le miroir n'était plus là. Le suspect se leva et dit : Bon on peut maintenant jeter les rideaux. Ça ne fonctionne pas du tout. VOUS POUVEZ ENTRER!.\nÀ peine ces mots dit, " \
            "des personnes à blouse blanche sont entrés avec une veste de force.\n-Je suis désolé, M. Carraway. Nous avons vraiment essayé. Je sais que votre ancien métier vous manque,alors on s'était dit que le dossier que vous avez jamais réussi à résoudre vous aiderait." \
            "ce sera alors pour une autre fois. \n\nCarraway essaya de se débattre. Il était un inspecteur, enfin, il pense. Les infirmiers lui injectèrent un sédatif. Et l'amènèrent dans un couloir blanc, vide. À tout jamais.\n\nFIN.")


    else:
        print_slow("Ouais on n'a pas ")

elif simple_choice == "OUI":                    #Approche de Fin 1 2 3 et 6
    corruption += 2
    lucidite += 2
    print_slow("Alors vous savez à quoi vous attendre. ")

show_stats()

"""
FIN 1 --Kramer mechant
controle   ≥ 8

FIN 2 --Buchanan mechant
violence   ≥ 10

FIN 3 --capitaine mechant
corruption ≥ 8

FIN 4 --Asylum
lucidite   ≥ 10

FIN 5 --Real ending
realite    ≥ 6

FIN 6 --sujet clos sans savoir
mensonge   ≤ 6

FIN 7 --?????
controle   ≥ 6
violence   ≥ 6
lucidite   ≥ 6
mensonge   ≤ 6
realite    ≥ 6
corruption ≤ 6
"""