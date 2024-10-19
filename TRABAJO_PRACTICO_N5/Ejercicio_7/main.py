from Facade import Facade
from Helper import Helper
from CaseHelper import CaseHelper

#El Cliente utiliza la fachada en lugar de invocar directamente los objetos del subsistema.

facade = Facade(Helper(),CaseHelper())

words = ["Hola", "Perro","Gato"]

for word in words:
    print("________________________________________________")
    print(facade.operation(word))
    print("________________________________________________")