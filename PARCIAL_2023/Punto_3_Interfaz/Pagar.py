from abc import ABC, abstractmethod

class Pagar(ABC):
    
    @abstractmethod
    def pagar_debito(self,pago):
        pass
    
    @abstractmethod
    def pagar_credito(self,pago,cuota):
        pass