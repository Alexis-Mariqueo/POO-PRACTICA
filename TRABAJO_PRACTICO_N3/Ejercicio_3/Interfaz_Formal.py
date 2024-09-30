#Poli: Muchas , Morfismo: Formas
#Esta caracteristica es la capacidad que objetos similares tienen para responder 
# de diferentes formas al mismo mensaje, y permite al programador 
# implementar múltiples formas de un mismo método, 
# dependiendo cada una de ellas de la clase sobre la que se realice la implementacion.
#Esto permite acceder a varios métodos distintos utilizando el mismo medio de acceso(el mismo nombre).

##Ejemplo polimorfismo 
class Pato:
    def hablar(self):
        print("Cuack Cuack")
class Perro:
    def hablar(self):
        print("Guau")

class Gato:
    def hablar(self):
        print("Miau")

class Gallo:
    def hablar(self):
        print("¡Cocorocooo!")

lista = [Pato(), Perro(), Gato(), Gallo()]
for animal in lista:
    animal.hablar()

##Clase Abstracta
##No se pueden crear instancias  de estas clases. (Objetos)
##Contiene metodos que son abastractos, que no estan implementados
##Como cualquier otra superclase, definn caracteristicas comunes a los objetos
## que son instancias en subclases.
##Aumenta la comprension del problema, fomentando la reutilización del código
##y la extensibilidad


from abc import ABC, abstractmethod

class Forma(ABC):
    
    def __init__(self,nombre,color ):
        self.__nombre = nombre
        self.__color = color
        
    @abstractmethod
    def area (self):
        pass
    
class Circulo(Forma):
    
    def __init__(self, radio = 0,color = ""):
        super().__init__(nombre = "Circulo",color ="")
        self.__radio = radio
        
    def area(self):
        return 3.14 * self.__radio * self.__radio
    
##creo el objeto

circulo = Circulo(2,"Rojo")
print("Area del circulo:{}".format(circulo.area()))


##Interfaces definicion:
##Definen un conjunto de métodos que un objeto debe cumplir, pero no como.
##Nos permiten abstraer el "que" debe hacer, dejando en "como" para más tarde,
## para cuando se tenga que implementar la funcionalidad


##Interfaz Formal
#Una Clase abstracta (que hereda de ABC) con los metodos definidos abstractos
# y con subclases obligadas a darle la implementación

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def acelerar(self, velocidad):
        pass

    @abstractmethod
    def frenar(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Auto(Vehiculo):
    def arrancar(self):
        print("El auto arranca.")

    def acelerar(self, velocidad):
        print(f"El auto acelera a {velocidad} km/h.")

    def frenar(self):
        print("El auto frena.")

    def apagar(self):
        print("El auto se apaga.")


class Moto(Vehiculo):
    def arrancar(self):
        print("La moto arranca.")

    def acelerar(self, velocidad):
        print(f"La moto acelera a {velocidad} km/h.")

    def frenar(self):
        print("La moto frena.")

    def apagar(self):
        print("La moto se apaga.")

vehiculos = [Auto(),Moto()]

for vehiculo in vehiculos:
  vehiculo.arrancar()
  vehiculo.acelerar(60)
  vehiculo.frenar()
  vehiculo.apagar()
  print()
  
## Es mejor una interfaz mas especifica porque define métodos y comportamientos precisos 
# que una clase debe implementar. 
# Se utiliza cuando es necesario garantizar que las clases sigan un 
# conjunto particular de operaciones o comportamientos.
# Ademas de ser mejor para el control, claridad y asegurar comportamientos detallados.
