
Titre = "L'ascension d'une étoile "

Introduction = "Tu as 17 ans et ce jour est celui que tu attends depuis toujours. " \
"Après des années d'entraînement, de sacrifices et de détermination, tu te tiens au seuil de ton rêve : \
devenir footballeur professionnel. Les recruteurs t'ont remarqué, les portes s'ouvrent, et ton destin est sur le point de basculer.\
    Mais avant tout, qui es-tu vraiment ?"

Question_1 = "quelle est ton poste sur le terrain"  
Question_1_choix_1 = "Attaquant : Tu es un finisseur né. Vitesse, instinct, sang-froid devant le but. Tu vis pour marquer et faire exploser les stades."
Question_1_choix_2 ="Milieu de terrain : Tu es le maestro. Vision du jeu, passes décisives, contrôle du tempo. Tu orchestres chaque attaque."


# Les 2 premiers sont pour le choix1(attaquants) et les 2 autres choix 2(millieu de terrain)
Question_2 = "Quelle est ta nationalité"
Question_2_rep_1 = "Brésilienne\
    :Tu viens du pays du jogo bonito. Formé sur les terrains de terre battue,\
      tu as la magie brésilienne dans les pieds. Dribble, technique pure, créativité.\
      Ronaldo Nazário est ton idole, le Phénomène qui a conquis le monde avec son talent et sa détermination."
Question_2_rep_2 = "Portugaise\
    :Tu es Portugais, d'un pays où le football est une religion. La passion et la garra te définissent. \
    Cristiano Ronaldo, CR7, est ta référence : travail acharné, ambition sans limite, volonté de fer.\
      Tu rêves de suivre ses traces"
Question_2_rep_3 = "Espagnole\
    :Tu viens d'Espagne, terre de tiki-taka et de possession. \
    Andrés Iniesta t'a inspiré : élégance, intelligence de jeu, humilité. \
    Tu as appris que la beauté du football réside dans le collectif et la précision"
Question_2_rep_4 ="Anglaise \
    :Tu es Anglais, forgé par la passion intense de la Premier League. David Beckham est ton modèle. \
        travail, précision, leadership. Ses coups francs légendaires et son professionnalisme t'ont montré le chemin vers l'excellence."

# 2 premiers choix son pour Brésil, 2 après Portugal, 2 après Espagnole et 2 dernier Angleterre
Question_3 = "Ton agent pose deux dossiers devant toi. deux clubs veulent te signer.\
    Tu dois choisir ton premier contract"











print (Titre)
print(Introduction)

"""
def formater_question(Titre, Introduction):
    page = f"Vous devez répondre à la question suivante:{Titre}"
    page = page +"/n" +"____________________________________"
    page = page +"/n" +"vous devez choisir parmis ces choix"
    page = page +Introduction
    return page 

choix = input(formater_question(Choix_1, Choix_1_rep_1, Choix_1_rep_2))
"""