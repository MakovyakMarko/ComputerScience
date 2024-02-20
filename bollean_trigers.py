# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:05:47 2023

@author: Marko
"""


x = False
y = True
# AND
z0 = x&x
z1 = x&y
z2 = y&x
z3 = y&y
print("AND:",z0,z1,z2,z3)

# NAND
z0 = not(x&x)
z1 = not(x&y)
z2 = not(y&x)
z3 = not(y&y)
print("NAND:",z0,z1,z2,z3)

# OR
z0 = x|x
z1 = x|y
z2 = y|x
z3 = y|y
print("OR:",z0,z1,z2,z3)

# NOR
z0 = not(x|x)
z1 = not(x|y)
z2 = not(y|x)
z3 = not(y|y)
print("NOR:",z0,z1,z2,z3)


# XOR
z0 = x^x
z1 = x^y
z2 = y^x
z3 = y^y
print("XOR:",z0,z1,z2,z3)

#NXOR
z0 = not(x^x)
z1 = not(x^y)
z2 = not(y^x)
z3 = not(y^y)
print("NXOR:",z0,z1,z2,z3)

# NOT
z0 = ~x&1
z1 = ~y&1
print("NOT:",z0,z1)
