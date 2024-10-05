from abc import ABC

class Persona(ABC):
    
    def __init__(self,legajo,nombre,apellido,dni,tipo) :
        self._legajo = legajo
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._tipo = tipo
        
    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self,tipo):
        self._tipo = tipo    
    
    def mostrar_informacion(self):
        print("Legajo: {}".format(self._legajo))
        print("Nombre: {}".format(self._nombre))
        print("Apellido: {}".format(self._apellido))
        print("Dni: {}".format(self._dni))