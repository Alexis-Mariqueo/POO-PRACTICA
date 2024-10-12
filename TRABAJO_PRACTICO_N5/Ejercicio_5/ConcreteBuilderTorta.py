from __future__ import annotations
from Torta import Torta
from TortaBuilder import TortaBuilder

class ConcreteBuilderTorta(TortaBuilder):
    
    def __init__(self)->None:
        self.reset()
        
    def reset (self)->None:
        self._torta = Torta()
        
    ##forma de convertir un método de una clase en un atributo, 
    ##lo que permite acceder a él como si fuera una propiedad, 
    # pero sin la necesidad de llamar explícitamente al método.
    #Decorador
    @property
    def torta (self) -> Torta:
        torta = self._torta
        self.reset()
        return torta           
    
    def set_masa(self,masa)->None:
        self._torta._masa= masa
        
        
    def set_relleno(self,relleno)->None:
        self._torta._relleno = relleno
        
    