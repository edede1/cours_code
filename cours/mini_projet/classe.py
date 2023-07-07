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

    def calculer_moyenne_classe(self):
        notes = [etudiant.note for etudiant in self.etudiants.values()]
        somme_notes = sum(sum(note) for note in notes)
        total_etudiants = sum(len(note) for note in notes)
        if total_etudiants != 0:
            moyenne_classe = somme_notes / total_etudiants
            return moyenne_classe
        else:
            return 0.0
