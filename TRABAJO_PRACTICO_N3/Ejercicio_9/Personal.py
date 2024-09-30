from TarifaProveedor import TarifaProveedor
import random
class Personal(TarifaProveedor):
    
    def __init__(self, mensaje_texto, minutos_llamada, gigas):
        super().__init__(nombre = "Personal", mensaje_texto = mensaje_texto, minutos_llamada = minutos_llamada, gigas = gigas)
        
    def get_nombre(self):
        return self._nombre
        
    def calulcar_minutos_llamada(self):
        return super().calulcar_minutos_llamada() * 1.20
    
    def calcular_consumo_gb(self):
        return super().calcular_consumo_gb() * 1.50