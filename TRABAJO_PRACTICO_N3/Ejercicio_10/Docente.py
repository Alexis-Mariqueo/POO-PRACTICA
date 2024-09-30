from Personal import Personal
import random

class Docente(Personal):
    
    def __init__(self, nombre_completo, antiguedad_anios, sector):
        super().__init__(nombre_completo, antiguedad_anios,horas_extra = random.randrange(2,10))
        self.__sector = sector
        
    def asignacion_horas(self):
        if self.__sector == "Simple":
            if random.randrange (0,100) < 95:
                return float(10) * 4.33 + float(self._horas_extra)
            else:
                return float(10) * 4.33
        if self.__sector == "Semiexclusiva":
            if random.randrange(0,100) < 75:
                return float(20) * 4.33 + float(self._horas_extra)
            else:
                return float(20) * 4.33 
        if self.__sector == "Exclusiva":
            if random.randrange(0,100) < 60:
                return float(40) * 4.33 * float(self._horas_extra)
            else:
                return float(40) * 4.33
            
    def imprimir(self):
        super().imprimir()
        print("Sector: {}".format(self.__sector))
            