class Alumno:
    
    def __init__(self,nombre = "",apellido = "",dni= 0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = 0
        
    @classmethod ##es un decorador que se utiliza para definir métodos de clase en el paradigma de programación orientada a objetos (POO).
    def iniciar_con_nombre_ape(cls,nombre,apellido): #cls hace referencia a la clase en sí
        alumno = cls.__new__(cls) # se llama antes que el objeto se construya
        alumno.__nombre = nombre # se modifica el atributo
        alumno.__apellido = apellido # se modifica el atributo
        return alumno #se crea el objeto
    
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_dni(self):
        return self.__dni
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def set_apellido(self,apellido):
        self.__apellido = apellido
    
    def set_dni(self,dni):
        self.__dni = dni    