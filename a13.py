# Algoritmo 13: Promedio de notas y aprobación

print("--- Promedio de notas ---")
print()

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print()
print("El promedio es:", round(promedio, 2))

if promedio >= 3.0:
    print("El estudiante APRUEBA")
else:
    print("El estudiante NO APRUEBA")
