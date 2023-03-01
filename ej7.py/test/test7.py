def test_agregar_una_vez():
    # Creamos una lista vacía
    elementos = []

    # Añadimos algunos elementos
    assert agregar_una_vez(elementos, 10) == [10]
    assert agregar_una_vez(elementos, -2) == [10, -2]
    assert agregar_una_vez(elementos, "Hola") == [10, -2, "Hola"]

    # Intentamos añadir un elemento duplicado
    try:
        agregar_una_vez(elementos, 10)
    except ValueError as e:
        assert str(e) == "Error: Imposible añadir elementos duplicados => 10."
