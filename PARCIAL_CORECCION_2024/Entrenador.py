

class Entrenador:
    
    def __init__(self,nombre,nivel,pokemon):
        self.__nombre = nombre
        self.__nivel_entrenador = nivel
        self.__pokemon_principal = pokemon ##Pokemon principal es un objeto de cualquier pokemon
        self.__pokedex_pokemon = []
        
    def atrapar_pokemon(self,pokemon_salvaje): ## En cada ataque se resta el 10% del salvajismo
        print("____________________________________________________________") ##Valor obtiene el resultado de restar el salvajismo original menos el 10% de ese salvajismo
        valor = int(pokemon_salvaje.getSalvajismo()-pokemon_salvaje.getSalvajismo()*0.10) #int es una funcion integrada que sirve para trabajar numeros enteros
        pokemon_salvaje.setSalvajismo(valor) #modifico el salvajismo del pokemon salvaje 
        self.__pokemon_principal.ataque(pokemon_salvaje) ## El pokemon principal ataca al pokemon salvaje
        if self.__nivel_entrenador > pokemon_salvaje.getSalvajismo() and pokemon_salvaje.getVida() > 0: ## Si el salvajismo es menor al nivel del entrenador y a su vez la vida no es menor a cero
            self.__pokedex_pokemon.append(pokemon_salvaje) ##capturo  al pokemon
            print("Pokemon salvaje capturado")
            return True ##retorno True
        if (pokemon_salvaje.getVida()<0): #Si el pokemon salvaje tiene poca vida no se puede capturar dicho pokemon
            print("Pokemon salvaje no puede ser atrapado por que su nivel de vida es 0")
            return False ## retorno False
            
         
    def imprimir(self):
        print("Nombre Entrenador:{}".format(self.__nombre))
        print("Nivel de Entrenador:{}".format(self.__nivel_entrenador))
        print("Pokedex")
        for poke in self.__pokedex_pokemon:
            poke.mostrar_pokemon()