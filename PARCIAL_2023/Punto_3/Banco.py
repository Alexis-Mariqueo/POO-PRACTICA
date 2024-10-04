from Cuenta import Cuenta

class Banco(Cuenta):
    
    def __init__(self, dueño,saldo,numero_cuenta,cbu):
        super().__init__(dueño,saldo,numero_cuenta)
        self.__cbu = cbu
           
    def pagar_debito(self, pago):
        return super().pagar_debito(pago * 0.1)
            
    def pagar_credito(self,pago,cuota):
        if self._saldo < pago:
            self._saldo ## devuelve el saldo y no realiza el pago
        else:
            if cuota <= 3:
                descontar = pago /cuota
                self._saldo = self._saldo - descontar 
            else:
                total_pago = (pago +  (2 * cuota) )
                interes = total_pago / cuota
                self._saldo = self._saldo - interes