from menu4 import Menu, Tarea

# Creamos algunas tareas con distintas prioridades
tareas = [
    Tarea('Comprar pan', 3),
    Tarea('Llamar al fontanero', 1),
    Tarea('Ir al supermercado', 4),
    Tarea('Hacer la compra', 2),
    Tarea('Limpiar la casa', 5),
]

# Creamos el menú y lo ejecutamos
menu4 = Menu(tareas)
menu4.menu()
