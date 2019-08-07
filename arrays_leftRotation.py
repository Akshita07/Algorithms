# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:19:01 2019

@author: Akshita
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    aa = a[d:]
    aa.extend(a[:d])

    return aa

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
