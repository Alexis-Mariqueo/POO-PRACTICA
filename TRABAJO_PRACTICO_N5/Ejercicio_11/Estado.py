from abc import ABC , abstractmethod

class Estado(ABC):
    
    @abstractmethod
    def abierta (self,cliente):
        pass
    
    @abstractmethod
    def suspendida (self,cliente):
        pass

    @abstractmethod
    def cerrada (self,cliente):
        pass