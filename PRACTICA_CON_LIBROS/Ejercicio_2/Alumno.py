from Persona import Persona

class Alumno(Persona):
    
    def __init__(self, legajo, nombre, apellido, dni,tipo):
        super().__init__(legajo, nombre, apellido, dni, tipo)
        
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: {}".format(self._tipo))