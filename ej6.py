edad = int(input("Introduce tu edad: "))
if edad < 0 or edad > 120:
    print("Edad no válida")
elif edad >= 18:
    print("Eres adulto.")
else:
    print("Eres menor de edad.")