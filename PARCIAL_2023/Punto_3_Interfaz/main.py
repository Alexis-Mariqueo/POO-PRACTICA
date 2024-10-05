from Banco import Banco
from BilleteraVirtual import BilleteraVirtual
from Impuesto import Impuesto
import random

lista_impuesto = []
mes_actual = 10 

bancaria = Banco("Alexis Mariqueo",60000,random.randrange(10000,20000),random.randrange(1000,9999))
virtual = BilleteraVirtual("Enzo Puñalef",50000,random.randrange(10000,20000),random.randrange(1000,9999))

for i in range(1,21):
    lista_impuesto.append(Impuesto(f"Impuesto_{i}",random.randrange(1000,20000),random.randrange(1,12)))

opciones = [1,2]

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
            if random.choice(opciones) == 1:
                if virtual.pagar_credito(impuesto_actual.get_monto(), random.randint(1, 36)):
                    pagado(impuesto_actual)
                    lista_impuesto.remove(impuesto_actual) # remuevo el impuesto de la lista
                else:
                    print("Saldo insuficiente")
                    bool1 = True
            else:
                if bancaria.pagar_debito(impuesto_actual.get_monto()):
                    pagado(impuesto_actual)
                    lista_impuesto.remove(impuesto_actual) # remuevo el impuesto de la lista
                else:
                    print("Saldo insuficiente")
                    bool2 = True        

        
        
        # PAGANDO BANCO 
        else:
            forma_pago = random.randint(1,2)
            if forma_pago == 1:
                if bancaria.pagar_credito(impuesto_actual.get_monto(), random.randint(1,12)):
                    pagado(impuesto_actual)
                    lista_impuesto.remove(impuesto_actual) # remuevo el impuesto de la lista
                else:
                    print("Saldo insuficiente")
                    bool2 = True
            else:
                if bancaria.pagar_debito(impuesto_actual.get_monto()):
                    pagado(impuesto_actual)
                    lista_impuesto.remove(impuesto_actual) # remuevo el impuesto de la lista
                else:
                    print("Saldo insuficiente")
                    bool2 = True        

print(bancaria.get_sueldo())
print(virtual.get_sueldo())         