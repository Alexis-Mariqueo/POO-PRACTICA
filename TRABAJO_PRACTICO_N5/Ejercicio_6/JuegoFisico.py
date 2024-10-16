from Importe import Importe

#Los Productos Concretos son distintas implementaciones de la interfaz de producto.
class JuegoFisico(Importe):
    
    def __init__(self,id_juego,importe,precio_traslado):
        self.__id_juego = id_juego
        self.__importe = importe
        self.__precio_traslado = precio_traslado
        
    def get_precio(self):
        return self.__importe * self.__precio_traslado