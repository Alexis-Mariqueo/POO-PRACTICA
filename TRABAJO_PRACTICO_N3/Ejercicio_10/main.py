from Docente import Docente
from NoDocente import Nodocente
from Reloj import Reloj
import random

opciones = [1,2]
sector = ["Simple","Semiexclusiva","Exclusiva"]
jornada = ["Completa","Reducida"]
lista_personal = []

for i in range(0,10):
    opcion = random.choice((opciones))
    if opcion == 1:
        lista_personal.append(Reloj(Docente(f"Docente_{i}",random.randrange(2,30),random.choice(sector))))
    else:
        lista_personal.append(Reloj(Nodocente(f"No_Docente_{i}",random.randrange(2,30),random.choice(jornada))))
        
for perso in lista_personal:
    print("____________________________________")
    perso.mostrar_informe()
    print("____________________________________")