"""
Recursividad
"""

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)
        
countdown(100)


"""
Extra

Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
sucesión de Fibonacci (la función recibe la posición).
"""

# Factorial de un número
def factorial(number: int) -> int:
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(6))

# Fibonacci position
def fibonacci(position: int) -> int:
    if position <= 0:
        print("La posición debe ser mayor a cero")
    elif position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)

print(fibonacci(4))

# Fibonacci serie
for i in range(1, 10):
    print(fibonacci(i))

