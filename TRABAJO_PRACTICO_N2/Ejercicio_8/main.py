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

for i in range(random.randrange(4,8)):
    i = Persona(random.randrange(13,65),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_1.agregar_persona(i)
    
for num in range(random.randrange(4,8)):
    num = Persona(random.randrange(1,98),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_2.agregar_persona(num)
    
for per in range(random.randrange(4,8)):
    per = Persona(random.randrange(1,98),random.choice(sexo),random.choice(respuesta),random.choice(respuesta))
    lista_familia_3.agregar_persona(per)
    
censo.agregar_familia(lista_familia_1)
censo.agregar_familia(lista_familia_2)
censo.agregar_familia(lista_familia_3)

censo.mostrar_censo()    

    


