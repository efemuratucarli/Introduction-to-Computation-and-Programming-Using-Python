# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:43:13 2021

@author: efemuratucarli
"""

# Finger exercise: Implement a function that meets the specification
def get_min(d):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first
    in the
    alphabet. E.g., if d = {x = 11, b = 12}, get_min
    returns 12."""
    ans = None
    if len(d) != 0:
        ans = 0
        letter = ""
        for k,v in d.items():
            if letter == "":
                ans = v
                letter = k
            elif k < letter:
                letter = k
                ans = v
            else:
                pass
        return ans
d = {"x" :11, "b" :12}
        
        