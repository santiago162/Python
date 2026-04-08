import os
import sys
import subprocess

ALGORITMOS = {
    "1":  "Suma y promedio de tres números enteros",
    "2":  "Área de un rectángulo",
    "3":  "Conversión de temperatura (Celsius a Fahrenheit)",
    "4":  "Salario semanal",
    "5":  "Salario con horas extra",
    "6":  "Total de una venta",
    "7":  "Venta con descuento fijo",
    "8":  "Venta con descuento por porcentaje",
    "9":  "Venta con IVA",
    "10": "Compra de varios productos",
    "11": "Comisión por ventas (5%)",
    "12": "Comisión escalonada",
    "13": "Promedio de notas y aprobación",
    "14": "Nota final ponderada",
    "15": "Mayor de dos números",
    "16": "Número par o impar",
    "17": "Edad de una persona",
    "18": "Clasificación por edad",
    "19": "Conversión de moneda (pesos a dólares)",
    "20": "Interés simple",
    "21": "Interés compuesto",
    "22": "Control de inventario",
    "23": "Costo de envío por peso",
    "24": "Factura de agua",
    "25": "Total y promedio de ventas del día",
}

while True:
    print()
    print("  ==========================================  ")
    print("    Taller 1 - Algoritmos básicos en Python  ")
    print("    BY: Santiago Caro Palacio               ")
    print("  ==========================================  ")
    print()

    for num, titulo in ALGORITMOS.items():
        print(f"  {num:>2}. {titulo}")

    print()
    print("   0. Salir")
    print()

    opcion = input("  Seleccione una opción: ").strip()

    if opcion == "0":
        print()
        print("  Hasta luego!")
        print()
        break

    if opcion in ALGORITMOS:
        archivo = f"a{opcion}.py"
        titulo = ALGORITMOS[opcion]

        print()
        print("  ------------------------------------------")
        print(f"  Algoritmo {opcion}: {titulo}")
        print("  ------------------------------------------")
        print()

        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"  Error: no se encontró el archivo '{archivo}'")
    else:
        print()
        print("  Opción no válida. Ingrese un número entre 0 y 25.")

    print()
    input("  Presione ENTER para continuar...")
    print()