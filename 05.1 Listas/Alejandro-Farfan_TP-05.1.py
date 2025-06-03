"""Actividades
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range
"""
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)
"""

2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
"""
mi_lista = ['pizza', 'viajar', 'música', 'libros', 'programar']  # Lista con 5 elementos
penultimo = mi_lista[3]  # El índice 3 corresponde al 4to elemento (penúltimo en lista de 5)
print(penultimo)  # Muestra: 'libros'

"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: 
lista_vacia = []
"""
# 1. Crear lista vacía
mi_lista = []

# 2. Agregar 3 palabras usando append()
mi_lista.append("casa")
mi_lista.append("arbol")
mi_lista.append("clima")

# 3. Imprimir la lista resultante
print(mi_lista)

"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla.
animales = ["perro", "gato", "conejo", "pez"]
"""
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazamos usando índices:
animales[1] = "loro"    # Segundo elemento (índice 1)
animales[-1] = "oso"    # Último elemento (índice -1)

print(animales)
"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

Explicación: El programa crea una lista de numeros. Luego utiliza la funcion remove y max, para remover el numero mas grande de la lista.
Por ultimo muestra por consola la lista modificada.
"""

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
"""

lista_10_al_30 = list(range(10, 31, 5))
print(lista_10_al_30[0:2])

"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
"""
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "206"
autos[2] = "308"
print(autos)

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
"""

dobles:list = []
doble_append:list = [5, 10, 15]

for n in doble_append:
    dobles.append(n*2)

print(dobles)

"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
"""
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)
"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
"""
lista_anidada = [
    15,                # Posición [0]
    True,              # Posición [1]
    [25.5, 57.9, 30.6], # Posición [2] (lista con 3 elementos)
    False              # Posición [3]
]

print(lista_anidada)

