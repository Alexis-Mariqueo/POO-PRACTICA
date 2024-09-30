from Hierba  import Hierba
from Fuego import Fuego
from Agua import Agua
from Entrenador import Entrenador
import random

lista_pokemones_salvajes = []
opciones = ["Agua","Fuego","Hierba"]

for i in range(0,11): ##Creo 10 pokemones
    opcion = random.choice(opciones) ##segun que opcion toque hago un pokemon del tipo
    if opcion == "Agua":
        lista_pokemones_salvajes.append(Agua(f"Agua_{i}"))
    if opcion == "Fuego":
        lista_pokemones_salvajes.append(Fuego(f"Fuego_{i}"))
    if opcion == "Hierba":
        lista_pokemones_salvajes.append(Hierba(f"Hierba_{i}")) 
    
random.shuffle(opciones) ##mezclo las opciones

entrenador = Entrenador("Alexis", random.randrange(0,100),lista_pokemones_salvajes[0]) ### creo el objeto de la clase entrenador



for pokemon in lista_pokemones_salvajes:
    posibilidades = 0 ## el contador se inicia en cero por cada intento
    while(posibilidades<3): ## Si los intentos son menores a tres se ejecuta el bucle
        posibilidades = posibilidades+1 ## se incrementa el contador en 1
        print('El entrenador realizo un ataque al pokemon {}'.format(pokemon.getNombre()))
        res = entrenador.atrapar_pokemon(pokemon) ## res guarda el valor que da en la simulacion
        if(res == True): ### si es verdadero
            print('El pokemon {} ha sido atrapado'.format(pokemon.getNombre()))
            pass
        if(res == False): ##si es falso
            print("El pokemon {} no ha podido ser atrapado".format(pokemon.getNombre()))
            pass



entrenador.imprimir()  ## muestra el entrenador


