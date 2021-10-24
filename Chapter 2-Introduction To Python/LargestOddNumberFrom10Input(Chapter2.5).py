"""
@author: efemuratucarli
"""

# Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered. If
# no odd number was entered, it should print a message to that effect.

number_of_inputs = 0
ans = None
while number_of_inputs < 10 :
    x = int(input("Enter a integer:"))
    if ans == None and abs(x) % 2 == 1:
        ans = x
    elif ans != None and x % 2 == 1 and x > ans:
        ans = x
    else:
        pass
    number_of_inputs += 1

if ans == None:
    print("There is no odd number in the input values")
else:
    print("Largest odd number is",ans)