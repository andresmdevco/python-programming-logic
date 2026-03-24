"""
Valor y referencia
"""

# Tipos de dato por valor
my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipos de dato por referencia (Todos los tipos de datos que no son primitivos)
# Los datos por referencia no copian su valor, heredan su posición de memoria
my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)


# Funciones con datos por valor
def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_c = 10
my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia 
def my_list_func(my_list: list):
    my_list_e = my_list
    my_list_e.append(30)
    
    my_list_d = my_list_e
    my_list_d.append(40)

    print(my_list_e)
    print(my_list_d)

my_list_c = [10, 20] 
my_list_func(my_list_c)
print(my_list_c)

"""
Extra

Crea dos programas que reciban dos parámetros (cada uno) definidos como
variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
se asigna a dos variables diferentes a las originales. A continuación, imprime
el valor de las variables originales y las nuevas, comprobando que se ha invertido
su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
"""

# Por valor
def value_funtion(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    
    return value_a, value_b


int_a = 34
int_b = 28
int_c, int_d = value_funtion(int_a, int_b)

print(f"{int_a}, {int_b}")
print(f"{int_c}, {int_d}")

# Por referencia
def ref_funtion(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp

    return value_a, value_b


list_a = [25, 35]
list_b = [45, 65]
list_c, list_d = ref_funtion(list_a, list_b)
print(f"{list_a}, {list_b}")
print(f"{list_c}, {list_d}")

