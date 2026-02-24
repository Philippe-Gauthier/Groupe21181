"""
Futurs dont vous êtes l'auteur!
Par: Nathan Paradis
"""






#faire attention avec les \n, qui ne sont pas comptés dans les textwrap, 
# modifier certains passages, surtout les "que faites vous" a la fin des mises en situation.




# "REMISE FINALE" DANS LA DESCRIPTION DU COMMIT DE LA BRANCHE MAIN






#imports
import time #pour pouvoir utiliser time.sleep dans le code
import textwrap #pour formatter le text présenté dans le terminal



#definition des variables

#text début du jeu
mise_en_contexte = "Vous êtes la grande Yisma, voyante reconnue a travers le monde (le monde étant Longueil), mais ce matin vous avez échappé votre boule de crystal en vous faisant un bol de céréales, vous devez donc inventer de toutes pieces le futur de vos clients de la journée en attendant de voir le réparateur de boules de crystal (qui est occupé pour les 3 prochaines semaines. Son service est très en demande, les boules sont devenues glissantes de nos jours)."
regles_instructions = "Instructions:\nL'aventure se joue en une journée, composée de deux parties, la mise en situation et la prise de décision.\nPour la partie mise en situation, vous allez avoir un texte unique au niveau a lire, ensuite, 3 options apparaitront sur le terminal, chacune\ndes options commencent par 1, 2, ou 3.\n\nAprès, vous aurez une décision a prendre. Pour faire cela, entrez le numéro de l'option que vous voulez choisir, soit 1, 2, ou 3, et entrez\nle dans le terminal (ce serait clairement indiqué qu'il est pret a recevoir votre décision).\n\nCa recommence ensuite avec une nouvelle mise en situation, puis une décision, et ainsi de suite jusqu'a une mise en situation finale qui\nterminera l'aventure.\n(Au moment de choisir, entrez 0 si vous voulez retourner au début de la journée)\n"

#text utilisé a plusieurs endroits
choix_retour = "\nretour au début de la journée...\n"
choix_fail = "\nCela ne faisait pas partie des choix, réessayez\n"

#textfin
jeu_fin = "\nFin! Rejouez pour voir toutes les options"



#variables de niveaux

#---3 layer
#ending
textmartinechance = "Vous lui dites qu'elle sera tres chanceuse cette semaine! Vous lui suggerez meme d'acheter un billet de 6 49. Elle vous sourit, vous dit merci et quitte votre tente. Vous savez qu'elle reviendra demain, et le jour d'apres, Martine vient vous voir a chaque jour depuis l'ouverture de votre tente il y a 29 ans."
martinechance = [textmartinechance]

#layer----4 layer
#ending
textmartinebain = "Vous lui dites qu'elle devrait prendre un bain avec du sel magique (que vous vendez 14,59$ le gramme). Elle rit et vous demande si ce n'est pas le genre de truc qu'un medecin recommanderait normalement. Elle quitte en riant, vous savez qu'elle reviendra quand même. (je suis désolé pour ces storylines autant pourries mais j'ai pu de jus creatif lol)"
martinebain = [textmartinebain]

#ending
textmartineesprits = "Vous lui dites qu'elle devrait prendre une séance avec ces ancetres (vous offrez ce service a 71.19$ pour 5 minutes). Elle vous dit qu'elle ne voit pas ce que parler a ses ancetres feraient a sa situation, mais elle accepte et vous dit qu'elle reviendrait demain pour faire une séance de 15 minutes. Bravo, vous pourrez enfin vous acheter mario kart world pour la switch 2 avec cet argent."
martineesprits = [textmartineesprits]

#ending
textmartinefil = "Vous lui dites qu'un très ancien truc pour repousser la malchance est de porter un petit bout de fil rouge autour de la cheville (vous ne savez pas pourquoi, mais vous en vendez a 47,68$ le bracelet). Elle vous dit qu'elle en prendrait bien un. Bravo, vous venez de vous faire 47,68$ sur le dos d'une innocente qui n'est même pas malchanceuse pour vrai."
martinefil = [textmartinefil]

