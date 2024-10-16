from Importe import Importe

#Los Productos Concretos son distintas implementaciones de la interfaz de producto.
class JuegoDigital(Importe):
    
    def __init__(self,id_juego,importe,precio_plataforma):
        self.__id_juego = id_juego
        self.__importe = importe
        self.__precio_plataforma = precio_plataforma
        
    def get_precio(self):
        return self.__importe * self.__precio_plataforma