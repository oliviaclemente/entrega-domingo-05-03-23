
import unittest

class PruebaCadena(unittest.TestCase):
    def test(self):
        cadena = "zeréP nauJ,01"
        cadena = cadena[::-1]
        nombre = cadena[3:]
        apellido = cadena[:3]
        nota = cadena[4]
        self.assertEqual(f"{nombre} {apellido} ha sacado un {nota} de nota.", "Juan Pérez ha sacado un 10 de nota.")

if __name__ == '__main__':
    unittest.main()