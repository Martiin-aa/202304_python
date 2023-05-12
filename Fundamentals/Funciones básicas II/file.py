# 1
def cuentaRegresiva(numero): # Cuenta regresiva
    lista = []
    for c in range(numero, -1, -1):
        lista.append(c)
    return lista
print(cuentaRegresiva(10)) # imprime [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 2
def imprDevol(lista): # imprimir el 1er numero y devolver el 2do numero
    print(lista[0]) # imprime 2
    return lista[1]
imprDevol([2, 8])

# 3
def primMasLong(lista): # función q acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista
    suma = lista[0] + len(lista)
    return suma
lista = [1, 2, 3, 4, 5]
print(primMasLong(lista)) # imprimirá 6

# 4
def valMaySeg(lista): # función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor.
    if len(lista) < 2:
        return False 
    array = []
    for v in range(0,len(lista)):
        if lista[v] > lista[1]:
            array.append(lista[v])
    return array
print(valMaySeg([5, 2, 7, 3, 8])) # [5, 7, 3, 8]
print(valMaySeg([5])) # imprimirá false

# 5
def longValor(tamaño, valor):
    lista = tamaño * [valor]
    return lista
print(longValor(5, 5)) # imprimirá [5, 5, 5, 5, 5]
