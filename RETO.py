saldo = 500
opcion = "" 

print("Bienvenido al Cajero Automático")

while opcion != "salir":
    print("Tu saldo actual es:", saldo, "€")
    opcion = input("Escribe 'retirar' para sacar dinero o 'salir' para terminar: ")

    if opcion == "retirar":
        monto = int(input("¿Cuánto deseas retirar?: "))

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
        if monto > saldo:
            print(" No tienes suficiente saldo.")
        if monto % 10 != 0:
            print("El monto debe ser múltiplo de 10.")
        if saldo >= monto:
            print("Retiro exitoso.")
            saldo -= monto
            print("Nuevo saldo:", saldo, "€")

    elif opcion == "salir":
        print("Gracias por usar el cajero, te esperamos.")
    else:
        print("Opción no válida. Intenta de nuevo.")
