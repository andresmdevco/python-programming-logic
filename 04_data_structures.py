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

"""
Extra

Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
(o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
 """


def contact_list(): 
    agenda: dict = {}

    def insert_contact(name):
        while True:
                phone_number = input(f"Escribe el numero de teléfono del contacto: ")
                if phone_number.isdigit() and len(phone_number) <= 10:
                    agenda[name] = phone_number
                    break
                else:
                    print("Debes ingresar un número de máximo 10 digitos.") 

    while True:

        print("")
        print("1. Buscar contacto\n" 
              "2. Añadir contacto\n"
              "3. Actualizar contacto\n"
              "4. Eliminar contacto\n"
              "5. Ver agenda\n"
              "6. Salir\n")
        option = input("Elige la opción que deseas: ")


        match option:
            case "1":
                name = input("Escribe el nombre del contacto que desea buscar: ")
                if name in agenda:
                    print(f"El número de telefono de {name} es: {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe.")

            case "2":
                name = input("Escribe el nombre del contacto nuevo: ")
                insert_contact(name)   

            case "3":
                name = input("Escribe el nombre del contacto que desea actualizar: ")
                if name in agenda:
                    insert_contact(name)     
                else:
                    print(f"El contacto {name} no existe.")

            case "4":
                name = input("Escribe el nombre del contacto que desea eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")

            case "5":
                print("\nAgenda")
                for name, phone in agenda.items():
                    print(f"{name} - {phone}")

            case "6":
                print("Saliendo de la agenda")
                break

            case _:
                print("Opción no válida. Eliga una opción del 1 al 6")    


contact_list()