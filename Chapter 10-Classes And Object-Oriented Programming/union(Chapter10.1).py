# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 20:53:26 2021

@author: efemuratucarli
"""
# Add a method satisfying the specification below
# to the Int_set class.
# def union(self, other):
# """other is an Int_set
# mutates self so that it contains exactly the
# elemnts in self
# plus the elements in other."""

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
    
    def union(self,other):
        """other is an Int_set mutates self so that it contains exactly the
        elements in self plus the elements in other."""
        union = self._vals[:]
        for element in other._vals:
            if element not in union:
                union.append(element)
        self._vals = union
        
        
        
        