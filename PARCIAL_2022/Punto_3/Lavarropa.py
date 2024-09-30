from Electrodomestico import Electrodomestico

class Lavarropas(Electrodomestico):
    
    def __init__(self, modelo, precio, marca, color,carga_frontal,capacidad):
        super().__init__(modelo, precio, marca, color)
        self.__capacidad = capacidad
        
    def imprimir(self):
        super().imprimir()
        print("Capacidad:{}".format(self.__capacidad))
        