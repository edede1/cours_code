def remplir_formulaire():
    print("Bienvenue ! Veuillez remplir le formulaire :")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    email = input("Email : ")
    adresse = input("Adresse : ")
    ville = input("Ville : ")
    pays = input("Pays : ")
    profession = input("Profession : ")
    telephone = input("Numéro de téléphone : ")

    # Construire le message avec les informations fournies
    message = f"Merci {prenom} {nom} pour avoir rempli le formulaire.\n\nVoici les informations que vous avez fournies :\n" \
              f"Nom : {nom}\nPrénom : {prenom}\nEmail : {email}\nAdresse : {adresse}\nVille : {ville}\nPays : {pays}\n" \
              f"Profession : {profession}\nNuméro de téléphone : {telephone}"

    return message


# Appel de la fonction pour remplir le formulaire
message_final = remplir_formulaire()

# Afficher le message avec les informations fournies
print("\n----------\n")
print("Voici vos informations :")
print(message_final)
