# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:20:37 2019

@author: Akshita
"""
from collections import defaultdict

def candyDistributor(T):
    
    totalCandy = len(T)
    candy2give = totalCandy//2
    print('candy2give',candy2give)
    
    candyDict = defaultdict(int)
    for i in range(totalCandy):
        candyDict[T[i]] += 1
        
    candyDictValues = sorted(candyDict.values(),reverse=True)
    print(candyDictValues)
    count = 0
    for value in candyDictValues:
        if candy2give >= value and value != 1:
            candy2give = candy2give - value + 1
            count += 1
        elif candy2give == value and value == 1:
            candy2give = candy2give - value
        elif candy2give < value:
            candy2give = 0
            count += 1
                                
    return(count)
    
if __name__ == '__main__':
    
    T = [3, 4, 3, 3, 3, 3, 5, 3, 3, 3]
    
    remainingTypeOfCandies = candyDistributor(T)
    
    print(remainingTypeOfCandies)