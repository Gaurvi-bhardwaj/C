# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:10:17 2021

@author: xzy
"""

#############Count Occurences of Each letter in a String##############
def most_frequent(s):
    l=list(s)
    print(l)
    result={}
    for each in l:
        result.update({each:l.count(each)})
        sort_orders = sorted(result.items(), key=lambda x: x[1], reverse=True)

    for i in sort_orders:
	    print(i[0], i[1])

        
#main
s=input('Enter string:')
most_frequent(s)