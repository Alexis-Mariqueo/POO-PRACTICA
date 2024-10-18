from Tienda import Tienda
from JuegoDigital import JuegoDigital

#Los Creadores Concretos sobrescriben el Factory Method base,
# de modo que devuelva un tipo diferente de producto.

class ConcreteCreatorJuegoDigital(Tienda):
    
    def creador_juego(self):
        return JuegoDigital('44567981',3523,1000)
    