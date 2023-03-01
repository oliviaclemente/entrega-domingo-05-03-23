numero_magico = 12345679

while True:
    numero_usuario = int(input("Introduce un número entre 1 y 9: "))
    if numero_usuario >= 1 and numero_usuario <= 9:
        numero_usuario *= 9
        numero_magico *= numero_usuario
        print("El número mágico es: {}".format(numero_magico))
        break
    else:
        print("El número no es correcto")