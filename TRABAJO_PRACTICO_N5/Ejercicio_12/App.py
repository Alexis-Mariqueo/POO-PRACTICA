from Pelicula import Pelicula
from Streaming import Streaming
from CatalogoCompleto import CatalogoCompleto
from CatalogoMenor import CatalogoMenor
from CatalogoMenor18 import CatalogoMenor18

lista_peliculas = [Pelicula('Kung Fu Panda',13),Pelicula('Star Wars',16),Pelicula('El club de la Pelea',16),Pelicula('Minions',8),Pelicula('Megamente',8),Pelicula('Sonic: La pelicula',8),Pelicula('El Resplandor',18)]

max = Streaming()

print("_____________________________________________________")
print("Catalogo Completo")
max.set_estrategia_catalogo(CatalogoCompleto())
max.catalogo(lista_peliculas)
print("_____________________________________________________")
print("Catalogo Menor de 18")
max.set_estrategia_catalogo(CatalogoMenor18())
max.catalogo(lista_peliculas)
print("_____________________________________________________")
print("Catalogo Menor de 13")
max.set_estrategia_catalogo(CatalogoMenor())
max.catalogo(lista_peliculas)
print("_____________________________________________________")