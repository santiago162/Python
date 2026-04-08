# Algoritmo 14: Nota final ponderada

print("--- Nota final ponderada ---")
print("  Talleres: 30%  |  Parcial: 30%  |  Final: 40%")
print()

talleres = float(input("Ingrese la nota de talleres: "))
parcial = float(input("Ingrese la nota del examen parcial: "))
final = float(input("Ingrese la nota del examen final: "))

nota_definitiva = (talleres * 0.30) + (parcial * 0.30) + (final * 0.40)

print()
print("La nota definitiva es:", round(nota_definitiva, 2))
