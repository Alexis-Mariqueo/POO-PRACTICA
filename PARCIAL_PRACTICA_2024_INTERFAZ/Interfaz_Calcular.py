from abc import ABC, abstractmethod

class Interfaz_Calcular(ABC):
    
    @abstractmethod
    def calcular_quimica(self,pais_favorito,equipo_favorito):
        pass
    
    @abstractmethod
    def _cargar_atributos(self,min,max,opcion):
        pass
    
