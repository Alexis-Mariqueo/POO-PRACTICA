from Carta import Carta

class BronceEspecial(Carta):
    
    def __init__(self, nombre, equipo, pais,habilidad_especial):
        super().__init__(nombre, equipo, pais)
        self._cargar_atributos(49,65,1)
        self.__habilidad_especial = habilidad_especial
        
    def imprimir(self):
        super().imprimir()
        print("Habilidad Especial:{}".format(self.__habilidad_especial))