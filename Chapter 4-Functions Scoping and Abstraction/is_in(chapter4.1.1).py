# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""

def is_in(str1,str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False
print(is_in("testdsafsfdamnzafasd","mnz"))