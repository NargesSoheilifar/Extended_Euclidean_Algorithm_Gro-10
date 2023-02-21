Python 3.12.0a5 (tags/v3.12.0a5:3c67ec3, Feb  7 2023, 16:36:51) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def extended_euclidean_algorithm(a, b):
...     # Base case
...     if b == 0:
...         return a, 1, 0
... 
...     # Recursive case
...     gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
...     x = y1
...     y = x1 - (a // b) * y1
...     return gcd, x, y
... 
... def modular_multiplicative_inverse(a, m):
...     # Use the Extended Euclidean algorithm to find the modular multiplicative inverse
...     gcd, x, y = extended_euclidean_algorithm(m, a % m)
...     if gcd != 1:
...         return None # Modular multiplicative inverse does not exist
...     else:
...         return x % m # Return the positive integer less than m
... 
... # Take inputs from the user
... a = int(input("Enter the modulus a: "))
... b = int(input("Enter the non-negative integer b: "))
... 
... # Calculate the results using the Extended Euclidean algorithm
... gcd, x, y = extended_euclidean_algorithm(a, b)
... mod_inv = modular_multiplicative_inverse(b, a)
... 
... # Print the results
... print("gcd(a, b) = ", gcd)
... print("x = ", x)
... print("y = ", y)
... print("modular multiplicative inverse of b modulo a = ", mod_inv)
