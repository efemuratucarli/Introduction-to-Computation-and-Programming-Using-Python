"""
@author: efemuratucarli
"""

# Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to use a for loop that is a primality test nested inside a for loop that
# iterates over the odd integers between 3 and 999.

sum_of_the_prime_numbers = 0
for i in range(3,1000,2):
    for x in range(2,i):
        if i % x == 0:
            break
    if i == x+1 :
        sum_of_the_prime_numbers += i
        
print(sum_of_the_prime_numbers)
    