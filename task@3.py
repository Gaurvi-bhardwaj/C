# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:15:32 2021

@author: xzy
"""

######### Print all positive numbers from list #########

l=int(input('Enter length of list:'))
list=[]
for i in range(0,l+1):
    a=float(input('enter any number;'))
    list.append(a)
    
print('The list is',list)

list1=[]
for j in list:
    if j>0:
       list1.append(j)
print('List containing all positive numbers:',list1)       