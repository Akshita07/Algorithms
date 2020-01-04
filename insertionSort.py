# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:17:17 2020

@author: Akshita
"""

def insertionSort(nums):
    
    n = len(nums)
    for i in range(1,n):
        j = i
        num = nums[i]
        while j-1 >= 0 and nums[j-1] > num:
            nums[j] = nums[j-1]
            j = j-1
        nums[j] = num

    return nums

nums = [34, 2, 98, 74, 63, 102]

print(insertionSort(nums))
        