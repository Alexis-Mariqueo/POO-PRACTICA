from ConcreteCreatorJuegoDigital import ConcreteCreatorJuegoDigital
from ConcreteCreatorJuegoFisico import ConcreteCreatorJuegoFisico

juego_digital = ConcreteCreatorJuegoDigital()
juego_fisico = ConcreteCreatorJuegoFisico()

juego_digital.creador_juego()
juego_fisico.creador_juego()