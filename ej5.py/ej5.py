import sys

def descomposicion(numero):
    # Convertir el número en una cadena y obtener su longitud
    cadena_num = str(numero)
    longitud = len(cadena_num)
    
    # Recorrer la cadena de derecha a izquierda y construir la descomposición
    descomposicion = []
    for i, digito in enumerate(cadena_num):
        unidades = int(digito)
        valor = unidades * 10 ** (longitud - i - 1)
        descomposicion.append(valor)
    
    # Devolver la descomposición formateada
    formato = "{:0>" + str(longitud) + "d}"
    descomposicion_formateada = [formato.format(valor) for valor in descomposicion]
    return descomposicion_formateada

# Comprobar si se ha proporcionado un argumento
if len(sys.argv) != 2:
    print("Uso: python descomposicion.py <numero>")
else:
    # Convertir el argumento en un número entero
    try:
        numero = int(sys.argv[1])
    except ValueError:
        print("El argumento debe ser un número entero")
    else:
        # Descomponer el número y mostrar la descomposición
        descomposicion_formateada = descomposicion(numero)
        for linea in descomposicion_formateada:
            print(linea)
