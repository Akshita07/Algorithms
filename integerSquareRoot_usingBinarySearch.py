# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:06:00 2019

@author: Akshita
"""

def isqrt(x):
    
    if x == 0 or x == 1:
        return x
        
    left = 0
    right = x//2
        
    while(left <= right):
        mid = (left + right)//2
            
        if mid*mid == x:
            return mid
        elif mid*mid < x:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
                
    return ans


print(isqrt(19))