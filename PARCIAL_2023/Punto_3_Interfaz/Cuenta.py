from Pagar import Pagar
from abc import ABC,abstractmethod


class Cuenta(Pagar,ABC):
    
    def __init__(self,dueño = "",saldo = 0,numero_cuenta= 0):
        self._dueño = dueño
        self._saldo = saldo
        self._numero_cuenta = numero_cuenta
        
    def set_sueldo(self,saldo):
        self._saldo = saldo
        
    def get_sueldo(self):
        return self._saldo
        
    def pagar_debito(self,pago):
        self._saldo = self._saldo - pago 
    
    @abstractmethod        
    def pagar_credito(self,pago,cuota):
        pass