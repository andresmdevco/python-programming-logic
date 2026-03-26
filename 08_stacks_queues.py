"""
Ejercicio
"""
# Pila/Stack (LIFO) Última en Entrar, Primera en Salir

stack = []

#push
stack.append(1) 
stack.append(2) 
stack.append(3) 
print(stack)

#pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)


# Cola/Queue (FIFO) Primera en Entrar, Primera en Salir

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)


# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
Extra

- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.

- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
"""

# 1 - Web

def web_nav():

    stack = []

    while True:

        action = input(
            "Añade una url o interactúa con palabras adelante/atrás/salir: "
        )

        if action == "salir":
            print("Saliendo de la web.")
            break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) - 1]}")
        else:
            print("Estas en la página de inicio.")

# web_nav()



# 1 - Impresora
def shared_printed():
    queue = []

    while True:

        action = input("Añada un documento o selecione imprimir/salir: ")
        
        if action == "salir":
            print("Apagando la impresora.")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo el documento: {queue.pop(0)}")
            else:
                print("No hay ningun documento en la cola para imprimir")
        else:
            queue.append(action)

        print(f"Cola de impresión: {queue}")


shared_printed()