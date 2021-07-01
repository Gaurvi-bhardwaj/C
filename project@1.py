# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:56:27 2021

@author: xzy
"""
import pickle
print('MENU')
print("1.Display all records")
print("2.Insert a record")
print("3.Close")
while True:
     choice=int(input('enter choice\n1.display\n2.insert\n3.exit'))
     
     if choice==1:
         f=open(r"C:\Users\xzy\Desktop\school.txt",'rb')
         try:
             while True:
               r= pickle.load(f)
               print(r)
         except EOFError:
              break
         f.close()
     
     elif choice==2:
         f=open(r"C:\Users\xzy\Desktop\school.txt",'rb')
         lst=[]
         pos=int(input("enter position where to insert information:"))
         rollno=int(input("enter roll no"))
         name=input("enter name:")
         place=input("enter place:")
         record={'roll_no':rollno,'name':name,'place':place}
         while True:
             try:
                 rec=pickle.load(f)
                 lst.append(rec)
             except EOFError:
                 break
         f.close()
         lst.insert(pos-1,record)
         f=open(r"C:\Users\xzy\Desktop\school.txt",'wb')
         for x in lst:
             pickle.dump(x,f)
         f.close()
      
     elif choice==3:
          print("quitted")
          
     else:
         print("invalid choice")