def salutation_invite(nom_utilisateur):
    message = f"Bonjour {nom_utilisateur} ! Bienvenue !"
    return message

# Demande le nom de l'utilisateur
nom = input("Entrez votre nom : ")

# Appelle la fonction et affiche le message
resultat = salutation_invite(nom)
print(resultat)
