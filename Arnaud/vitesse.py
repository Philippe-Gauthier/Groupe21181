def kmh_vers_mph(kmh):
    mph = kmh / 1.609
    return mph

kmh = float(input("Quelle est la vitesse a convertir? "))
print(kmh_vers_mph(kmh))