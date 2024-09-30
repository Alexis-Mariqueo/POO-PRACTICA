from Barbaro import Barbaro
from Caballero import Caballero
import random

barbaro_1 = Barbaro("Kracker")
caballero_1 = Caballero("Menfis")

turno = [1,2]


for i in range(0,5):
    opcion = random.choice(turno)
    if opcion == 1:
        print(f"El barbaro {barbaro_1.get_nombre()} ataca al caballero {caballero_1.get_nombre()}")
        caballero_1.set_vida(caballero_1.defender (barbaro_1.atacar()))
        print("Vida caballero: {}".format(caballero_1.get_vida()))
    if opcion == 2:
        print(f"El caballero {caballero_1.get_nombre()} ataca al barbaro {barbaro_1.get_nombre()}")
        barbaro_1.set_vida(barbaro_1.defender (caballero_1.atacar()))
        print("Vida Barbaro: {}".format(barbaro_1.get_vida()))

        
