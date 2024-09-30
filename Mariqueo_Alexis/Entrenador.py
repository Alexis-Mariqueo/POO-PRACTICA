class Entrenador():
    
    def __init__(self,nombre,nivel_entrenador: int,pokemon_principal) -> None:
        self.__nombre = nombre
        self.__nivel_entrenador = nivel_entrenador
        self.__pokemon_principal = pokemon_principal
        self.__pokedex = []
        
    def pokemon_entrenador(self,pokemon):
        self.__pokedex.append(pokemon)
        
    def Atrapar_pokemon(self,salvajismo,pokemon):
        if self.__nivel_entrenador>salvajismo:
            for i in self.__pokedex:
                ataque = i.Ataque_pokemon(pokemon.getTipo())
                daño = ataque
                pokemon.setSalvajismo(1.01)
                pokemon.setVida(pokemon.Defensa_pokemon(daño))
                if pokemon.getVida() > 0:
                    print(f"Vida pokemon:{pokemon.getVida()}")
                    print(f"Es posible capturar al pokemon {pokemon.getNombre()}")
                
            if pokemon.getVida() > 0:
                print("Pokemon Capturado")
                self.__pokedex.append(pokemon)
            else:
                print("No es posible capturar este pokemon con tan poca vida")  
        else:
            print("No es posible atrapar a el pokemon con ese nivel de entrenador")
            
    def mostrar_pokedex(self):
        print(f"Nombre Entrenador:{self.__nombre}")
        print(f"Nivel Entrenador:{self.__nivel_entrenador}")
        for poke in self.__pokedex:
            poke.mostrar_pokemon()