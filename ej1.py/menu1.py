cadena = "zeréP nauJ,01"

cadena = cadena[::-1]

nombre = cadena[3:]
apellido = cadena[:3]
nota = cadena[4]

print(nombre, apellido, "ha sacado un", nota, "de nota.")

print("""
    1. Nombre
    2. Apellido
    3. Nota
    4. Salir
""")

opcion = int(input("Elige una opcion: "))

if opcion == 1:
    print(nombre)
elif opcion == 2:
    print(apellido)
elif opcion == 3:
    print(nota)
elif opcion == 4:
    print("Adios")
else:
    print("Elige una opcion correcta")