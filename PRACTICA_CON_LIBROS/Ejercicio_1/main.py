from EmpleadoPlanta import EmpleadoPlanta
from EmpleadoHora import EmpleadoHora
import random
lista_empleados = []

for i in range(1,11):
    lista_empleados.append(EmpleadoHora(f"Empleado_hora_{i}",random.randint(1000,10000),random.randint(3,8)))
    lista_empleados.append(EmpleadoPlanta(f"Empleado_Planta{i}",random.randint(10000,20000)))
    
print("Lista Empleados")    
for per in lista_empleados:
    if per.get_tipo() == "Empleado Planta":
        print("______________________________________________________")
        print("Nombre: {}".format(per.get_nombre()))
        print("Sueldo al anio: {}".format(per.calcular_sueldo()))
        print("______________________________________________________")
    if per.get_tipo() == "Empleado Hora":
        print("______________________________________________________")
        print("Nombre: {}".format(per.get_nombre()))
        print("Sueldo mensual: {}".format(per.calcular_sueldo()))
        print("______________________________________________________")