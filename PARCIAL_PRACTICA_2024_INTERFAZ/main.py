from BronceEspecial import BronceEspecial
from Especial import Especial
from Oro import Oro
from Plantilla import Plantilla
import random

lista_habilidades = ["Ataque","Pase","Defensa"]
lista_clubes=["Arsenal","MonteVideo City Torque","Inter Miami","Manchester City"]
lista_paises =["Argentina","Inglaterra","Holanda","Japon"]
opciones = [1,2,3]
usuario_1 = Plantilla("Alexis",random.choice(lista_paises),random.choice(lista_clubes))
usuario_2 = Plantilla("Gonzalo",random.choice(lista_paises),random.choice(lista_clubes))
lista_jugadores_1 = []
lista_jugadores_2 = []

for i in range(0,22):
    opcion = random.choice(opciones)
    if i <= 11:
        if opcion == 1:
            bronce = BronceEspecial (f"jugador_{i}",random.choice(lista_clubes),random.choice(lista_paises),random.choice(lista_habilidades))
            lista_jugadores_1.append(bronce)
        if opcion == 2:
            oro = Oro(f"jugador_{i}",random.choice(lista_clubes),random.choice(lista_paises))
            lista_jugadores_1.append(oro)
        if opcion == 3:
            especial = Especial(f"jugador_{i}",random.choice(lista_clubes),random.choice(lista_paises))
            especial.agregar_habilidad(f"{random.choices(lista_habilidades,k = random.randint(1,3))}")
            lista_jugadores_1.append(especial) 
    else:
        if opcion == 1:
            bronce = BronceEspecial (f"jugador_{i}",random.choice(lista_clubes),random.choice(lista_paises),random.choice(lista_habilidades))
            lista_jugadores_2.append(bronce)
        if opcion == 2:
            oro = Oro(f"jugador_{i}",random.choice(lista_clubes),random.choice(lista_paises))
            lista_jugadores_2.append(oro)
        if opcion == 3:
            especial = Especial(f"jugador_{i}",random.choice(lista_clubes),random.choice(lista_paises))
            especial.agregar_habilidad(random.choices(lista_habilidades,k = random.randint(1,3)))
            lista_jugadores_2.append(especial)



random.shuffle(lista_jugadores_1)
random.shuffle(lista_jugadores_2)

for i in lista_jugadores_1:
    usuario_1.agregar_carta(i)
    
for num in lista_jugadores_2:
    usuario_2.agregar_carta(num)
    
usuario_1.imprimir_plantel()
usuario_2.imprimir_plantel()