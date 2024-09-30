from abc import ABC, abstractmethod

class Persona(ABC):
    
    def __init__(self,nombre,apellido,edad,horas_trabajadas,valor_hora):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._horas_trabajadas = horas_trabajadas
        self._valor_hora = valor_hora
        
    @abstractmethod
    def get_renumeracion_mensual(self):
        pass
    
    def set_valor_hora(self,valor): ## por si el valor por hora cambia
        self._valor_hora = valor
        
    def imprimir(self):
        print("Nombre: {}".format(self._nombre))
        print("Apellido: {}".format(self._apellido))
    