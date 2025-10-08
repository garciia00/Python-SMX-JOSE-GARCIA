texto = input("Introduce un texto: ")
contador = texto.lower().count("python")
contador1 = texto.lower().count("pyton")
contador2 = texto.lower().count("Python")
contador3 = contador + contador1 + contador2    
print(f"La palabra 'Python' aparece {contador3} vez/veces en el texto.")
