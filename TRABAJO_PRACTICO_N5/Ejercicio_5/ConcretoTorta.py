from Builder import Builder
from Torta import Torta

class ConcretoTorta(Builder):

    def __init__(self):
        self._torta = None
        
    def get_torta (self):
        return self._torta
    
    def crear_torta(self):
        self._torta = Torta()
        
    def agregar_masa(self,masa):
        self._torta.set_masa(masa)
        
    def agregar_relleno(self,relleno):
        self._torta.set_relleno(relleno)
    
    #def agregar_masa_coco(self):
    #    self._torta.set_masa("Coco")
        
    #def agregar_relleno_coco(self):
    #    self._torta.set_relleno("Dulce de Leche y Durazno")
    
    #def agregar_masa_chocolate(self):
    #    self._torta.set_masa('Chocolate')

   # def agregar_relleno_chocolate(self):
   #     self._torta.set_relleno('Crema con Frutilla y Mermelada de Frutos Rojos')
