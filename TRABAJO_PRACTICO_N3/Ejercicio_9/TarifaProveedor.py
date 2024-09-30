from abc import ABC, abstractmethod
import random
class TarifaProveedor(ABC):
    
    def __init__(self,nombre,mensaje_texto,minutos_llamada,gigas):
        self._nombre = nombre
        self._mensaje_texto = mensaje_texto
        self._minutos_llamada = minutos_llamada
        self._gigas = gigas
        
    @abstractmethod    
    def get_nombre(self):
        pass

    def calcular_sms(self):
        return 1 * float(self._mensaje_texto) 
    
    def calulcar_minutos_llamada(self):
        return 15 * float(self._minutos_llamada)
    
    def calcular_consumo_gb(self):
        return 20 * float(self._gigas)

    
    def calcular(self):
        return  float(self.calcular_sms() + self.calulcar_minutos_llamada() + self.calcular_consumo_gb())
    
         



        