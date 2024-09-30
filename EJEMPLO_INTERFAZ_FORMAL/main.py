from EmpleadoTemporal import EmpleadoTemporal
from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto
import random

opciones = ["1","2"]
lista_empleados = []

for i in range(0,3):
    opcion = random.choice(opciones)
    if opcion == "1":
        lista_empleados.append(EmpleadoTiempoCompleto("Empleado_completo_{}".format(i),random.randrange(30000,150000)))
    if opcion == "2":
        lista_empleados.append(EmpleadoTemporal("Empleado_temporal_{}".format(i),random.randrange(10000,20000),random.randrange(3,8)))
        

for emple in lista_empleados:
    emple.mostrar_informacion()
    

###POLIMORFISMO
##Polimorfismo dinámico: Se resuelve en tiempo de ejecución. 
## En Python, el comportamiento de super() es dinámico porque el método que se invoca a través de super() 
## depende de la estructura de la herencia y del contexto de la llamada en tiempo de ejecución. 
