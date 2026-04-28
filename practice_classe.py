class car:
    def  __init__(self, vitesse, couleur):
        self.vitesse = vitesse
        self.couleur = couleur
        


toyota = car( "fast", "rouge")

print(toyota.vitesse)

toyota.vitesse = "veryfast"
print(toyota.vitesse)