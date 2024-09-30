from Persona import Persona
from Empresa import Empresa
import random

sexo = ["M","F"]
respuesta = [True,False]
empresa = Empresa("Chango mas","Maipu 9000")
for i in range(5):
    i = Persona(random.randrange(18,60),random.choice(sexo),random.choice(respuesta),True)
    empresa.agregar_empleado(i)
    
    
num = 1
print("_______________________________________________")
print("Nombre Empresa: {}".format(empresa.get_nombre()))
print("Direccion: {}".format(empresa.get_direccion()))
print("Empleados:")
for i in empresa.get_empleados():
    print("_______________________________________________")
    print(f"Empleado_{num}")
    i.imprimir()
    num+= 1
print("Total Empleados: {}".format(empresa.total_empleados()))