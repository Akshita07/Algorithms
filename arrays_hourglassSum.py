# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:08:46 2019

@author: Akshita
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    ans = -63
    for i in range(0,4):
        j = 0
        while(j < 4):
            summ = 0
            summ += arr[i][j] + arr[i][j+1] + arr[i][j+2] 
            summ += arr[i+1][j+1]
            summ += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            j += 1
            if(summ > ans):
                ans = summ
    return ans


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
