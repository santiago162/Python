# Algoritmo 1: Suma y promedio de tres números enteros

print("--- Suma y promedio de tres números enteros ---")
print()

try:
    x = int(input("Ingrese el primer número entero: "))
    y = int(input("Ingrese el segundo número entero: "))
    z = int(input("Ingrese el tercer número entero: "))

    suma = x + y + z
    promedio = suma / 3

    print()
    print("La suma total es:", suma)
    print("El promedio es:", promedio)

except ValueError:
    print("Error: debes ingresar un número entero válido.")
