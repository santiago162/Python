# Algoritmo 24: Factura de agua

print("--- Factura de agua ---")
print()

consumo = float(input("Ingrese el consumo de agua (m³): "))
valor_metro = float(input("Ingrese el valor por metro cúbico: "))

total = consumo * valor_metro

print()
print("Valor total de la factura:", total)
