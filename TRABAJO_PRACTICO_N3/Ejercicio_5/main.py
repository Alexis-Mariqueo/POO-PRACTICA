from Barbaro import Barbaro
from Caballero import Caballero
from Miexcepcion import Miexcepcion
import random

barbaro_1 = Barbaro("Kracker")
caballero_1 = Caballero("Menfis")

turno = [1,2]

ex = Miexcepcion("")
de = Miexcepcion("")

for i in range(0,3):
    try:
        opcion = random.choice(turno)
        if opcion == 1:
            print(f"El barbaro {barbaro_1.get_nombre()} ataca al caballero {caballero_1.get_nombre()}")
            caballero_1.set_vida(caballero_1.defender (barbaro_1.atacar()))
            ex.metodo(caballero_1.get_vida(),caballero_1.get_nombre())
            print("Vida caballero: {}".format(caballero_1.get_vida()))
        if opcion == 2:
            print(f"El caballero {caballero_1.get_nombre()} ataca al barbaro {barbaro_1.get_nombre()}")
            barbaro_1.set_vida(barbaro_1.defender (caballero_1.atacar()))
            ex.metodo(barbaro_1.get_vida(),barbaro_1.get_nombre())
            print("Vida Barbaro: {}".format(barbaro_1.get_vida()))
    except Miexcepcion as ex:
        print(ex.mensaje)
        if caballero_1.get_vida() <0:
            caballero_1.set_vida(0)
            print(f"Vida de caballero: {caballero_1.get_vida()}")
        if barbaro_1.get_vida() < 0:
            barbaro_1.set_vida(0)
            print(f"Vida de barbaro: {barbaro_1.get_vida()}")
        break
        
        

        