#---3 layer
textmartinemalchance = "Vous lui dites de faire attention cette semaine, car selon le positionnement de l'étoile vega elle sera malchanceuse jusqu'a la fin de la semaine. Martine vous demande s'il y a quelquechose qu'elle pourrait faire pour se protèger contre sa malchance.\n\nQue lui proposez-vous?"
martinemalchance1 = "Un bain de sel"
martinemalchance2 = "Une seance avec les esprits"
martinemalchance3 = "Un fil rouge"

martinemalchance = [textmartinemalchance, martinemalchance1, martinemalchance2, martinemalchance3]

#----4 layer
#ending
textmartinenormal = "Vous lui dites que c'est parfaitement normal que certaines semaines soient plus 'normales' que les autres. Ce n'est pas a chaque semaine que l'on gagne la loto. Elle semble un peu décue, mais elle comprends. (j'suis tanné d'écrire des options help me pls)"
martinenormal = [textmartinenormal]

#ending
textmartineverite = "Vous lui dites que votre boule de crystal est cassée, que vous ne pouvez pas voir son futur pour vrai, c'est pour ca que vous avez fait une estimation si 'normale' de sa chance de la semaine. Elle comprends votre situation, et vous recommande un réparateur de boules de crystal dont vous n'aviez jamais entendu parler auparavent, et de plus, selon elle, il est celibataire. Lui dire la vérité était le meilleur choix semble-t'il."
martineverite = [textmartineverite]

#ending
textmartinedouter = "Vous lui dites que c'est une insulte de douter une voyante, et que cela double sa malchance. Elle s'excuse profusément et vous demande s'il y a une facon de réduire sa malchance. Vous lui dites que vous vendez des plantes magiques qui chassent les mauvais esprits, et que ca lui ferait un total de 258,37$. Bravo vous vous êtes fait trop d'argent pour un service de voyance frauduleux, vous vous sentirez mal pour le reste de votre vie, mais au moins vous pourrez renouvelez votre abonnement costco pour les deux prochaines années."
martinedouter = [textmartinedouter]

#---3 layer
textmartinelesdeux = "Vous lui dites que sa chance sera un peu des deux cette semaine, soit un peu de chance, et un peu de malchance. Elle vous regarde suspicieusement 'alors la normale?'. Vous vous dites que vous devriez peut etre faire plus attention a comment vous répondez aux questions avant que quelqu'un réalise que votre boule est cassée et que vous êtes une fraude (aujourd'hui en tout cas).\n\nQue dites-vous?"
martinelesdeux1 = "Lui dire que c'est l'habituel d'avoir un peu des deux"
martinelesdeux2 = "Lui dire la vérité: que votre boule est brisée"
martinelesdeux3 = "Lui dire que c'est innaceptable de douter une voyante"
martinelesdeux = [textmartinelesdeux, martinelesdeux1, martinelesdeux2, martinelesdeux3]

#--2 layer
textmartine = " Martine entre dans votre tente, c'est une femme un peu plus agée que vous, mais pas de beaucoup, c'est votre cliente la plus loyale. Elle vous demande de lui dire sa chance pour la semaine.\n\nQuelle sera sa chance?"
martine1 = "Beaucoup de chance"
martine2 = "Beaucoup de malchance"
martine3 = "Un peu des deux"

martineclient1 = [textmartine, martine1, martine2, martine3]



#----4 layer

#ending
textdevined6 = "Vous lui dites qu'Elder Scrolls 6 sortira avant les autres, mais qu'il sera décevant après toute cette attente. Vous voyez qu'il est décu de votre réponse, il dit 'Vous ne connaissez rien sur ce sujet, vous êtes une fraude!'. Il part en vous payant en dessous de votre taux habituel. Vous continuez a fixer la sortie de votre tente pour quelques secondes avant de vous dire que vous etes trop vieille pour faire ce travail et que vous devriez prendre votre retraite."
devined6 = [textdevined6]

#ending
textdevinbb2 = "Vous lui dites que vous n'êtes pas sur quel jeu sortira en premier, mais vous lui dites avec certitude que Bloodborne 2 ne sortira jamais. Son visage s'affaisse, il sort son portefeuille, vous paye, et s'en va. Vous venez de perdre un futur client."
devinbb2 = [textdevinbb2]

#ending
textdevinhl3 = "Vous lui dites que Half-Life 3 sortira le premier, et de plus, ce sera plus tot qu'il l'esperait! Devin sourit, et vous paye généreusement. Vous vous êtes fait un nouveau client régulier."
devinhl3 = [textdevinhl3]

