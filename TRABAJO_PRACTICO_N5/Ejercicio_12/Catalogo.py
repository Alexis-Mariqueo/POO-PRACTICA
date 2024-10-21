from abc import ABC,abstractmethod

class Catalogo(ABC):
    
    @abstractmethod
    def catalogo(self,lista):
        pass