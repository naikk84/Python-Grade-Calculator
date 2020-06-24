# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:36:21 2020

@author: naikk
"""

grade = input("Enter Score:")
try:
    g = float(grade)
    if g > 1:
        print("Enter value in the range of 0 to 1")
    elif g < 0 :
        print ("Enter value in the range of 0 to 1")
    elif g < 0.6 :
        print("F")
    elif g >= 0.6 and g < 0.7 :
        print("D")
    elif g >= 0.7 and g < 0.8:
        print("C")
    elif g >= 0.8 and g < 0.9:
        print("B")
    elif g >= 0.9  and g <= 1.0:
        print("A")
except:
    print("enter the value in numbers")
    quit()

