# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""
# Add some code to the implementation of
# Newton–Raphson that keeps track of the number of iterations used
# to find the root. Use that code as part of a program that compares the
# efficiency of Newton–Raphson and bisection search. (You should
# discover that Newton–Raphson is far more efficient.)

epsilon = 0.001
while True:
    try:
        number = float(input("Enter a number to learn its square root: "))
        if number < 0:
            print("The square root of a negative number does not exist among the set of Real Numbers.")
            continue
        break
    except ValueError:
        print("You should enter a numeric value")

#copying the input in order to compare two methods.
number2 = number
guess = number/2
number_of_guesses = 1

#Implementation of Newton-Raphson Method
while abs(guess**2-number) >= epsilon:
    guess = guess - ((guess**2-number)/(2*guess))
    number_of_guesses += 1
    
print("Square root of",number,"is about",guess)
print(f"Number of guesses {number_of_guesses}")

#Implementation of Bisection Search
high = number2
low = 0
guess2 = (high + low) / 2
number_of_guesses2 = 1
while abs(guess2 ** 2 - number2) >= epsilon:
    if guess2 ** 2 > number2 :
        high = guess2
    else:
        low = guess2
    guess2 = (high + low)/2
    number_of_guesses2 += 1
        
print(f"Square root of {number2} is about {guess2}")
print(f"Number of guesses {number_of_guesses2}")
print(f"Newton-Raphson method is {number_of_guesses2 / number_of_guesses} \
times more efficient than bisection search method")