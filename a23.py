# Algoritmo 23: Costo de envío por peso

print("--- Costo de envío por peso ---")
print()

peso = float(input("Ingrese el peso del paquete (kg): "))

if peso <= 5:
    envio = 10000
else:
    envio = 20000

print()
print("El costo del envío es:", envio)
