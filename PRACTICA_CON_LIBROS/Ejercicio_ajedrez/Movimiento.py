from abc import ABC,abstractmethod

class Movimiento(ABC):
    
    @abstractmethod
    def mover_pieza(self,movimiento,fila,columna):
        pass
    
    @abstractmethod
    def ataque(self,pieza):
        pass