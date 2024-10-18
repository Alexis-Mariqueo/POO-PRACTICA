from Juego import Juego

#Los Productos Concretos son distintas implementaciones de la interfaz de producto.
class JuegoDigital(Juego):
    
    def __init__(self, id_juego, precio,precio_plataforma):
        super().__init__(id_juego, precio)
        self.__precio_plataforma = precio_plataforma
        
    def get_precio(self):
        return self._precio * self.__precio_plataforma