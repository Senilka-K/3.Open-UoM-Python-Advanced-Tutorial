# Examples for Stacks

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

my_stack = []
push(my_stack, "a")
push(my_stack,"b")
push(my_stack,"c")
print(my_stack)

pop(my_stack)
print(my_stack)

#Exampels for Queues

fruits = {"Apple", "Mango", "Banana", "Grapes"}
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.pop()
print(fruits)
fruits.discard("Pineapple")
print(fruits)
