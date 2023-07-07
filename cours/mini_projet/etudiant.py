from personne import Personne

class Etudiant(Personne):
    def __init__(self, nom, date_naissance, matricule, note):
        super().__init__(nom)
        self.date_naissance = date_naissance
        self.matricule = matricule
        self.note = note

    def afficher(self):
        print(f"Nom: {self.nom}, Date de naissance: {self.date_naissance}, Matricule: {self.matricule}, Note: {self.note}")

    def calculer_moyenne(self):
        return sum(self.note) / len(self.note)
