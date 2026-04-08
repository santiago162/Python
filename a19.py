# Algoritmo 19: Conversión de moneda (pesos colombianos a dólares)

print("--- Conversión de moneda: Pesos colombianos a dólares ---")
print()

pesos = float(input("Ingrese el valor en pesos colombianos: "))
tasa = float(input("Ingrese la tasa de cambio (pesos por dólar): "))

dolares = pesos / tasa

print()
print(f"${pesos:,.0f} COP equivale a ${dolares:,.2f} USD")
