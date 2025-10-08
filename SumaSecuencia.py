entrada = input("EScribe una secuencia de numeros de dos digitos separados por espacios: ")

numeros = []
for x in entrada.split():
    numeros.append(int(x))
suma = sum(numeros)

print("La suma de los números es:", suma)
