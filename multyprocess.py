# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:07:49 2023

@author: Marko
"""

import multiprocessing

# Функція, яка буде виконуватися в першому процесі
def func1():
    print("Процес 1 виконується")

# Функція, яка буде виконуватися в другому процесі
def func2():
    print("Процес 2 виконується")

if __name__ == '__main__':
    # Створення об'єктів процесів
    process1 = multiprocessing.Process(target=func1)
    process2 = multiprocessing.Process(target=func2)

    # Запуск процесів
    process1.start()
    process2.start()

    # Очікування завершення процесів
    process1.join()
    process2.join()

    print("Обидва процеси завершилися")