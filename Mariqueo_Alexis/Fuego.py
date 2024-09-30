from Pokemon import Pokemon
import random

class Fuego(Pokemon):
    
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.__tipo = "Fuego"
        self.__debilidad = "Agua"
        
    def getTipo(self):
        return self.__tipo
        
    def Ataque_pokemon(self,pokemon):
        if pokemon == "Hierba":
            if random.randint(1,100) > 70:
                return self._ataque * 1.05
            else:
                return self._ataque
        else:
            return self._ataque 
        
    def Defensa_pokemon(self,daño):
        if self._defensa > 50:
            return self._vida
        else:
            return self._vida - daño