# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:06:01 2019

@author: Akshita
"""

N, Q = map(int,input().split())

array = list(map(int,input().split()))

for _ in range(Q):
    query = list(map(int,input().split()))
    
    if query[0] == 1:
        if array[query[1]-1] == 0:
            array[query[1]-1] = 1
        else:
            array[query[1]-1] = 0
    else:
        if array[query[2]-1] == 0:
            print('EVEN')
        else:
            print('ODD')