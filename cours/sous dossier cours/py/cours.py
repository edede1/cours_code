class Etudiant:
    def __init__(self, nom, date_naissance, matricule, note):
        self.nom = nom
        self.date_naissance = date_naissance
        self.matricule = matricule
        self.note = note


class SalleClasse:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
        print("Etudiant ajouté avec succès.")

    def modifier_etudiant(self, matricule, new_nom, new_date_naissance, new_note):
        for etudiant in self.etudiants:
            if etudiant.matricule == matricule:
                etudiant.nom = new_nom
                etudiant.date_naissance = new_date_naissance
                etudiant.note = new_note
                print("Etudiant modifié avec succès.")
                return
        print("Aucun étudiant trouvé avec ce matricule.")

    def supprimer_etudiant(self, matricule):
        for etudiant in self.etudiants:
            if etudiant.matricule == matricule:
                self.etudiants.remove(etudiant)
                print("Etudiant supprimé avec succès.")
                return
        print("Aucun étudiant trouvé avec ce matricule.")

    def afficher_liste_etudiants(self):
        print("Liste des étudiants de la salle de classe:")
        for etudiant in self.etudiants:
            print("Nom:", etudiant.nom)
            print("Date de naissance:", etudiant.date_naissance)
            print("Matricule:", etudiant.matricule)
            print("Note:", etudiant.note)
            print("------------------------")


# Fonction principale
def main():
    # Création de la salle de classe
    salle = SalleClasse("Classe A")

    while True:
        print("***************")
        print("Gestion de la salle de classe")
        print("1. Ajouter un étudiant")
        print("2. Modifier un étudiant")
        print("3. Supprimer un étudiant")
        print("4. Afficher la liste des étudiants")
        print("5. Quitter")
        choix = input("Entrez votre choix: ")

        if choix == "1":
            nom = input("Entrez le nom de l'étudiant: ")
            date_naissance = input("Entrez la date de naissance de l'étudiant: ")
            matricule = input("Entrez le matricule de l'étudiant: ")
            note = input("Entrez la note de l'étudiant: ")
            etudiant = Etudiant(nom, date_naissance, matricule, note)
            salle.ajouter_etudiant(etudiant)

        elif choix == "2":
            matricule = input("Entrez le matricule de l'étudiant à modifier: ")
            new_nom = input("Entrez le nouveau nom de l'étudiant: ")
            new_date_naissance = input("Entrez la nouvelle date de naissance de l'étudiant: ")
            new_note = input("Entrez la nouvelle note de l'étudiant: ")
            salle.modifier_etudiant(matricule, new_nom, new_date_naissance, new_note)

        elif choix == "3":
            matricule = input("Entrez le matricule de l'étudiant à supprimer: ")
            salle.supprimer_etudiant(matricule)

        elif choix == "4":
            salle.afficher_liste_etudiants()

        elif choix == "5":
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")


# Appel de la fonction principale
if __name__ == "__main__":
    main()
