from abc import ABC

class Electrodomestico(ABC):
    
    def __init__(self,modelo,precio,marca,color):
        self._modelo = modelo
        self._precio = precio
        self._marca = marca
        self._color = color
        
    def imprimir(self):
        print("Precio: {}".format(self._precio))
        print("Marca: {}".format(self._marca))
        
    