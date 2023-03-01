import unittest

class TestNumeroMagico(unittest.TestCase):

    def test_numero_magico(self):
        numero_magico = 12345679
        numero_usuario = 5
        numero_usuario *= 9
        numero_magico *= numero_usuario
        self.assertEqual(numero_magico, 555555555)

if __name__ == '__main__':
    unittest.main()
