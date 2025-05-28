""" Ejercicios
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
4! = 4 * 3 * 2 * 1 = 24
 """

def factorial(nro):
    if nro == 1:
        return 1
    return nro * factorial(nro-1)

ejer1 = int(input("Ingrese el numero hasta el cual calcular el factorial: "))

for i in range(1, ejer1+1):
    print(f"El factorial de {i} es {factorial(i)}.")

""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. """

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-2) + fibonacci(pos-1)
    
ejer2 = int(input("Ingrese el numero hasta el cual calcular la serie Fibonacci: "))

for i in range(ejer2+1):
    print(f"En la posición {i}, Fibonacci {fibonacci(i)}")

""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente. Prueba esta función en un algoritmo general. """

def potencia(base, exp):
     if exp == 0:
         return 1
     else:
            return base * potencia(base, exp - 1)

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")



""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto. """

def decimal_binario(n):
    if n == 0:
        return ""
    else:
            return decimal_binario(n // 2) + str(n % 2)
numero = int(input("Ingrese el número decimal: "))
binario = decimal_binario(numero)
print(f"El número {numero} en binario es: {binario if binario else '0'}")

""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print(f"Es {texto} un palindromo? {es_palindromo(texto)}")


""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

def suma_digitos(n):
     if n == 0:
         return 0
     else:
         return(n % 10) + suma_digitos(n // 10)
numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los digitos de {numero} es {suma_digitos(numero)}")

""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
 """

def contar_bloques(n):
     if n == 1:
         return 1
     else:
        return n + contar_bloques(n - 1)

fila_de_abajo = int(input("Ingrese el número de bloques en el nivel mas bajo: "))
print(f"El número de bloques total utilizado es de {contar_bloques(fila_de_abajo)}")


""" 
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4 
 """
def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    # Tomamos el último dígito del número
    ultimo_digito = numero % 10
    # Verificamos si el último dígito es igual al dígito buscado
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
        print(contar_digito(12233421, 2))  # Output: 3
print(contar_digito(5555, 5))      # Output: 4
print(contar_digito(123456, 7))    # Output: 0
