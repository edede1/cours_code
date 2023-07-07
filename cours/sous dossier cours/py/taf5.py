employes = []

def ajouter_employe():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    salaire = float(input("Salaire : "))
    role = input("Rôle : ")

    employe = {
        "nom": nom,
        "prenom": prenom,
        "salaire": salaire,
        "role": role
    }

    employes.append(employe)
    print("Employé ajouté avec succès.")

def obtenir_liste_employes():
    liste_employes = []
    for employe in employes:
        liste_employes.append(employe["prenom"] + " " + employe["nom"])
    return liste_employes

ajouter_employe()
ajouter_employe()

liste_employes = obtenir_liste_employes()
print("Liste de tous les employés :")
for employe in liste_employes:
    print(employe)

print(liste_employes)