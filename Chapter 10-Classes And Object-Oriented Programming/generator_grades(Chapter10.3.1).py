# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:01:44 2021

@author: efemuratucarli
"""

# Finger exercise: Add to Grades a generator that meets the
# specification
# def get_students_above(self, grade):
# """Return the students a mean grade > g one at a time"""

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
    
class MIT_person(Person):
    _next_id_num = 0 
    
    def __init__(self,name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1
    
    def get_id_num(self):
        return self._id_num
    
    def __lt__(self,other):
        return self._id_num < other._id_num

class Student(MIT_person):
    pass

class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year
    def get_class(self):
        return self._year
    
class Grad(Student):
    pass

class Grades(object):
    def __init__(self):
        self._students = []
        self._grades = {}
        self._is_sorted = True
    
    def add_student(self, student):
        if student in self._students:
            raise ValueError('Duplicate Student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False
        
    def add_grade(self,student,grade):
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')
            
    def get_grades(self,student):
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')
    
    def get_students(self):
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s
    
    def get_students_above(self,grade):
        """Return the students a mean grade > g one at a time"""
        for s in self._students:
            total_grade = 0
            number_of_grades = 0
            for student_grade in self.get_grades(s):
                total_grade += student_grade
                number_of_grades += 1
            if (total_grade/number_of_grades) > grade:
                yield "the average grade of {} is {} which is larger than {}".format(s,(total_grade/number_of_grades),grade)

s1 = UG('helena', 2000)
s2 = Grad('dino')               
s3 = UG('maria', 1995)
s4 = Grad('diane')
grade_book = Grades()
grade_book.add_student(s1)
grade_book.add_student(s2)
grade_book.add_student(s3)
grade_book.add_student(s4)

for s in grade_book.get_students():
    grade_book.add_grade(s, 70)

grade_book.add_grade(s1, 81)
grade_book.add_grade(s2, 75)
grade_book.add_grade(s3, 30)
grade_book.add_grade(s4, 60)

for g in grade_book.get_students_above(65):
    print(g)