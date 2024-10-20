from Reportero import Reportero
from SistemaMeteorologico import SistemaMetereologico

# El producto es el sujeto, es el objeto OBSERVADO
clima = SistemaMetereologico("lluvia")

# Los clientes son los OBSERVADORES
reportero_1 = Reportero("Gaston")
reportero_2 = Reportero("Pablo")
reportero_3 = Reportero("Ale")

# Los clientes se suscriben al producto
clima.agregar_observador(reportero_1)
clima.agregar_observador(reportero_2)
clima.set_clima("Soleado")
clima.set_clima("Nublado")
clima.agregar_observador(reportero_3)
clima.set_clima("Ventoso")
# Cambiar el precio del producto, lo cual notifica a los suscriptores
#clima.set_clima("Soleado")
#clima.notificar_actualizacion()
#print()
#clima.set_clima("Ventoso")
#print()
#clima.set_clima("Nublado")