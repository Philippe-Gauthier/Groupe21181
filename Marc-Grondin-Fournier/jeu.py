import random
print("Menu jeux, /n A: Roulette russe, /n B: Pile ou face, /n C: Courte paille" )
menu=input("Sélectionner un jeu!")

match menu:
        case 1:
            roll=random.randint(1, 6)
            choix =int(input("Bienvenu au jeu de la roulette russe! Quelle trou du barrilet à 6 coups choisir pour mettre la munition? (1,2,3,4,5,6)"))    
            while choix != roll:                
                                
                if choix<roll:
                    for choix in 6:                    
                     print("Vous avez survécu, au tour de l'adversaire!")
                     tour_adv=choix+1
                     if(tour_adv==roll):
                         print("Votre adversaire est mort!")
                         break

                elif choix>roll:
                    for reversed(choix) in 1:  
                        print("Vous avez survécu, au tour de l'adversaire!") 
                        tour_adv=choix-1
                        if(tour_adv==roll):
                            print("Votre adversaire est mort!")
                            break
                                  
