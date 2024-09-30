from abc import ABC
import random

class Pokemon(ABC):
    
    def __init__(self,nombre):
        self._nombre = nombre
        self._vida = 100
        self._ataque = self.generacion_atributos(0,100)
        self._defensa = self.generacion_atributos(0,100)
        self._velocidad = self.generacion_atributos(0,100)
        self._salvajismo = self.generacion_atributos(0,100)
        
    def generacion_atributos(self,min,max):
        return random.randint(min,max) 
    
    def setVida(self,vida):
        self._vida = vida
        
    def setSalvajismo(self,reduccion):
        self._salvajismo = self._salvajismo - reduccion
    
    def getNombre(self):
        return self._nombre
    
    def getVida(self):
        return self._vida
    
    
    def getSalvajismo(self):
        return self._salvajismo
    

        
    def mostrar_pokemon(self):
        print("______________________________")
        print(f'Nombre: {self._nombre}')
        print(f'Ataque: {self._ataque}')
        print(f'Defensa: {self._defensa}')
        print(f'Velocidad: {self._velocidad}')
        print(f'Salvajismo: {self._salvajismo}')
        print("______________________________")