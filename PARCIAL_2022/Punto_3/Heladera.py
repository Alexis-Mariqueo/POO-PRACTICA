from Electrodomestico import Electrodomestico

class Heladera(Electrodomestico):
    
    def __init__(self, modelo, precio, marca, color,capacidad_total,capacidad_freezer):
        super().__init__(modelo, precio, marca, color)
        self.__capacidad_total = capacidad_total
        self.__capacidad_freezer = capacidad_freezer
        
    def imprimir(self):
        super().imprimir()
        print("Capacidad Frezzer: {}".format(self.__capacidad_freezer))