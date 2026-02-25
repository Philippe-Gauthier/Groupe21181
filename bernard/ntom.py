"""NOM: NTOM BERNARD
PROJET1: examen de revision pour son cours d'electronique
partie_1 de l'examen de revision en electronique"""

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
reponse("filtrer les hautes frequences", "filtrer les bases frequences", "redresser un courant", "2")

print("La loi d_Ohm s_écrit")
reponse("P=U⋅IP=U⋅I", "U=R⋅IU=R⋅I", "R=P/IR=P/I", "2")

print("Dans un circuit série, le courant est")
reponse("Le même dans tous les composants","Différent dans chaque résistance","Nul dans le premier composant")

print("Dans un circuit parallèle la tension aux bornes de chaque branche est")
reponse("Nulle","La même","Proportionnelle au courant")

print("La puissance électrique instantanée s’exprime par")
reponse("P=U/IP=U/I","P=U⋅IP=U⋅I","P=U2/RP=U2/R")

print("Un générateur idéal de tension")
reponse("A une résistance interne nulle","A une résistance interne infinie","Ne peut pas fournir de courant")

print("Une diode idéale en polarisation directe")
reponse("Bloque totalement le courant","Laisse passer le courant sans chute de tension","Laisse passer le courant avec une petite chute de tension")

print("La tension de seuil approximative d’une diode silicium est")
reponse("0,1 V","0,3 V","0,7 V")

print("Une diode Zener est utilisée principalement pour")
reponse("Redresser un courant alternatif","Limiter une tension","Filtrer un signal")

print("Dans un pont de Graetz, le nombre de diodes utilisées est")
reponse("2","3","4")

print("Un redresseur double alternance par pont de diodes fournit")
reponse("Une tension purement continue","Une tension pulsée de même fréquence que le réseau","Une tension pulsée de fréquence double du réseau")

"""PARTIE: TRANSISTORS BIPOLAIRE"""

print("Un transistor bipolaire NPN correctement polarisé en régime linéaire a")
reponse("Jonction base-émetteur bloquée","Jonction base-émetteur passante","Jonction base-collecteur passante")

print("Le transistor BJT peut être utilisé comme")
reponse("Résistance pure","Commutateur ou amplificateur","Transformateur")

print("Dans un transistor NPN en mode actif")
reponse("Le courant de collecteur est approximativement égal au courant d’émetteur","Le courant de base est beaucoup plus grand que le courant de collecteur","Il n’y a pas de courant de base")

print("Le gain en courant d’un transistor BJT est généralement noté")
reponse("αα","ββ","γγ")

print("Un transistor saturé se comporte approximativement comme")
reponse("Un interrupteur ouvert","Un interrupteur fermé","Un condensateur")

"""PARTIE: Amplificateurs opérationnels (AOP)"""

print("Un amplificateur opérationnel idéal a")
reponse("Gain infini et résistance d’entrée infinie","Gain nul et résistance d’entrée nulle","Gain fini et résistance d’entrée nulle")

print("Un montage suiveur de tension (AOP) a un gain en tension de")
reponse("0","0,5","1")

print("Un AOP saturé")
reponse("Fonctionne en régime linéaire","Donne une sortie proche des rails d’alimentation","A une sortie toujours nulle")

print("Le montage inverseur avec AOP donne une sortie")
reponse("En phase avec l’entrée","En opposition de phase avec l’entrée","Toujours positive")

print("Dans un comparateur à AOP sans hystérésis, un faible bruit sur l’entrée")
reponse("N’a aucun effet","Peut provoquer de multiples commutations","Augmente le gain")

"""PARTIE: FILTRES ET REGIMES SINUSOIDAL"""

print("Un filtre passe-bas RC du premier ordre")
reponse("Laisse passer les hautes fréquences","Atténue les basses fréquences","Laisse passer les basses fréquences et atténue les hautes")

print("La fréquence de coupure d’un filtre RC passe-bas est donnée par")
reponse("fc=1/(2πRC)fc=1/(2πRC)","fc=2πRCfc=2πRC","fc=R/Cfc=R/C")

print("Le déphasage d’une résistance pure en régime sinusoïdal est")
reponse("0°","90°","-90°")

print("Dans une bobine idéale en régime sinusoïdal, le courant est")
reponse("En phase avec la tension","En avance de 90° sur la tension","En retard de 90° sur la tension")

print("La puissance active dans un circuit purement inductif est")
reponse("Nulle","Maximale","Égale à la puissance apparente")

"""PARTIE: ELECTRONIQUE NUMERIQUE"""

print("Une porte logique ET (AND) a une sortie à 1")
reponse("Si au moins une entrée est à 1","Si toutes les entrées sont à 1","Si toutes les entrées sont à 0")

print("Une porte logique OU (OR) a une sortie à 0")
reponse("Si toutes les entrées sont à 1","Si au moins une entrée est à 1","Si toutes les entrées sont à 0")

print("La porte NON (NOT) réalise")
reponse("L’addition logique","La multiplication logique","L’inversion logique")

print("Une porte NAND est équivalente à")
reponse("NOT suivi de OR","NOT suivi de AND","AND suivi de NOT")

print("Une bascule D (flip-flop D)")
reponse("Mémorise","l’état de l’entrée D à chaque front d’horloge","Inverse son état à chaque impulsion")

print("La valeur efficace d’une tension sinusoïdale de 230 V correspond à une amplitude crête d’environ")
reponse("115 V","230 V","325 V")

print("Un transformateur abaisseur 230 V / 12 V")
reponse("Augmente la tension","Diminue la tension","Ne modifie pas la tension")

print("Pour décharger un gros condensateur en sécurité, on utilise")
reponse("Un court-circuit direct","Une résistance de forte valeur","Une diode")

print("La soudure de composants sensibles (CMOS) nécessite")
reponse("Une température illimitée","Une protection contre l’électricité statique","Un courant très élevé")

print("Un circuit imprimé (PCB) sert principalement à")
reponse("Stocker des données","Assurer les connexions électriques entre composants","Mesurer la tension")

"""PARTIE : BONUS"""

print("l'unite de l'ampere")
reponse("A","V","W")

print("le symbole de la volmetre")
reponse("V","R","A")

print("le symbole de l'unite de la puissance")
reponse("W","I","P")

print("le symbole de l'unite du farad")
reponse("F","D","A")

print("le symbole de l'unite de la frequence")
reponse("HZ","R","W")

print("l' unite de la reactance")
reponse("ohm","farad","volt")

print("le role du multimetre")
reponse("prendre des mesures","court-circuite","coupe le circuit")
        
print("le role du volmetre")
reponse("mesure de la tension","mesure du courant","mesure de la resistance")
print("le role du capteur")
reponse("detecter","mesure","bloquer")

print("le role du generateur de courant")
reponse("fournir un courant","bloquer le ciruit","bruler les equipements")