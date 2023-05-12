# 1
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15 # Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
print(x)

estudiantes[0]['last_name'] = 'Bryant' # Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
print(estudiantes)

directorio_deportes['fútbol'][0] = 'Andrés' # En el directorio_deportes, cambia "Messi" por "Andrés".
print(directorio_deportes)

z[0]['y'] = 30 # Cambia el valor 20 en z a 30.
print(z)

# 2
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(estudiantes): # Crea una función para que, dada una lista de diccionarios,
    for i in estudiantes:           # la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.
        for llave, valor in i.items():
            print(f"{llave} - {valor}")
    return estudiantes
iterateDictionary(estudiantes)

# 3
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(nombreclave, estudiantes): # Crea una función que, dada una lista de diccionarios y un nombre clave,
    for i in estudiantes:                         # la función imprima el valor almacenado en esa clave para cada diccionario.
        print(i[nombreclave])                   
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

# 4
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):                  # Crea una función que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista,
    for llave, valor in dojo.items(): # y luego imprima los valores asociados dentro de la lista de cada clave.
        llave = llave.upper()
        print(f"{len(valor)} {llave}")
        for elemento in valor:
            print(elemento)
printInfo(dojo)
