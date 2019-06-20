# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:21:43 2019

@author: Akshita

Sum of integers in two lists element-wise
"""

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = list(map(sum,zip(A,B)))

print(' '.join(map(str,C)))