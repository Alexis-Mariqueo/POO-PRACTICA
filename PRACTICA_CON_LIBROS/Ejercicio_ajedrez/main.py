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
movimiento = [1,2]
while tablero_ajedrez.tiempo() >= 5.00 or  tablero_ajedrez.get_jaque() == True:
    opcion = 1
    tablero_ajedrez.tiempo()
    if opcion == 1:
        pieza = random.choice(lista_jugador_1)
        pieza.mover_pieza(random.choice(movimiento),random.choice(fila),random.choice(columna))
        if random.randrange(1,100) < 75:
            pieza_atacada = random.choice(lista_jugador_2) 
            pieza.atacar(pieza_atacada)
            lista_jugador_2.pop(pieza_atacada)
        if random.randrange(1,100) < 25:
            tablero_ajedrez.set_jaque()
            print("El jugador 1 hizo jaque")
            print("Tiempo jugado: {}".format(tablero_ajedrez.get_tiempo()))
            break
    opcion = opcion  + 1    
    if opcion ==2:
        pieza = random.choice(lista_jugador_2)
        pieza.mover_pieza(random.choice(movimiento),random.choice(fila),random.choice(columna))
        if random.randrange(1,100) < 75:
            pieza_atacada = random.choice(lista_jugador_1) 
            pieza.atacar(pieza_atacada)
            lista_jugador_1.pop(pieza_atacada)
        if random.randrange(1,100) < 25:
            tablero_ajedrez.set_jaque()
            print("El jugador 2 hizo jaque")
            print("Tiempo jugado: {}".format(tablero_ajedrez.get_tiempo()))
            break
    if tablero_ajedrez.tiempo() == 5.00:
        break
    
    
    
    
    