# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""
def log(x,base,epsilon):
    """Assume x and epsilon int or float, base an int,
    x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon"""
    lower_bound = 0
    #finding a lower bound for the answer
    while base**lower_bound < x:
        lower_bound += 1
    low_bound = lower_bound - 1
    # if base** lower_bound == x high_bound should be one more than lower_bound in order to find the solution in the interval
    high_bound = lower_bound + 1
    ans = (high_bound+low_bound)/2
    while abs(base**ans-x) > epsilon:
        if base**ans > x:
            high_bound = base**ans
        else:
            lower_bound = base**ans
        ans = (high_bound+low_bound)/2
    return ans


    