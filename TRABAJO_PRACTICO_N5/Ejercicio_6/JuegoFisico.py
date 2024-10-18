from Juego import Juego

#Los Productos Concretos son distintas implementaciones de la interfaz de producto.
class JuegoFisico(Juego):
    
    def __init__(self, id_juego, precio,precio_traslado):
        super().__init__(id_juego, precio)
        self.__precio_traslado = precio_traslado
        
    def get_precio(self):
        return self._precio * self.__precio_traslado