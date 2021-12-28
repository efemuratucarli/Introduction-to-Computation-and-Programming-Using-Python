# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 16:51:02 2021

@author: efemuratucarli
"""


# Finger exercise: Implement a subclass of Person that meets the
# specification
# class Politician(Person):
# """ A politician is a person who can belong to a
# political party"""
# def __init__(self, name, party = None):
# """name and party are strings"""
# def get_party(self):
# """returns the party to which self belongs"""
# def might_agree(self, other):
# """returns True if self and other belong to the same
# part
# or at least one of then does not belong to a
# party"""

import datetime

class Person(object):
    def __init__(self,name):
        """Assumes name is a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(" ")
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self._birthday = None
    
    def get_name(self):
        """Returns self's full name"""
        return self._name
    
    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name
    
    def set_birthday(self,birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self._birthday = birthdate
        
    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days
    
    def __lt__(self,other):
        """Assume other a Person object
           Return True if self precedes other in alphabetical order,
           and False otherwise.Comparison is based on last names, but
           if these are the same then full names are compared."""
        if self._last_name == other._last_name :
            return self._name < other._name
        return self._last_name < other._last_name
    
    def __str__(self):
        """Return self's name"""
        return self._name
    
class Politician(Person):
    """ A politician is a person who can belong to a
        political party"""
    def __init__(self, name, party = None):
        """name and party are strings"""
        super().__init__(name)
        self._party = party
    
    def get_party(self):
        if self._party == None:
            raise ValueError("This politician is not a member of any party")
        return self._party
    
    def might_agree(self, other):
        """returns True if self and other belong to the same
           party or at least one of then does not belong to a
           party"""
        if self._party == None or other._party == None:
            return True
        if self._party == other._party :
            return True
        return False
    

        
        
        
        
        