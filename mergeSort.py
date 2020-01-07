# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:57:00 2020

@author: Akshita

Note: Not working properly at the moment! Figure out later.
"""
def merge(nums,L,R):
    
    i=j=k=0
    
    while i < len(L) and j < len(R):
        if L[i]<R[j]:
            nums[k] = L[i]
            i = i+1
        else:
            nums[k] = R[j]
            j = j+1
        k = k+1
        
    if i < len(L):
        while i!=len(L):
            nums[k] = L[i]
            i = i+1
            k = k+1
    elif j < len(R):
        while j!=len(R):
            nums[k] = R[j]
            j = j+1
            k = k+1
            
    
def mergeSort(nums):
    
    if len(nums) > 1:
        
        mid = len(nums)//2
        mergeSort(nums[:mid])
        mergeSort(nums[mid:])
        
        L = nums[:mid]
        R = nums[mid:]
        
        return merge(nums,L,R)
    

nums = [34, 2, 98, 74, 63, 102]
mergeSort(nums)
print(nums)
    