#---3 layer
textdevinjeux = "Vous lui dites que l'amour est difficile a lire en ces temps incertains (l'ombre de vénus vous bloque la vue) mais que vous voyez clairement le futur des jeux videos. Soudainement tout excité, Devin vous demande avec passion lequel entre trois jeux sortira en premier.\n\n Quel jeu sortira en premier?"
devinjeu1 = "Elder Scrolls 6"
devinjeu2 = "Bloodborne 2"
devinjeu3 = "Half-Life 3"

devinjeux = [textdevinjeux, devinjeu1, devinjeu2, devinjeu3]



#-----5 layer

#ending
textdevingoodending = "Vous lui dites qu'il va vivre une très belle vie, qu'il aura des enfants, et que ses enfants auront des enfants, et qu'il allait mourrir paisiblement main dans la main avec sa femme. Il vous fait un drole de visage, puis vous revele alors qu'il est homosexuel. Il vous traite d'homophobe, vous sacre une bonne claque en plein dans la tronche et il part sans payer. Vous aviez besoin de cet argent pour votre abonnement netflix sans pubs, vous tombez donc dans la depression."
devingoodending = [textdevingoodending]

#ending
textdevinbadending = "Vous lui dites que les apparences sont trompeuse, et qu'il finira par se divorcer, et de tomber dans l'alcoolisme. Il vous regarde d'un regard vide, et puis il vous remercie de l'avoir prévenu. Il part apres avoir payé pour votre service, vous vous sentez mal de détruire les espoirs d,un si jeune homme mais vous vous dites que c'est pour le plus grand bien (pouvoir vous payer votre abonnement amazon prime pour la livraison gratuite)."
devinbadending = [textdevinbadending]

#ending
textdevindepressed = "Est-ce vraiment une fin??? qui sait, peut etre que lorsque voux cliquerez pour recommencer le jeu et voir les autres fins vous allez trouver quelquechose de noueau ici, qui sait (et pour les gens qui sont encore ici, rebonjour, et ca me tentait vraiment pas de continuer cette branche. J'avais besoin d'une troisieme option, et je suis trop pareusseux pour l'écrire.)"
devindepressed = [textdevindepressed]

#----4 layer

textdevinlove = "Vous lui dites qu'il va rencontrer tres bientot l'amour de sa vie, vous le voyez clairement dans votre boule de crystale (brisée, mais vous ne mentionnez pas cela). Il vous supplie de lui en dire plus.\n\n Quel est son futur amoureux?"
devinlove1 = "Good ending"
devinlove2 = "Bad ending"
devinlove3 = "Depressing ending"

devinlove = [textdevinlove, devinlove1, devinlove2, devinlove3]



textdevinnolove = "Vous lui dites qu'il n'aura tristement pas la chance de vivre l'amour dans sa vie, mais c'est l'opportunité pour lui de se consacrer a d'autres passions, telles que le pickle ball professionnel. Vous voyez Devin s'affaisser un peu, puis il se leve, et quitte. Vous croyez entendre des pleurs venant de l'exterieur de votre tente. Vous realisez alors qu'il ne vous a pas payé, vous aviez besoin de l'argent pour payer votre spotify premium, vous tombez donc en depression nerveuse."
devinnolove = [textdevinnolove]



textdevintarot = "Cartes tarot, haha, balatro reference. J'ai pas eu le temps (et la patience) d'écrire cette fin."
devintarot = [textdevintarot]

textdevinlignes = "lignes de la main, J'ai pas eu le temps (et la patience) d'écrire cette fin."
devinlignes = [textdevinlignes]

textdevinthe = "feuilles de thé, j'ai pas eu le temps (et la patience) d'écrire cette fin."
devinthe = [textdevinthe]

textdevindevier = "Vous ne pensiez pas avoir besoin d'en dire plus, il vous a pris au dépourvu, et vous ne pouveaz pas vous fier sur votre boule de crystal. vous décidez donc de sortir l'artillerie lourde. Vous dites a Devin d'attendre quelques secondes pour que vous puissiez aller chercher votre matériel.\n\nQuel item prennez-vous?"
devindevier1 = "Cartes de Tarot"
devindevier2 = "Livre sur les lignes de la main"
devindevier3 = "Feuilles de thé"

