from Persona import Persona
from Familia import Familia
from Censo import Censo
import datetime
import random

censo = Censo(datetime.date(2024,9,27))

sexo = ["M","F"]
respuesta = [True, False]

lista_familia_1 = Familia()
lista_familia_2 = Familia()
lista_familia_3 = Familia()
lista_familia_4 = Familia()
lista_familia_5 = Familia()

for i in range(random.randrange(4,8)):
    i = Persona(random.randrange(13,65),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_1.agregar_persona(i)
    
for num in range(random.randrange(4,8)):
    num = Persona(random.randrange(1,98),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_2.agregar_persona(num)
    
for per in range(random.randrange(4,8)):
    per = Persona(random.randrange(1,98),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_3.agregar_persona(per)

for inte in range(random.randrange(4,8)):
    inte = Persona(random.randrange(1,98),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_4.agregar_persona(inte)
    
for perso in range(random.randrange(4,8)):
    perso = Persona(random.randrange(1,98),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_5.agregar_persona(perso)
    
opciones = [3,4,5]
genera = random.choice(opciones)

if genera == 3:
    censo.agregar_familia(lista_familia_1)
    censo.agregar_familia(lista_familia_2)
    censo.agregar_familia(lista_familia_3)
if genera == 4:
    censo.agregar_familia(lista_familia_1)
    censo.agregar_familia(lista_familia_2)
    censo.agregar_familia(lista_familia_3)
    censo.agregar_familia(lista_familia_4)
if genera == 5:
    censo.agregar_familia(lista_familia_1)
    censo.agregar_familia(lista_familia_2)
    censo.agregar_familia(lista_familia_3)
    censo.agregar_familia(lista_familia_4)
    censo.agregar_familia(lista_familia_5)
   
    
censo.mostrar_datos_censo()