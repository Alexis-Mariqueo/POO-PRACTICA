from Electrodomestico import Electrodomestico

class Cocina (Electrodomestico): ##subclase
    
    def __init__(self, modelo, marca, precio,electrica,cantidad_hornallas):
        super().__init__(modelo, marca, precio)
        self.__electrica = electrica
        self.__cantidad_hornallas = cantidad_hornallas
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Es electrica: {}".format(self.__electrica))
        print("Cantidad Hornallas: {}".format(self.__cantidad_hornallas))
        
