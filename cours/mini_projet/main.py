from etudiant import Etudiant
from classe import Classe
from personne import Personne


classe = Classe("Classe A")

while True:
    print("\n----- Menu -----")
    print("1. Ajouter un nouvel étudiant")
    print("2. Modifier la note d'un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Afficher la liste des étudiants")
    print("5. Quitter")
    print("5. Calculer la moyenne d'un étudiant")
    print("6. Calculer la moyenne de la classe")
    print("7. Quitter")
    choix = input("Entrez votre choix (1-7): ")
    if choix == "1":
        nom = input("Nom de l'étudiant: ")
        date_naissance = input("Date de naissance: ")
        matricule = input("Matricule: ")
        note = input("Note: ")
        etudiant = Etudiant(nom, date_naissance, matricule, note)
        classe.ajouter_etudiant(etudiant)
        print("Étudiant ajouté avec succès.")

    elif choix == "2":
        matricule = input("Matricule de l'étudiant: ")
        nouvelle_note = input("Nouvelle note: ")
        classe.modifier_etudiant(matricule, nouvelle_note)

    elif choix == "3":
        matricule = input("Matricule de l'étudiant: ")
        classe.supprimer_etudiant(matricule)

    elif choix == "4":
        classe.afficher_liste_etudiants()
    
    elif choix == "5":
        matricule = input("Matricule de l'étudiant: ")
        if matricule in classe.etudiants:
            etudiant = classe.etudiants[matricule]
            moyenne_etudiant = etudiant.calculer_moyenne()
            print(f"La moyenne de l'étudiant {etudiant.nom} est {moyenne_etudiant}")
        else:
            print("Étudiant non trouvé.")

    elif choix == "6":
        moyenne_classe = classe.calculer_moyenne_classe()
        print(f"La moyenne de la classe {classe.nom} est {moyenne_classe}")
    
    elif choix == "7":
        break
    
    else:
        print("Choix invalide. Veuillez réessayer.")
