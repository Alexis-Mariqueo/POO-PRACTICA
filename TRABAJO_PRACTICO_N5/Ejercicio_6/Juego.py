from abc import ABC,abstractmethod

#El Producto declara la interfaz, que es común a todos los objetos 
# que puede producir la clase creadora y sus subclases.
class Juego(ABC):
    
    def __init__(self,id_juego,precio):
        self._id_juego = id_juego
        self._precio = precio
    
    @abstractmethod
    def get_precio(self) -> float:
        pass
    