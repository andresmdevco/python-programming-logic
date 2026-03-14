'''
Operadores
'''

# Operadores aritmeticos
print(f"Suma: 30 + 7 = {30 + 7}")
print(f"Resta: 30 - 7 = {30 - 7}")
print(f"Multiplicación: 30 x 7 = {30 * 7}")
print(f"División: 30 / 7 = {30 / 7}")
print(f"Módulo: 30 % 7 = {30 % 7}")
print(f"Exponente: 30 ** 7 = {30 ** 7}")
print(f"División entera: 30 // 7 = {30 // 7}")

# Operadores lógicos
print(f"AND &&: 30 + 7 == 37 and 5 - 2 == 3 es {30 + 7 == 37 and 5 - 2 == 3}") 
print(f"OR ||: 30 + 7 == 30 or 5 - 2 == 3 es {30 + 7 == 30 or 5 - 2 == 3}")
print(f"NOT !: not 10 + 5 == 15 es {not 10 + 5 == 16}")

# Operadores de comparación
print(f"Igualdad: 30 == 7 es {30 == 7}")
print(f"Desigualdad: 30 != 7 es {30 != 7}")
print(f"Mayor que: 30 > 7 es {30 > 7}")
print(f"Menor que: 30 < 7 es {30 < 7}")
print(f"Mayor o igual que: 30 >= 7 es {30 >= 7}")
print(f"Menor o igual que: 30 <= 7 es {30 <= 7}")

# Operadores de asignación
num = 12 # asignación
print(num)
num += 3 # suma y asignación
print(num)
num -= 4 # resta y asignación
print(num)
num *= 6 # multiplicación y asignación
print(num)
num /= 4 # división y asignación
print(num)
num %= 3 # módulo y asignación
print(num)
num **= 4 # exponente y asignación
print(num)
num //= 2 # division entera y asignación
print(num)

# Operadores de identidad (Compara el valor en memoria)
new_num = num
print(f"num is new_num es {num is new_num}")
print(f"num is not new_num es {num is not new_num}")

# Operadores de pertenencia
print(f"'r' in 'andres' = {'r' in 'andres'}")
print(f"'h' not in 'andres' = {'h' not in 'andres'}")

# Operadores de bit
x = 10 # 1010
y = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 ^ 3 = {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") #1010 - 0010
print(f"Desplazamiento a la derecha: 10 << 2 = {10 << 2}") #1010 - 101000

''' 
Estructuras de control
'''

# Condicionales

my_string = "Andres"

if my_string == "Andres":
    print("my_string es 'Andres'")
elif my_string == "Felipe":
    print("my_string es 'Felipe'")    
else:
    print("my_string no es 'Andres' ni 'Felipe'")

# Iterativas

for i in range(11):
    print(i)


i = 0
while i<=10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


''' 
Extra

Crea un programa que imprima por consola todos los números 
comprendidos entre 10 y 55 (incluidos), pares, 
y que no son ni el 16 ni múltiplos de 3.
'''
for number in range (10,56):
    if number % 2 == 0 and number % 3 != 0 and number != 16 :
        print(number)
