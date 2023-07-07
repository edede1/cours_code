import os
import datetime

def ajouter_operation_a_historique(nom_utilisateur, operation):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    chemin_fichier = os.path.join("logs", "historique.txt")

    date_temps = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ligne = f"{nom_utilisateur}, {operation}, {date_temps}\n"

    with open(chemin_fichier, "a") as fichier:
        fichier.write(ligne)

nom_utilisateur = input("Entrez votre nom : ")

while True:
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        resultat = nombre1 + nombre2

        print("Le résultat de l'addition est :", resultat)

        operation = f"{nombre1} + {nombre2} = {resultat}"
        ajouter_operation_a_historique(nom_utilisateur, operation)

        continuer = input("Voulez-vous effectuer une autre opération ? (O/N) : ")

        if continuer.upper() == "N":
            break

    except ValueError:
        print("Veuillez entrer des nombres valides.")

print("Fin du programme.")
