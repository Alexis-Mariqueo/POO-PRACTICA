from abc import ABC,abstractmethod

class Cuenta(ABC):
    
    def __init__(self,dueño,saldo,numero_cuenta):
        self._dueño = dueño
        self._saldo = saldo
        self._numero_cuenta = numero_cuenta
        
    def set_sueldo(self,saldo):
        self._saldo = saldo
        
    @abstractmethod    
    def pagar_debito(self,pago):
        pass
    
    @abstractmethod
    def pagar_credito(self,pago,cuota):
        pass