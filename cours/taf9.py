class Animal:
    def __init__(self, nom, couleur, genre):
        self.nom = nom
        self.couleur = couleur
        self.genre = genre

    def display(self):
        print("Nom:", self.nom)
        print("Couleur:", self.couleur)
        print("Genre:", self.genre)

    def manger(self):
        return "Je mange un peu de tout !"


class Carnivore(Animal):
    def __init__(self, nom, couleur, genre):
        super().__init__(nom, couleur, genre)

    def manger(self):
        return "Je mange de la viande"


class CarniSauvage(Carnivore):
    def __init__(self, nom, couleur):
        super().__init__(nom, couleur, "sauvage")

    def parler(self):
        print("Je vis dans la forêt !")


# Exemple d'utilisation des classes
animal_domestique = Animal("Chien", "Marron", "domestique")
animal_domestique.display()
print(animal_domestique.manger())

carnivore_sauvage = CarniSauvage("Lion", "Jaune")
carnivore_sauvage.display()
print(carnivore_sauvage.manger())
carnivore_sauvage.parler()

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def se_deplacer(self):
        pass

    @abstractmethod
    def manger(self, aliment):
        pass

class Carnivore(Animal):
    def se_deplacer(self):
        print("Le carnivore se déplace.")

    def manger(self, aliment):
        print("Le carnivore mange", aliment)

class CarniSauvage(Carnivore):
    def se_deplacer(self):
        print("Le carnivore sauvage se déplace.")

    def manger(self, aliment):
        print("Le carnivore sauvage mange", aliment)
