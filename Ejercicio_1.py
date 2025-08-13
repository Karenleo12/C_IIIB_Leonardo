"""
Calculadora de Operaciones Básicas en Python.
Permite realizar suma, resta, multiplicación y división de dos números.
Funcionalidades:
1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Dividir dos números
5. Salir del sistema

Realizado por: Karen Leonardo - 02/06/2025
"""

# Importamos la librería 'os' para poder limpiar la consola
import os

# Función para limpiar la consola
def limpiar_consola():
    if os.name == 'nt':         # Si el sistema es Windows
        os.system('cls')        # Limpia con 'cls'

# Función para pedir dos números al usuario
def solicitar_numeros():
    num1 = float(input("Ingrese el primer número: "))    # Solicita el primer número
    num2 = float(input("Ingrese el segundo número: "))   # Solicita el segundo número
    return num1, num2                                     # Retorna ambos números como una tupla

# Función para sumar
def suma(a, b):
    return a + b     # Retorna el resultado de la suma

# Función para restar
def resta(a, b):
    return a - b     # Retorna el resultado de la resta

# Función para multiplicar
def multiplicacion(a, b):
    return a * b     # Retorna el resultado de la multiplicación


# Bucle principal del programa
while True:
    limpiar_consola()   # Limpia la consola en cada iteración
    print("CALCULADORA BÁSICA")   # Título del menú
    print("1. Sumar")                         # Opción 1
    print("2. Restar")                        # Opción 2
    print("3. Multiplicar")                   # Opción 3
    print("5. Salir")                         # Opción 4
    
    opcion = input("Seleccione una opción: ")  # El usuario elige una opción

    if opcion == '1':                            # Si elige suma
        print("\n SUMA")                  # Encabezado
        n1, n2 = solicitar_numeros()             # Solicita dos números
        print(f"Resultado: {n1} + {n2} = {suma(n1, n2)}")  # Muestra el resultado
        input("Presione Enter para continuar...")          # Pausa

    elif opcion == '2':                          # Si elige resta
        print("\n RESTA")                 # Encabezado
        n1, n2 = solicitar_numeros()             # Solicita dos números
        print(f"Resultado: {n1} - {n2} = {resta(n1, n2)}")  # Muestra el resultado
        input("Presione Enter para continuar...")          # Pausa

    elif opcion == '3':                          # Si elige multiplicación
        print("\n MULTIPLICACIÓN")        # Encabezado
        n1, n2 = solicitar_numeros()             # Solicita dos números
        print(f"Resultado: {n1} * {n2} = {multiplicacion(n1, n2)}")  # Muestra el resultado
        input("Presione Enter para continuar...")                      # Pausa

    elif opcion == '4':                          # Si elige salir
        print("\nGracias por usar la calculadora. ¡Hasta pronto!")  # Mensaje de despedida
        break                                    # Sale del bucle

    else:
        print("Opción no válida.")              # Si la opción no es válida
        input("Presione Enter para continuar...")  # Pausa