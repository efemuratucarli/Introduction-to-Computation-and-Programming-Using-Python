# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""

def find_root(x,power,epsilon):
    if x < 0 and power % 2 == 0:
        return None #Negative number has no even-powered roots
    low = min(-1,x)
    high = max(1,x) 
#has to pick 1 instead of 0 because the values between 0 and 1
#have bigger roots than theirselves. For example sqrt(1/4) is equal to 1/2
    ans = (high+low)/2
    
    while abs(ans**power - x) >= epsilon:
        if ans**power > x:
            high = ans
        else:
            low = ans
        ans = (high+low)/ 2
    return ans

print(find_root(25,2,0.001) + find_root(-8, 3, 0.001) + find_root(16, 4, 0.001))