from __future__ import annotations
from abc import ABC, abstractmethod

#La clase Creadora declara el método fábrica que devuelve 
# nuevos objetos de producto. Es importante que el tipo de
# retorno de este método coincida con la interfaz de producto.
class Tienda(ABC):

# -> anotation, permite indicar que es lo que se devuelve, pero no obliga.
    @abstractmethod
    def creador_juego(self):
        pass

    
