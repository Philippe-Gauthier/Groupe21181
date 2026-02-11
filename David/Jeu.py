
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
Question_2_choix_1 = "Brésilienne\
    :Tu viens du pays du jogo bonito. Formé sur les terrains de terre battue,\
    tu as la magie brésilienne dans les pieds. Dribble, technique pure, créativité.\
    Ronaldo Nazário est ton idole, le Phénomène qui a conquis le monde avec son talent et sa détermination."
Question_2_choix_2 = "Portugaise\
    :Tu es Portugais, d'un pays où le football est une religion. La passion et la garra te définissent. \
    Cristiano Ronaldo, CR7, est ta référence : travail acharné, ambition sans limite, volonté de fer.\
    Tu rêves de suivre ses traces"
Question_2_choix_3 = "Espagnole\
    :Tu viens d'Espagne, terre de tiki-taka et de possession. \
    Andrés Iniesta t'a inspiré : élégance, intelligence de jeu, humilité. \
    Tu as appris que la beauté du football réside dans le collectif et la précision"
Question_2_choix_4 ="Anglaise \
    :Tu es Anglais, forgé par la passion intense de la Premier League. David Beckham est ton modèle. \
     travail, précision, leadership. Ses coups francs légendaires et son professionnalisme t'ont montré le chemin vers l'excellence."

# 2 premiers choix son pour Brésil, 2 après Portugal, 2 après Espagnole et 2 dernier Angleterre
Question_3 = "Ton agent pose deux dossiers devant toi. deux clubs veulent te signer.\
    Tu dois choisir ton premier contract"

Question_3_choix_1 ="PALMEIRAS 30 000€/semaine pour 3 ans - Rôle : Titulaire assuré \
    . Allianz Parque, passion intense, champion d'Amérique du Sud. Titulaire garanti, tremplin idéal pour l'Europe. \
    L'ambiance brésilienne au quotidien."
Question_3_choix_2 ="FLAMENGO 35 000€/semaine pour 3 ans - Rôle  : Titulaire assuré, \
    le plus populaire du Brésil. Maracanã mythique, 40 millions de supporters. Titulaire assuré, pression énorme \
    mais exposition maximale en Amérique du Sud."
Question_3_choix_3 ="SPORTING LISBONNE 25 000€/semaine pour 3 ans - Rôle : Titulaire assuré  \
    L'académie qui a formé Ronaldo. Salaire modeste, mais tu seras titulaire dès le début. Temps de jeu maximal pour te développer."
Question_3_choix_4 ="REAL MADRID 100 000€/semaine pour 3 ans - Rôle : Réserviste Le géant blanc. \
    Santiago Bernabéu, 80 000 fans, salaire de star. Mais tu seras réserviste avec peu de temps de jeu au début. La concurrence est féroce."
Question_3_choix_5 ="VILLARREAL 75 000€/semaine pour 3 ans - Rôle : Titulaire assuré. \
    Excellent salaire et statut de titulaire garanti. Développement optimal et confiance du club dès le premier jour."
Question_3_choix_6 ="ASTON VILLA 50 000€/semaine pour 3 ans - Rôle : Titulaire Premier League.\
      Salaire correct, statut de titulaire. Exposition mondiale immédiate et compétition intense chaque semaine."
Question_3_choix_7 ="MANCHESTER UNITED 75 000€/semaine  pour 3 ans - Rôle : Remplaçant\
      Old Trafford. Excellent salaire, club mythique de Premier League. Tu seras remplaçant avec des opportunités régulières de prouver ta valeur."
Question_3_choix_8 ="BAYERN MUNICH 90 000€/semaine pour 3 ans - Rôle : Remplaçant. \
     Allianz Arena, excellence allemande, domination en Bundesliga. Très bon salaire mais tu seras remplaçant. Formation rigoureuse et professionnalisme absolu."


"""
#Ce qui arrive au joueur quand il choissisent leur contract/ mise en scène (premier match)

if(choix_joueur == 1):
    print("")

elif(choix_joueur ==2 ):
    print("")        
else(choix_joueur == 3):
    print("")   

else(choix_joueur == 8):
print("À domicile: stade Allianz Arena - Jour 1 de la Bundesliga.Tu entres à la mi-temps. 63e minute\
     passe décisive parfaite, ton coéquipier marque ! Victoire 3-0. Le coach allemand te fait un signe approbateur")

"""
# Les 2 premier sont si tu as choisis Palmeiras,après Flamengo, Sporting, Real, Villarreal, Aston, Man utd et Bayern
Question_4 = "Les tranferts d'hivers sont arrivés. Ton club va te proposer 2 choix. À toi de choisir."
contexte_palmeiras ="Tu es un itulaire indiscutable, 16 buts, idole des supporters.\
    Le président te parle franchement: Tu es notre joyau. Mais l'Europe t'appelle. Benfica veut te recruter. C'est à toi de décider."
Question_4_choix_1 ="Rester à Palmeiras - Héros du club, confort, mais tu retardes ton passage en Europe"
Question_4_choix_2 ="Benfica - 12M€ - 40k€/semaine, Ligue des Champions, tremplin européen, titulaire assuré"

