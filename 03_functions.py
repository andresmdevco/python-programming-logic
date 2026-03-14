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