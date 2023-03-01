import unittest
from descomposicion import descomposicion

class TestDescomposicion(unittest.TestCase):
    def test_descomposicion(self):
        self.assertEqual(descomposicion(7), ["0007"])
        self.assertEqual(descomposicion(40), ["0040"])
        self.assertEqual(descomposicion(600), ["0600"])
        self.assertEqual(descomposicion(3000), ["3000"])
        self.assertEqual(descomposicion(3647), ["0007", "0040", "0600", "3000"])

    def test_descomposicion_con_cero(self):
        self.assertEqual(descomposicion(0), ["0000"])

    def test_descomposicion_con_numeros_grandes(self):
        self.assertEqual(descomposicion(123456789), ["0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009"])

    def test_descomposicion_con_argumento_invalido(self):
        self.assertEqual(descomposicion("a"), None)

if __name__ == '__main__':
    unittest.main()



