# Listas
school_items = ["Cuaderno", "Lápiz", "Calculadora", "Tijeras"]
print(school_items)
school_items.append("Borrador") # Inserción
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

