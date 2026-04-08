# Algoritmo 9: Venta con IVA

print("--- Venta con IVA (19%) ---")
print()

valor_venta = float(input("Ingrese el valor de la venta sin IVA: "))

iva = valor_venta * 0.19
total_con_iva = valor_venta + iva

print()
print("Valor del IVA (19%):", iva)
print("Total a pagar con IVA:", total_con_iva)
