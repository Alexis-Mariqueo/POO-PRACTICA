
class Paquete: ##Considero que debo usar una clase paquete ya que es distinto a la clase transporte
    
    def __init__(self,peso,ancho,alto,longitud): ##Considero que debo usar estos atributos ya que el enunciado
        self.__peso = peso                      ##Especifica que debe tener peso y dimensiones
        self.__ancho = ancho                    ##Esto seria parte de la dimension
        self.__alto = alto                      ##Esto seria parte de la dimension
        self.__longitud = longitud              ##Esto seria parte de la dimension
    
    def get_peso(self): ##Utilizo este get para que me devuelva el valor del peso
        return self.__peso 
        
    def calcular_peso_volumetrico(self): ## Calculo el peso volumetrico del paquete
        return (self.__alto * self.__ancho *self.__longitud) /5000
        
        
    ##NO ESPECIFICA DONDE USARLO PERO YO LO UTILIZO A LA HORA DE MOSTRAR LA INFORMACION    
    def __str__(self): ##Convierto en cadena los atributos del paquete ya que dice que debo devolver una cadena de los atributos de mi clase paquete
        return f"Peso: {self.__peso}, Ancho: {self.__ancho}, Alto: {self.__alto}, Longitud: {self.__longitud}"