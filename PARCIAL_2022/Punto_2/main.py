from Persona import Persona
from Familia import Familia

import random

numero_familias = random.randrange(1,10)

apellidos = ["Pérez","Rodriguez","Sanches","Mariqueo","Mariao","Nahuelanca","Velazques","Navarro","Mansilla","Caipichun","Pérez","Rodriguez","Sanches","Mariqueo","Mariao","Nahuelanca","Velazques","Navarro","Mansilla","Caipichun"]
nombres = ["Alexis","Facundo","Ismael","Samuel","Tamara","Viviana","Tamara","Rodrigo","Enzo","Ramiro","Alexis","Facundo","Ismael","Samuel","Tamara","Viviana","Tamara","Rodrigo","Enzo","Ramiro"]

for i in range(numero_familias):
    integrantes = random.randrange(1,10)
    apellido = random.choice(apellidos)
    lista_familia = Familia (apellido)
    for i in range(integrantes):    
        lista_familia.agregar_familiar(Persona(random.choice(nombres),apellido))
        
    lista_familia.mostrar_integrante()

        