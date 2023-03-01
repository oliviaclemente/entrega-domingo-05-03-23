tareas = [("Comprar leche", 2), ("Llamar al fontanero", 1), ("Sacar al perro", 3)]
tareas.sort(key=lambda x: x[1])
from collections import deque

cola_tareas = deque()
for tarea in tareas:
    cola_tareas.append(tarea[0])

from collections import deque

# Lista de tareas con prioridades
tareas = [("Comprar leche", 2), ("Llamar al fontanero", 1), ("Sacar al perro", 3)]

# Ordenar tareas por prioridad
tareas.sort(key=lambda x: x[1])

# Crear cola de tareas sin los números de orden
cola_tareas = deque()
for tarea in tareas:
    cola_tareas.append(tarea[0])

# Imprimir la cola de tareas
print(cola_tareas)

deque(['Llamar al fontanero', 'Comprar leche', 'Sacar al perro'])
