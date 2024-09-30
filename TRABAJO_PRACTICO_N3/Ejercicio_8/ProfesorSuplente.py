from Persona import Persona

class ProfesorSuplente(Persona):
    
    def __init__(self, nombre, apellido, edad, horas_trabajadas):
        super().__init__(nombre, apellido, edad, horas_trabajadas, valor_hora = 200.00)
        
    def get_renumeracion_mensual(self):
        return self._valor_hora * self._horas_trabajadas
    
    def imprimir(self):
        super().imprimir()
        print("Renumeracion: {}".format(self.get_renumeracion_mensual()))