class Ninja:
    # implementar __init__( nombre, apellido, premios, mascota).
    def __init__(self, nombre, apellido, premios, mascota):
        self.name = nombre
        self.lastname = apellido
        self.awards = premios
        self.pet = mascota
# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar().
    def caminar(self):
        self.pet.jugar()
        return self
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer().
    def alimentar(self):
        self.pet.comer()
        return self
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido().     
    def bañar(self):
        self.pet.sonido()
        return self
# info() - imprime la informacion del perfil del dueño.
    def info(self):
        print(f"Perfil del dueño\nNombre: {self.name}\nApellido: {self.lastname}\nPremios: {self.awards}\n")

class Mascota:
    # implementar __init__( name , tipo , golosinas, sonido).
    def __init__(self, nombre, tipo, golosinas, sonido):
        self.name = nombre
        self.type = tipo
        self.candies = golosinas
        self.energy = 0
        self.health = 0
        self.noise = sonido
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25.
    def dormir(self):
        self.energy += 25
        print(f"incremento de la energia de {self.name} a {self.energy} al dormir")
        return self
# comer() - incrementa la energía de la mascota en 5 y la salud en 10.
    def comer(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} al alimentarse incrementa su energia a {self.energy} y su salud a {self.health}")
        return self
# jugar() - incrementa la salud de la mascota en 5.
    def jugar(self):
        self.health += 5
        print(f"incremento de la salud de {self.name} a {self.health} al caminar")
        return self
# ruido() - imprime el sonido que produce la mascota
    def sonido(self):
        print(f"{self.name} {self.noise} al bañarse")
        return self
# info() - imprime la informacion del perfil da las mascotas.
    def info(self):
        print(f"Perfil de mascota\nNombre: {self.name}\nTipo: {self.type}\nGolosina: {self.candies}\n")
        return self
