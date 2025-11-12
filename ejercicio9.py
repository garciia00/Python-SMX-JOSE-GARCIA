import random

numero_secreto = random.randint(1, 10)

intento = int(input("Adivina el numero secreto entre 1 y 10: "))

while intento != numero_secreto:
    if intento > numero_secreto:
        print("El numero es mas bajo")
    else:
        print("El numero es mas alto")
    
    intento = int(input("Intenta otra vez: "))

print("Correcto, el numero secreto era", numero_secreto)
