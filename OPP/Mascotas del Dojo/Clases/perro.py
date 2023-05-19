from .owner import Mascota
# herencia de mascota.perro
class Perro(Mascota):
    def __init__(self, nombre, tipo, golosinas, sonido):
        super().__init__(nombre, tipo, golosinas, sonido)
