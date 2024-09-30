from Cocina import Cocina
from Lavarropa import Lavarropa
import random

cocina = Cocina(f"N{random.randrange(1000000,9999999)}","Escorial",random.randrange(300000,2500000),"No",4)
lavarropa = Lavarropa(f"N{random.randrange(1000000,9999999)}","Drean",random.randrange(250000,1500000),"No",f"{random.randrange(7,12)} kg")

print("___________________________________")
cocina.mostrar_informacion()
print("___________________________________")
lavarropa.mostrar_informacion()
print("___________________________________")