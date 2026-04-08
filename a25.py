# Algoritmo 25: Total y promedio de ventas del día

print("--- Total y promedio de ventas del día ---")
print()

num_ventas = int(input("Ingrese el número de ventas del día: "))
print()

total = 0

for i in range(num_ventas):
    venta = float(input(f"Ingrese el valor de la venta {i + 1}: "))
    total += venta

promedio = total / num_ventas

print()
print("Total vendido:", total)
print("Promedio por venta:", round(promedio, 2))
