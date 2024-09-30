import random

class Persona:
    
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = random.randrange(1,98)
        
    def get_edad(self):
        return self.__edad
        
    def imprimir(self):
        print("Nombre:{}".format(self.__nombre))