def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        raise ArithmeticError("Division by zero is not allowed")
    except NameError:
        raise NameError("Variable not defined")

# Exemple d'utilisation
try:
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    resultat = division(num1, num2)
    print("Le résultat de la division est :", resultat)
except ArithmeticError as ae:
    print("Erreur arithmétique :", str(ae))
except NameError as ne:
    print("Erreur de nom :", str(ne))
except ValueError:
    print("Veuillez entrer des nombres valides")
finally:
    print("Fin du programme")
