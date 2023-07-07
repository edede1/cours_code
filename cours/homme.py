class Homme:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_informations(self):
        print("Nom :", self.nom)
        print("Âge :", self.age)

    def obtenir_nom(self):
        return self.nom

    def obtenir_age(self):
        return self.age

    def changer_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def changer_age(self, nouvel_age):
        self.age = nouvel_age

homme1 = Homme("John Doe", 30)
homme2 = Homme("Jane Smith", 25)

homme1.afficher_informations()
print("")

homme2.afficher_informations()
print("")

nom_homme1 = homme1.obtenir_nom()
age_homme1 = homme1.obtenir_age()

print("Nom de l'homme 1 :", nom_homme1)
print("Âge de l'homme 1 :", age_homme1)
print("")

homme2.changer_nom("Jane Johnson")
homme2.changer_age(27)

homme2.afficher_informations()
