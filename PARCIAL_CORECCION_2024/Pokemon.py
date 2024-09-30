from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    
    def __init__(self,nombre,tipo,debilidad):
        self._nombre = nombre
        self._vida = 100
        self._tipo = tipo
        self._debilidad =debilidad
        self._ataque = random.randrange(0,100) ## doy valor a los atributos
        self._defensa = random.randrange(0,100) ##doy valor a los atributos
        self._velocidad = random.randrange(0,100) ##doy valor a los atributos
        self._salvajismo = random.randrange(0,100)
        
    @abstractmethod #Metodo que se declara pero no se usa en la clase base
    def defensa(self,danio): ## estás diciendo que cualquier clase que herede de esta clase abstracta debe implementar ese método, de lo contrario no podrá ser instanciada.
        pass    
    
    ##Como tengo que redefinir solo un metodo de ataque lo coloco en el padre
    ##Se redefine en la clase hija Agua
    def ataque(self,atacado): ##Recibe el pokemon
        if self._tipo == atacado.getDebilidad(): ##Utiliza la debilidad del pokemon
            if random.randrange(0,100) < 70: #70% de probabilidad de hacer un ataque critico
                atacado.defensa(int(self._ataque*1.50))   #Si ataca a un Pokémon débil a este tipo, un 70% de probabilidad de realizar un ataque crítico, lo que aumentará el ataque normal en un 50%.
                pass
        atacado.defensa(self._ataque)
        
    def getDebilidad(self):
        return self._debilidad
    
    def getNombre(self): 
        return self._nombre
        
    def getSalvajismo(self): 
        return self._salvajismo
    
    def getVida(self):
        return self._vida
            
    def setSalvajismo(self,valor): ##Seteo o modifico el salvajismo 
        self._salvajismo = valor
        
    def mostrar_pokemon(self): ##Muestro el pokemon
        print("________________________________________")
        print("Nombre Pokemon:{}".format(self._nombre))
        print("Ataque:{}".format(self._ataque))
        print("Defensa:{}".format(self._defensa))
        print("Velocidad:{}".format(self._velocidad))
        print("Salvajismo:{}".format(self._salvajismo))
        print("________________________________________")