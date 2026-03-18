"""
Gestion de budget
Auteur: Joseph Boka
"""
Liste_depenses = {
    "Logement" : 1250,
    "Hydro" : 170,
    "Epicerie" : 500,
    "Communication" : 100,
    "Carburant" : 200,
    "assurance" : 200,
    "Garderie" : 300,
    "Loisir" : 500,
    "Imprevus" : 500
}
for element in Liste_depenses:
    print(f"{element},{Liste_depenses[element]}$")
    Liste_depenses[element]
#calcul du montant total
Total = 0 
for montant in Liste_depenses.values():
    Total += montant
    print(f"montant total : {Total}$")

#Calcul du pourcentage du montant
