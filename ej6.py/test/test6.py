import unittest

from separador import separar

class SeparadorTestCase(unittest.TestCase):
    def test_separar(self):
        pares, impares = separar([6,5,2,1,7])
        self.assertEqual(pares, [2, 6])
        self.assertEqual(impares, [1, 5, 7])
        
        pares, impares = separar([10, -3, 7, 0, 6])
        self.assertEqual(pares, [-3, 0, 6, 10])
        self.assertEqual(impares, [7])
        
        pares, impares = separar([])
        self.assertEqual(pares, [])
        self.assertEqual(impares, [])
        
if __name__ == '__main__':
    unittest.main()
