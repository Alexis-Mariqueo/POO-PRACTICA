from Carta import Carta

class Oro(Carta):
    
    def __init__(self, nombre, equipo, pais):
        super().__init__(nombre, equipo, pais)
        self._cargar_atributos(74,90,2)
        