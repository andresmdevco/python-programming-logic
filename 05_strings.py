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

# Interpolación
print(f"Saludo: {c1}, grupo: {c2}!")

# Transformación en lista de caracteres
print(list(c3))

# Transformación de lista en cadena
l1 = [c1, ", ", c2, "!"]
print("".join(l1))

# Transformaciones numéricas
c4 = "123456.123"
c4 = float(c4)
print(c4)

# Comprobaciones varias
c4 = "123456"
print(c1.isalnum())
print(c1.isalpha())
print(c4.isalpha())
print(c4.isnumeric())


"""
Extra

Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
 - Palíndromos
 - Anagramas
 - Isogramas
"""

def check_word(word1: str, word2: str):
    words = [word1, word2]

    # Palíndromos
    for word in words:
        if word == word[::-1]:
            print(f"La palabra {word} es un palíndromo")
        else:
            print(f"La palabra {word} no es un palíndromo") 
    
    # Anagramas
    if sorted(word1) == sorted(word2):
        print(f"Las palabras {word1} y {word2} son anagramas")
    else:
        print(f"Las palabras {word1} y {word2} no son anagramas")

   
    # Isogramas
    def isogram(word: str):
        letter_dict = dict()
        for letter in word:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1

        isogram = True
        values = list(letter_dict.values())
        isogram_len = values[0]
        for letter_count in values:
            if letter_count != isogram_len:
                isogram = False
                break
    
        if isogram == True:
            print(f"La palabra {word} es un isograma")
        else:
            print(f"La palabra {word} no es un isograma")


    for word in words:
        isogram(word)
            


check_word("reconocer", "patopatopato")
check_word("amor", "roma")