devindevier = [textdevindevier, devindevier1, devindevier2, devindevier3]

#---3 layer
textdevinamour = "Vous lui dites que le futur en termes de sorties de jeux est assez flou ce matin (mercure retrograde) mais vous voyez clairement son futur amoureux. Il vous demande de lui en dire plus.\n\nQue lui dites-vous?"
devinamour1 = "Amour"
devinamour2 = "Pas d'amour"
devinamour3 = "Dévier le sujet"

devinamour = [textdevinamour, devinamour1, devinamour2, devinamour3]



#-----5 layer

#ending
textdevinrepete = "Il vous regarde fixemment et vous dit très lentement: 'oui... je... m'appelle... Devin'. Vous lui expliquez alors ce qu'est un devin, il rougit s'excuse alors de son ignorance. Il est si désemparé qu'il vous paye et quitte la tente après ses excuses. Vous regardez l'entré de votre tente et vous dites a vous memes: 'les jeunes de nos jours...'. Vous vous dites que vous ne voulez pas gérer ce genre de personnages aujourd'hui, et vous retournez vous couchez chez vous."
devinrepete = [textdevinrepete]

#ending???
textdevinexcuse = "Il accepte votre excuse, et, passant a la suite, il vous demande si vous savez s'il sera riche dans le futur. (4th wall break jumpscare, je me gardais ici des options pour continuer au cas ou j'aurais pas assez de choix, mais puisque vous lisez ceci, j'imagine que j'avais assez d'options.)"
devinexcuse = [textdevinexcuse]

#ending
textdevinriendire = "Il fronce les sourcils, 'me prennez vous pour un idiot?', et vous répondez 'oui' avec confiance. Il sort de votre tente, enragé. Vous avez perdu un client"
devinriendire = [textdevinriendire]

#----4 layer

textdevindevin = "Il vous dit que oui il s'appelle Devin\n\nVous le regardez dans les yeux et lui dites:"
devindevin1 = "'Non, êtes-vous devin?'"
devindevin2 = "'My bad fam'"
devindevin3 = "Rien dire et rouler des yeux"

devindevin = [textdevindevin, devindevin1, devindevin2, devindevin3]

#ending
textdevinriche = "A la premiere mention d'argent, Il devient fou et vous saute a la gorge, et vous crie 'MONEEEYYYYYYY' (vous ne parlez pas anglais donc ne savez aucunement ce que cela veut dire), vous sortez calmement votre spray au poivre et l'arrosez en plein dans les yeux, il vous lâche, se met a pleurnicher et il vous dit qu'il n'a jamais eu beaucoup d'argent, que ses parents avaient seulement un manoir, 5 maisons, 2 blocs appartement, 11 roulottes et une plage privée a Hawai, qu'il avait toujours conduit une vieille lamborghini de 2021, et qu'il n'avait jamais été gâté de sa vie a part la fois ou ses parents lui ont donné une carte de crédit pour qu'il puisse s'acheter tout ce qu'il voulait a leur compte. Vous n'avez rien de plus a dire sur la situation. Et, de plus, en tant qu'écrivain de cette histoire je ne sais meme pas ou je veux aller avec cette branche, alors honêtement elle va finir drette la, boom, finito, allez voir les autres branches a la place."
devinriche = [textdevinriche]

#ending
textdevinspecial = "Il vous demande si vous le prennez pour un handicapé a le traiter de 'spécial' comme ca, et quitte votre tente. Vous vous demandez ce qui rend ces jeunes si susceptibles de nos jours. Un peu découragée, vous retournez chez vous pour écouter la lutte professionelle (votre sport préféré)."
devinspecial = [textdevinspecial]

#---3 layer
textdevinnom = "Vous l'interrompez et lui demandez d'ou vient son nom. Vous pensiez que seuls les devins de grandes familles pouvaient s'appeller Devin, mais vous trouvez que ce jeune homme n'a vraiment pas l'air du genre 'famille riche et connue avec des pouvoirs divinatoires'.\n\nVous lui demandez si:"
devinnom1 = "Il est devin"
devinnom2 = "Il est riche"
devinnom3 = "Il savait que son nom était spécial"

devinnom = [textdevinnom, devinnom1, devinnom2, devinnom3]



