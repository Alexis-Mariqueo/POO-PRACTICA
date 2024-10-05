from Empleado import Empleado

class EmpleadoPlanta(Empleado):
    
    def __init__(self, nombre,sueldo_mensual):
        super().__init__(nombre, 0, 0,"Empleado Planta")
        self.__sueldo = sueldo_mensual
        
        
    def calcular_sueldo(self):
        return self.__sueldo * 12 #Se multiplica por los meses para saber el sueldo anual