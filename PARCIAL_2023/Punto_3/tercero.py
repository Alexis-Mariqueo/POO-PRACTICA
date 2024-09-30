import random 

class Cuenta:
    def __init__(self, saldo, dueño, nro_cuenta):
        self._saldo = saldo
        self._dueño = dueño
        self._nro_cuenta = nro_cuenta
    
    def pagar_credito(self, monto_cuota):
        if self._saldo < monto_cuota:
            return False
        else:
            self._saldo -= monto_cuota
            return True




class CuentaBanco(Cuenta):
    def __init__(self, saldo, dueño, nro_cuenta, cbu= "cbu"):
        super().__init__(saldo, dueño, nro_cuenta)
        self.__clave = cbu
    
    
    def pagar_debito(self, monto):
        if self._saldo < monto:
            return False
        else:
            self._saldo -= monto
            reintegro = monto * 0.10
            self._saldo += reintegro
            return True
    
    
    def pagar_credito(self, monto, cuotas_elegidas):
        monto_cuota = monto / cuotas_elegidas
        if cuotas_elegidas <= 3:
            return super().pagar_credito(monto_cuota)
        else:
            interes = 2 * cuotas_elegidas
            monto_cuota *= (interes / 100 + 1)
            return super().pagar_credito(monto_cuota)
    
    
    def get_cvu(self):
        return self.__clave





class BilleteraVirtual(Cuenta):
    def __init__(self, saldo, dueño, nro_cuenta, cvu = "cvu"):
        super().__init__(saldo, dueño, nro_cuenta)
        self.__clave = cvu
    
    
    def pagar_credito(self, monto, cuotas_elegidas):
        monto_cuota = monto / cuotas_elegidas
        monto_cuota *= 1.08
        return super().pagar_credito(monto_cuota)
    
    
    def get_cvu(self):
        return self.__clave




class Impuesto:
    def __init__(self, nombre, monto, periodo):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__estado_cobrado = False
        self.__numero_comprobante = None
    
    
    def get_monto(self):
        return self.__monto
    
    
    def get_nombre(self):
        return self.__nombre
    
    
    def validar_pago(self, mes, numero_comprobante):
        if mes == self.__periodo:
            self.__estado_cobrado = True
            self.__numero_comprobante = numero_comprobante





banco = CuentaBanco(50000, "Mansilla Maximiliano", 4355, 66665045540540)
billetera_virtual = BilleteraVirtual(40000, "Mansilla Martin", 4344, 3453425454353452)
lista_impuesto = []
mes_actual = 8





for i in range(1, 21):
    lista_impuesto.append(Impuesto(f"Impuesto {i}", random.randint(1000, 20000), random.randint(1, 12)))





def pagado(impuesto_actual):
    numero_comprobante = random.randint(1, 20000)
    print("Pago realizado correctamente al impuesto: " + impuesto_actual.get_nombre())
    impuesto_actual.validar_pago(mes_actual, numero_comprobante)










bool1, bool2 = False, False
while True:
    
    if (bool1 and bool2) or len(lista_impuesto) == 0: # SALE DEL BUCLE SI MIS 2 CUENTAS NO TIENEN SALDO PARA PAGAR
        break
    else:
        
        impuesto_actual = random.choice(lista_impuesto)
        
        eligiendo_cuenta = random.randint(1,2) #1 billetera virtual, #2 banco
        # PAGANDO BILLETERA VIRTUAL
        if eligiendo_cuenta == 1:
            if billetera_virtual.pagar_credito(impuesto_actual.get_monto(), random.randint(1, 36)):
                pagado(impuesto_actual)
                lista_impuesto.remove(impuesto_actual) # remuevo el impuesto de la lista
            else:
                print("Saldo insuficiente")
                bool1 = True
        
        
        # PAGANDO BANCO 
        else:
            forma_pago = random.randint(1,2)
            if forma_pago == 1:
                if banco.pagar_credito(impuesto_actual.get_monto(), random.randint(1,12)):
                    pagado(impuesto_actual)
                    lista_impuesto.remove(impuesto_actual) # remuevo el impuesto de la lista
                else:
                    print("Saldo insuficiente")
                    bool2 = True
            else:
                if banco.pagar_debito(impuesto_actual.get_monto()):
                    pagado(impuesto_actual)
                    lista_impuesto.remove(impuesto_actual) # remuevo el impuesto de la lista
                else:
                    print("Saldo insuficiente")
                    bool2 = True        

## yo plantearia el ejercicio con una interfaz pagar, solamente con un metodo pagar_credito, ya que 
## serian lo que ambas clases tienen que implementar para quue funcionen correctamente. 
##
