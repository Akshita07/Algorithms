# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:26:04 2020

@author: Akshita
"""

def selectionSort(nums):
    
    n = len(nums)
    for i in range(0,n):
        min_el = nums[i]
        index = i
        for j in range(i+1,n):
            if nums[j] < min_el:
                min_el = nums[j]
                index = j
        if i != index:
            nums[i],nums[index] = nums[index],nums[i]
        
    return nums

nums = [34, 2, 98, 74, 63, 102]

print(selectionSort(nums))
                
            