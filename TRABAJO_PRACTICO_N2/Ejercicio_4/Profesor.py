class Profesor:
    
    def __init__(self,nombre="",apellido=""):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__materia = []
        
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def set_apellido(self,apellido):
        self.__apellido = apellido    
    
    def get_nombre(self):
        return self.__nombre
        
    def get_apellido(self):
        return self.__apellido
    
    def get_materia(self):
        return self.__materia
    
    def add_materia(self,materia):
        self.__materia.append(materia)