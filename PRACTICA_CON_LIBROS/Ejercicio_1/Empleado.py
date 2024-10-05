from abc import ABC,abstractmethod

class Empleado(ABC):
    
    def __init__(self,nombre,horas_trabajadas,tarifa_por_hora,tipo):
        self._nombre = nombre
        self._horas_trabajadas = horas_trabajadas
        self._taifa_por_hora = tarifa_por_hora
        self._tipo = tipo
        
    def get_tipo(self):
        return self._tipo
    
    def get_nombre(self):
        return self._nombre    
        
    @abstractmethod   
    def calcular_sueldo(self):
        pass
        
    