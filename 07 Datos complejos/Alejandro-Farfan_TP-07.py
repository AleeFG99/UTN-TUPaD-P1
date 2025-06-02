"""Actividades
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Verificar el diccionario actualizado
print(precios_frutas)


"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""

# Diccionario actual (resultado del punto anterior)
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizar los precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)


"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
# Diccionario actualizado (resultado de los puntos anteriores)
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Crear una lista solo con los nombres de las frutas (claves del diccionario)
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print(lista_frutas)

"""4)
Escribí un programa que permita almacenar y consultar números telefónicos.
Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:
contactos = {"Juan": "123456", "Ana": "987654"} # Consultar: "Juan" muestra "123456"
"""
# Crear un diccionario para almacenar los contactos
contactos = {}

print("Carga de 5 contactos:")

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = telefono

# Consultar un contacto
print("\nConsulta de contactos:")
nombre_consulta = input("Ingrese el nombre a consultar: ")

# Buscar y mostrar el número si existe
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto {nombre_consulta} en la agenda.")

"""5)Solicita al usuario una frase e imprime:
Las palabras únicas (usando un set).
Un diccionario con la cantidad de veces que aparece cada palabra.
Ejemplo:
#Entrada -> "hola mundo hola"

#Salida:

Palabras_únicas: {'hola', 'mundo'}

Recuento: {'hola': 2, 'mundo': 1}

"""

# Solicitar la frase al usuario
frase = input("Ingrese una frase: ")

# Dividir la frase en palabras
palabras = frase.split()

# 1. Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# 2. Contar la frecuencia de cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("\nPalabras únicas:", palabras_unicas)
print("Recuento:", recuento)


"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:
alumnos = {
          "Sofía": (10, 9, 8),
          "Luis": (6, 7, 7)

}

"""

# Diccionario para almacenar los alumnos y sus notas
alumnos = {}

print("Ingrese los datos de 3 alumnos:")

# Solicitar datos para 3 alumnos
for i in range(3):
    nombre = input(f"\nNombre del alumno {i+1}: ")
    
    # Solicitar las 3 notas
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    # Guardar como tupla en el diccionario
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar promedios
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {notas} -> Promedio: {promedio:.2f}")

"""7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2:
Mostrá los que aprobaron ambos parciales.
Mostrá los que aprobaron solo uno de los dos.
Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

"""
# Conjuntos de estudiantes que aprobaron cada parcial
parcial1 = {"Juan", "María", "Pedro", "Ana", "Luis"}
parcial2 = {"Ana", "Luis", "Carlos", "Sofía", "Pedro"}

# 1. Estudiantes que aprobaron ambos parciales
ambos_parciales = parcial1 & parcial2  # Intersección

# 2. Estudiantes que aprobaron solo uno de los dos
solo_parcial1 = parcial1 - parcial2    # Diferencia
solo_parcial2 = parcial2 - parcial1    # Diferencia
solo_un_parcial = solo_parcial1.union(solo_parcial2)  # Unión

# 3. Total de estudiantes que aprobaron al menos un parcial
total_aprobados = parcial1.union(parcial2)  # Unión

# Mostrar resultados
print("Estudiantes que aprobaron ambos parciales:", ambos_parciales)
print("Estudiantes que aprobaron solo un parcial:", solo_un_parcial)
print("Total de estudiantes que aprobaron al menos un parcial:", total_aprobados)



"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario:
Consultar el stock de un producto ingresado.
Agregar unidades al stock si el producto ya existe.
Agregar un nuevo producto si no existe.

"""
# Diccionario inicial de productos y stock
stock = {
    "Manzanas": 50,
    "Bananas": 30,
    "Fideos": 20,
    "Pan": 40
}

def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓN DE STOCK ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")
    
    # Opción 1: Consultar stock
    if opcion == "1":
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario")
    
    # Opción 2: Agregar unidades a producto existente
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock:
            try:
                unidades = int(input(f"Ingrese las unidades a agregar a {producto}: "))
                stock[producto] += unidades
                print(f"Stock actualizado: {producto} ahora tiene {stock[producto]} unidades")
            except ValueError:
                print("Error: Debe ingresar un número entero")
        else:
            print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo")
    
    # Opción 3: Agregar nuevo producto
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock:
            try:
                unidades = int(input(f"Ingrese el stock inicial de {producto}: "))
                stock[producto] = unidades
                print(f"Producto '{producto}' agregado con {unidades} unidades")
            except ValueError:
                print("Error: Debe ingresar un número entero")
        else:
            print(f"El producto '{producto}' ya existe. Use la opción 2 para agregar unidades")
    
    # Opción 4: Mostrar todo el inventario
    elif opcion == "4":
        print("\n--- INVENTARIO COMPLETO ---")
        for producto, unidades in stock.items():
            print(f"{producto}: {unidades} unidades")
    
    # Opción 5: Salir
    elif opcion == "5":
        print("Saliendo del sistema de gestión de stock...")
        break
    
    else:
        print("Opción no válida. Por favor ingrese un número del 1 al 5")



"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo:
agenda = {

          ("lunes", "10:00"): "Reunión",

          ("martes", "15:00"): "Clase de inglés"
}
Permití consultar qué actividad hay en cierto día y hora.

"""
# Agenda inicial con algunos eventos de ejemplo
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Cita médica"
}

def consultar_evento():
    """Permite consultar un evento en la agenda"""
    print("\n--- CONSULTAR EVENTO ---")
    dia = input("Ingrese el día (ej: lunes): ").lower()
    hora = input("Ingrese la hora (formato HH:MM): ")
    
    clave = (dia, hora)
    if clave in agenda:
        print(f"\nEvento programado: {agenda[clave]}")
    else:
        print("\nNo hay eventos programados para ese día y hora")

def agregar_evento():
    """Permite agregar un nuevo evento a la agenda"""
    print("\n--- AGREGAR EVENTO ---")
    dia = input("Ingrese el día (ej: lunes): ").lower()
    hora = input("Ingrese la hora (formato HH:MM): ")
    evento = input("Ingrese la descripción del evento: ")
    
    clave = (dia, hora)
    agenda[clave] = evento
    print(f"\nEvento '{evento}' agregado correctamente para el {dia} a las {hora}")

def mostrar_menu():
    print("\n--- AGENDA DE EVENTOS ---")
    print("1. Consultar evento")
    print("2. Agregar evento")
    print("3. Mostrar agenda completa")
    print("4. Salir")

# Menú principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        consultar_evento()
    elif opcion == "2":
        agregar_evento()
    elif opcion == "3":
        print("\n--- AGENDA COMPLETA ---")
        for (dia, hora), evento in agenda.items():
            print(f"{dia.capitalize()} {hora}: {evento}")
    elif opcion == "4":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Por favor ingrese un número del 1 al 4")




"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde:
Las capitales sean las claves.
Los países sean los valores.
Ejemplo:
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}

"""
# Diccionario original
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Perú": "Lima"
}

# Crear el diccionario invertido
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar resultados
print("Diccionario original:")
print(original)

print("\nDiccionario invertido (capitales como claves):")
print(invertido)