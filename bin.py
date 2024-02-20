# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:40:28 2023

@author: Marko
"""
try:
    x = int(input("Введіть число: "))
    binary = bin(x)
    print("Деяткове",x,"це двійкове", binary)
except ValueError:
    print("Введене значення має бути числом")
    