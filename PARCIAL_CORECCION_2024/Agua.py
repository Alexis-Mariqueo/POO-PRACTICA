from Pokemon import Pokemon
import random

class Agua(Pokemon):
    
    def __init__(self, nombre):
        super().__init__(nombre,"Agua", "Hierva")

    def ataque(self,atacado):
        if self._tipo == atacado.getDebilidad():  ## pregunta si el tipo de pokemon con el que lucha es igual a la debilidad del pokemon atacado
            atacado.defensa(int(self._ataque*1.70))  ## aumenta el ataque en 70% 
            pass
        atacado.defensa(self._ataque) ## el pokemon atacado se defiende
        
    def defensa(self,danio): 
        if danio > self._ataque: ## Teneren cuenta el nivel de defensa al recibir el ataque
            danio-=self._defensa ## el danio disminuye con la defensa
            if danio < 0: ## si el danio es negativo el se pasa a positivo multiplicando por menos 1
                danio = danio * -1 
            if random.randrange(0,100) < 30: ## TIENE UN 30% DE DISMINUIR EL DANIO 
                danio -= danio * 0.50 ## DISMINUYE EL DANIO A UN %50
                self._vida -= danio ## SE RESTA A LA VIDA EL DANIO
            else:
                self._vida -= danio ## SE RESTA NORMAL
        
    