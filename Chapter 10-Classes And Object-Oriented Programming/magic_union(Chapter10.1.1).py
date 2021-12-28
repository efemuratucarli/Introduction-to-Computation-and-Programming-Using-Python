# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:35:07 2021

@author: efemuratucarli
"""
# Finger exercise: Replace the union method you added to Int_set
# by a method that allows clients of Int_set to use the + operator to
# denote set union.

class Int_set(object):
    def __init__(self):
        self._vals = []
    
    def insert(self,e):
        if e not in self._vals:
            self._vals.append(e)
   
    def member(self,e):
        if e in self._vals:
            return True
        return False
    
    def remove(self,e):
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + " not found")
   
    def get_members(self):
        return self._vals[:]
   
    def __str__(self):
        if self._vals == []:
            return {}
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ","
        return f'{{{result[:-1]}}}'
    
    def __add__(self,other):
        """other is an Int_set mutates self so that it contains exactly the
        elements in self plus the elements in other."""
        union = self._vals[:]
        for element in other._vals:
            if element not in union:
                union.append(element)
        self._vals = union
        return self._vals