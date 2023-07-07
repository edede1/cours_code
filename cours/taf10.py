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

carnivore = Carnivore()
carnivore.se_deplacer()  
carnivore.manger("de la viande")  

carni_sauvage = CarniSauvage()
carni_sauvage.se_deplacer()  
carni_sauvage.manger("de la viande")  
