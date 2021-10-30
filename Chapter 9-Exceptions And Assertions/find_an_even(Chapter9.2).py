# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:06:57 2021

@author: efemuratucarli
"""
# Implement a function that satisfies the
# specification

def find_an_even(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even
    number"""
    for val in L:
        try:
            if val % 2 == 0 :
                return val
        except:
            pass
    raise ValueError("L does not contain an even number")