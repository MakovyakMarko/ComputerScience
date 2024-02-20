# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 14:10:09 2023

@author: Marko
"""

import math
try:
    def total_seconds(min, sec):
        return min * 60 + sec
    def speed(time):
        return 3600/time
    pace_minutes = int(input("Хвилини на 1 милю? "))
    pace_seconds = int(input("Секунди на 1 милю? "))
    miles = int(input("Всього миль? "))
    mph = speed(total_seconds(pace_minutes,pace_seconds))
    mph_format = "{:.2f}".format(mph)
    print("Ваша швидкість бігу буде: ",mph_format, "миль за годину")
    
    total = miles*total_seconds(pace_minutes,pace_seconds)
    elapsed_minutes = total // 60
    elapsed_seconds = total % 60
    print("Загальний час пробіжки:",elapsed_minutes, "хвилин",",",elapsed_seconds, "секунд")
except ZeroDivisionError:
    print("Ділення на ноль не допускається")