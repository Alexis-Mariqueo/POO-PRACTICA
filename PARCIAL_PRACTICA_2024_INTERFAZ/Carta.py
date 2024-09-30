from abc import ABC
from Interfaz_Calcular import Interfaz_Calcular
import random

class Carta(Interfaz_Calcular,ABC):
    
    def __init__(self,nombre,equipo,pais) -> None:
        self._nombre = nombre
        self._equipo = equipo
        self._pais = pais
        self._velocidad = 0
        self._tiro = 0
        self._regate = 0
        self._defensa = 0
        self._pase = 0
        self._fisico = 0
        
    def _cargar_atributos(self, min, max, opcion):
        if opcion == 1:
            self._velocidad = random.randrange(min,max) + 2
            self._tiro = random.randrange(min,max) + 2
            self._regate = random.randrange(min,max) + 2
            self._defensa = random.randrange(min,max) + 2
            self._pase = random.randrange(min,max) + 2
            self._fisico = random.randrange(min,max) + 2
        if opcion == 2:
            self._velocidad = random.randrange(min,max) * 1.05
            self._tiro = random.randrange(min,max) * 1.05
            self._regate = random.randrange(min,max) * 1.05
            self._defensa = random.randrange(min,max) * 1.05
            self._pase = random.randrange(min,max) * 1.05
            self._fisico = random.randrange(min,max) * 1.05
        if opcion == 3:
            self._velocidad = self.__cargar_valor(min,max)
            self._tiro = self.__cargar_valor(min,max)
            self._regate = self.__cargar_valor(min,max)
            self._defensa = self.__cargar_valor(min,max)
            self._pase = self.__cargar_valor(min,max)
            self._fisico = self.__cargar_valor(min,max)
    
    def __cargar_valor(self,min,max):
        valor = random.randrange(min,max) * 1.02
        if valor < 99:
            return valor
        else:
            return 99
        
    def calcular_quimica(self, pais_favorito, equipo_favorito):
        if self._pais == pais_favorito and self._equipo == equipo_favorito:
            return 100
        if self._pais != pais_favorito or self._equipo != equipo_favorito:
            return 80
        else:
            return 0
        
    def imprimir(self):
        print("Nombre:{}".format(self._nombre))
        print("Equipo:{}".format(self._equipo))
        print("Pais:{}".format(self._pais))  
        print("Velocidad:{}".format(self._velocidad))
        print("Tiro:{}".format(self._tiro))
        print("Regate:{}".format(self._regate))
        print("Defensa:{}".format(self._defensa))
        print("Pase:{}".format(self._pase))
        print("Fisico:{}".format(self._fisico))