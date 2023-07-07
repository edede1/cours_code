# erreurs.py

class Erreur(Exception):
    pass

class ErreurMinAge(Erreur):
    pass

class ErreurMaxAge(Erreur):
    pass

class ErreurSexe(Erreur):
    pass

# joueur.py

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
        

# main.py

from joueur import Joueur
from erreurs import Erreur, ErreurMinAge, ErreurMaxAge, ErreurSexe

try:
    joueur1 = Joueur("Alice", 20, "F", 10)
    joueur2 = Joueur("Bob", 17, "M", 5)
    joueur3 = Joueur("Caroline", 25, "F", 7)
except ErreurMinAge as e:
    print("Erreur : L'âge du joueur est inférieur à 18 ans.")
except ErreurMaxAge as e:
    print("Erreur : L'âge du joueur est supérieur ou égal à 35 ans.")
except ErreurSexe as e:
    print("Erreur : Le sexe du joueur doit être 'F' ou 'f'.")
except Erreur as e:
    print("Erreur : Une erreur inattendue est survenue.")
    print(str(e))
except Exception as e:
    print("Erreur : Une exception a été levée.")
    print(str(e))
