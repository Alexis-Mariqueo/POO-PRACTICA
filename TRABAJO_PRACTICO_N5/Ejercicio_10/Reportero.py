from Observador import Observador

class Reportero (Observador):
    
    def __init__(self,nombre: str):
        self.__nombre = nombre
        
    def actualizar(self, clima):
        print(f"El reportero {self.__nombre } informa que el clima ha cambiado de estado: {clima}")