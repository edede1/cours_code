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