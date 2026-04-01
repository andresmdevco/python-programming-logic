"""
Pruebas unitarias
"""
import unittest
from datetime import datetime, date

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


"""
Extra

Crea un diccionario con las siguientes claves y valores:
 "name": "Tu nombre"
 "age": "Tu edad"
 "birth_date": "Tu fecha de nacimiento"
 "programming_languages": ["Listado de lenguajes de programación"]
 Crea dos test:
    - Un primero que determine que existen todos los campos.
    - Un segundo que determine que los datos introducidos son correctos.
"""



class TestData(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name": "Andrés Muñoz",
            "age": 25,
            "birth_date": datetime.strptime("06-08-2000", "%d-%m-%Y").date(),
            "programming_languages": ["Javascript", "Python", "C++"]
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)


unittest.main()