# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""

# The Empire State Building is 102 stories high. A
# man wanted to know the highest floor from which he could drop an
# egg without the egg breaking. He proposed to drop an egg from the
# top floor. If it broke, he would go down a floor, and try it again. He
# would do this until the egg did not break. At worst, this method
# requires 102 eggs. Implement a method that at worst uses seven
# eggs.

#ideal_floor can be any number between 0 and 102. We will find it at worst seven steps
#Because in every step of the process, The interval, that contain the correct answer, is reduced by half.
#such as 103-51-25-12-6-3-1 >>>(log2(103))

ideal_floor = 55
# the high bound should be one more than 102 because when the high guess become 101, 
#int((high+low)/2) will become int(101.5) and this will return everytime 101. 
#In order to avoid from infinite loop, the high bound should be one more than 102
high = 103
low = 0
ans = int((high+low)/2)
number_of_guesses = 0

while ans != ideal_floor:
    number_of_guesses += 1
    if ans > ideal_floor:
        high=ans
    else:
        low = ans
    ans = int((high+low)/2)
    
print(ans)
print(number_of_guesses)
    