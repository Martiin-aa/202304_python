from Clases import Ninja, Mascota, Perro , Gato

pet1 = Perro("Pluto", "puddle", "galletas","ladra")
pet2 = Gato("Noyah", "quiltro", "jamon", "maulla")
mascotas_lista = [pet1, pet2]
owner = Ninja("Martin", "Araya", 25, mascotas_lista[0])

owner.info()
pet1.info()
owner.alimentar().caminar().bañar()
