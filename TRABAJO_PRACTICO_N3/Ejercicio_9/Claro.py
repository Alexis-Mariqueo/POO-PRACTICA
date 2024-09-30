from TarifaProveedor import TarifaProveedor

class Claro(TarifaProveedor):
    
    def __init__(self, mensaje_texto, minutos_llamada, gigas):
        super().__init__(nombre = "Claro", mensaje_texto = mensaje_texto, minutos_llamada = minutos_llamada, gigas = gigas)
        
    def get_nombre(self):
        return self._nombre

    def calcular(self):
        return float(self.calcular_sms() + self.calulcar_minutos_llamada() + self.calcular_consumo_gb()) * 1.20
    