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