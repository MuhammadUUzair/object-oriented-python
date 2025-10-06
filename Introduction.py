"""
Introduction.py
---------------------
This script demonstrates the basic concepts of:
- Python data types
- Class creation
- Object instantiation
- Constructor (__init__) behavior
"""

# -----------------------------
# 🔹 Python Built-in Data Types
# -----------------------------

# Integer
a = 5
print(a, "is of type:", type(a))

# Float
b = 5.5
print(b, "is of type:", type(b))

# String
c = "uzair"
print(c, "is of type:", type(c))

# Capitalize the first letter
c = c.capitalize()
print("After capitalize:", c)

# String representing a number
d = "5"
print(d, "is of type:", type(d))

# -----------------------------
# 🔹 Complex Numbers
# -----------------------------
a = 5 + 6j
print("\nComplex number:", a)
print("Real part:", a.real)
print("Imaginary part:", a.imag)

# -----------------------------
# 🔹 List and append() method
# -----------------------------
s1 = ['xyz']
print("\nInitial list:", s1)

# Append a single element
s1.append("abc")
print("After append:", s1)

# Append a list (nested list)
s1.append([5, 6, 2, 1])
print("After appending a list:", s1)

# -----------------------------
# 🔹 Classes and Objects
# -----------------------------

class Bike:
    """A simple class with no attributes (for demonstration)."""
    pass

# Creating an instance (object) of Bike
YBR = Bike()
print("\nObject created:", YBR)
print("Type of object:", type(YBR))

# -----------------------------
# 🔹 Constructor Demonstration
# -----------------------------

class Bike:
    """Demonstrates the __init__ constructor and the use of 'self'."""
    def __init__(self):
        # 'self' refers to the current instance (object)
        print("\nInside constructor (__init__)")
        print("Object memory address:", id(self))
        print("This method runs automatically when the object is created.")

# Creating an object automatically calls __init__
YBR = Bike()
print("Object memory address (outside class):", id(YBR))
