# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:53:03 2019

@author: Akshita
"""

from collections import defaultdict

N = int(input())
array = list(map(int,input().split()))
Q = int(input())

dictArr = defaultdict(int)

for i in range(N):
    dictArr[array[i]] += 1
    
for _ in range(Q):
    B = int(input())
    
    if B in dictArr.keys():
        print(dictArr[B])
    else:
        print('NOT PRESENT')