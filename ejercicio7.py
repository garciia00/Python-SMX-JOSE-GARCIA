num = int(input("Introduce un número del 1 al 10: "))
if num < 1 or num > 10:
    print("Número fuera de rango.")
elif num < 5:
    print("Tienes un insuficiente.")
elif num == 5:
    print("Tienes un suficiente.")
elif num == 6:
    print("Tienes un bien.")
elif num == 7 or num == 8:
    print("Tienes un notable.")
else:
    print("Tienes un sobresaliente.")
