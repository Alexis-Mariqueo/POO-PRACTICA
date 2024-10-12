from abc import ABC, abstractmethod

class TortaBuilder(ABC):
    
    @property
    @abstractmethod
    def torta(self)->None:
        pass
    
    @abstractmethod
    def set_masa(self,masa) -> None:
        pass
    
    @abstractmethod
    def set_relleno(self,relleno) ->None:
        pass
    

    