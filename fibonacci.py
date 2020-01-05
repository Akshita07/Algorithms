# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:05:06 2020

@author: Akshita
"""

def fib(n):
    
    if n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(4))