#--2 layer
textdevin = "Votre premier client de la journée rentre dans votre tente, c'est un jeune homme d'environ vingt-trente ans, il vous donne son nom: Devin. Devin vous demande si vous pouvez lui parler de son futur amoureux ou du futur des jeux videos (vous ne conaissez rien aux jeux videos, ca commence bien la journée...).\n\n De quoi lui parlez-vous?"
devin1 = "De jeux videos"
devin2 = "D'amour"
devin3 = "De ou son nom provient"

devinclient2 = [textdevin, devin1, devin2, devin3]





#=====CHIEN=====#

#----4 layer
#ending
textchienhocher = "Tristement, sa chienne est infidele envers lui, vous lui dites que c'est la vérité, et qu'elle a couché avec un berger allemand il y a deux jours. Le chien vous regarde avec un air extremement piteux, vous avez pitié de lui. Il quitte votre tente apres avoir déposé quelques biscuits en forme d'os comme paiement pour votre service. Apres toutes ces émotions vous vous dites que vous devriez retourner chez vous, vous voulez faire sur que votre berger allemand ne soit pas en train de jouer dans votre cour."
chienhocher = [textchienhocher]

#ending
textchiensecouer = "Tristement, son maitre a des plans de le mettre en adoption a la SPA, vous lui dites que c'est bel et bien la vérité. Il n'arrive pas a y croire, et jure en sortant de votre tente 'Wouf wouf... waf wouf wouf' ce que, si vous avez bien compris, veut dire qu'il planifie mordre son maitre a un endroit particulier, mais vous n'avez pas bien compris quel endroit exactement... Apres toutes ces émotions vous vous dites que vous devriez retourner chez vous et nourrir votre chat."
chiensecouer = [textchiensecouer]

#ending
textchienrien = "Tristement, vous venez d'apprendre au chien qu'il a la rage en phase terminale et qu'il ne lui reste pas longtemps a vivre. Le chien vous regarde d'un air démoli, il se retourne tranquilement, dépose un os par terre en guise de paiement (vous acceptez les paiements mOStercard depuis quelques mois) et quitte votre tente. Vous vous dites que vous devriez arreter de voler innutilement l'espoir a de pauvres chiens innocents et reconsidérez votre travail. Vous vous dites que allez aller postuler a la fourriere la plus proche (au moins vous allez abréger leur souffrances)."
chienrien = [textchienrien]

#---3 layer
textchienwraf = "Vous pensez avoir bien répondu, mais le chien se met a grogner Il vous demande en jappant: 'WAF WOUF WOUF WIF WRAF??'\n\nQue faites-vous?"
chienwraf1 = "Hocher la tête"
chienwraf2 = "Secouer la tête"
chienwraf3 = "Rien faire"

chienwraf = [textchienwraf, chienwraf1, chienwraf2, chienwraf3]


#---3 layer
#ending
textchienrrr = "Vous venez d'insulter sa mere. Le chien vous regarde avec dédain, puis sort de votre tente en pissant. Vous vous dites que vous auriez du continuer vos cours de langage canin. Mais vous vous dites aussi que le temps que vous utilisiez pour ce cours est mieux placé maintenant (vous allez au casino a la place)."
chienrrr = [textchienrrr]


#----4 layer
#ending
textchienencourager = "Vous dites au chien de prendre courage, et que selon la légende, la race féline allait bientot disparaitre dans un génocide rapide et brutal perpétrée par Le Grand Chihuahua, aussi connu sous le nom de Bibine, et son armée de Huskies enragés. Le chien vous demande 'wouf waf wou?' et vous lui répondez que s'il s'entraine, il aurait une bonne chance d'etre recruté dans leur armée. Le chien, une nouvelle étincelle d'espoir dans le regard, vous remercie, dépose un 20 piasses baveux dans votre main, et quitte votre tente. Vous vous demandez pourquoi vous avez inventé cette histoire, puis vous vous dites que ca ne devrait pas vous affecter long terme, tant que vous gardez votre chat, Mystique, a l'intérieur."
chienencourager = [textchienencourager]

#ending
textchienrassurer = "Vous le rassurez, lui disant que c'est pafaitement normal pour un grand danois comme lui de se faire intimider par le chaton des voisins, et qu'il fallait simplement qu'il montre a ce chaton c'est qui le boss. Le chien, satisfait de votre service (pas tant divinatoire mais bon, c'est un chien apres tout), vous paye et quitte votre tente."
chienrassurer = [textchienrassurer]

