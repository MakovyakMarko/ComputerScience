# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 23:59:27 2023

@author: Marko
"""

class LinearAlgorithms:
    @staticmethod
    def linear_search(arr, target):
        """Лінійний пошук елемента у масиві"""
        for i, num in enumerate(arr):
            if num == target:
                return i
        return -1

    @staticmethod
    def count_occurrences(arr, target):
        """Підрахунок кількості входжень елемента у масив"""
        count = 0
        for num in arr:
            if num == target:
                count += 1
        return count

    @staticmethod
    def compute_sum(arr):
        """Обчислення суми елементів у масиві"""
        total = 0
        for num in arr:
            total += num
        return total

    @staticmethod
    def find_maximum(arr):
        """Пошук найбільшого елемента у масиві"""
        if not arr:
            return None
        max_num = arr[0]
        for num in arr:
            if num > max_num:
                max_num = num
        return max_num

    @staticmethod
    def find_minimum(arr):
        """Пошук найменшого елемента у масиві"""
        if not arr:
            return None
        min_num = arr[0]
        for num in arr:
            if num < min_num:
                min_num = num
        return min_num

    @staticmethod
    def filter_elements(arr, condition):
        """Фільтрація елементів у масиві за певною умовою"""
        filtered = []
        for num in arr:
            if condition(num):
                filtered.append(num)
        return filtered

    @staticmethod
    def find_substring(string, substring):
        """Пошук підрядка у рядку"""
        n = len(string)
        m = len(substring)
        for i in range(n - m + 1):
            if string[i:i + m] == substring:
                return i
        return -1

linear_alg = LinearAlgorithms()

arr = [1, 2, 3, 4, 5]
target = 3

index = linear_alg.linear_search(arr, target)
print(f"Елемент {target} знаходиться на позиції {index}")

count = linear_alg.count_occurrences(arr, target)
print(f"Елемент {target} зустрічається {count} разів")

total_sum = linear_alg.compute_sum(arr)
print(f"Сума елементів у масиві: {total_sum}")

maximum = linear_alg.find_maximum(arr)