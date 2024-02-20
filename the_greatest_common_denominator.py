# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:51:57 2023

@author: Marko
"""

import re
try:
    try: 
        m = input("Enter A: ")
        if m.isalpha():
            raise ValueError("Enter digit value")
        m = int(m)
        if m < 0:
            raise ValueError("Enter positive numbers")
    except ValueError as e:
        print(e)
    try:
        n = input("Enter B: ")
        if n.isalpha():
            raise ValueError("Enter digit value")
        n = int(n)
        if n < 0:
            raise ValueError("Enter positive numbers")
    except ValueErorr as e:
        print(e)
    try:
        if m == n:
            raise ValueError("Enter different values")
        if m < n:
            raise ValueError("a must be greater than b")
    except ValueError as e:
        print(e)
except KeyError as e:
    print(e)
def gcd(m,n):
    while n != 0:
        r=m % n
        m=n
        n=r
        return n
        
gcd = gcd(m,n)
print(gcd)