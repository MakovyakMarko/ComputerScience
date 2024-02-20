# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:43:32 2023

@author: Marko
"""
try:
    x = int(input("Введіть число: "))
    crypto = x^0x55555555
    print("Зашифроване", x, "це", crypto)
    decrypt = crypto ^ 0x55555555
    print("Шифр", crypto, "це", decrypt)
except ValueError:
    print("Введене значення має бути числом")