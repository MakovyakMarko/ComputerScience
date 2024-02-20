# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 00:06:35 2023

@author: Marko
"""
class SearchManager:
    def __init__(self):
        self.files = []
    
    def add_file(self, file_path):
        self.files.append(file_path)
    
    def linear_search(self, file_path, target):
        results = []
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                try:
                    if target == int(line.strip()):
                        results.append((file_path, i+1))
                except ValueError:
                    pass
        
        return results
    
    def binary_search(self, target):
        results = []
        # Implement binary search here
        
    @staticmethod
    def count_occurrences(file_path, target):
        count = 0
        with open(file_path, 'r') as file:
            for line in file:
                if target in line:
                    count += 1
        return count

    @staticmethod
    def compute_sum(file_path):
        total = 0
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    total += num
                except ValueError:
                    pass
        return total

    @staticmethod
    def find_maximum(file_path):
        max_num = None
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    if max_num is None or num > max_num:
                        max_num = num
                except ValueError:
                    pass
        return max_num

    @staticmethod
    def find_minimum(file_path):
        min_num = None
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    if min_num is None or num < min_num:
                        min_num = num
                except ValueError:
                    pass
        return min_num

    @staticmethod
    def filter_elements(file_path, condition):
        filtered = []
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    if condition(num):
                        filtered.append(num)
                except ValueError:
                    pass
        return filtered

    @staticmethod
    def find_substring(file_path, substring):
        with open(file_path, 'r') as file:
            content = file.read()
            index = content.find(substring)
        return index


# Створюємо об'єкт класу FileProcessor
file_processor = SearchManager()


# Виклик методів на файлах
# ... (продовжуйте з викликом методів як у попередньому коді)
# Виклик методу lineat_search() на файлі file1.txt
target = 20
result = file_processor.linear_search('file1.txt', target)
print(f"Linear Search in file1.txt for target {target}: {result}")

# Виклик методу count_occurrences() на файлі file2.txt
target = 'example.com'
result = file_processor.count_occurrences('file2.txt', target)
print(f"Occurrences of '{target}' in file2.txt: {result}")

# Виклик методу compute_sum() на файлі file1.txt
result = file_processor.compute_sum('file1.txt')
print(f"Sum of numbers in file1.txt: {result}")

# Виклик методу find_maximum() на файлі file2.txt
result = file_processor.find_maximum('file2.txt')
print(f"Maximum number in file2.txt: {result}")

# Виклик методу find_minimum() на файлі file1.txt
result = file_processor.find_minimum('file1.txt')
print(f"Minimum number in file1.txt: {result}")

# Виклик методу filter_elements() на файлі file2.txt
condition = lambda x: len(x) > 10  # Фільтр: довжина рядка більше 10
result = file_processor.filter_elements('file2.txt', condition)
print(f"Filtered elements in file2.txt: {result}")

# Виклик методу find_substring() на файлі file1.txt
substring = 'world'
result = file_processor.find_substring('file1.txt', substring)
print(f"Substring '{substring}' found at index: {result}")    

class FileSearchProcessor:
    def linear_search(self, filename, target):
        with open(filename, 'r') as file:
            content = file.readlines()

        for i, line in enumerate(content):
            if line.strip() == target:
                return i

        return None

    def count_occurrences(self, filename, target):
        count = 0
        with open(filename, 'r') as file:
            for line in file:
                if target in line:
                    count += 1
        return count

    def compute_sum(self, filename):
        total = 0
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    total += num
                except ValueError:
                    pass
        return total

    def find_maximum(self, filename):
        # Реалізація пошуку найбільшого числа у файлі
        pass
        max_num = None
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    if max_num is None or num > max_num:
                        max_num = num
                except ValueError:
                    pass
        return max_num
    def find_minimum(self, filename):
        # Реалізація пошуку найменшого числа у файлі
        min_num = None
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    if min_num is None or num < min_num:
                        min_num = num
                except ValueError:
                    pass
        return min_num
    def filter_elements(self, filename, condition):
        # Реалізація фільтрації елементів у файлі за певною умовою
        filtered = []
        with open(filename, 'r') as file:
            for line in file:
                try:
                    num = int(line)
                    if condition(num):
                        filtered.append(num)
                except ValueError:
                    pass
        return filtered

    def find_substring(self, filename, substring):
        # Реалізація пошуку підрядка у файлі
        with open(filename, 'r') as file:
            content = file.read()
            index = content.find(substring)
        return index

file_processor = FileSearchProcessor()

# Лінійний пошук у файлі file1.txt для значення 5
result = file_processor.linear_search("file1.txt", "5")
print("Linear Search:", result)

# Підрахунок кількості входжень елемента у файлі file2.txt
occurrences = file_processor.count_occurrences("file2.txt", "example.com")
print("Occurrences:", occurrences)

# Обчислення суми елементів у файлі file1.txt
total_sum = file_processor.compute_sum("file1.txt")
print("Sum:", total_sum)

# Пошук найбільшого числа у файлі file2.txt
maximum = file_processor.find_maximum("file2.txt")
print("Maximum:", maximum)

# Пошук найменшого числа у файлі file1.txt
minimum = file_processor.find_minimum("file1.txt")
print("Minimum:", minimum)

# Фільтрація елементів у файлі file2.txt за певною умовою
condition = lambda x: x % 2 == 0  # Фільтруємо парні числа
filtered_elements = file_processor.filter_elements("file2.txt", condition)
print("Filtered Elements:", filtered_elements)

# Пошук підрядка "world" у файлі file1.txt
substring_index = file_processor.find_substring("file1.txt", "world")
print("Substring Index:", substring_index)
