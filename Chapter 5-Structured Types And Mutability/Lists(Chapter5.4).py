# -*- coding: utf-8 -*-
"""
@author: efemuratucarli

"""
# Finger exercise: Implement a function satisfying the following
# specification. Hint: it will be convenient to use lambda in the body of
# the implementation.

def f(L1, L2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9 """
    result = sum(map(lambda x,y : x**y,L1,L2))
    return result
        
    