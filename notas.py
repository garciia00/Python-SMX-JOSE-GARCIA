nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

if nota1 <= 4 and nota2 <= 4 and nota3 <= 4:
    nota_final = 0
elif (nota1 > 4 or nota2 > 4 or nota3 > 4) and not (nota1 > 4 and nota2 > 4 and nota3 > 4):
    nota_final = 2
else:
    nota_final = (0.3 * nota1) + (0.2 * nota2) + (0.5 * nota3)

print("La nota final es:", nota_final)
