def agregar_una_vez(lista, el):
    if el in lista:
        raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
    lista.append(el)
    return lista

if __name__ == '__main__':
    elementos = []
    while True:
        print("1. Añadir elemento")
        print("2. Mostrar elementos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            try:
                el = input("Introduce un elemento: ")
                elementos = agregar_una_vez(elementos, el)
            except ValueError as e:
                print(str(e))
        elif opcion == "2":
            print("Contenido de la lista:")
            print(elementos)
        elif opcion == "3":
            break
        else:
            print("Opción inválida")
