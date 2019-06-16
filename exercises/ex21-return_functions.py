def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Diving {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(25, 3)
height = subtract(175, 3)
weight = multiply(34, 2)
iq = divide(100, 5)

print(f"Age: {age}, Height: {height}, Weight: {weight} and Iq: {iq}")

# A puzzle for the extra credit, type it in anyway..
print("Here is the puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")