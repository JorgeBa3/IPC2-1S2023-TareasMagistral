class Tarea:
    contador = {}
    def texto(txt):
        palabras = txt.split()
        Tarea.contar(palabras)
        Tarea.mostrar()
        return

    def contar(palabras):
        for palabra in palabras:
            if palabra in Tarea.contador:
                Tarea.contador[palabra] += 1
            else:
                Tarea.contador[palabra] = 1
        return
    
    def mostrar():
        for palabra, cantidad in Tarea.contador.items():
            print("'" + palabra + "' aparece: " + str(cantidad) + " veces.")
        return
    
    
parrafo = input("Ingrese el parrafo: ")
Tarea.texto(parrafo)