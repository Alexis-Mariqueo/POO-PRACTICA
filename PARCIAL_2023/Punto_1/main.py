from Ticket import Ticket
from Producto import Producto

ticket = Ticket("30/9/2024")
producto = ["Adermicina","Ibuprofeno","Diclofenac"]
dosis = [30,600,75]
precio = [1000,2500,3000]

for i in range(0,3):
    ticket.agregar_producto(Producto(producto[i],dosis[i],precio[i]))
    
ticket.imprimir_ticket()
