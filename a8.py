# Algoritmo 8: Venta con descuento por porcentaje

print("--- Venta con descuento por porcentaje ---")
print()

precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

descuento = precio * (porcentaje_descuento / 100)
precio_final = precio - descuento

print()
print("Valor del descuento:", descuento)
print("Precio final a pagar:", precio_final)
