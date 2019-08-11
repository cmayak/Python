# Add two numbers to get output
def add(x, y):
    z = x + y
    print(z)
# Subtract two number to get output
def subtract(x, y):
    z = x - y
    print(z)
# Multiply two numbers to get output
def multiply(x, y):
    z = x * y
    print(z)
# Diving two numbers with a condition for dividing by zero to get output
def divide(x, y):
    if y == 0:
        print("Divide by zero Error!")
    else:
        z = x / y
        print(z)

add(1,1)
subract(2,1)
multiply(3,3)
divide(4,2)
divide(5,0)
