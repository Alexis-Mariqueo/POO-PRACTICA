from abc import ABC

class Personal(ABC):
    
    def __init__(self,nombre_completo,antiguedad_anios,horas_extra):
        self._nombre_completo = nombre_completo
        self._antiguedad_anios = antiguedad_anios
        self._horas_extra = horas_extra
        
    ## Lo deben implementar los dos hijos de diferentes formas    
    def asignacion_horas(self):
        pass
    
    def imprimir(self):
        print("Nombre y apellido: {}".format(self._nombre_completo))
        print("Años de Antiguedad: {}".format(self._antiguedad_anios))
    