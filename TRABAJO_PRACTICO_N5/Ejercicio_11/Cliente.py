
class Cliente:
    
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def get_edad(self):
        return self.__edad
    
    def get_nombre(self):
        return self.__nombre
    
    def imprimir_cliente(self):
        print(f"Nombre Cliente: {self.__nombre}")
        print(f"Edad Cliente: {self.__edad}")