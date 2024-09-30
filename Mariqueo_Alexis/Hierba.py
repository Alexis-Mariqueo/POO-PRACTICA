from Pokemon import Pokemon
import random

class Hierba(Pokemon):
    
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.__tipo = "Hierba"
        self.__debilidad = "Fuego"

    def getTipo(self):
        return self.__tipo        
        
    def Ataque_pokemon(self,pokemon):
        if pokemon == "Agua":
            if random.randint(1,7) == 7: 
                return  self._ataque * 1.05
            else:
                return self._ataque
        else:
            return self._ataque
        
    def Defensa_pokemon(self,daño):
        if self._velocidad > 50:
            if random.randint(1,7) == 7:
                return self._vida
            else:
                return self._vida - daño    
        elif self._velocidad <= 50:
            return self._vida - daño
            
                