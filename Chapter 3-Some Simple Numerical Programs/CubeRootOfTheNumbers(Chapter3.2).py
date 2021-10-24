# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""

# What would have to be changed to make the code
# in Figure 3-5 work for finding an approximation to the cube root of
# both negative and positive numbers? Hint: think about changing low
# to ensure that the answer lies within the region being searched.

# # Figure 3-5
# epsilon = 0.01
# num_guesses, low = 0, 0
# high = max(1, x)
# ans = (high + low)/2
# while abs(ans**2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     num_guesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# print('number of guesses =', num_guesses)
# print(ans, 'is close to square root of', x)

x = -7
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, abs(x))
ans = (high + low)/2
while abs(ans**3 - abs(x)) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2

# if x < 0 cube root will be also negative.
if x < 0:
    ans = -ans
print('number of guesses =', num_guesses)
print(ans, 'is close to cube root of', x)

