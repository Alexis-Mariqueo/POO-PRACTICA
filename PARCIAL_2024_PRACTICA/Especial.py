from Carta import Carta

class Especial(Carta):
    
    def __init__(self, nombre, equipo, pais):
        super().__init__(nombre, equipo, pais)
        self._calcular_atributos(89,99,3)
        self.__lista_habilidades = []
    
    def especial_habilidad(self,habilidad):
        self.__lista_habilidades.append(habilidad)
                
    def calcular_quimica(self, pais_favorito, equipo_favorito):
        return 100
    
    def imprimir(self):
        super().imprimir()
        print("Lista Habilidades :")
        for i in self.__lista_habilidades:
            print(i)