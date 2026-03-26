"""
Clases
"""

class Programmer:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list) -> None:
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(f"Nombre: {self.name} | Apellidos: {self.surname} |Edad: {self.age} | Lenguajes {self.languages}")


my_programmer = Programmer("Andrés", 25, ["C++", "Javascript", "Python"])
my_programmer.print()
my_programmer.surname = "Muñoz"
my_programmer.print()
my_programmer.age = 26
my_programmer.print()