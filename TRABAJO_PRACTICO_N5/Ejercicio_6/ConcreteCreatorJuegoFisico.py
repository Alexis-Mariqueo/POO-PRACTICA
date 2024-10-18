from Tienda import Tienda
from JuegoFisico import JuegoFisico

#Los Creadores Concretos sobrescriben el Factory Method base,
# de modo que devuelva un tipo diferente de producto.

class ConcreteCreatorJuegoFisico(Tienda):
    
    def creador_juego(self) :
        return JuegoFisico('45678961',1200.0,1000.0)


