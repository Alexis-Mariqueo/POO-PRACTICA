from Personal import Personal
import random

class Nodocente(Personal):
    
    def __init__(self, nombre_completo, antiguedad_anios,jornada):
        super().__init__(nombre_completo, antiguedad_anios,horas_extra = random.randrange(2,10))
        self.__jornada = jornada 
        
    def asignacion_horas(self):
        if self.__jornada == "Reducida":
            if random.randrange(0,100) < 80:
                return float(20) * 4.33 + self._horas_extra
            else:
                return float(20) * 4.33
        if self.__jornada == "Completa":
            if random.randrange(0,100) < 80:
                return float(30) * 4.33 + self._horas_extra
            else:
                return float(30) * 4.33
            
            
    def imprimir(self):
        super().imprimir()
        print("Jornada: {}".format(self.__jornada))