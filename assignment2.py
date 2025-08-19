# Input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swap using temp variable
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")
