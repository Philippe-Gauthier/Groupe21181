print ("CHOISISSEZ VOTRE ADVERSAIRE!")

print ("A) Donald Trump")
print ("B) Adolph Hitler")
print ("C) Phillipe Gauthier")

reponse = input("votre réponse : ").upper()




if reponse == "A":
    print ("VOUS AVEZ CHOISI DONALD TRUMP. choisissez votre arme")

    print ("A) un bâton")
    print ("B) le wokisme")
    print ("C) une bombe atomique")
    
    reponse_trump_1 = input("votre réponse : ").upper()

    if reponse_trump_1 == "A":
        print ("vous avez frappé Donald Trump avec un bâton. Il à la gentillesse de vous offrir un aller simple pour visiter le titanic.")
        print ("N'oubliez pas la manette de PS3. mauvaise fin.")
    
    if reponse_trump_1 == "B":
        print ("vous avez essayé de combattre Donald Trump avec le wokisme") 
        print ("Malheureusement, il ne comprend pas ce concept et vous envoie en prison pour 20 ans.")
        print ()
        print ("Vous êtes maintenant en prison. que voulez-vous faire?")
        print ("A) vous l'avez mérité. c'était stupide de s'attaquer au futur Furheur. vous restez en prison.")
        print ("B) vous essayez de vous échapper.")
        print ("C) vous essayez d'amadouer un garde")

        reponse_trump_2 = input("votre réponse : ").upper()

        if reponse_trump_2 == "A":
             print ("vous avez attendu en prison. vous avez gâché 20 ans de votre vie.")
             print("Trump est maintenant mort et vous n'avez rien accomplis de plus. Mauvaise fin")
        if reponse_trump_2 == "B":
             print ("vous voulez vous échapper. vous regardez autour de vous. que faites-vous?")
             print ("A) vous prenez votre compagnon de cellule comme bouclier humain.")
             print ("B) vous utilisez vos pouvoirs psychiques pour attirer le garde vers vous.")
             print ("C) vous voyez une pelle.")
             reponse_trump_2b = input ("votre réponse : ").upper()
             if reponse_trump_2b == "A":
                  print ("vous vous rendez compte que les guardes n'ont pas d'armes et vous plaque au sol.")
                  print ("vous finissez avec une sentence de prison à vie pour votre stupidité")
             if reponse_trump_2b == "B":
                  print ("vous n'avez pas de pouvoir psychiques.")
                  print("le garde vous prend pour un fou et vous envoie en asile psychiatrique. mauvaise fin")
             if reponse_trump_2b =="C":
                  print("vous trouvez une pelle sur le sol. que faites-vous?")
                  print("A) creuser.")
                  print("B) ne pas creuser.")
                  reponse_trump_2_pelle = input("votre réponse : ").upper()
                  if reponse_trump_2_pelle == "A":
                       print ("vous creusez et vous échappez de la prison. vous avez gagné! BRAVO!")
                  if reponse_trump_2_pelle == "B":
                       print ("vous ne creusez pas. c'est pas très intelligent ça. vous restez en prison. mauvaise fin")
        if reponse_trump_2 == "C":
             print("vous essayez d'amadouer un garde.") 
             import random
             roll = random.randint(1, 20)
             print("vous avez roulé:", roll)
             if 1<= roll <= 10:
                  print("vous avez échoué. vous avez augmenté votre peine à prison à vie")
             elif 11<= roll <= 20:
                    print("vous avez réussi. le garde vous donne les clés et son uniforme. vous partez.")
                    print("un autre garde vous intercept et vous demande votre carte d'indentification. que faites-vous?")
                    print ("A) vous vous rendez")
                    print ("B) vous courez pour votre vie")
                    reponse_trump_2_garde = input("votre réponse : ").upper()
                    if reponse_trump_2_garde == "A":
                         print ("vous vous rendez. vous revenez en prison. tout ça pour ça? mauvaise fin.")
                    if reponse_trump_2_garde == "B":
                         print ("vous courez pour votre vie.")
                         import random
                         roll = random.randint(1, 20)
                         print("vous avez roulé:", roll)
                         if 1<= roll <= 10:
                              print("échec. vous tombez et vous faites attraper.")
                         elif 11<= roll <= 20:
                                   print("vous réussissez et échappez aux gardes. bravo. vous revenez a votre vie d'avant")
                         elif roll == 20:
                                   print ("les gardes vous tirent dessus, mais vous esquivez toutes les balles")
                                   print ("avec votre nouveau pouvoir, vous devenez millionaire. meilleure fin.")


        

    if reponse_trump_1 == "C":
        print ("vous avez lancé une bombe atomique sur Donald Trump. vous avez tué le continent de l'amérique du nord.") 
        print ("vous avez péri dans l'explosion. mauvaise fin.")




if reponse == "B":
        print ("vous avez choisi Adolph Hitler. choisissez votre arme")
        
        print ("A) un walther PPK")
        print ("B) tu filme un tiktok avec lui")
        print ("C) le bon sens")

        reponse_adolph_1 = input("votre réponse : ").upper()
        if reponse_adolph_1 == "A":
            print ("vous avez tiré sur Adolph Hitler avec un walther PPK. vous le touchez, mais il porte un gilet pare-balle. que faites vous?")
            print ("A) vous prenez peur et courez")
            print ("B) vous lui lancez le fusil dessus")
            print ("C) vous lui foncez dedans")
            reponse_adolph_1_gilet = input("votre réponse : ").upper()

            if reponse_adolph_1_gilet == "A":
                 print ("vous laissez tomber le fusil et il le ramasse. il vous tire dessus")
                 import random
                 roll = random.randint(1, 20)
                 print("vous avez roulé:", roll)
                 if 1 <= roll <= 15:
                      print ()

        if reponse_adolph_1 == "B":
            print ("vous avez filmé un tiktok avec Adolph Hitler. il ne comprend rien à la technologie et vous dénonce au gestapo.")

        if reponse_adolph_1 == "C":
            print ("il est mort depuis longtemps. vous perdez votre temps. mauvaise fin.")















if reponse == "C":
        print ("vous avez choisi Phillipe Gauthier. choisissez votre arme")
        
        print ("A) un code maloptimisé")
        print ("B) 50 variables nommées john")
        print ("C) une ak47")

        reponse_phillipe_1 = input("votre réponse : ").upper()

        if reponse_phillipe_1 == "A":
             print ("il regarde votre code et vous explique a quel point votre code est mauvais.") 
             print ("vous faites une dépression et finissez votre vie dans une grotte. mauvaise fin.")
        if reponse_phillipe_1 == "B":
             print ("il vous dit de les changer sinon il pratique ses cours de takewondo sur vous.")
        if reponse_phillipe_1 == "C":
             print ("vous sortez votre ak47 de votre sac et il appelle la police. vous êtes arrêté pour port d'arme illégal.")
             print ("vous repensez a vos choix de vie et finissez agriculteur.")