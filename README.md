Extended Euclidean Algorithm

The Extended Euclidean Algorithm is a method to find the greatest common divisor of two integers and also to compute the coefficients of Bezout's identity, which are used to express the greatest common divisor as a linear combination of the two integers.

This program takes two inputs: a, the modulus and b, a non-negative integer that is less than a. The program computes and returns three values: gcd(a, b), the integers x and y such that ax + by = gcd(a, b), and the modular multiplicative inverse of b modulo a.

Running the program

Ensure that you have Python installed on your computer. If you do not have it installed, you can download it from the official Python website: https://www.python.org/downloads/
Download or clone the extended-euclidean-algorithm repository.
Open a terminal or command prompt and navigate to the program file's directory.
Run the program using the following command: python extended_euclidean_algorithm.py
Follow the prompts to enter the values of a and b when prompted.

Sample input and output

Suppose we want to compute the greatest common divisor of a = 24 and b = 18, along with the coefficients x and y such that ax + by = gcd(a, b), and the modular multiplicative inverse of b modulo a. We would run the program as follows:

Enter the modulus a: 24
Enter the non-negative integer b: 18
gcd(a, b) =  6
x =  -1
y =  2
modular multiplicative inverse of b modulo a =  None

The output tells us that the greatest common divisor of a = 24 and b = 18 is gcd(a, b) = 6. The integers x and y satisfy the equation ax + by = gcd(a, b), which in this case is 24(-1) + 18(2) = 6. Thus, we have x = -1 and y = 2.

The modular multiplicative inverse of b = 18 modulo a = 24 is None, because gcd(a, b) = gcd(24, 18) = 6, which means that 18 and 24 are not relatively prime, and so b = 18 does not have a modular multiplicative inverse modulo a = 24.

Limitations

The program is designed to take inputs for a and b that are non-negative integers. The program may produce incorrect results or fail to terminate if the inputs are not in this format. Additionally, the program does not handle cases where a and b are not relatively prime (i.e., where their greatest common divisor is not equal to 1), in which case the modular multiplicative inverse does not exist.
