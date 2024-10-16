from ConcretoTorta import ConcretoTorta
from Director import Director

concreta_torta_1 = ConcretoTorta()
director_1 = Director(concreta_torta_1)


print("__________________________________________________")
director_1.torta_vainilla()
torta_simple=director_1.get_torta()
torta_simple.imprimir()
print("__________________________________________________")
director_1.torta_coco()
torta_basica=director_1.get_torta()
torta_basica.imprimir()
print("__________________________________________________")
director_1.torta_chocolate()
torta_full=director_1.get_torta()
torta_full.imprimir()
print("__________________________________________________")