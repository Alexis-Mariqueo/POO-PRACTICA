from Claro import Claro
from Movistar import Movistar
from Personal import Personal
from Miexcepcion import Miexcepcion

ex= Miexcepcion("")

while True:
    try:
        sms = float(input("Ingrese la cantidad sms: "))
        ex.metodo(sms,0,0)
        llamada = float(input("Ingrese la cantidad de minutos por llamada: "))
        ex.metodo(sms,llamada,0)
        gb = float(input("Ingrese la cantidad de consumo GB: "))
        ex.metodo(sms,llamada,gb)
        break
    except Miexcepcion as hex:
        print(hex.mensaje)
    except ValueError:
        print("El caracter ingresado no es un numero")

        
movistar = Movistar(sms,llamada,gb)
claro = Claro(sms,llamada,gb)
personal = Personal(sms,llamada,gb)

print("__________________________")
print("Proveedor: {}".format(movistar.get_nombre()))
print("Total sms: {}".format(movistar.calcular_sms()))
print("Total llamada: {}".format(movistar.calulcar_minutos_llamada()))
print("Total consumo gb:{}".format(movistar.calcular_consumo_gb()))     
print("__________________________")
print("__________________________")
print("Proveedor: {}".format(claro.get_nombre()))
print("Total sms: {}".format(claro.calcular_sms()))
print("Total llamada: {}".format(claro.calulcar_minutos_llamada()))
print("Total consumo gb:{}".format(claro.calcular_consumo_gb()))
print("__________________________")
print("__________________________")
print("Proveedor: {}".format(personal.get_nombre()))
print("Total sms: {}".format(personal.calcular_sms()))
print("Total llamada: {}".format(personal.calulcar_minutos_llamada()))
print("Total consumo gb:{}".format(personal.calcular_consumo_gb()))        
print("__________________________")