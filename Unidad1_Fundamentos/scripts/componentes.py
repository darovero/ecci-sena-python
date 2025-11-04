# Sintaxis
print("Ejemplo de Sintanxis")
if 5 > 2:
    print("Esta es nuestra primer clase de Python \n")

# Variables
print("Ejemplo de Variables")

nombre = "David"
edad = 35
es_docente = False
print(f"El nombre es {nombre}, tiene {edad} años. ¿Es docente? {es_docente} \n")

# Tipos de datos
print("Ejemplo de Tipos de datos")

numero = 10
pi = 3.14
mensaje = "Bienvenidos al curso"
estudiante = False
valores = [1, 2, 3, 4]

print(type(numero))
print(type(pi))
print(type(mensaje))
print(type(estudiante))
print(type(valores))

# Operadores
print("\nEjemplo de Operadores")

a = 8
b = 4
print(a + b)  # Suma
# print(a + b) / 2  # Suma
print(a < b)   # Comparación

# Condicionales
print("\nEjemplo de Condicionales")

nota = 4.5

if nota >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")

# Bucles
print("\nEjemplo de Bucles")

materias = ["Matemáticas", "Física", "Programación", "Inglés"]
for materia in materias:
    print(f"Hoy tenemos clase de: {materia}")

# Funciones
print("\nEjemplo de Funciones")

def saludar(nombre):
    print(f"Hola, {nombre}. ¡Bienvenido a la clase de Python!")

def verificar_docente(nombre, lista_docentes):
    if nombre in lista_docentes:
        saludar(nombre)
    else:
        print(f"{nombre} no está registrado como docente.")

docentes = ["David", "Laura", "Carlos"]

verificar_docente("David", docentes)
verificar_docente("Ana", docentes)

# Módulos
print("\nEjemplo de Módulos")

import saludos as saludos

print(saludos.saludar(nombre))
print(saludos.despedir(nombre))


# Librerías
print("\nEjemplo de Librerías")

import numpy as np

# Crear dos arreglos
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Sumar los arreglos
resultado = a + b

print("Arreglo A:", a)
print("Arreglo B:", b)
print("Suma:", resultado)
