from Elemento import Elemento
 
##La Hoja es un elemento básico de un árbol que no tiene subelementos. 

class Archivo(Elemento):
    
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__tipo = None
        
    def asignar_rol(self,rol):
        self.__tipo = rol
        
    def mostrar_contenido(self):
        print(f'  + {self.__nombre}.{self.__tipo}')
        
    