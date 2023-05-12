for b in range(0,151): # imprime todos los numeros enteros del 0 al 150.
    print(b)

for m in range(0,1001,5): # imprime todos los multiplos de 5 del 0 al 1000.
    print(m)

for c in range(1,101): # imprime números del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
    if c % 10 == 0: 
        print("Coding Dojo")
    elif c % 5 == 0: 
        print("Coding")
    else:
        print(c)

suma = 0
for w in range(0,500000): # agrega los enteros impares del 0 al 500,000, e imprime la suma final.
    if w % 2 != 0:
        suma = suma + w
print(f"la suma total es: {suma}")

for r in range(2018,0,-4): # imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
    print(r)

lowNum = 2
highNum = 9
mult = 3
for flexible in range(lowNum, highNum+1): # establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
    if flexible % mult == 0:
        print(flexible)
