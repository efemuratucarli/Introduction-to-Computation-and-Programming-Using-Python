"""
@author: efemuratucarli
"""

# Write a program that examines three variables—
# x, y, and z—and prints the largest odd number among them. If none
# of them are odd, it should print the smallest value of the three.

x = 23
y = 9
z = 7

if x % 2 == 1 and (x > y or y % 2 == 0) and (x>z or z % 2 == 0):
    print(x)
elif y % 2 == 1 and (y > x or x % 2 == 0) and (y>z or z % 2 == 0):
    print(y)
elif z % 2 == 1 and (z > x or x % 2 == 0) and (z>y or y % 2 == 0):
    print(z)
else:
    if x < y and x < z:
        print(x)
    elif y < x and y < z:
        print(y)
    else:
        print(z)