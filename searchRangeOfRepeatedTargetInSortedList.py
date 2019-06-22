# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:29:24 2019

@author: Akshita
"""

def searchRange(nums, target):
        
    lower = -1
    upper = -1
        
    if len(nums) == 0:
        return [lower,upper]
        
    left = 0
    right = len(nums) - 1
        
    while left <= right:
        mid = (left + right)//2
            
        if nums[mid] == target:
            right = mid - 1
            lower = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)//2
        
        if nums[mid] == target:
            left = mid + 1
            upper = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
                
    return [lower,upper]

nums = [1, 1, 3, 3, 3, 3, 5, 5]

print(searchRange(nums,3))