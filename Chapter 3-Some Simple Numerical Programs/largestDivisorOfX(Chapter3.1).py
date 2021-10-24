# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""

# Change the code in Figure 3-2 so that it returns
# the largest rather than the smallest divisor. Hint: if y*z = x and y is
# the smallest divisor of x, z is the largest divisor of x.

#The code in Figure 3-2
# # Figure 3-2
# # Test if an int > 2 is prime. If not, print smallest divisor
# x = int(input('Enter an integer greater than 2: '))
# smallest_divisor = None
# for guess in range(2, x):
#     if x%guess == 0:
#         smallest_divisor = guess
#         break
# if smallest_divisor != None:
#     print('Smallest divisor of', x, 'is', smallest_divisor)
# else:
#     print(x, 'is a prime number')

x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
for guess in range(2, x):
    if x%guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Largest divisor of', x, 'is', x/smallest_divisor)
    # if a * b = c and a is the smallest divisor, then b becomes the largest divisor of c
    # for example 13*2=26 , 2 is the smallest divisor of 26 and 13 is the largest divisor of 26 (except 1 and 26)
else:
    print(x, 'is a prime number')


