from abc import ABC,abstractmethod

#El Producto declara la interfaz, que es común a todos los objetos 
# que puede producir la clase creadora y sus subclases.
class Importe(ABC):
    @abstractmethod
    def get_precio(self) -> float:
        pass