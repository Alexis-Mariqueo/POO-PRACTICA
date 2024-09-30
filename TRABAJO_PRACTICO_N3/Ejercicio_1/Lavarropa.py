from Electrodomestico import Electrodomestico

class Lavarropa(Electrodomestico): ##subclase
    
    def __init__(self, modelo, marca, precio,carga_frontal,capacidad_ropa):
        super().__init__(modelo, marca, precio)
        self.__carga_frontal = carga_frontal
        self.__capacidad_ropa = capacidad_ropa
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print ("Carga Frontal: {}".format(self.__carga_frontal))
        print ("Capacidad Ropa: {}".format(self.__capacidad_ropa))