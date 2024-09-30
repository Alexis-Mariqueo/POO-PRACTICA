from Cocina import Cocina
from Heladera import Heladera
from Lavarropa import Lavarropas
import random

lista_heladeras = []
lista_cocinas = []
lista_lavarropas = []

marca = ["Escorial","Gafa","LG"] 
color = ["rojo","negro","blanco","gris"]
booleano = ["Si","No"]

for i in range(0,11):
    lista_cocinas.append(Cocina(f"Cocina_{i}",random.randrange(200000,1800000),marca[0],random.choices(color),random.choices(booleano)))
    lista_heladeras.append(Heladera(f"Heladera_{i}",random.randrange(200000,1800000),marca[1],random.choices(color),f"{random.randrange(75,700)} Lt",f"{random.randrange(100,300)} Lt"))
    lista_lavarropas.append(Lavarropas(f"Lavarropa_{i}",random.randrange(200000,1800000),marca[2],random.choices(color),random.choices(booleano),f"{random.randrange(6,13)} Kg"))
        
random.shuffle(lista_cocinas)
random.shuffle(lista_heladeras)
random.shuffle(lista_lavarropas)

cocina_no_repe= random.sample(lista_cocinas,3)

for coci in cocina_no_repe:
    print("________________________")
    coci.imprimir()
    print("________________________")
    
heladera_no_repe = random.sample(lista_heladeras,3)

for hela in heladera_no_repe:
    print("________________________")
    hela.imprimir()
    print("________________________")
    
lavarropa_no_repe = random.sample(lista_lavarropas,3)
    
for lava in lavarropa_no_repe:
    print("________________________")
    lava.imprimir()
    print("________________________")
   
opciones = ["1","2","3"]

print("PRODUCTOS MAS RECOMENDADOS")
print("___________________________________________________")
for i in range (0,3):
    opcion = random.choice(opciones)
    if opcion == "1":
        cocina = random.sample(lista_cocinas,1)
        for i in cocina:
            print("_________________________")
            i.imprimir()
            print("_________________________")
    if opcion == "2":
        heladera = random.sample(lista_heladeras,1)
        for i in heladera:
            print("_________________________")
            i.imprimir()
            print("_________________________")
    if opcion == "3":
        lavarropa = random.sample(lista_lavarropas,1)
        for i in lavarropa:
            print("_________________________")
            i.imprimir()
            print("__________________________")
print("___________________________________________________")