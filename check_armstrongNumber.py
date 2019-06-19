# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 05:53:40 2019

@author: Akshita
"""

def check_if_armstrong(num):
    n = len(num)
    num = int(num)
    numm = num
    summ = 0
    while num > 0:
        
        digit = num%10
        num = num//10
        summ += pow(digit,n)
        
        if summ > numm:
            return 'No'
    
    if summ == numm:
        return 'Yes'
    else:
        return 'No'
    
num = input()

print(check_if_armstrong(num))