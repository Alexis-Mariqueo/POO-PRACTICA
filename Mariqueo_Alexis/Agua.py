from Pokemon import Pokemon
import random

class Agua(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__tipo = "Agua"
        self.__debilidad = "Hierba"
        
    def getTipo(self):
        return self.__tipo
    
    def Ataque_pokemon(self,pokemon):
        if pokemon == "Fuego":
            return self._ataque * 1.07
        else:
            return self._ataque
        
    def Defensa_pokemon(self, daño):
        if random.randint(1,100) < 30:
            return (self._vida * 1.05) - daño
        else:
            return self._vida - daño