# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:36:45 2019

@author: Akshita
"""

def binarySearch(nums, target):
    
    if len(nums) == 0:
        return -1
    
    left = 0
    right = len(nums)-1
        
    while left <= right:
        mid = (left + right)//2
            
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
                
    return -1


nums = [-1,0,3,5,9,12]
target = 9

print(binarySearch(nums, target))