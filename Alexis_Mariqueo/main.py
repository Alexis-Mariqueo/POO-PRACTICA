from Paquete import Paquete
from Furgoneta import Furgoneta
from Cartero import Cartero
from GestorEnvios import GestorEnvios
import random

gestionar = GestorEnvios()

lista_transporte = [] ##Creo una lista de transporte
opciones = [1,2] 

liviano = Paquete(4,5,5,5)
pesado = Paquete(7,8,8,8)

for i in range(0,3):
    opcion = random.choice(opciones)
    if opcion == 1:
        lista_transporte.append(Furgoneta())
    if opcion == 2:
        lista_transporte.append(Cartero())

gestionar.gestionar_envio(lista_transporte,liviano,100)
gestionar.gestionar_envio(lista_transporte,pesado,100)
##Utilice interfaz formal porque no tiene sentido que un Cartero sea un transporte
##Si lo haria de otra forma seria que transporte sea una  clase concreta en el cual<
##segun su tipo haria un calculo_distinto 
##Los atributos serian los mismos tipo,velocidad_promedio,costo,valor_hora,tiempo,costo
##Los metodos serian get_tiempo ,get_costo,get_tipo, transportar_paquetes que tenga de parametro
##el tipo de transporte,agregaria un metodo que segun el tipo devuelva un valor_distinto
##Si bien no implemento polimorfismo, es porque las clases que dieron en el ejemplo no tienen herencia conceptualmente 
