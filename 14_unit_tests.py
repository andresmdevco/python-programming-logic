"""
Pruebas unitarias
"""
import unittest

def sum(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return num1 + num2

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(12, 4), 16)
        self.assertEqual(sum(4, -9), -5)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 3.2), 5.7)
        self.assertEqual(sum(2, 4.2), 6.2)
        self.assertEqual(sum(2.5, 2.5), 5)
        
    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("3", 12)
        with self.assertRaises(ValueError):
            sum(3, "12")
        with self.assertRaises(ValueError):
            sum("3", "12")    
        with self.assertRaises(ValueError):
            sum("a", 12)      

unittest.main()