# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:54:11 2019

@author: Akshita

Check Permutation: Given two strings, write a method to decide if one is a 
                   permutations of the other.
"""
import time
from collections import defaultdict

def check_permutation(A,B):
    """
    O(NlogN)
    """
    if len(A) != len(B):
        return False
    
    A = sorted(A)
    B = sorted(B)
    
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
        
    return True

def check_permutation_2(A,B):
    """
    O(N)
    """
    if len(A) != len(B):
        return False
    
    Adict = defaultdict(int)
    Bdict = defaultdict(int)
    
    for char in A:
        Adict[char] +=1
        
    for char in B:
        Bdict[char] += 1
        
    if len(Adict) != len(Bdict):
        return False
    
    for k,v in Adict.items():
        if Bdict[k] != v:
            return False
        
    return True

def main():
    
    A = 'tacocat'
    B = 'catttco'
    
    start = time.perf_counter()
    print(check_permutation(A,B))
    end = time.perf_counter()
    print('For O(NlogN) fuction, time taken is: {0:.6f}'.format(end-start))
    
    start = time.perf_counter()
    print(check_permutation_2(A,B))
    end = time.perf_counter()
    print('For O(N) fuction, time taken is: {0:.6f}'.format(end-start))
    
if __name__ == '__main__':
    
    main()


