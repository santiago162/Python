# Algoritmo 10: Compra de varios productos

print("--- Compra de varios productos ---")
print()

cantidad = int(input("Ingrese la cantidad de productos comprados: "))
print()

total = 0

for i in range(cantidad):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    total += precio

print()
print("El total de la compra es:", total)
