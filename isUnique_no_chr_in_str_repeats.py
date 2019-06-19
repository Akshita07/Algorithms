# -*- coding: utf-8 -*-
"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.

* Try implementing without additional data structure

@author: Akshita
"""
import time
from collections import defaultdict

def is_unique_1(A):
    """
    @string: A
    No extra data structure used
    
    O(NlogN)
    """
    B = sorted(A)
    
    for i in range(1,len(B)):
        if B[i-1] == B[i]:
            return False
    
    return True

def is_unique_2(A):
    """
    @String: A
    Use of extra data structure
    
    O(N)
    """
    B = defaultdict(int)
    
    for char in A:
        B[char] += 1
        if B[char] > 1:
            return False
        
    return True
    
if __name__ == '__main__':
    
    A = 'alskjotvmnew' 
    
    start = time.perf_counter()
    print(is_unique_1(A))
    end = time.perf_counter()
    print('For O(NlogN) fuction, time taken is: {0:.6f}'.format(end-start))
    
    start = time.perf_counter()
    print(is_unique_1(A))
    end = time.perf_counter()
    print('For O(N) fuction, time taken is: {0:.6f}'.format(end-start))
