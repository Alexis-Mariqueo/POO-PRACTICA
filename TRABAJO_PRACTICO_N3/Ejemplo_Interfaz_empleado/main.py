from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto
from EmpleadoTemporal import EmpleadoTemporal
import random

lista_empleados = []

opciones = [1,2]
for i in range(0,3):
    opcion = random.choice(opciones)
    if opcion == 1:
        lista_empleados.append(EmpleadoTiempoCompleto(f"Empleado_{i}",random.randrange(120000,200000)))
    if opcion == 2:
        lista_empleados.append(EmpleadoTemporal(f"Empleado_{i}",random.randrange(20000,30000),random.randrange(2,8)))
    
random.shuffle(lista_empleados)        
for per in lista_empleados:
    print("________________________")
    per.mostrar_informacion()
    print("________________________")
    
##Esto es un polimorfismo dinamico porque se realiza la sobreescritura de metodos en tiempo de ejecucion.
##Para implementar un polimorfismo estatico en python se debe hacer sobrecarga de operadores ya que python

##EJEMPLO 
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

p1 = Punto(2, 3)
p2 = Punto(4, 5)
p3 = p1 + p2  # Sobrecarga del operador '+'
print(p3.x, p3.y)  # Salida: 6 8