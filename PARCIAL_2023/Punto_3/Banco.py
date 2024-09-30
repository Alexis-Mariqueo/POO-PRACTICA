from Cuenta import Cuenta

class Cuenta(Cuenta):
    
    def __init__(self, dueño):
        super().__init__(dueño, saldo = 80000, numero_cuenta = "N° 1908400")
           
    def pagar_debito(self,pago):
        reintegro = (pago * 10)/100
        self._saldo = self._saldo - pago
        self._saldo = self._saldo + reintegro
    
    def pagar_credito(self,pago,cuota):
        if cuota <= 3:
            descontar = pago /cuota
            for i in range(cuota):
                if i == 1:
                    self._saldo = self._saldo - descontar
            pago = pago - descontar
            self._saldo = self._saldo - pago 
        else:
            total_pago = (pago +  (2 * cuota) )
            interes = total_pago / cuota
            for i in range(cuota):
                if i == 1:
                    self._saldo = self._saldo - interes
            self._saldo = self._saldo -(total_pago - interes)    