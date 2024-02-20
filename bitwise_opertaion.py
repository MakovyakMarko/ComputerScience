# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:27:54 2023

@author: Marko
"""

def bitwise_and(number1, number2):
    result = number1 & number2
    return result

def bitwise_or(number1, number2):
    result = number1 | number2
    return result

def bitwise_xor(number1, number2):
    result = number1 ^ number2
    return result

def bitwise_not(number):
    result = ~number & 0xFFFFFFFF
    return result
def truncate_result(number, length):
    mask = (1 << length) - 1
    result = bitwise_not(number) & mask
    return result

def bitwise_shift_left(number, shift):
    result = number << shift
    return result

def bitwise_shift_right(number, shift):
    result = number >> shift
    return result

def cyclic_shift_right(number, shift):
    bits = number.bit_length()
    mask = 2 ** bits - 1
    return ((number >> shift) | (number << (bits - shift))) & mask

def cyclic_shift_left(number, shift):
    bits = number.bit_length()
    mask = 2 ** bits - 1
    return ((number << shift) | (number >> (bits - shift))) & mask

number1 = 0b11011010
number2 = 0b10101010

result_and = bitwise_and(number1, number2)
result_or = bitwise_or(number1, number2)

print("Bitwise AND \nnum 1", bin(number1),"\nnum 2", bin(number2),"\nreslt", bin(result_and))  # Вивід: 0b10001010
print("Bitwise OR \nnum 1", bin(number1),"\nnum 2", bin(number2),"\nreslt", bin(result_or))  # Вивід: 0b11111010

number = 0b10101010
mask = 0b11110000

result_xor = bitwise_xor(number, mask)

print("Bitwise XOR \nnum 1",bin(number), "\nmask ", bin(mask), "\nreslt", bin(result_xor))  # Вивід: 0b01011010

number = 0b11100010

result_not = truncate_result(number, 8)

print("Bitwise NOT \nnum",bin(number),"\nreslt",bin(result_not))  # Вивід: -0b10101011

bitwise_shit_left = bitwise_shift_left(result_not, 3)
print("Bitwise shift left 3\nnum", bin(result_not), "\nresult", bin(bitwise_shit_left))

bitwise_shit_right = bitwise_shift_right(result_not, 1)
print("Bitwise shift right 1 \nnum", bin(result_not), "\nresult", bin(bitwise_shit_right))

number = 0b11001010
shifted = cyclic_shift_right(number, 3)
print("Cicle shift right \nnumber", bin(number),"\nshift 3\nresult", bin(shifted))  # Вивід: 0b01011001

number = 0b11001010
shifted = cyclic_shift_left(number, 3)
print("Cicle shift left \nnumber", bin(number),"\nshift 3\nresult", bin(shifted))  # Вивід: 0b01010110


ch = 'a'  # Строчная буква 'a'
ascii_code = ord(ch)  # Получаем код ASCII символа
mask = 0b00100000  # Маска для сброса шестого бита
result = chr(ascii_code & ~mask)  # Применяем операцию "И" с инвертированной маской и получаем прописную букву 'A'
print(ch,"+ mask", bin(mask), "\nresult", result)

ch = 'A'  # Прописная буква 'A'
ascii_code = ord(ch)  # Получаем код ASCII символа
mask = 0b00100000  # Маска для установки шестого бита
result = chr(ascii_code | mask)  # Применяем операцию "ИЛИ" с маской и получаем строчную букву 'a'
print(ch,"+ mask", bin(mask), "\nresult", result)

def cyclic_shift_left(hex_number):
    # Перетворення шістнадцяткового числа у бінарний формат
    binary_number = bin(int(hex_number, 16))[2:].zfill(len(hex_number)*4)
    
    # Виконання циклічного зсуву вліво
    shifted_number = binary_number[1:] + binary_number[0]
    
    # Перетворення бінарного числа у шістнадцятковий формат
    result = hex(int(shifted_number, 2))[2:].upper()
    
    return result

hex_number = "0x5C"
shifted_number = cyclic_shift_left(hex_number)
print("HEX",hex_number,"\nshifted left for 1 \nresult",shifted_number)