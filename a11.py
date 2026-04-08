# Algoritmo 11: Comisión por ventas (5%)

print("--- Comisión por ventas ---")
print()

ventas = float(input("Ingrese el valor total de ventas realizadas: "))

comision = ventas * 0.05
total_recibir = ventas + comision

print()
print("Valor de la comisión (5%):", comision)
print("Total a recibir:", total_recibir)
