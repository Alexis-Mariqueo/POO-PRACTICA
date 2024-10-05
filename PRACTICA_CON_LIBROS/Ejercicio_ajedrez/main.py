from Peon import Peon
from Caballo import Caballo
from Alfil import Alfil
from Torre import Torre
from Reina import Reina
from Rey import Rey
from Tablero import Tablero
import random 

lista_jugador_1 = []
lista_jugador_2 = []

tablero_ajedrez = Tablero()

for i in range(0,7):
    lista_jugador_1.append(Peon())
    lista_jugador_2.append(Peon())
    
for i in range(0,1):
    lista_jugador_1.append(Alfil())
    lista_jugador_1.append(Caballo())
    lista_jugador_1.append(Torre())
    lista_jugador_2.append(Alfil())
    lista_jugador_2.append(Caballo())
    lista_jugador_2.append(Torre())
    
lista_jugador_1.append(Reina())
lista_jugador_1.append(Rey())
lista_jugador_2.append(Reina())
lista_jugador_2.append(Rey())

fila = [1,2,3,4,5,6,7,8]
columna = ["a","b","c","d","f","g","h"]
while (tablero_ajedrez.get_tiempo() > 0.00 or  tablero_ajedrez.get_jaque() == False) or lista_jugador_1 != 0 or  lista_jugador_2 != 0:
    opcion = 1
    tablero_ajedrez.set_tiempo(tablero_ajedrez.tiempo())
    if opcion == 1:
        pieza = random.choice(lista_jugador_1)
        pieza.mover_pieza(random.choice(fila),random.choice(columna))
        if random.randrange(1,100) < 75:
            pieza_atacada = random.choice(lista_jugador_2) 
            pieza.ataque(pieza_atacada,random.choice(fila),random.choice(columna))
            lista_jugador_2.remove(pieza_atacada)
        if random.randrange(1,100) < 10:
            tablero_ajedrez.set_jaque()
            print("El jugador 1 hizo jaque")
            print("Tiempo jugado: {}".format(tablero_ajedrez.get_tiempo()))
            break
    opcion = opcion  + 1
    tablero_ajedrez.set_tiempo(tablero_ajedrez.tiempo())    
    if opcion ==2:
        pieza2 = random.choice(lista_jugador_2)
        pieza2.mover_pieza(random.choice(fila),random.choice(columna))
        if random.randrange(1,100) < 75:
            pieza_atacada = random.choice(lista_jugador_1) 
            pieza2.ataque(pieza_atacada,random.choice(fila),random.choice(columna))
            lista_jugador_1.remove(pieza_atacada)
        if random.randrange(1,100) < 10:
            tablero_ajedrez.set_jaque()
            print("El jugador 2 hizo jaque")
            print("Tiempo jugado: {}".format(tablero_ajedrez.get_tiempo()))
            break
        tablero_ajedrez.set_tiempo(tablero_ajedrez.tiempo())
    if tablero_ajedrez.get_tiempo() >= 5.00 or(lista_jugador_1 == 0 or lista_jugador_2 == 0):
        break

    
    
    