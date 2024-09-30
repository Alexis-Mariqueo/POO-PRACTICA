from Cuenta import Cuenta

class BilleteraVirtual(Cuenta):
    
    def __init__(self, dueño):
        super().__init__(dueño, saldo, numero_cuenta)
        self.__cvu = "042340502349"
        
    def pagar_debito(self, pago):
        self._saldo = self._saldo - pago    
        
    def pagar_credito(self, pago, cuota):
        if cuota <= 3:
            descontar = pago /cuota
            total_pago = pago - descontar
            for i in range(cuota):
                if i == 1:
                    self._saldo = self._saldo - descontar    
            self._saldo = self._saldo - total_pago
        else:
            total_pago = (pago +  (8 * cuota) )
            interes = total_pago / cuota
            for i in range(cuota):
                if i == 1:
                    self._saldo = self._saldo - interes
            total_pago = total_pago - interes
            self._saldo = self._saldo - total_pago