from collections import deque

def ordenar_tareas_por_prioridad(tareas):
    # Ordenar tareas por prioridad
    tareas.sort(key=lambda x: x[1])

    # Crear cola de tareas sin los números de orden
    cola_tareas = deque()
    for tarea in tareas:
        cola_tareas.append(tarea[0])

    # Imprimir la cola de tareas
    print(cola_tareas)

def menu():
    # Lista de tareas con prioridades
    tareas = [("Comprar leche", 2), ("Llamar al fontanero", 1), ("Sacar al perro", 3)]

    while True:
        print("=== MENÚ ===")
        print("1. Ordenar tareas por prioridad")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ordenar_tareas_por_prioridad(tareas)
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
