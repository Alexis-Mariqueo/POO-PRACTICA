from Creator import Creator
from ConcreteCreatorJuegoDigital import ConcreteCreatorJuegoDigital
from ConcreteCreatorJuegoFisico import ConcreteCreatorJuegoFisico

def enviar_notificacion(creator: Creator) -> None:
    print(f"Cliente: Se le envia el comprobante del juego.\n"
        f"{creator.notificar_precio()}", end="")

print("Enviar notificacion importe Juego Fisico")
enviar_notificacion(ConcreteCreatorJuegoFisico())
print("\n")

print("Enviar notificacion importe Juego Digital")
enviar_notificacion(ConcreteCreatorJuegoDigital())