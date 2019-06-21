# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:38:18 2019

@author: Akshita
"""

def findPeakElement(nums):
    if len(nums) == 1:
        return 0
        
    left = 0
    right = len(nums) - 1
        
    while left <= right:
        mid = (left + right)//2
                        
        if mid == 0 and nums[mid] > nums[mid+1]:
            return mid
        elif mid == len(nums) - 1 and nums[mid] > nums[mid-1]:
            return mid
        elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid - 1
            

nums = [1, 2, 3, 1]
print(findPeakElement(nums))