# -*- coding: utf-8 -*-
"""
@author: efemuratucarli

"""
def find_last(s,sub):
    """s and sub are non-empty strings
    Returns the index of the last occurence of sub in s.
    Return none if sub does not occur in s"""
    a = s.find(sub)
    if a == -1:
        return None
    while a != -1 and s != "":
        ans = a
        a = s.find(sub,a+len(sub))
    return ans

print(find_last("abcab","ab"))