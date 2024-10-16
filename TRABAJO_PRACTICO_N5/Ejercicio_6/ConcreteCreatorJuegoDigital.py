from Creator import Creator
from Importe import Importe
from JuegoDigital import JuegoDigital

#Los Creadores Concretos sobrescriben el Factory Method base,
# de modo que devuelva un tipo diferente de producto.

class ConcreteCreatorJuegoDigital(Creator):
    
    def factory_method(self) -> Importe:
        return JuegoDigital('44567981',35.23,1.1)
    