# Algoritmo 20: Interés simple

print("--- Interés simple ---")
print()

capital = float(input("Ingrese el capital: "))
tasa = float(input("Ingrese la tasa de interés (%): "))
tiempo = float(input("Ingrese el tiempo en meses: "))

interes = capital * (tasa / 100) * tiempo
total = capital + interes

print()
print("Interés simple:", interes)
print("Total a pagar:", total)
