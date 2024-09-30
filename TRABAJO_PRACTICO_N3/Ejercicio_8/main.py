from ProfesorTitular import ProfesorTitular
from ProfesorSuplente import ProfesorSuplente

titulares = []
titulares.append(ProfesorTitular("Aldana","Gutierrez",40,40,15))
titulares.append(ProfesorTitular("Pedro","Perez",30,30,4))
titulares.append(ProfesorTitular("Maria","Gomez",29,40,1))
suplentes = []
suplentes.append(ProfesorSuplente("Tomas","Sosa",28,40))
suplentes.append(ProfesorSuplente("Luciana","Torres",35,40))

for titu in titulares:
    print("__________________________")
    titu.imprimir()
    print("__________________________")
    
for suple in suplentes:
    print("__________________________")
    suple.imprimir()
    print("__________________________")