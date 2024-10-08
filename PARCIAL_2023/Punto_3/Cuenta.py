from abc import ABC,abstractmethod

class Cuenta(ABC):
    
    def __init__(self,dueño,saldo,numero_cuenta):
        self._dueño = dueño
        self._saldo = saldo
        self._numero_cuenta = numero_cuenta
        
    def set_sueldo(self,saldo):
        self._saldo = saldo
        
    def get_sueldo(self):
        return self._saldo
        
    def pagar_debito(self,pago):
        if self._saldo < pago:
            self._saldo ## devuelve el saldo y no hace el pago
        else:
            self._saldo = self._saldo - pago 
    
    @abstractmethod        
    def pagar_credito(self,pago,cuota):
        pass