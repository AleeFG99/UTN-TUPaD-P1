"""1. Algoritmo de busqueda
a. Busqueda lineal (O(n))

"""

def busqueda_lineal(lista, objetivo):

    #Busca un elemento en una lista (no necesita estar ordenada)

    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i # Devuelve el indice si lo encuentra
    return -1  #No  encontrado

import time
import random
tamaño_lista = 50000
lista = random.sample(range(1, 100000), tamaño_lista)  # Lista de números únicos


# Elegir un objetivo aleatorio
objetivo = random.choice(lista)

# Medir tiempo de búsqueda lineal
inicio_lineal = time.time()
resultado_lineal = busqueda_lineal(lista, objetivo)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Búsqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo_lineal:.6f} segundos")




"""b. Busqueda Binaria (O(logn))

"""

def busqueda_binaria(lista, objetivo):

    #Requere lista ordenada previamente
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

lista_ordenada = sorted(lista)  # Lista ordenada para búsqueda binaria
# Medir tiempo de búsqueda binaria
inicio_binaria = time.time()
resultado_binaria = busqueda_binaria(lista_ordenada, objetivo)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria

# Resultados
print(f"Búsqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo_lineal:.6f} segundos")

print(f"Búsqueda Binaria: Resultado = {resultado_binaria}, Tiempo = {tiempo_binaria:.6f} segundos")






"""2. Algoritmo de Ordenamiento 
a. Ordenamiento de Burbuja (O(n²))

"""
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]  # Intercambio
    return lista

# Ejemplo:

lista = [64, 34, 25, 12, 22, 11, 90]

print(ordenamiento_burbuja(lista.copy()))  # [11, 12, 22, 25, 34, 64, 90]



""" b. Ordenamiento por Seleccion (O(n²))
"""
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i   # Encuentra el minimo en la lista que desordenada 
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j

        #Intercambia el minimo con el primer elemento desordenado.

        lista[i], lista[min_idx] = lista[min_idx], lista[i]   
    return lista

# Ejemplo:
print(ordenamiento_seleccion(lista.copy()))  # [11, 12, 22, 25, 34, 64, 90]



""" c. Ordenaminto por insercion (O(n²))
"""

def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]  #Elemento a insertar
        j = i-1
        #Mueve los elementos que la clave hacia la derecha
        while j >=0 and clave < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave #Inserta la clave en su posicion correcta
    return lista

# Ejemplo:
print(ordenamiento_insercion(lista.copy()))  # [11, 12, 22, 25, 34, 64, 90]



""" d. QuickSort (O(n long n) promedio)

"""
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista)//2] #Elemento del medio
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

# Ejemplo:
print(quicksort(lista.copy()))  # [11, 12, 22, 25, 34, 64, 90]



""" 3. Comparacion de rendimiento 

"""
import time
import random

# Generar lista aleatoria grande
datos_grandes = random.sample(range(1, 100000), 10000)

def medir_tiempo(func, datos):
    inicio = time.time()
    func(datos.copy())
    return time.time() - inicio

# Resultados:
print(f"Burbuja: {medir_tiempo(ordenamiento_burbuja, datos_grandes):.4f} segundos")
print(f"Selección: {medir_tiempo(ordenamiento_seleccion, datos_grandes):.4f} segundos")
print(f"Inserción: {medir_tiempo(ordenamiento_insercion, datos_grandes):.4f} segundos")
print(f"QuickSort: {medir_tiempo(quicksort, datos_grandes):.4f} segundos")
