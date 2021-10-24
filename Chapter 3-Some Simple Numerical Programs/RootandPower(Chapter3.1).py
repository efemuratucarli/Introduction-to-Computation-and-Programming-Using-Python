# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""

# Write a program that asks the user to enter an
# integer and prints two integers, root and pwr, such that 1 < pwr < 6
# and root**pwr is equal to the integer entered by the user. If no such
# pair of integers exists, it should print a message to that effect.

x = int(input("Enter an integer: "))
pwr = 2
root = 0
while root**pwr < abs(x):
    pwr = pwr + 1
    if pwr == 5 and root**pwr < abs(x):
        root += 1
        pwr = 2
    if root**pwr > abs(x):
        root += 1
        pwr = 2

if root ** pwr == abs(x):
    if x < 0 and pwr % 2 == 1:
        print("(",-root,")","**",pwr,"=",x,sep="")
    if x >= 0:
        print(root,"**",pwr,"=",x)
    
else:
    print("The number",x,"cannot be expressed as a root**pwr form when pwr is in the interval of (1-6)")

        
        
        
    
    