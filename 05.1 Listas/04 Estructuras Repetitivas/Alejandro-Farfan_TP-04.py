"""
Actividades
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
# Versión con bucle while
numero = 0
while numero <= 100:
    print(numero)
    numero += 1

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
    
    # Solicitar al usuario un número entero
numero = input("Ingrese un número entero: ")

# Verificar que el input sea un número entero válido
try:
    # Convertir a entero (esto también manejará el caso de números con signo)
    numero_int = int(numero)
    
    # Contar los dígitos (usamos el valor absoluto para manejar números negativos)
    cantidad_digitos = len(str(abs(numero_int)))
    
    print(f"El número {numero_int} tiene {cantidad_digitos} dígito(s).")
    
except ValueError:
    print("Error: Por favor ingrese un número entero válido.")

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("Ingrese otro numero: "))
resultado = 0

if primer_numero != segundo_numero:
    if primer_numero > segundo_numero:
        numero_max = primer_numero
        numero_min = segundo_numero
    else:
        numero_max = segundo_numero
        numero_min = primer_numero

    for i in range(numero_min+1, numero_max):
        resultado += i
    print(f"La suma es: {resultado}")

else:
    print("Los numeros son iguales.")

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

sumaTotal = 0
numero = int(input("Ingrese un numero: "))

while numero != 0:
  sumaTotal += numero
  numero = int(input("Ingrese un numero: "))

print(f"La suma total es: {sumaTotal}")

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
from random import randint

numero_aleatorio = randint(0,9)
contador_intentos = 1

numero = int(input("Ingrese un numero: "))

while numero != numero_aleatorio:
  contador_intentos += 1
  print("Numero incorrecto.")
  numero = int(input("Ingrese un numero: "))

print(f"Correcto!, El numero era: {numero_aleatorio} y necesitaste {contador_intentos} intentos.")

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
for i in range(100,-1, -1):
  if i % 2 == 0:
    print(i)

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
numero = int(input("Ingrese un numero: "))
suma_total = 0

if numero > 0:
  for i in range(numero+1):
    suma_total += i
  print(f"La suma total es {suma_total}")
else:
  print("EL numero debe ser positivo.")

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
def analizar_numeros():
    # Inicializar contadores
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    ceros = 0  # Para contar los ceros (no positivos ni negativos)
    
    # Solicitar al usuario la cantidad de números a ingresar (puede cambiarse fácilmente)
    cantidad_numeros = 100  # Cambiar este valor para pruebas con menos números
    
    print(f"Ingrese {cantidad_numeros} números enteros:")
    
    for i in range(cantidad_numeros):
        while True:
            try:
                numero = int(input(f"Número {i+1}: "))
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
        
        # Contar pares e impares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        # Contar positivos, negativos y ceros
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"- Números pares: {pares}")
    print(f"- Números impares: {impares}")
    print(f"- Números positivos: {positivos}")
    print(f"- Números negativos: {negativos}")
    print(f"- Ceros: {ceros}")

# Ejecutar el programa
analizar_numeros()

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
TOTAL_NUMEROS = 100
suma_total_numeros = 0
media_valores = 0

for i in range(TOTAL_NUMEROS):
  ingreso = int(input("Ingrese un numero: "))
  suma_total_numeros += ingreso

media_valores = suma_total_numeros / TOTAL_NUMEROS
print("La media es", media_valores)

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero = int(input("Ingrese un numero: "))

numero_invertido = 0
while numero > 0:
  digito = numero % 10
  numero_invertido = numero_invertido * 10 + digito

  numero = numero // 10

print(f"El numero invertido es: {numero_invertido}.")