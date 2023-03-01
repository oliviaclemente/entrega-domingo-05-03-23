# Creamos una lista vacía
elementos = []

# Añadimos elementos a la lista utilizando la función agregar_una_vez
elementos = agregar_una_vez(elementos, 10)
elementos = agregar_una_vez(elementos, -2)
elementos = agregar_una_vez(elementos, "Hola")
elementos = agregar_una_vez(elementos, 10)  # Este elemento ya está en la lista y lanzará un error

# Mostramos el contenido de la lista
print(elementos)  # Debería imprimir [10, -2, 'Hola']
