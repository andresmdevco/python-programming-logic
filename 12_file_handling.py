"""
Manejo de ficheros
"""

import os

file_name="andresmdevco.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("Andrés Muñoz\n")
    file.write("25\n")
    file.write("Python")

with open(file_name, "r", encoding="utf-8") as file:
    print(file.read())

os.remove(file_name)

"""
Extra

Desarrolla un programa de gestión de ventas que almacena sus datos en un 
archivo .txt.
- Cada producto se guarda en una línea del archivo de la siguiente manera:
[nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.
"""
file_name="andres_shop.txt"

open(file_name, "a", encoding="utf-8")

while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")

    match option:
        case "1":
            name = input("Nombre: ")
            quantity = input("Cantidad vendida: ")
            price = input("Precio: ")
            with open(file_name, "a", encoding="utf-8") as file:
                file.write(f"{name}, {quantity}, {price}\n")

        case "2":
            name = input("Nombre: ")
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                        break

        case "3":
            name = input("Nombre: ")
            quantity = input("Cantidad vendida: ")
            price = input("Precio: ")
            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(file_name, "w", encoding="utf-8") as file:
                for line in lines:
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                    else:
                        file.write(line)

        case "4":
            name = input("Nombre: ")
            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(file_name, "w", encoding="utf-8") as file:
                for line in lines:
                    if line.split(", ")[0] != name:
                        file.write(line)

        case "5":
            with open(file_name, "r", encoding="utf-8") as file:
                print(file.read())
        case "6":
            total = 0
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            print(total)
        case "7":
            name = input("Nombre: ")
            total = 0
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
            print(total)
        case "8":
            print("Saliendo del programa")
            os.remove(file_name)
            break
        case _:
            print("Opción no válida. Elija un número del 1 al 8")

    