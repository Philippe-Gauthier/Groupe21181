def convertisseur_heure(minute):
    heure = minute // 60
    return heure

def convertisseur_minute(minute):
    minutes = minute % 60
    return minutes

minute = int(input("combien de minutes? "))
print(f"{convertisseur_heure(minute)}h {convertisseur_minute(minute)} min")