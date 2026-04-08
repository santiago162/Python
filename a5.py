# Algoritmo 5: Salario con horas extra

print("--- Salario con horas extra ---")
print()

horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

if horas_trabajadas > 40:
    horas_extra = horas_trabajadas - 40
    salario = (40 * valor_hora) + (horas_extra * valor_hora * 1.5)
else:
    salario = horas_trabajadas * valor_hora

print()
print("El salario total es:", salario)
