# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:18:29 2019

@author: Akshita

Find Nth Prime in the given range
"""
import math

def is_prime(num):
    
    if num <= 1:
        return False
    
    for ii in range(2,int(math.sqrt(num))+1):
        if num%ii == 0:
            return False
    
    return True

def nth_prime(first,last,n):
    
    if first < 0 or last > 1500000:
        return "Invalid Input"
    elif last < first:
        return "Invalid Input"
    
    count = 0
    for i in range(first,last):
        if is_prime(i):
            count += 1
            if count == n:
                return i
            
    return "No prime number is present at this index"

def main():
    first = int(input())
    last = int(input())
    n = int(input())
    
    print(nth_prime(first,last,n),end='\n')
    
if __name__ == '__main__':
    
    main()
