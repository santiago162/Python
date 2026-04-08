# Algoritmo 21: Interés compuesto

print("--- Interés compuesto ---")
print()

capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés (%): "))
periodos = int(input("Ingrese el número de períodos: "))

monto_final = capital * (1 + tasa / 100) ** periodos

print()
print("Monto final:", round(monto_final, 2))
