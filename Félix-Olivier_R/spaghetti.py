import time
print("La création, la musique, l'art en général, j'ai jamais réussi à trouver une bonne raison d'abandonner tout et de m'y mettre pour de bon. J'ai 21 ans, en ce moment je travail dans le provigo du coin. Chu, comme, zéro populaire, par contre c'est plus par choix que pas résultat de mes actions ou whatever. Je dirais pas que j'ai beaucoup d'argent, mais j'ai quand même un ford raptor 2017.  Suite") 
attendre=input("Lorsqu'est écrit 'Suite' appuyez sur ENTER, SINON ATTENDEZ, cela est le dernier rappel.")
print("Très bon prix d'ailleurs. Ça me rappele l'intéraction que j'ai eu avec le vendeur, c'était quand même vraiment goofy. Après avoir démontré mon intérêt le gars m'avais donné un coup de fil. Suite")
attendre=input()
# Premier évènement: coup de téléphone, 2 options présenté
print("-Bonjour, est-ce que je parle à Nicolas?")
print("** Insérez le NOMBRE de l'option de votre choix lorsque demandé et appuyer sur ENTER, cela est le dernier rappel. **")
time.sleep(2)
phone_1=input("---- Option *1*: Oui -- Option *2*: Non ----:")

if(phone_1=="1"): # OUI
    print("-Oui c'est bien moi.")
    time.sleep(2)
    print("-Je m'adresse à qui?")
else: # NON
    if(phone_1=="2"):
        print("-Non scuse moi lgros, tu dois avoir le mauvais numéro.") 
        time.sleep(3)
        print("J'étais sûr c'était un foutu spam, j'ai pas réfléchi..   Suite")
        attendre=input()
        print("-Ah je suis désolé. Tu n'es pas la personne qui m'avait envoyé un message ce matin pour le ford ce matin?")
        time.sleep(3)
        print("Ah shit")
        time.sleep(1)
        print("Je ne pouvais pas retourner la situation, je sais pas si j'avais simplement pas allumé, mais j'ai choké. J'avais 18 ans je sais pas trop quoi te dire.   Suite")
        attendre=input()



