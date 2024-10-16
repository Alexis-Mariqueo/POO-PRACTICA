from abc import ABC, abstractmethod

##En el builder van los pasos de creacion de la torta
class Builder(ABC):
    
    @abstractmethod
    def agregar_masa(self) -> None:
        pass
    
    @abstractmethod
    def agregar_relleno(self) ->None:
        pass
    
    
    

    