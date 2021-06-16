# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:15:32 2021

@author: xzy
"""

########### Fibonacci Series ##########

a=0
b=1
print(a)
print(b)
for i in range(0,20):
    c=a+b
    a,b=b,c
    print(c)