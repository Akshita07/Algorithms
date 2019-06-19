# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:32:06 2019

@author: Akshita
"""

k = float(input())

r = float(input())

v = float(input())

amount = k + k*r

time_in_months = 1

while amount <= v:
    
    amount = amount + k + k*r
    time_in_months += 1

if time_in_months%12 != 0:
    time_in_years = int(round(time_in_months/12 + 1,0))
else:
    time_in_years = int(round(time_in_months/12,0))


print(time_in_years)

time_in_months = time_in_years*12
amount = k
while time_in_months > 0:
    amount = amount + k + k*r
    time_in_months -= 1
    
print(int(round(amount,0)))