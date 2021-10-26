# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:06:30 2021

@author: efemuratucarli
"""

# Write a program that first stores the first ten
# numbers in the Fibonnaci sequence to a file named fib_file. Each
# number should be on a separate line in the file. The program should
# then read the numbers from the file and print them

with open("fibonacci.txt","w") as fib_file:
    d = {0:1,1:1}
    def fib(x):
        global d
        if x == 1 or x == 0 :
            return 1
        else:
            ans = fib(x-1) + fib(x-2)
            if x not in d:
                d[x] = ans
            return ans
    fib(9)
    for i in range(10):
        fib_file.write(str(d[i]) + "\n")

with open("fibonacci.txt","r") as fib_file:
    for line in fib_file:
        print(line)