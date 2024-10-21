
class Pelicula:
    
    def __init__(self,nombre_pelicula,clasificacion_pelicula):
        self.__nombre = nombre_pelicula
        self.__clasificacion_pelicula = clasificacion_pelicula
        
    def get_edad(self):
        return self.__clasificacion_pelicula
    
    def mostrar_pelicula(self):
        print(f"Nombre Pelicula: {self.__nombre}")
        if self.__clasificacion_pelicula >= 18:
            print(f"Clasificacion Pelicula: Mayores de 18")
        elif self.__clasificacion_pelicula <18 and self.__clasificacion_pelicula >=16:
            print(f"Clasificacion pelicula: Mayores de 16")
        elif self.__clasificacion_pelicula< 16 and self.__clasificacion_pelicula >= 13:
            print(f"Clasificacion pelicula: Mayores de 13")
        elif self.__clasificacion_pelicula < 13:
            print(f"Clasificacion pelicula: Todo Publico")