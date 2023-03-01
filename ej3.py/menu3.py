def elementos_repetidos(lista_1, lista_2):
    return list(set([elem for elem in lista_1 if elem in lista_2]))

def main():
    while True:
        print("Ingrese dos listas de elementos separados por comas:")
        entrada_1 = input("Lista 1: ")
        entrada_2 = input("Lista 2: ")

        lista_1 = entrada_1.split(",")
        lista_2 = entrada_2.split(",")

        resultado = elementos_repetidos(lista_1, lista_2)

        print("Los elementos que se repiten en ambas listas son:", resultado)
        print()

        continuar = input("¿Desea continuar? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()
