# -*- coding: utf-8 -*-
"""
@author: efemuratucarli
"""
def is_in(str1,str2):
    if str1 == "" or str2 == "":
        return -1
    elif str1 in str2 or str2 in str1:
        return True
    else:
        return False

def test_is_in(str1s,str2s):
    for str1 in str1s:
        for str2 in str2s:
            result = is_in(str1,str2)
            if not result:
                val = "Neither string occurs anywhere in the other"
            elif result == -1:
                if str1 == "" and str2 == "" :
                    val = "Both of them are empty string"
                elif str1 == "":
                    val = "str1 is an empty string"
                else:
                    val = "str2 is an empty string"
            else:
                val = "Either string occurs anywhere in the other"
            
            print(f'str1 = {str1}  str2 = {str2} \n{val}\n')

str1s = ("test","","afdsfsdfa")
str2s = ("es","fafsdfasf","")
test_is_in(str1s, str2s)