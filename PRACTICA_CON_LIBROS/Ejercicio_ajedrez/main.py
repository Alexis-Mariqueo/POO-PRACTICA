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


while tablero_ajedrez.tiempo() >= 8.00 or  tablero_ajedrez.jaque():
    opcion = 1
    tablero_ajedrez.tiempo()
    if opcion == 1:
        pass
    opcion = opcion  + 1    
    if opcion ==2:
        
        
    
    
    