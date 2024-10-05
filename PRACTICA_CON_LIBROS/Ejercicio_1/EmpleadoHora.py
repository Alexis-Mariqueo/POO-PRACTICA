from Empleado import Empleado

class EmpleadoHora(Empleado):
    
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, horas_trabajadas, tarifa_por_hora,"Empleado Hora")
    
    def calcular_sueldo(self):
        return self._horas_trabajadas * self._taifa_por_hora 