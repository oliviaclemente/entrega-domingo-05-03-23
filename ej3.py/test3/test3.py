import unittest

def elementos_repetidos(lista_1, lista_2):
    return list(set([elem for elem in lista_1 if elem in lista_2]))

class TestElementosRepetidos(unittest.TestCase):

    def test_elementos_repetidos(self):
        lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
        lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
        resultado_esperado = ["h", "o", "l", "a", " "]
        resultado_obtenido = elementos_repetidos(lista_1, lista_2)
        self.assertEqual(resultado_obtenido, resultado_esperado)

if __name__ == '__main__':
    unittest.main()
