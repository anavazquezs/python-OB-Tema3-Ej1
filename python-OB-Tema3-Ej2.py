import math

peso_en_kg = float(input("Ingrese su peso en Kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
indice_masa_corporal = math.floor(peso_en_kg/(estatura**2))
print("Su IMC es: ", indice_masa_corporal)
