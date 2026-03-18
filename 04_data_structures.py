"""
Estructuras
"""

# Listas
school_items = ["Cuaderno", "Lápiz", "Calculadora", "Tijeras"]
print(school_items)
school_items.append("Borrador") # Inserción
school_items.append("Borrador")
print(school_items)
school_items.remove("Lápiz") # Eliminación
print(school_items)
print(school_items[1]) # Acceso
school_items[1] = "Regla" # Actualización
print(school_items)
school_items.sort() # Ordenación
print(school_items)

# Tuplas
fruits = ("Manzana", "Maracuyá", "Cereza", "Sandía", "4")
print(fruits[1]) # Acceso
print(fruits[4])
print(fruits)
fruits = tuple(sorted(fruits)) # Ordenación
print(fruits)
print(type(fruits))

# Sets: Estructura no ordenada - Datos no duplicados
first_set = {"Gato", "Elefante", "León", "Canguro", "Cocodrilo"}
print(first_set)
first_set.add("andresu@gmail.com") # Inserción
first_set.add("andresu@gmail.com")
first_set.remove("Elefante")
print(first_set)
first_set = set(sorted(first_set)) # No se puede ordenar
print(first_set)
print(type(first_set))

# Diccionario
my_dict: dict = {
    "name":"andres", 
    "alias":"andresmdevco",
    "age":"25", 
    "nationality":"Colombiano", 
}

my_dict["email"] = "andres@gmail.com" # Inserción
print(my_dict)
del my_dict["nationality"] # Eliminación
print(my_dict)
print(my_dict["name"]) # Acceso
my_dict["age"] = "35" # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

