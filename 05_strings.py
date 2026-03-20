"""
Operaciones
"""

c1 = "Hola"
c2 = "Gamers"

# Concatenación
print(c1 + " " + c2 + "!")

# Repetición
print((c1 + " ") * 3)

# Indexaxión
print(c2[0] + c2[1] + c2[2] + c2[3] + c2[4] + c2[5])

# Longitud
print(len(c2))

# Slicing (porción) - El índice final no se tiene en cuenta
print(c2[0:4])
print(c2[3:])
print(c2[2:4])
print(c2[:4])

# Búsqueda
print("l" in c1)
print("Ho" in c1)
print("j" in c1)

# Reemplazo
print(c1.replace("o","a"))

# División 
print(c2.split("m"))

# Mayúsculas y minúsculas y letras en mayúsculas
print(c1.upper())
print(c2.lower())
print("inteligencia artificial".title())
print("inteligencia artificial".capitalize())

# Eliminación de espacios al principio y al final
print(" hoy hace ".strip() + "frio")

# Búsqueda al principio y al final
print(c2.startswith("Ga"))
print(c2.startswith("Sa"))
print(c2.endswith("rs"))
print(c2.endswith("os"))

c3 = "Andrés Felipe @felipe"

# Búsqueda de posición
print(c3.find("felipe"))
print(c3.find("Felipe"))
print(c3.find("F"))
print(c3.lower().find("f"))

# Búsqueda de ocurrencias
print(c3.lower().count("f"))

# Formateo
print("Saludo: {}, grupo: {}!".format(c1, c2))