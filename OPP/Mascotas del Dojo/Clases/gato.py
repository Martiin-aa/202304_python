from .owner import Mascota
# herencia de mascota.gato
class Gato(Mascota):
    def __init__(self, nombre, tipo, golosinas, sonido):
        super().__init__(nombre, tipo, golosinas, sonido)
