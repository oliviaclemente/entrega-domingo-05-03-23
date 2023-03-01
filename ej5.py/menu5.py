import sys

def descomposicion(num):
    # Validar que el argumento sea un número entero positivo
    try:
        num = int(num)
        if num <= 0:
            raise ValueError()
    except:
        print("El argumento debe ser un número entero positivo.")
        return None
    
    # Descomponer el número en unidades, decenas, centenas, etc.
    unidades = []
    for i, d in enumerate(str(num)[::-1]):
        unidades.append(int(d) * (10 ** i))
    
    # Formatear las unidades como cadenas de longitud 4
    unidades = [f"{u:04d}" for u in unidades[::-1]]
    
    return unidades

if __name__ == "__main__":
    # Comprobar si se ha especificado un número como argumento
    if len(sys.argv) != 2:
        print("Uso: python descomposicion.py [numero]")
        print("Ejemplo: python descomposicion.py 3647")
    else:
        # Descomponer el número y mostrar los resultados
        num = sys.argv[1]
        unidades = descomposicion(num)
        if unidades is not None:
            for u in unidades:
                print(u)
                
# Path: ej5.py/ej5.py

