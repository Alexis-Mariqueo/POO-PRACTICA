from Empleado import Empleado

class EmpleadoTemporal(Empleado):
    
    def __init__(self,nombre,sueldo_por_hora,horas_trabajadas):
        self.__nombre = nombre
        self.__sueldo_por_hora = sueldo_por_hora
        self.__horas_trabajadas = horas_trabajadas
        
    def calcular_salario(self,sueldo_por_hora,horas_trabajadas):
        super().calcular_salario()
        total = 0
        for i in range(horas_trabajadas):
            total = total + sueldo_por_hora
        return total
    
    def mostrar_informacion(self):
        print("Nombre:{}".format(self.__nombre))
        print("Sueldo por hora:{}".format(self.__sueldo_por_hora))
        print("Horas Trabajadas:{}".format(self.__horas_trabajadas))
        print("Total sueldo por hora:{}".format(self.calcular_salario(self.__sueldo_por_hora,self.__horas_trabajadas)))
        