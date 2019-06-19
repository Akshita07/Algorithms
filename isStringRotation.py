# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:03:02 2019

@author: Akshita

String Rotation
"""

def is_string_rotation(A,B):
    
    AA = A + A
    
    return B in AA
    
def main():
    
    A = 'waterbottle'
    B = 'erbottlewat'
    
    print(is_string_rotation(A,B))
    
if __name__ == '__main__':
    
    main()