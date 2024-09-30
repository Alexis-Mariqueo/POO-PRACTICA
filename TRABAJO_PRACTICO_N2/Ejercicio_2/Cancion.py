class Cancion:
    
    def __init__(self,nombre = "",autor = "",duracion = 0.0):
        self.__nombre = nombre
        self.__autor = autor
        self.__duracion = duracion
    
    ##La clase Cancion es un molde para crear objetos (instancias) que comparten atributos (datos)
    ## y comportamientos (métodos)
    ##CRITERIOS DE LA CLASE:
        #ALTAMENTE COHESIVAS: La clase representa una única entidad (no varias),los datos y lo que puede
        #hacer con ellos están muy relacionados entre si.
        #MINIMAMENTE ACOPLADA: La clase limita sus interacciones con otras, se limita a relacionarse con aquellas
        #que son necesarias y para las cuales fue diseñada
        #ENCAPSULADA: Mantiene resguadarda su información y como la manipula de las otras clases y permite
        # el acceso de manera intencionada
        
        
    ### Getters para devolver el valor que contienen los atributos
    
    @property    
    def get_nombre(self):
        return self.__nombre
    
    @property
    def get_autor(self):
        return self.__autor
    
    @property
    def get_duracion(self):
        return self.__duracion
    
    ## SETTERS para modificar el valor que contienen los atributos
    
    @get_autor.setter
    def set_autor(self,autor):
        self.__autor = autor
        
    @get_nombre.setter    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    @get_duracion.setter
    def set_duracion(self,duracion):
        self.__duracion = duracion
    
    