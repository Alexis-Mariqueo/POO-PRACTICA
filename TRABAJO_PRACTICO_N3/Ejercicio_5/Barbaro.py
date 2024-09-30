from Personaje import Personaje
import random

class Barbaro(Personaje):
    
    def __init__(self,nombre):
        super().__init__(nombre,vida = 100, nivel_ataque = 70, nivel_defensa = 10)
        
    def atacar(self): ## Extiendo el ataque de barbaro
        if random.randrange(0,100) < 70:
            return self._nivel_ataque * 1.30
        else:
            return self._nivel_ataque