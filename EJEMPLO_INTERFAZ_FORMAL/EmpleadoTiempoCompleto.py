from Empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    
    def __init__(self,nombre,sueldo_anual):
        self.__nombre = nombre
        self.__sueldo_anual = sueldo_anual
        
    def calcular_salario(self):
        pass
        
    def mostrar_informacion(self):
        print("Nombre:{}".format(self.__nombre))
        print("Sueldo Anual: {}".format(self.__sueldo_anual))