#ending
textchienreprimander = "Vous dites au chien que c'est innacceptable de tenir des propos autant diffamatoires envers les chats. Vous lui apprennez que sans votre chat vous n'auriez jamais été dans le domaine de la divination, car cest grace a une relation symbiotique avec votre chat que vous arrivez a lire le futur (pas pour rien qu'ils étaient révérés comme des dieux a l'époque Égyptienne). Le chien, incrédule, quitte la tente sans payer (C'est un chien apres tout, a quoi vous attendiez vous apres tout cela, un os ou des petites gateries?). Vous avez a peine vu le temps passer, il est maintenant midi, vous avez faim et vous vous dirigez vers le macdo pour vous commander un big mac en réfléchissant a vos choix de vie."
chienreprimander = [textchienreprimander]

#---3 layer
textchienwoof = "Vous croyez avoir utilisé la bonne grammaire, mais vous n'êtes pas 100% sure. Le chien vous regarde d'un air satisfait, vous venez de répondre parfaitement a sa question, et puis vous comprenez qu'il vous testait. Le chien vous pose alors la question pour laquelle il était venu aujourd'hui: 'wouf wuif... waf wif grr, wawaf wrouh 'MIOOWWWW', wouf wouf wah wuff woo?'\n\nQue faites-vous?"
chienwoof1 = "L'encourager"
chienwoof2 = "Le rassurer"
chienwoof3 = "Le réprimander"

chienwoof = [textchienwoof, chienwoof1, chienwoof2, chienwoof3]


#--2 layer
textchien = "Le chien entre dans votre tente, vous êtes un peu confuse, vous lui dites de s'asseoir (vous êtes fluente en chien, mais ca fait un bail alors vous êtes un peu rouillée). Le chien s'asseoit, et il vous demande: 'Wouf wouf wrouf warf waf wif rrwar wuif?'\n\n Que lui répondez-vous?"
chien1 = "'Wraf wif waf wuff wraf wouf rrr wah rwaf grraw'"
chien2 = "'rrr wouf wif wif grr wouf arw wruif awouu waf'"
chien3 = "wouf"

chienclient3 = [textchien, chien1, chien2, chien3]



#=====CLIENTS=====#

#-1 layer
text1 = "Vous arrivez a votre tente de divination au milieu d'un petit centre d'achat, juste a coté du dollarama (pour attirer toutes les superstitieuses qui magasinnent là bas). Vous avez une petite file qui vous attend devant votre tente, deux personnes et un chien (?).\n\nQui faites-vous entrer en premier?"
client1 = "Martine (une habituée)"
client2 = "Devin (un nouveau)"
client3 = "Le chien (???)"

lvl1 = [text1, client1, client2, client3]





#definition des fonctions du jeu

#petite fonction de print, seulement utlisée pour "l'animation" de "loading" dans le jeu
def print_par_lettre(text):
    """ 
    Petite fonction pour print des caracteres les uns apres les autres
    Inputs: strings de text courts (certains problemes de formattage, seulement utiliser avec des petites strings)
    Outputs: la meme string qu'a l'input, mais écrit caractere par caractere avec un délai
    """
    for caracteres in text:
        print(f"{caracteres}", end="", flush=True)
        time.sleep(0.4) #changer a 0.008s pour des strings plus longues
    print("\n\n")



#fonction pour demander au jouer s'il est pret a commencer le jeu
def start_game():
    """
    Fonction pour confirmer le début du jeu avec un input du joueur
    Inputs: confirmation du joueur par un input de y ou n
    Outputs: strings de texte
    """
    while True:
        start_confirmation = input("Pret a jouer? (y/n) ")
        if start_confirmation == "y":
            print_par_lettre(".....") #fonction utilisée ici pour le "loading"
            break
        elif start_confirmation == "n":
            print("Ah bon, au revoir alors")
            time.sleep(1.5)
        else:
            print("? ? ?")
            time.sleep(1.5)



