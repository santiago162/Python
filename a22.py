# Algoritmo 22: Control de inventario

print("--- Control de inventario ---")
print()

inicial = int(input("Cantidad inicial en inventario: "))
vendida = int(input("Cantidad vendida: "))
recibida = int(input("Cantidad recibida: "))

inventario_final = inicial - vendida + recibida

print()
print("Inventario final:", inventario_final)
