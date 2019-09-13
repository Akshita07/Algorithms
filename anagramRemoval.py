# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:14:01 2019

@author: Akshita
"""

from itertools import permutations

def removeAnagrams(s):
    
    list_of_strs = s[:]
    
    for strr in list_of_strs:
        perms = permutations(list(strr))
        for perm in list(perms):
            strr1 = ''.join(perm)
            if strr1 in list_of_strs and strr1 != strr:
                list_of_strs.remove(strr1)
                
    list_of_strs.sort()
    
    print(list_of_strs)
    
if __name__ == '__main__':
    
    s = ['code',
         'anagrams',
         'aaangrms',
         'odec']
    
    removeAnagrams(s)