# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:55:03 2019

@author: Akshita
"""

def findClosestElements(nums, k, x):
        
    if len(nums) <= k:
        return nums
        
    left = 0
    right = len(nums) - k - 1
        
    while left <= right:
        mid = (left + right)//2
            
        if x - nums[mid] > nums[mid + k] - x:
            left = mid + 1
        else:
            right = mid - 1
                
    return nums[left:left+k]

nums = [1, 2, 3, 4, 5]
k = 4
x = 3
print(findClosestElements(nums,k,x))