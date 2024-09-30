from abc import ABC , abstractmethod

class Electrodomestico(ABC): ##SUPERCLASE
    
    def __init__(self,modelo = "",marca = "",precio =0):
        self.__modelo = modelo
        self.__marca = marca
        self.__precio = precio
        
    @abstractmethod
    def mostrar_informacion(self):
        print("Modelo: {}".format(self.__modelo))
        print("Marca: {}".format(self.__marca))
        print("Precio: {}".format(self.__precio))

###Herencia
##La herencia es un mecanismo de abstraccion, consiste en la capacidad de derivar nuevas clases 
# a partir de otras ya existentes
# Permite reutilizar codigo y mantener la complejidad de las nuevas clases dentro de los limites manejables