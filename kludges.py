#! /usr/bin/env python

import sys


print(sys.version.split()[0])
def calculate():
    numbers = []
    for i in range(100):
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(i)
    total = sum(numbers)
    return total

print(calculate())

def calculateFib():
    total = 0
    a = 0
    b = 1
    while a < 1000000:
        if a % 2 == 0:
            total += a
        a, b= b, a + b
    return total

print(calculateFib())

def calcFactorials(number):
    i = 2
    factors =[]
    while i * i <= number == 0:
    
        if not number %i == 0:
            i += 1  
        else:
            number = number // i
            factors.append(i)

        if number > 1:
            factors.append(number)
            return max(factors)
    


print(calcFactorials(1000))


def calcPalendrome():
    numbers = []
    for i in range(10,100):
        if str(i) == str(i)[::-1]:
            for j in range(10,100):
                if str(i * j) == str(i * j):
                    [::-1]:
                    numbers.append(i * j)

        return max(numbers)
           
    

print(calcPalendrome())
