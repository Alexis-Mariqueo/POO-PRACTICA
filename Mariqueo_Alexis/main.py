from Hierba import Hierba
from Fuego import Fuego
from Agua import Agua
from Entrenador import Entrenador
import random

lista_nombres = ["Sonic","Tails","Amy","Shadow","Jacket","Eggman","Knuckles","Rayman"]
lista_pokemon = []
lista_aleatoria_pokemon = []


entrenador = Entrenador("Alexis",random.randint(1,100),"Sonic")
for i in range(10):
    nombre_hierva = random.choice(lista_nombres)
    hierba = Hierba(nombre_hierva)
    nombre_fuego = random.choice(lista_nombres)
    fuego = Fuego(nombre_fuego)
    nombre_agua = random.choice(lista_nombres)
    agua = Agua(nombre_agua)
    lista_pokemon.append(hierba)
    lista_pokemon.append(fuego)
    lista_pokemon.append(agua)
    lista_aleatoria_pokemon.append(random.choice(lista_pokemon))

    
random.shuffle(lista_aleatoria_pokemon)

for i in range(3):
    entrenador.pokemon_entrenador(random.choice(lista_aleatoria_pokemon))

pokemon = random.choice(lista_aleatoria_pokemon)


entrenador.mostrar_pokedex()
entrenador.Atrapar_pokemon(pokemon.getSalvajismo(),pokemon)    