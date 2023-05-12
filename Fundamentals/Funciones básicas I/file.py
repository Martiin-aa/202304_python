#1
def número_de_grupos_alimentarios(): # imprimirá 5
    return 5
print(número_de_grupos_alimentarios())

#2
def número_de_ramas_militares(): # imprimirá número_de_días_en_una_semana undefined 
    return 5
print(número_de_días_en_una_semana() + número_de_ramas_militares())

#3
def número_de_libros_en_espera(): # imprimirá 5
    return 5
    return 10
print(número_de_libros_en_espera())

#4
def número_de_dedos(): # imprimirá 5
    return 5
    print(10)
print(número_de_dedos())

#5
def número_de_lagos_grandes(): # imprimirá 5, y luego none
    print(5)
x = número_de_lagos_grandes()
print(x)

#6
def add(b,c): # imprimirá undifined
    print(b+c)
print(add(1,2) + add(2,3))

#7
def concatenar(b,c): # imprimirá error sintaxis incorrecto
    return str(b)+str(c)
="función de soporte python from-rainbow">print(concatenar(2,5))

#8
def número_de_océanos_o_dedos_o_continentes(): # imprimirá error de identamiento
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(número_de_océanos_o_dedos_o_continentes())

#9
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b,c): # imprimirá error de sintaxis y undefined
    if b<c:
        return 7
    else:
        return 14
    return 3
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3))
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))

#10
def addition(b,c): # imprimirá 8
    return b+c
    return 10
print(addition(3,5))

#11
b = 500
print(b)
def foobar(): # imprimirá 500 (2 veces), y luego dará un error por los signos
    b ="operador de palabra clave from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)

#12
b = 500
print(b)
def foobar(): # imprimirá 500, 500, 300, y luego 500
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#13
b = 500
print(b)
def foobar(): # imprimirá 500, 500, 300, y luego 300 
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#14
def foo(): # imprimirá 1, 3, y luego 2
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#15
def foo(): # imprimirá 1, 3, 5, y luego 10
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
