from Pokemon import Pokemon
import random

class Fuego(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre, "Fuego", "Agua")
    
    def defensa(self,danio):
        if danio > self._ataque: ##Tener en cuenta el nivel de defensa al recibir el ataque.
            danio-= self._defensa ## el danio es decrementado por la defensa
            if danio < 0: ## si el danio es menor a cero se pasa a positivo
                danio = danio*-1
            self._vida-= danio ## a la vida se le resta el danio