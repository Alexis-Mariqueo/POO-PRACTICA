from Movimiento import Movimiento
from abc import ABC

class Pieza(Movimiento,ABC):
    
    def __init__(self,tipo_pieza):
        self._tipo_pieza = tipo_pieza
        self._movimientos = 0
    
    def get_tipo(self):
        return self._tipo_pieza    
    
    def contador_movimientos(self):
        return self._movimientos + 1
    
    def mover_pieza(self,movimiento,fila,columna):
        print(f"El peon se movio en la fila {fila}, columna {columna}")
        self.contador_movimientos()
        
        
    def ataque(self, pieza,fila,columna):
        print(f"{self.get_tipo()} ataco a la pieza '{pieza.get_tipo()}' que se encontraba en la fila {fila} , columna{columna}")