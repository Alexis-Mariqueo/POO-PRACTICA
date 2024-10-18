from abc import ABC, abstractmethod

##La interfaz describe operaciones que son comunes a elementos simples y complejos del árbol
class Elemento(ABC):
    
    @abstractmethod
    def asignar_rol(self,rol):
        pass
    
    @abstractmethod
    def mostrar_contenido(self):
        pass