contexte_flamengo ="Star de l'équipe,  buts, adoré au Maracanã.Ton agent débarque avec une grosse nouvelle.\
      Le FC Porto veut t'acheter. Flamengo ne veut pas te laisser partir maintenant, mais c'est ta décision."
Question_4_choix_3 ="Rester à Flamengo - Continuer à dominer au Brésil, gloire locale assurée"
Question_4_choix_4 ="FC Porto - 18M€ - 55k€/semaine, Ligue des Champions, club formateur, titulaire probable"

contexte_sporting = "Tu es incroyable , 8 buts en 18 matchs.Ton téléphone explose. Ton agent est excité : 1 grand club veut te prendre en prêt maintenant !\
      Le Sporting ne veut pas te vendre, mais ils ne peuvent pas refuser certaines offres."
Question_4_choix_5 ="Rester au Sporting - Continuer ton excellente progression, stabilité"
Question_4_choix_6 ="Naples prêt - 30M€ - Serie A, 45k€/semaine, titulaire probable, style de jeu technique"

contexte_real ="Tu n'as toujours pas joué depuis le début de saison. Ton agent t'appelle.\
      Le Real veut te prêter six mois pour que tu aies du temps de jeu."
Question_4_choix_7 ="Rester au Real Madrid - Continuer à t'entraîner avec les meilleurs, mais rester sur le banc"
Question_4_choix_8 ="Prêt à Getafe - La Liga, titulaire garanti, club modeste mais du temps de jeu précieux"

contexte_villareal = "Tu as bien progressé, quelques entrées en jeu. Le directeur sportif te convoque. On est contents de toi.\
      Mais Séville veut t'acheter. Ils offrent 15 millions et te garantissent d'être titulaire."
Question_4_choix_9 ="Rester à Villarreal - Tu connais le club, bonne progression, patience nécessaire"
Question_4_choix_10 ="Partir à Séville - Plus gros club, titulaire garanti, meilleure exposition européenne"

contexte_aston = "L'entraineur est fier de toi tu joues bien, mais il y a un autre joueur qui joue a ta place. \
    Il te propose de changer de position alors tu pourras devenir titulaire ou de garder ton poste et être remplaçant. \
    Il croit en toi dans l'autre position"
Question_4_choix_11 ="Tu changes de poste"
Question_4_choix_12 ="Tu garde ton poste et tu es remplaçant"

conexte_man_Utd = "Tu as joué 12 matchs depuis la blessure du titulaire, performances correctes Le coach te convoque.\
    Le titulaire revient le mois prochain. Je suis désolé de t'annoncer ceci, mais tu n'es plus dans les plans de l'entraineur. \
    On va te vendre il y a deux équipes intéresser en toi. On te laisse le choix de choisir laquelle tu veux "
Question_4_choix_13 ="Newcastle - Premier League, titulaire assuré, projet ambitieux"
Question_4_choix_14 ="Atlético Madrid - 25M€ - 80k€/semaine, La Liga, remplaçant mais gros club"

contexte_bayern = "Quelques belles entrées, 8 passes décisives. Le directeur sportif te rencontre : \
    On veut prolonger ton contrat de 2 ans. Même salaire (90k€/sem), mais tu restes dans notre projet.\
     Par contre, Dortmund veut t'acheter."
Question_4_choix_15 ="Prolonger au Bayern - Sécurité, meilleure formation, mais toujours remplaçant"
Question_4_choix_16 ="Dortmund - 20M€ - 70k€/semaine, titulaire probable, club formateur de jeunes"


Question_5 = "Qu'est-ce qui t'arrive dans ton équipe? que vas tu faire ? "
Question_5_choix_1 =""
Question_5_choix_2 =""
Question_5_choix_3 =""
Question_5_choix_4 =""
Question_5_choix_5 =""
Question_5_choix_6 =""
Question_5_choix_7 =""
Question_5_choix_8 =""
Question_5_choix_9 =""
Question_5_choix_10 =""
Question_5_choix_11 =""
Question_5_choix_12 =""
Question_5_choix_13=""
Question_5_choix_14=""
Question_5_choix_15 =""
Question_5_choix_16 =""
Question_5_choix_17 =""
Question_5_choix_18 =""
Question_5_choix_19 =""
Question_5_choix_20 =""
Question_5_choix_21 =""
Question_5_choix_22 =""
Question_5_choix_23 =""
Question_5_choix_24 =""
Question_5_choix_25 =""
Question_5_choix_26 =""
Question_5_choix_27 =""
Question_5_choix_28 =""
Question_5_choix_29 =""
Question_5_choix_30 =""
Question_5_choix_31 =""
Question_5_choix_32 =""







































"""
def formater_question(Titre, Introduction):
    page = f"Vous devez répondre à la question suivante:{Titre}"
    page = page +"/n" +"____________________________________"
    page = page +"/n" +"vous devez choisir parmis ces choix"
    page = page +Introduction
    return page 

choix = input(formater_question(Choix_1, Choix_1_rep_1, Choix_1_rep_2))
"""