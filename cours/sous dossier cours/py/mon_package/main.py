from mon_package.complexes import addition_complexe, multiplication_complexe
from mon_package.chaines import inverser_chaine, compter_mots

nombre1 = complex(2, 3)
nombre2 = complex(1, 4)

resultat_addition = addition_complexe(nombre1, nombre2)
print("Résultat de l'addition :", resultat_addition)

resultat_multiplication = multiplication_complexe(nombre1, nombre2)
print("Résultat de la multiplication :", resultat_multiplication)

chaine = "Bonjour, comment ça va ?"

chaine_inverse = inverser_chaine(chaine)
print("Chaine inversée :", chaine_inverse)

nombre_mots = compter_mots(chaine)
print("Nombre de mots :", nombre_mots)
