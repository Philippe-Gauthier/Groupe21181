# Read Me Plan Work In Progress


Entrées: Imputs par le terminal, soit des mots (oui, non, etc), soit des chiffres pour selectionner une option


Sorties: tout se fait a partir du terminal. le logiciel va afficher du texte selon ce que l'on imput dans le terminal, après avoir affiché le résultat, il y aura toujours des instructions ou des options qui seront données a l'utilisateur pour savoir comment continuer


controle: structure en arbre, un seul chemin valide pour se rendre a chaque résultat, et non une infinité de chemins possibles. il y aura toujours une facon de retourner a l'étape précédente en rentrant un mot ou un chiffre dans le terminal, 


Vous etes une voyante mais votre boule de crystal est brisée, inventez le futur de vos clients







# NE PAS LIRE PLUS BAS POUR NE PAS SE SPOILER #




# notes

Mini tutoriel en imput avec une option: start

minimum 50 choix pour l'arbre


Premiere option:
Quel client prendre en premier:
- Martine 
- Serge
- Devin


futurs par client:
Martine:
- Martine rentre dans votre tente, c'est une femme un peu plus agée que vous, mais pas de beaucoup, c'est votre cliente la plus loyale. Elle vous demande de lui dire sa chance pour la semaine ou de lui dire si sa santé sera bonne dans les prochaines années.
  - Chance
    - chance: Vous lui dites qu'elle sera très chanceuse dans les prochaines semaines, l'étoile Véga lui est favorable, vous lui recommendez meme d'acheter un billet de lotterie quelcoque
      - lotterie (tu gagne en volant le billet gagnant) - 
    - Malchance - lotterie (tu te fais voler le billet gagnant) -
  - Santé



Serge:
- Serge rentre dans votre tente, c'est un homme d'a peu près votre age. Il s'assoit devant vous et votre boule de crystal et vous demande si vous pouvez lui dire si le Canadien va gagner le match de ce soir contre les Bruins
  - Oui: Serge dit "Yes! jvais parier gros dessus ce soir debord" Vous soupirez, vous savez qu'il aurait parié sur le match peu importe ce que vous auriez dit
  - Non: Serge dit "Shit, j'ai deja parié 417 piasses sur le Canadien" Vous soupirez, Serge est clairement décu, mais il n'apprendra pas sa lecon, vous le savez, car Serge revient ici a chaque match de hockey, il ne gagne jamais ses paris, que votre boule de crystal soit brisée ou pas. Serge vous demande ensuite si vous savez si les hotdogs du Costco vont monter de prix dans les prochaines années.
    - Oui
    - Non
  




Devin: 
- Votre premier client de la journée rentre dans votre tente, c'est un jeune homme d'environ vingt-trente ans, il vous donne son nom: Devin. Devin vous demande si vous pouvez lui parler de son futur amoureux ou du futur des jeux videos (vous ne conaissez rien aux jeux videos, ca commence bien la journée...).
  - jeux videos: vous lui dites que l'amour est difficile a lire en ces temps incertains (l'ombre de vénus vous bloque la vue) mais que vous voyez clairement le futur des jeux videos. Soudainement tout excité, Devin vous demande avec passion quel jeu sortira le premier.
    - Elder Scrolls 6: Vous lui dites qu'Elder Scrolls 6 sortira avant les autres, mais qu'il sera décevant après toute cette attente. Vous voyez qu'il est décu de votre réponse, il dit "vous ne connaissez rien sur ce sujet, vous etes une fraude!". Il part en vous payant en dessous de votre taux habituel. Vous continuez a fixer la sortie de votre tente pour quelques secondes avant de vous dire que vous etes trop vieille pour faire ce travail et que vous devriez prendre votre retraite.
    - Bloodborne 2: vous lui dites que vous n'etes pas sur quel jeu sortira en premier, mais vous lui dites avec certitude que Bloodborne 2 ne sortira jamais. Son visage s'affaisse, il sort son portefeuille, vous paye, et s'en va. Vous venez de perdre un futur client.
    - Half-Life 3: vous lui dites que Half-Life 3 sortira le premier, et de plus, ce sera plus tot qu'il l'esperait! Devin sourit, et vous paye généreusement. Vous vous etes fait un nouveau client régulier.
  
  - Amour: Vous lui dites que le futur en termes de sorties de jeux est assez flou ce matin (mercure retrograde) mais vous voyez clairement son futur amoureux. Il vous demande de lui en dire plus.
    - amour: Vous lui dites qu'il va rencontrer tres bientot l'amour de sa vie, vous le voyez clairement dans votre boule de crystale (brisée, mais vous ne mentionnez pas cela). Il vous supplie de lui en dire plus.
      - good ending: vous lui dites qu'il va vivre une tres belle vie, qu'il aura des enfants, et que ses enfants auront des enfants, et qu'il allait mourrir paisiblement main dans la main avec sa femme. Il vous fait un drole de visage, puis vous revele alors qu'il est homosexuel. Il vous traite d'homophobe, et il part sans payer. Vous aviez besoin de cet argent pour votre abonnement netflix sans pubs, vous tombez donc dans la depression
      - bad ending: vous lui dites que les apparences sont trompeuse, et qu'il finira par se divorcer, et de tomber dans l'alcoolisme. Il vous regarde d'un regard vide, et puis il vous remercie de l'avoir prévenu. Il part apres avoir payé pour votre service, vous vous sentez mal de détruire les espoirs d,un si jeune homme mais vous vous dites que c'est pour le plus grand bien (pouvoir vous payer votre abonnement amazon prime pour la livraison gratuite).
    - pas d'amour: Vous lui dites qu'il n'aura tristement pas la chance de vivre l'amour dans sa vie, mais c'est l'opportunité pour lui de se consacrer a d'autres passions, telles que le pickle ball professionnel. Vous voyez Devin s'affaisser un peu, puis il se leve, et quitte. Vous croyez entendre des pleurs venant de l'exterieur de votre tente. Vous realisez alors qu'il ne vous a pas payé, vous aviez besoin de l'argent pour payer votre spotify premium, vous tombez donc en depression nerveuse.


  


idées de futurs possibles: 
- santé/pas santé - maladies possibles

- riche - quelle marque de voiture tu possede - est ce que tu es genereux ou pas
- pauvre - quelle marque de voiture te donne en general le plus d'argent dans ton verre tim hortons
- voyages










# Fonctions

Fonction pour afficher le résultat d'un choix en page de texte (la page correspondante)
entrée: input de choix dans le terminal
sortie: texte dans le terminal
