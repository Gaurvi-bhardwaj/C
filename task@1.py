# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file

"""
######## Area of Circle #######

import math 

a=float(input('Radius of circle: '))   #variable inputs radius of circle 
area=math.pi*a*a                       #Calculation

print('The area of circle with radius',a,'is',area)


######## Print given File Extension ########

x=input('Enter Filename:')
a=x.split('.')
b=a[-1]

''' Programming File Dictionary'''

prog_file={'c':'C source code file','cgi':'Perl script file',
                   'class':'Java class file','cpp':'C++ source code file',
                   'py':'python','vb':'visual basic file',
                   'java':'java source code file','php':'PHP script file'}
for keys in prog_file:                  
    if b in prog_file.keys() :
       print(prog_file[b])
    
