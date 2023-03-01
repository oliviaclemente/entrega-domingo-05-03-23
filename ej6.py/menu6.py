def separar(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    
    return pares, impares

def main():
    while True:
        print("Bienvenido al separador de números pares e impares")
        print("1. Separar números")
        print("2. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            numeros = input("Ingrese una lista de números separados por comas: ")
            lista = [int(num) for num in numeros.split(",")]
            pares, impares = separar(lista)
            print("Números pares: ", pares)
            print("Números impares: ", impares)
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
