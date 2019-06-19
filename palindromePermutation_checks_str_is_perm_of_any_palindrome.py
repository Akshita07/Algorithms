# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:27:46 2019

@author: Akshita

Palindrome Permutation: Given a string, write a function tocheck if it is a 
                        permutation of a palindrome. Palindrome does not need
                        to be limited to just dictionary words.
"""
import time
from collections import defaultdict

def is_palindrome_permutation(A):
    """
    O(N)
    """
    A = A.replace(' ','')
    
    chrCount = defaultdict(int)
    
    for char in A:
        chrCount[char] += 1
    
    odd = 0
    for v in chrCount.values():
        if v%2 != 0:
            odd += 1
    
    if odd > 1:
        return False
    else:
        return True
    
def main():
    
    A = 'taco cat'
    
    start = time.perf_counter()
    print(is_palindrome_permutation(A))
    end = time.perf_counter()
    print('For O(N) fuction, time taken is: {0:.6f}'.format(end-start))
    
if __name__ == '__main__':
    
    main()