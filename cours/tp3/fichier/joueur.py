from erreurs import ErreurMinAge, ErreurMaxAge, ErreurSexe

class Joueur:
    def __init__(self, nom, age, sexe, numero):
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.numero = numero

        if self.age < 18:
            raise ErreurMinAge("L'âge du joueur est inférieur à 18 ans")
        elif self.age >= 35:
            raise ErreurMaxAge("L'âge du joueur est supérieur ou égal à 35 ans")
        
        if self.sexe.upper() not in ['F', 'f']:
            raise ErreurSexe("Le sexe du joueur doit être 'F' ou 'f'")
        