class Puesto:
    
    def __init__(self,nombre_puesto= ""):
        self.__nombre_puesto = nombre_puesto

    def get_nombre_puesto(self):
        return self.__nombre_puesto
    
    def get_nombre_puesto(self,puesto):
        self.__nombre_puesto = puesto
        
    def __str__(self):
        return (f"Puesto: {self.__nombre_puesto}")
        