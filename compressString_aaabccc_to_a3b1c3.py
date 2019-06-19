# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:47:43 2019

@author: Akshita

String Compression: Implement a method to perform basic string compression using
                    the counts of repeated characters. For ex, the string aabccc
                    would become a2b1c3. If the compressed string would not become
                    smaller than the original, method should return the original.
                    Sting has onlu uppercase and lowercase letters.
"""
import time

def compress_string(A):
    """
    @string: A
    
    O(N)
    """
    
    lst = []
    prev = A[0]
    count = 0
    for char in A:
        if char != prev:
            lst.append(prev)
            lst.append(str(count))
            prev = char
            count = 1
        else:
            count += 1
    
    lst.append(prev)
    lst.append(str(count))
    
    B = ''.join(lst)
    
    if len(B) < len(A):
        return B
    else:
        return A
    
def main():
    
    A = 'abbbb'
    
    start = time.perf_counter()
    print(compress_string(A))
    end = time.perf_counter()
    print('For O(N) fuction, time taken is: {0:.6f}'.format(end-start))
    
    
if __name__ == '__main__':
    
    main()
