# Algoritmo 6: Total de una venta

print("--- Total de una venta ---")
print()

producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad comprada: "))

total_pagar = precio_unitario * cantidad

print()
print("Producto:", producto)
print("Total a pagar:", total_pagar)
