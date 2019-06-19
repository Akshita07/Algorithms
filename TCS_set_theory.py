# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:05:05 2019

@author: Akshita
"""

p1 = int(input())

p2 = int(input())

p3 = int(input())

q = int(input())

e = int(input())

r = int(input())

ans1 = int((e-r-q+p1+p2+p3)/3)

print(ans1,end='\n')

ans2 = int(e-r-p1-p2-p3+2*q)

print(ans2)