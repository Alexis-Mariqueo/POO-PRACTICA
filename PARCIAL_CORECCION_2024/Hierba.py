from Pokemon import Pokemon
import random

class Hierba(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre, "Hierba", "Fuego")
    
        
    def defensa(self,danio): ##Defensa recibe el daño del pokemon
        if danio > self._defensa: ##Tener en cuenta el nivel de defensa al recibir el ataque
            if self._velocidad > 50: ##su velocidad es mayor a 50,
                if random.randrange(0,2) == 0: ## SI CAE EL NUMERO CERO SE EJECUTA ESTA LINEA
                    danio -= self._defensa ## danio se le resta la defensa
                    if danio < 0:
                        danio = danio*-1 ## si el daño es negativo se cambia a positivo
                    self._vida -= danio ## se decrementa la vida
            else:
                self._vida -= danio ## se decrementa la vida 