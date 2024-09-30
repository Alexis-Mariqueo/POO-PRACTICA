from Empleado import Empleado

class EmpleadoTemporal(Empleado):
    
    def __init__(self,nombre,sueldo_hora,horas_trabajadas):
        self.__nombre = nombre
        self.__sueldo_hora = sueldo_hora
        self.__horas_trabajadas = horas_trabajadas
        
    def calcular_salario(self):
        return self.__sueldo_hora * self.__horas_trabajadas    
        
    def mostrar_informacion(self):
        print("Nombre: {}".format(self.__nombre))
        print("Sueldo por hora: {}".format(self.__sueldo_hora))
        print("Horas trabajadas: {}".format(self.__horas_trabajadas))
        print("Sueldo Mensual: {}".format(self.calcular_salario()))
        
