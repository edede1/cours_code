from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, nom, date_naissance):
        self.nom = nom
        self.date_naissance = date_naissance

    @abstractmethod
    def afficher_infos(self):
        pass

class Etudiant(Personne):
    def __init__(self, nom, date_naissance, matricule, note):
        super().__init__(nom, date_naissance)
        self.matricule = matricule
        self.note = note

    def afficher_infos(self):
        print(f"Nom : {self.nom}")
        print(f"Date de naissance : {self.date_naissance}")
        print(f"Matricule : {self.matricule}")
        print(f"Note : {self.note}")

class SalleClasse:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = {}

    def ajouter_etudiant(self, etudiant):
        self.etudiants[etudiant.matricule] = etudiant
        print(f"L'étudiant {etudiant.nom} a été ajouté à la salle de classe.")

    def modifier_etudiant(self, matricule, nouveau_nom):
        if matricule in self.etudiants:
            etudiant = self.etudiants[matricule]
            etudiant.nom = nouveau_nom
            print(f"Le nom de l'étudiant avec le matricule {matricule} a été modifié.")

    def supprimer_etudiant(self, matricule):
        if matricule in self.etudiants:
            etudiant = self.etudiants.pop(matricule)
            print(f"L'étudiant {etudiant.nom} avec le matricule {matricule} a été supprimé de la salle de classe.")
        else:
            print(f"Aucun étudiant avec le matricule {matricule} n'a été trouvé.")

    def afficher_liste_etudiants(self):
        print(f"Liste des étudiants dans la salle de classe {self.nom}:")
        for etudiant in self.etudiants.values():
            etudiant.afficher_infos()
            print("------")

# Exemple d'utilisation
salle_de_classe = SalleClasse("Classe A")

etudiant1 = Etudiant("Alice", "2002-05-10", "001", 15)
etudiant2 = Etudiant("Bob", "2003-09-15", "002", 18)

salle_de_classe.ajouter_etudiant(etudiant1)
salle_de_classe.ajouter_etudiant(etudiant2)

salle_de_classe.modifier_etudiant("001", "Alex")
salle_de_classe.supprimer_etudiant("002")

salle_de_classe.afficher_liste_etudiants()
