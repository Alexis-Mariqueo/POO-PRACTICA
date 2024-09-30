from Persona import Persona
from Empresa import Empresa
from Puesto import Puesto
import random

sexo = ["M","F"]
respuesta = [True,False]
empresa = Empresa("Chango mas","Maipu 9000")

persona_1 = Persona(random.randrange(18,60),random.choice(sexo),random.choice(respuesta),True,Puesto("Administrativo"))
empresa.agregar_empleado(persona_1)    
persona_2 = Persona(random.randrange(18,60),random.choice(sexo),random.choice(respuesta),True,Puesto("Administrativo"))
empresa.agregar_empleado(persona_2)
persona_3 = Persona(random.randrange(18,60),random.choice(sexo),random.choice(respuesta),True,Puesto("Administrativo"))
empresa.agregar_empleado(persona_3)    
persona_4 = Persona(random.randrange(18,60),random.choice(sexo),random.choice(respuesta),True,Puesto("Gerente"))
empresa.agregar_empleado(persona_4)        
persona_5 = Persona(random.randrange(18,60),random.choice(sexo),random.choice(respuesta),True,Puesto("Tesorero"))
empresa.agregar_empleado(persona_5)
    
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