# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""
def mult(a, b = None):
    if b and type(b)== int and type(a)== int:
        print(a*b)
    elif not b and type(a) == int:
        print(a)
    else:
        print("One or two of the argument is not a integer")
        
mult(9)