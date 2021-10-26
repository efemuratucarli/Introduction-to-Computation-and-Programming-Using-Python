# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:38:47 2021

@author: efemuratucarli
"""
# The harmonic sum of an integer, n > 0, can be
# calculated using the formula 1+(1/2)+...(1/n). Write a recursive function
# that computes this.

def harmonic(x):
    if x == 1:
        return 1
    else:
        return 1/x + harmonic(x-1)
    