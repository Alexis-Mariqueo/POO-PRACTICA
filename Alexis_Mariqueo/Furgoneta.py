from Transporte import Transporte

class Furgoneta(Transporte):
    
    def __init__(self):#Considero que debe tener esto el constructor
        self.__tipo = "Furgoneta"
        self.__velocidad_promedio = 60.0
        self.__valor_hora = 1000.0
        self.__tiempo = 0.0
        self.__costo = 0.0
            
    def get_tipo(self): 
        return self.__tipo
    
    def get_tiempo(self):
        return self.__tiempo
    
    def get_costo(self):
        return self.__costo
    
    
    def transportar_paquetes(self, distancia, peso_paquete):##Calculo el indicador de costo de transporte
        if peso_paquete > 100.0:
            return -1 ##Devuelvo -1 en caso de superar el peso
        else:
            self.__tiempo = self.__velocidad_promedio/distancia
            self.__costo = self.__valor_hora * distancia
            return 0.7 * self.__tiempo + 0.3 * self.__costo
            
            