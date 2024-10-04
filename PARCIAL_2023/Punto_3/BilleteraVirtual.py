from Cuenta import Cuenta

class BilleteraVirtual(Cuenta):
    
    def __init__(self, dueño,saldo,numero_cuenta,cvu):
        super().__init__(dueño, saldo, numero_cuenta)
        self.__cvu = cvu
        
    def get_cvu (self):
        return self.__cvu
        
    def pagar_credito(self, pago, cuota):
        if self._saldo < pago:
            print("Saldo insuficiente")
        else:
            total_pago = (pago +  (8 * cuota))
            interes = total_pago / cuota
            self._saldo = self._saldo - interes