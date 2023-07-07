from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def afficher(self):
        pass

class Etudiant(Personne):
    def __init__(self, nom, date_naissance, matricule, note):
        
        super().__init__(nom)
        self.date_naissance = date_naissance
        self.matricule = matricule
        self.note = note

    def afficher(self):
        print(f"Nom: {self.nom}, Date de naissance: {self.date_naissance}, Matricule: {self.matricule}, Note: {self.note}")

class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = {}

    def ajouter_etudiant(self, etudiant):
        self.etudiants[etudiant.matricule] = etudiant

    def modifier_etudiant(self, matricule, nouvelle_note):
        if matricule in self.etudiants:
            self.etudiants[matricule].note = nouvelle_note
            print("Note modifiée avec succès.")
        else:
            print("Étudiant non trouvé.")

    def supprimer_etudiant(self, matricule):
        if matricule in self.etudiants:
            del self.etudiants[matricule]
            print("Étudiant supprimé avec succès.")
        else:
            print("Étudiant non trouvé.")

    def afficher_liste_etudiants(self):
        print(f"Liste des étudiants dans la classe {self.nom}:")
        for etudiant in self.etudiants.values():
            etudiant.afficher()

classe = Classe("Classe A")

while True:
    print("\n----- Menu -----")
    print("1. Ajouter un nouvel étudiant")
    print("2. Modifier la note d'un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Afficher la liste des étudiants")
    print("5. Quitter")
    choix = input("Entrez votre choix (1-5): ")

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
        break

    else:
        print("Choix invalide. Veuillez réessayer.")
