# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:52:49 2020

@author: Akshita
"""

def bubbleSort(nums):
    
    n = len(nums)
    flag = 1
    while flag:
        flag = 0
        for i in range(0,n-1):
            if nums[i+1] < nums[i]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                flag = 1
                
    return nums

nums = [34, 2, 98, 74, 63, 102]

print(bubbleSort(nums))
                