#Fonction pour detecter la fin d'une branche
def failstate_detect(niveau_selectionne):
    """
    Fonction pour vérifier si le prochain choix du joueur sera son dernier dans chaque branche de l'arbre
    Inputs: variable du niveau actuel contenant une liste de choix (ou pas)
    Outputs: retour au début du jeu ou continution du jeu
    """
    while True:
        fail_check = len(niveau_selectionne)
        if fail_check > 1:
            break
        else:
            print(f"\n{niveau_selectionne[0]}")
            time.sleep(1.5)
            while True:
                print(jeu_fin)
                start_confirmation = input("\nVoulez vous retourner au début de la journée? (y/n) ")
                if start_confirmation == "y":
                    print(choix_retour)
                    time.sleep(1)
                    print_par_lettre(".....")
                    time.sleep(0.5)
                    loop_niveau(lvl1)
                elif start_confirmation == "n":
                    print("\nAh bon, au revoir alors (vous pouvez maintenant fermer le jeu)")
                    time.sleep(1.5)
                else:
                    print("\n? ? ?")
                    time.sleep(1)



#module d'extraction d'information de niveau + formattage pour fiter dans le terminal, à utiliser en duo avec la prochaine fonction
def level_extractor(niveau_selectionne):
    """
    Fonction d'extraction et de formattage du texte et des options possible d'une variable de niveau
    Inputs: output de la derniere fonction, soit une variable de niveau avec une liste de choix
    Outputs: variables pour chaque choix et le texte du niveau, formattés pour ne pas séparer un mot en deux
    """
    situation0 = textwrap.fill(niveau_selectionne[0], width = 140)
    choix1 = textwrap.fill(niveau_selectionne[1], width = 140)
    choix2 = textwrap.fill(niveau_selectionne[2], width = 140)
    choix3 = textwrap.fill(niveau_selectionne[3], width = 140)

    return situation0, choix1, choix2, choix3



#module de présentation des choix, utiliser avec la fonction ci dessus
def presentation_choix(situation0, choix_1, choix_2, choix_3):
    """
    Fonction qui formatte le texte et les choix d'un niveau en liste lisible et claire, puis demande une question a l'utilisateur
    Inputs: Output de la derniere fonction, soit les variables pour chaque choix et le texte formattés
    Outputs: Liste formattée de la situation et des choix possibles sur le terminal, et une variable de réponse au choix en int
    """
    time.sleep(0.5)
    print(f"\n{situation0}\n")
    time.sleep(1.5)
    print(f"1: {choix_1}\n")
    time.sleep(0.5)
    print(f"2: {choix_2}\n")
    time.sleep(0.5)
    print(f"3: {choix_3}\n")
    time.sleep(0.5)
    reponse = int(input("Quel est votre choix? "))
    return reponse



#module d'assignation de valeur au résultat du choix, prends le résultat de la fonction ci dessus et lui assigne une valeur fixe
def resultat_choix(reponse):
    """
    Fonction d'assignation de valeur au résultat du choix fait a la fonction plus haut
    Inputs: réponse en int a la question posée par la fonction ci dessus
    Output: Chiffre en int entre 0 et 4 dans une variable
    """
    if reponse == 1 or reponse == 2 or reponse == 3 or reponse == 0:
        choix_final = reponse
    else:
        choix_final = 4
    
    return choix_final



#combinaison de toutes les fonctions ci dessus sauf les 2 premieres, + fonction de "looping" du code au cas ou la réponse n'est pas valide 
def loop_niveau(input_niveau):
    """
    Fonction combinant presque toutes les fonctions ci dessus afin de les mettre dans une "loop" qui valide que le choix du joueur est valide
    et répete cette boucle jusqu'a ce que le joueur entre une réponse valide.
    Inputs: Variable de niveau
    Output: Variable pour déterminer le prochain niveau
    """
    while True:
        failstate_detect(input_niveau)
        situation0, choix1, choix2, choix3 = level_extractor(input_niveau)
        reponse_user = presentation_choix(situation0, choix1, choix2, choix3)

        verif_reponse = resultat_choix(reponse_user)
        if verif_reponse == 4:
            print(choix_fail)
            time.sleep(1.5) #retour aux choix
        elif verif_reponse == 0:
            confirmation = input("Voulez vous vraiment retourner au début de la journée? (y/n) ")
            if confirmation == "y":
                print(choix_retour)
                time.sleep(1)
                print_par_lettre(".....")
                time.sleep(0.5)
                loop_niveau(lvl1) #retour au niveau1
            elif confirmation == "n":
                print("continuons alors...\n")
                time.sleep(1.5) #retour aux choix
            else:
                print("Bon, tu parles chinois maintenant, j'imagine que ca veut dire 'on continue' alors...\n")
                time.sleep(1) #retour aux choix
        elif verif_reponse != 4:
            prochain_niveau = verif_reponse #donner l'indication pour le prochain niveau
            break

    return prochain_niveau





