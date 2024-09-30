from Electrodomestico import Electrodomestico

class Cocina(Electrodomestico):
    
    def __init__(self, modelo, precio, marca, color,electrica):
        super().__init__(modelo, precio, marca, color)
        self.__electrica = electrica
        
    def imprimir(self):
        super().imprimir()
        print("Es Electrica:{}".format(self.__electrica))