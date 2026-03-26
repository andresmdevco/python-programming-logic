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


my_programmer = Programmer("Andrés", 25, ["C++", "Javascript", "Python"]) # Instancia de la clase
my_programmer.print()
my_programmer.surname = "Muñoz"
my_programmer.print()
my_programmer.age = 26
my_programmer.print()

"""
Extra

Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido.
"""

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = Stack()
my_stack.push(25)
my_stack.push(35)
my_stack.push(45)
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()



class Queue:
    def __init__(self):
        self.queue = []
    
    def equeue(self, item):
        return self.queue.append(item)

    def deequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.equeue("Factura.pdf")
my_queue.equeue("CV.pdf")
my_queue.equeue("Inventario.pdf")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
print(my_queue.count())
my_queue.print()

