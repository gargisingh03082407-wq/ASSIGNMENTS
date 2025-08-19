Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def factorial(n):
...     result = 1
...     for i in range(2, n + 1):
...         result *= i
...     return result
... 
... # Input from user
... num = int(input("Enter a number: "))
... 
... if num < 0:
...     print("Factorial is not defined for negative numbers.")
... else:
...     print(f"The factorial of {num} is {factorial(num)}")
