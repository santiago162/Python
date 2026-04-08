# Algoritmo 7: Venta con descuento fijo

print("--- Venta con descuento fijo ---")
print()

valor_compra = float(input("Ingrese el valor total de la compra: "))

if valor_compra > 200000:
    descuento = valor_compra * 0.10
    valor_final = valor_compra - descuento
    print()
    print("Descuento aplicado (10%):", descuento)
else:
    valor_final = valor_compra
    print()
    print("No aplica descuento.")

print("Valor final a pagar:", valor_final)
