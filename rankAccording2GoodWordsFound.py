# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:30:02 2019

@author: Akshita
"""
from collections import defaultdict

A = 'hello_hi_hola'
goodWords = A.split('_')

num = 3

B = ['hi_my_name_is_akshita','hello_how_are_you_hola','hi_hola']

cntIndx = []
for i in range(num):
    stringWords = B[i].split('_')
    
    d = defaultdict(int)
    for word in stringWords:
        d[word] += 1
        
    count = 0
    for word in goodWords:
        if word not in d.keys():
            count += 0
        else:
            count += d[word]
    
    cntIndx.append((count,i))
    #counts.append(count)
    #index.append(i)
    
ans = [x for y,x in sorted(cntIndx,reverse = True, key = lambda t: t[0])]

print(ans)
    