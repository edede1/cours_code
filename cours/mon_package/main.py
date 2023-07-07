# main.py
from mon_package.module_complexes import *
from mon_package.module_chaines import *

# Manipulation des complexes
a = 2 + 3j
b = 4 + 5j

print("Addition complexe :", addition_complexe(a, b))
print("Soustraction complexe :", soustraction_complexe(a, b))
print("Multiplication complexe :", multiplication_complexe(a, b))
print("Division complexe :", division_complexe(a, b))

# Manipulation des chaînes de caractères
chaine = "Hello, World!"

print("Longueur de la chaîne :", longueur_chaine(chaine))
print("Chaîne inversée :", inverser_chaine(chaine))
print("Est-ce un palindrome ?", est_palindrome(chaine))
