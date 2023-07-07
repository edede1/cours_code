import cmath

a = 3 + 4j
b = 1 + 2j

# Addition
c = a + b
print("Addition :", c)

# Soustraction
d = a - b
print("Soustraction :", d)

# Multiplication
e = a * b
print("Multiplication :", e)

# Division
f = a / b
print("Division :", f)

# Partie réelle
partie_reelle = a.real
print("Partie réelle de a :", partie_reelle)

# Partie imaginaire
partie_imaginaire = a.imag
print("Partie imaginaire de a :", partie_imaginaire)

# Conjugaison
conjugue = a.conjugate()
print("Conjugé de a :", conjugue)

# Module
module = abs(a)
print("Module de a :", module)

# Argument
argument = cmath.phase(a)
print("Argument de a :", argument)
