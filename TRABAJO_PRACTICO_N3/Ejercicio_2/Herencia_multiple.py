class Padre():
  def __init__(self):
    print("hola desde clase padre")

class Madre():
  def __init__(self):
    print("hola desde la clase madre")

class Hijo(Padre,Madre):
  def __init__(self):
    super().__init__()
    print("Hola desde la clase hijo")

hijo = Hijo()

### Herencia múltiple
#La idea de la herencia múltiple es poder heredar de más de una clase. 
# Es una lógica más intuitiva con respecto al mundo real.
#El concepto cambia ya que debemos pensar al objeto como una combinación de varias clases
# que no se superponen. Por ejemplo un Maratonista es en parte Deportista, Padre, Hombre, etc...
#  " un A puede ser visto como un B"#

##Problema que se presenta al implementar herencia multiple es el problema del diamante
#Se llama así porque si hiciéramos un diagrama UML dibujaria un diamante. 
# El problema es identificar cómo es el orden de llamadas cuando tenemos 
#una superclase de las cuales heredan dos clases y a su vez estas son padre de otra clase más
##Los otros problemas que se pueden presentar son:
# AMBIGUEDAD: El uso de herencias a apartir de clases con metodos 
# que tienen los mismo nombres pero significado diferente.
#El aumento de tiempo auxiliar que se añade a los programas

#COLISIONES: SE PRODUCEN CUANDO DOS O MÁS SUPERCLASES DIFERENTES TIENEN
#EL MISMO NOMBRE PARA ALGÚN ELEMENTO EN SUS INTERFACES

#SOLUCION PARA EL PROBLEMA:

#### Method Resolution Order (MRO)
#Python usa el algoritmo C3 de linearización para determinar el MRO. 
# Define la secuencia en las cuales las clases base son buscadas 
# cuando se busca un método o atributo de un objeto. Importante para evitar ambigüedades y conflictos.

class A:
    def saludo(self):
        print("Hola desde A")

class B(A):
    def saludo(self):
        print("Hola desde B")

class C(A):
    def saludo(self):
        print("Hola desde C")

class D(B, C):
    pass

obj = D()
obj.saludo()

#hola alexis
