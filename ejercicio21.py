import random
import time

print("Adivina el número entre 1 y 100")

numero_secreto = random.randint(1, 10)
inicio = time.time()
intentos = 0
adivinado = False

while not adivinado:
    intento = input("Introduce tu número: ")
    if not intento.isdigit():
        continue
    intento = int(intento)
    intentos += 1
    if intento == numero_secreto:
        adivinado = True

fin = time.time()
duracion = fin - inicio

print(f"Has adivinado el número {numero_secreto} en {intentos} intentos.")
print(f"Tiempo total: {round(duracion)} segundos.")
