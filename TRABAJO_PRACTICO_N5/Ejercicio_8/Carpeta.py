from Elemento import Elemento

##El Contenedor (también llamado compuesto) es un elemento que tiene subelementos: hojas u 
# otros contenedores. Un contenedor no conoce las clases concretas de sus hijos. 
# Funciona con todos los subelementos únicamente a través de la interfaz componente.

class Carpeta (Elemento):
    
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__elementos = []
        self.__tipo = None
        
    def asignar_rol(self, rol):
        self.__tipo = rol
        
    def agregar_elemento(self,elemento):
        self.__elementos.append(elemento)
        
    def eliminar_elemento(self,elemento):
        self.__elementos.append(elemento)
        
    def mostrar_contenido(self):
        print(f'* {self.__nombre} ({self.__tipo})')
        for elemento in self.__elementos:
            elemento.mostrar_contenido()