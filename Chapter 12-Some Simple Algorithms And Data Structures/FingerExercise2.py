# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:45:18 2022

@author: efe
"""

# Finger exercise: Use merge_sort to sort a list to tuples of integers.
# The sorting order should be determined by the sum of the integers in
# the tuple. For example, (5, 2) should precede (1, 8) and follow (1,
# 2, 3).

def merge(left,right,compare):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L,compare = lambda x,y : x <= y):
    if len(L) < 2 :
        return L
    else:
        mid = len(L)//2
        left = merge_sort(L[0:mid],compare)
        right = merge_sort(L[mid:],compare)
    return merge(left,right,compare)

def compare_tuple_of_ints(t1,t2):
    """
    

    Parameters
    ----------
    t1 : a tuple consists of integers
    t2 : a tuple consists of integers

    Returns
    True if the sum of integers in t1 is less than the sum of integers in t2

    """
    if sum(t1) < sum(t2):
        return True
    return False

#example
l = [(5,2),(1,8),(1,2,3),(0,)]
print(merge_sort(l,compare_tuple_of_ints))