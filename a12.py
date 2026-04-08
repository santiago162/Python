# Algoritmo 12: Comisión escalonada

print("--- Comisión escalonada ---")
print()

ventas = float(input("Ingrese el valor de ventas mensuales: "))

if ventas > 1000000:
    comision = ventas * 0.10
    porcentaje = "10%"
else:
    comision = ventas * 0.05
    porcentaje = "5%"

print()
print(f"Porcentaje de comisión aplicado: {porcentaje}")
print("La comisión es:", comision)
