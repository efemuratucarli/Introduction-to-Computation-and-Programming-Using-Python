# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:17:33 2021

@author: efemuratucarli
"""
# Write a function that meets the specification
# def shopping_days(year):
# """year a number >= 1941
# returns the number of days between U.S. Thanksgiving
# and
# Christmas in year"""
import calendar as cal

def shopping_days(year):
    """year a number >= 1941
    returns the number of days between U.S. Thanksgiving
    and Christmas in year"""
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return (30-thanksgiving) + 25