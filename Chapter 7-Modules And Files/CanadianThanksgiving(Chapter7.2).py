# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:00:34 2021

@author: efemuratucarli
"""
# Since 1958, Canadian Thanksgiving has occurred
# on the second Monday in October. Write a function that takes a year
# (>1957) as a parameter, and returns the number of days between
# Canadian Thanksgiving and Christmas.
import calendar as cal

def shopping_days(year):
    month = cal.monthcalendar(year, 10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]
    return (31-thanksgiving) + 55