from datetime import date
from dateutil.relativedelta import relativedelta


class Persona:
    
    def __init__(self,nombre = "",apellido = "",fecha_nacimiento = 0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_fecha(self):
        return self.__fecha_nacimiento
        
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def set_apellido(self,apellido):
        self.__apellido = apellido
        
    def set_fecha(self,fecha):
        self.__fecha_nacimiento = fecha  
        
    def calcular_edad(self):
        hoy = date.today()
        diferencia = relativedelta (hoy,self.__fecha_nacimiento)
        return diferencia.years
    
    def __str__(self):
        return (f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Fecha Nacimiento: {self.__fecha_nacimiento}, Edad: {self.calcular_edad()}")