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

