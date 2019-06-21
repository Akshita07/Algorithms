# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:28:17 2019

@author: Akshita
"""

def findMin(nums):
        
    if len(nums) == 1:
        return nums[0]
        
    left = 0
    right = len(nums) - 1
    mid = (left + right)//2
    minVal = nums[mid]
        
    while left <= right:
        mid = (left + right)//2
        
        if nums[mid] < minVal:
            minVal = nums[mid]
                
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
                
    return minVal

nums = [3,4,5,0,1,2]
print(findMin(nums))