#début du code du jeu

fmise_en_contexte = textwrap.fill(mise_en_contexte, width = 140) #simple formattage
print(f"{fmise_en_contexte}\n\n\n")
time.sleep(1.5)

print(regles_instructions)
time.sleep(1.5)

start_game() #commencement du jeu si le joueur entre "y"

niveau = loop_niveau(lvl1) #début du niveau 1


#suite de if pour passer a chaque prochain niveau
#la position de ligne en ligne de "if niveau" forme un sinus verticale! C'est de l'art!!
if niveau == 1:
    niveau = loop_niveau(martineclient1)#option 1 lvl1
    if niveau == 1:
        niveau = loop_niveau(martinechance)
    elif niveau == 2:
        niveau = loop_niveau(martinemalchance)
        if niveau == 1:
            niveau = loop_niveau(martinebain)
        elif niveau == 2:
            niveau = loop_niveau(martineesprits)
        elif niveau == 3:
            niveau = loop_niveau(martinefil)
    elif niveau == 3:
        niveau = loop_niveau(martinelesdeux)
        if niveau == 1:
            niveau = loop_niveau(martinenormal)
        elif niveau == 2:
            niveau = loop_niveau(martineverite)
        elif niveau == 3:
            niveau = loop_niveau(martinedouter)
elif niveau == 2:
    niveau = loop_niveau(devinclient2)#option 2 lvl1
    if niveau == 1:
        niveau = loop_niveau(devinjeux)
        if niveau == 1:
            niveau = loop_niveau(devined6)
        elif niveau == 2:
            niveau = loop_niveau(devinbb2)
        elif niveau == 3:
            niveau = loop_niveau(devinhl3)
    elif niveau == 2:
        niveau = loop_niveau(devinamour)
        if niveau == 1:
            niveau = loop_niveau(devinlove)
            if niveau == 1:
                niveau = loop_niveau(devingoodending)
            elif niveau == 2:
                niveau = loop_niveau(devinbadending)
            elif niveau == 3:
                niveau = loop_niveau(devindepressed)
        elif niveau == 2:
            niveau = loop_niveau(devinnolove)
        elif niveau == 3:
            niveau = loop_niveau(devindevier)
            if niveau == 1:
                niveau = loop_niveau(devintarot)
            elif niveau == 2:
                niveau = loop_niveau(devinlignes)
            elif niveau == 3:
                niveau = loop_niveau(devinthe)
    elif niveau == 3:
        niveau = loop_niveau(devinnom)
        if niveau == 1:
            niveau = loop_niveau(devindevin)
            if niveau == 1:
                niveau = loop_niveau(devinrepete)
            elif niveau == 2:
                niveau = loop_niveau(devinexcuse)
            elif niveau == 3:
                niveau = loop_niveau(devinriendire)
        elif niveau == 2:
            niveau = loop_niveau(devinriche)
        elif niveau == 3:
            niveau = loop_niveau(devinspecial)
elif niveau == 3:
    niveau = loop_niveau(chienclient3)#option 3 lvl1
    if niveau == 1:
        niveau = loop_niveau(chienwraf)
        if niveau == 1:
            niveau = loop_niveau(chienhocher)
        elif niveau == 2:
            niveau = loop_niveau(chiensecouer)
        elif niveau == 3:
            niveau = loop_niveau(chienrien)
    elif niveau == 2:
        niveau = loop_niveau(chienrrr)
    elif niveau == 3:
        niveau = loop_niveau(chienwoof)
        if niveau == 1:
            niveau = loop_niveau(chienencourager)
        elif niveau == 2:
            niveau = loop_niveau(chienrassurer)
        elif niveau == 3:
<<<<<<< HEAD
            niveau = loop_niveau(lvl1_3_3_3)
=======
            niveau = loop_niveau(chienreprimander)
>>>>>>> main
