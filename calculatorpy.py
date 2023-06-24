# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:24:39 2023

@author: COMPUTOUCH
"""

while True:
    first_num=float(input("enter the first number: "))
    
    operation=input(" the operation type:")
    
    secone_num=float(input("enter the second number: "))
    
    if operation=="+":
        print("the result is:",first_num+secone_num)
    elif operation=="-":
         print("the result is:",first_num-secone_num)
    elif operation=="*":
         print("the result is:",first_num*secone_num)
    elif operation=="/":
         print("the result is:",first_num/secone_num)
    else:
        print("error")
        
    repeat=input("do you want to perform anather operatio (y/n):")
    if repeat=="n":
        break
print("program exited")
    
        
