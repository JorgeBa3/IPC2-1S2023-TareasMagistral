parrafo = input("Ingrese el parrafo: ")
texto=parrafo

palabras = texto.split()
contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

for palabra, cantidad in contador.items():
    print("'" + palabra + "' aparece: " + str(cantidad) + " veces.")


