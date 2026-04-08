# Algoritmo 18: Clasificación por edad

print("--- Clasificación por edad ---")
print()

edad = int(input("Ingrese su edad: "))

print()

if edad < 18:
    print("Eres menor de edad.")
elif edad < 60:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")
