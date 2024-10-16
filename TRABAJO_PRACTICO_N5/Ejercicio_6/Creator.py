from __future__ import annotations
from abc import ABC, abstractmethod

#La clase Creadora declara el método fábrica que devuelve 
# nuevos objetos de producto. Es importante que el tipo de
# retorno de este método coincida con la interfaz de producto.
class Creator(ABC):

# -> anotation, permite indicar que es lo que se devuelve, pero no obliga.
    @abstractmethod
    def factory_method(self):
        pass

    def notificar_precio(self) -> str:
        notificador = self.factory_method()
        result = f"Precio de juego: {notificador.get_precio()}"

        return result
    
