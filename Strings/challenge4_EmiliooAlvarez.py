
from math import sqrt
print('Welcome to the Right Triangle Solver App:')

print("what is the first leg of the triangle: ")
a = float(input("a: "))
print('What is the second leng of the triangle:')
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )
