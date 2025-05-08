 #1)Crear un programa que imprima por pantalla: "Hola Mundo!"
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

#Pedir al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")
#imprimir el saludo usando f-strin
print(f"hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su pais: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais} ")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
#solicitar al usuario el radio del circulo
radio = float(input("introduce el radio del circulo:"))
#calcular el area (π*r²) y perimetro (2πr)
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
#mostrar resultados
print(f"el area del circulo con radio {radio} es {area}")
print(f"el perimetro del circulo con radio {radio} es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 
#pedir al usuario la cantidad de segundos
segundos = float(input("ingrese la cantidad de segundos:"))
#convertir el segundo a horas
horas = segundos / 3600 
#mostrar el resultado
print(f"{segundos} segundos equivalen a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
#pedir al usuario que ingrese uun numero
numero = int(input("por favor ingrese el numero para generar la tabla de multiplicar:"))
#imprimir la tabla de multiplicar del 1 al 10
print(f"tabla de multiplicar {numero}:")
for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i}={resultado}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
#pedir al usurio que ingrese dos numeros enteros distintos de cero
print("Por favor, ingresa dos numeros enteros distintos de cero")
num1 = int(input("Primer numero:"))
num2 = int(input("Segundo numero:"))
#verificar que ninguno sea cero
while num1 == 0 or num2 == 0:
    print("Error: Amdos numeros deben ser distintos de cero")
#Realizar las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
#mostrar los resultados
print("Resultados:")
print(f"suma : {num1}+{num2}={suma}")
print(f"resta : {num1}-{num2}={resta}")
print(f"multiplicacion : {num1}*{num2}={multiplicacion}")
print(f"division : {num1}/{num2}={division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
#solicitar al usuario su altura (en metros) y su peso (en kilogramos)
print("Calcularoda de indice de masa corporal(IMC)")
altura = float(input("Ingrese su altura en metros:"))
peso = float(input("Ingrese su peso en kilogramos:"))
#calcular el IMC
IMC = peso/(altura**2)
#mostrar el resultado 
print(f"Tu indice de masa corporal(IMC) es:{IMC:.2f}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
#solicitar al usuario la temperatura en celsius
celsius = float(input("Ingresa la temperatura en grados celsius:"))
#calcular la conversion a fahrenheit
fahrenheit =(celsius*9/5)+32
#mostrar el resultado
print(f"{celsius}°C equivalen a {fahrenheit:.1f}°F")
#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.
print("Calculadora de promedio de tres numeros")
#solicitar los tres numeros al usuario
num1 = float(input("Ingresa el primer numero:"))
num2 = float(input("Ingresa el segundo numero:"))
num3 = float(input("Ingresa el tercer numero:"))
#calcula el promedio
promedio = (num1+num2+num3)/3
#mostrar el resultado
print(f"El promedio de {num1},{num2}y{num3} es: {promedio}")