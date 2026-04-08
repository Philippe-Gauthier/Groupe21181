
import random

list =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def Mac(list):
    Mac_adress = []
    result = ""
    for i in range(5):
        result = str(random.choice(list)) + str(random.choice(list))
        Mac_adress.append(result)
        str(result)

    print(Mac_adress)

Mac(list)



