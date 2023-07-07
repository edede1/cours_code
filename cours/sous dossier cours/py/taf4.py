menu = {
    1: "Banane",
    2: "Orange",
    3: "Pomme",
    4: "Pastèque",
    5: "Raisin"
}

print("Menu du restaurant :")
for key, value in menu.items():
    print(f"{key} - {value}")

choix = int(input("Faites votre choix en entrant le numéro correspondant : "))

if choix in menu:
    plat = menu[choix]
    print(f"Votre choix est {plat}.")
else:
    print("Choix invalide. Veuillez sélectionner un plat disponible dans le menu.")
