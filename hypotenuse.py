# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:34:41 2023

@author: Marko
"""
import math
#sideA = int(input("Довжина сторони А? "))
#sideB = int(input("Довжина сторони В? "))
#hypotenuse =  math.sqrt(sideA**2 + sideB **2)
#print(int(hypotenuse))
try:
    sideA = float(input("Довжина сторони А? "))
    sideB = float(input("Довжина сторони В? "))
    hypotenuse =  math.sqrt(sideA**2 + sideB **2)
    print(hypotenuse)
except ValueError:
    print("Введене значення має бути числом")