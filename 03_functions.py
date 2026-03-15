"""
Funciones definidas por el usuario
"""

# Simple
def greet():
    print("Saludos amigos developers")

greet()   


# Con retorno
def return_greet():
    return "Saludos amigos developers"

greet = return_greet()
print(greet) # forma1
print(return_greet()) # forma2


# Con un argumento
def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Andrés")


# Con varios argumentos
def addition(num1, num2):
    return num1 + num2

print(addition(4,8))

def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet('Hello','Andrew')
args_greet(name='Andrew', greet='Hello')


# Con argumentos predeterminado
def default_arg_greet(name = "Felipe"):
    print(f"Hola, {name}")

default_arg_greet()

def default_addition(num1 = 3, num2 = 12):
    return num1 + num2

print(default_addition())


# Con argumentos y retorno
def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hellow", "Andrew"))


# Con retorno de varios valores
def multiple_return_greet():
    return "Saludos", "Andrés"

greet, name = multiple_return_greet()
print(greet)
print(name)


# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Andres", "Developer", "Bienvenido")


# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    languaje="Python", 
    name="Andres", 
    profession="Developer", 
    age=25
)


"""
Funciones dentro de funciones
"""

def other_function():
    def inner_function():
        print("Funcion interna: Hola a todos")
    inner_function()

other_function()


"""
Funciones del lenguaje()
"""

print(len("Snake"))
print(type("Snake"))
print(type(3.4))
print("AndresDev".upper())


"""
Variables locales y globales
"""

global_var = "Python"

print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")


print(global_var)
# print(local_var) No se puede acceder desde afuera de la función

hello_python()

"""
Extra

Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
# Ejercicio conocido como Fizz Buzz

def check_multiplies(str1, str2)-> int:
    count_number = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(str1, str2)
        elif number % 3 ==0:
            print(str1)
        elif number % 5 ==0:
            print(str2)
        else:
            print(number)
            count_number += 1

    return count_number

print(check_multiplies("Manzana", "Naranja"))
 

