from Creator import Creator
from Importe import Importe
from JuegoFisico import JuegoFisico

#Los Creadores Concretos sobrescriben el Factory Method base,
# de modo que devuelva un tipo diferente de producto.

class ConcreteCreatorJuegoFisico(Creator):
    
    def factory_method(self) -> Importe:
        return JuegoFisico('45678961',40.0,30.0)


