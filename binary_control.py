# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:04:14 2023

@author: Marko
"""
# функція, котра перекодовує байти в символи 
# згілно правил кодування UTF-8
def decode_utf8_bytes(encoded_bytes):
    characters = []
    i = 0
    while i < len(encoded_bytes):
        byte = encoded_bytes[i]
        if byte < 128:
            # 1-byte encoding
            characters.append(chr(byte))
            i += 1
        elif byte < 224:
            # 2-byte encoding
            byte1 = byte & 31
            byte2 = encoded_bytes[i + 1] & 63
            codepoint = (byte1 << 6) | byte2
            characters.append(chr(codepoint))
            i += 2
        elif byte < 240:
            # 3-byte encoding
            byte1 = byte & 15
            byte2 = encoded_bytes[i + 1] & 63
            byte3 = encoded_bytes[i + 2] & 63
            codepoint = (byte1 << 12) | (byte2 << 6) | byte3
            characters.append(chr(codepoint))
            i += 3
        else:
            # Invalid byte, skip
            i += 1

    return ''.join(characters)


encoded_bytes = b'234\xd1\x96\xd0\xb0\xd1\x96'
decoded_characters = decode_utf8_bytes(encoded_bytes)
print(decoded_characters)  # Виведе: 234іаі

# функція бітового додавання з вразуванням 
# переповнення 
def add_binary_numbers(num1, num2):
    # Перевірка на від'ємність
    is_negative1 = int(num1[0])  # Знаковий біт першого числа
    is_negative2 = int(num2[0])  # Знаковий біт другого числа

    # Перевірка на переповнення
    max_length = max(len(num1), len(num2))
    if len(num1) < max_length:
        num1 = num1[0] + num1[1:].zfill(max_length-1)
    if len(num2) < max_length:
        num2 = num2[0] + num2[1:].zfill(max_length-1)

    # Запис чисел у зворотному порядку для зручності складання
    num1 = num1[::-1]
    num2 = num2[::-1]

    carry = 0  # Запам'ятовування переносу
    result = []  # Результат складання

    for i in range(max_length):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        # Додавання бітів та переносу
        sum_bits = bit1 + bit2 + carry

        if sum_bits == 0 or sum_bits == 2:  # Результат 0 або 2
            result.append('0')
        else:  # Результат 1 або 3
            result.append('1')

        if sum_bits >= 2:  # Встановлення переносу
            carry = 1
        else:
            carry = 0

    # Перевірка на переповнення
    if carry == 1 and is_negative1 == is_negative2:
        return "Overflow"

    # Перевірка на зміну знаку
    if carry != is_negative1 and carry != is_negative2:
        return "Overflow"

    # Додавання знакового біта до результату
    result.append(str(carry))

    # Повернення результату у правильному порядку та знаку
    return ''.join(result[::-1])


num1 = "0111"  # -5 в двійковому додатковому коді
num2 = "1011"  # 5 в двійковому додатковому коді

result = add_binary_numbers(num1, num2)
print(result)


# ось приклад функції для перетворення числа в 
# двійкову систему з надлишком:
def excess_binary(number, N):
    # Додаємо N до числа
    excess_value = number + N

    # Перетворюємо в двійкову нотацію
    binary = bin(excess_value)[2:]

    # Повертаємо двійкову нотацію
    return binary

binary = excess_binary(5, 3)
print(binary)

# функція, котра перетворює двійковий код з надлишком 
# в десятковий формат:

def excess_binary_to_decimal(binary_code):
    sign_bit = binary_code[0]  # Перший біт - знак числа
    value_bits = binary_code[1:]  # Решта бітів - значення числа

    # Визначаємо знак числа
    sign = -1 if sign_bit == '1' else 1

    # Перевіряємо, чи число має надлишок
    has_excess = binary_code[1:].count('1') > binary_code[1:].count('0')

    # Перетворюємо решту бітів в десяткову систему
    decimal_value = int(value_bits, 2)

    # Враховуємо надлишок
    if has_excess:
        excess = pow(2, len(value_bits)) // 2
        decimal_value -= excess

    # Повертаємо результат, помножений на знак числа
    return decimal_value * sign
values = ['00011', '01111', '11100', '11010', '00000', '10000']

for binary in values:
    decimal = excess_binary_to_decimal(binary)
    print(f"Двійковий код: {binary}, Десяткове число: {decimal}")
# функція, яка перетворює десяткові значення в двійковий додатковий код довжиною вісім бітік:
def decimal_to_excess_binary(decimal_value):
    if decimal_value >= 0:
        binary = bin(decimal_value)[2:].zfill(8)
    else:
        binary = bin(256 + decimal_value)[2:]
    return binary

print("а. 6")
print("Двійковий код:", decimal_to_excess_binary(6))

print("г. 13")
print("Двійковий код:", decimal_to_excess_binary(13))

print("б. -6")
print("Двійковий код:", decimal_to_excess_binary(-6))

print("д. -1")
print("Двійковий код:", decimal_to_excess_binary(-1))

print("в. -17")
print("Двійковий код:", decimal_to_excess_binary(-17))

print("е. 0")
print("Двійковий код:", decimal_to_excess_binary(0))

# функція, яка приймає вхідне значення у форматі рядка 
# бітів і повертає обернене значення в тому ж форматі 
# двійокового додаткового коду
def inverse_binary_code(bits):
    inverted_bits = ""
    for bit in bits:
        inverted_bit = "0" if bit == "1" else "1"
        inverted_bits += inverted_bit
    return inverted_bits

result_a = inverse_binary_code("00000001")
print("Обернене значення (а):", result_a)

result_b = inverse_binary_code("01010101")
print("Обернене значення (б):", result_b)

result_c = inverse_binary_code("11111100")
print("Обернене значення (в):", result_c)

result_d = inverse_binary_code("11111110")
print("Обернене значення (г):", result_d)

result_e = inverse_binary_code("00000000")
print("Обернене значення (д):", result_e)

result_f = inverse_binary_code("01111111")
print("Обернене значення (е):", result_f)

# функція, яка обчислює найбільше і найменше число, 
# які можуть бути записані в двійковому додатковому 
# коді з заданою кількістью бітів:
def compute_range(num_bits):
    min_val = -2**(num_bits-1)
    max_val = 2**(num_bits-1) - 1
    return min_val, max_val

four_bit_range = compute_range(4)
print("Чотири біти:", four_bit_range)

six_bit_range = compute_range(6)
print("Шість бітів:", six_bit_range)

eight_bit_range = compute_range(8)
print("Вісім бітів:", eight_bit_range)

bit_16 = compute_range(16)
print("Шістнадцять біт: ", bit_16)

bit_32 = compute_range(32)
print("Тридцять два біти:", bit_32)

bit_64 = compute_range(64)
print("Шістдесять чотири біти: ", bit_64)
# функція для виконання операції додавання д війковому 
# додатковому коді:
    
def excess_to_decimal(bits):
    # Определение длины битовой комбинации
    length = len(bits)

    # Преобразование двоичной строки в десятичное число
    value = int(bits, 2)

    # Вычитание избытка из значения
    excess = 2**(length-1)
    value -= excess

    return value

def add_binary_with_excess(binary1, binary2):
    def excess_to_decimal(excess_binary):
        length = len(excess_binary)
        if excess_binary[0] == '0':
            return int(excess_binary, 2)
        else:
            max_value = 2 ** (length - 1)
            complement_value = int(excess_binary[1:], 2)
            decimal_value = complement_value - max_value
            return decimal_value

    def decimal_to_excess_binary(decimal_value, length):
        if decimal_value >= 0:
            binary = bin(decimal_value)[2:].zfill(length)
        else:
            max_value = 2 ** (length - 1)
            complement_value = max_value - abs(decimal_value)
            binary = bin(complement_value)[2:].zfill(length)
        return binary

    length = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(length)
    binary2 = binary2.zfill(length)

    decimal1 = excess_to_decimal(binary1)
    decimal2 = excess_to_decimal(binary2)

    sum_decimal = decimal1 + decimal2
    sum_binary = decimal_to_excess_binary(sum_decimal, length)

    return sum_binary

binary1 = '0101'
binary2 = '0010'
sum_binary = add_binary_with_excess(binary1, binary2)
print(binary1, "+", binary2, "=", sum_binary)
# Задача а
a = '0101'
b = '0010'
result1 = add_binary_with_excess(a, b)
print(a, "+", b, "=", result1)  # [0, 1, 1, 1]

# Задача г
a = '1110'
b = '0011'
result2 = add_binary_with_excess(a, b)
print(a, "+", b, "=", result2)  # [1, 0, 0, 0]

# Задача б
a = '0011'
b = '0001'
result3 = add_binary_with_excess(a, b)
print(a, "+", b, "=", result3)  # [0, 0, 1, 0]

# Задача д
a = '1010'
b = '1110'
result4 = add_binary_with_excess(a, b)
print(a, "+", b, "=", result4)  # [0, 1, 0, 0, 0]

# Задача в
a = '0101'
b = '1010'
result5 = add_binary_with_excess(a, b)
print(a, "+", b, "=", result5)  # [1, 1, 1, 1]

# функція, яка перетворює бінарний додатковий код 
# в десяткове значення
binary1 = '0101'
decimal1 = excess_to_decimal(binary1)
print(binary1, "в десятковій: ", decimal1) 
binary2 = '0010'
decimal2 = excess_to_decimal(binary2)
print(binary2, "в десятковій: ", decimal2) 
sum_num = decimal1 + decimal2
print("Сумма", decimal1, "+", decimal2, "=", sum_num)
binary3 = '1110'
decimal3 = excess_to_decimal(binary3)
print(binary3, "в десятковій: ", decimal3) 
binary4 = '0011'
decimal4 = excess_to_decimal(binary4)
print(binary4, "в десятковій: ", decimal4)  
sum_num1 = decimal3 + decimal4
print("Сумма", decimal3, "+", decimal4, "=", sum_num1)
binary5 = '0011'
decimal5 = excess_to_decimal(binary5)
print(binary5, "в десятковій: ", decimal5) 
binary6 = '0001'
decimal6 = excess_to_decimal(binary6)
print(binary6, "в десятковій: ", decimal6)  
sum_num2 = decimal5 + decimal6
print("Сумма", decimal5, "+", decimal6, "=", sum_num2)
binary7 = '1010'
decimal7 = excess_to_decimal(binary7)
print(binary7, "в десятковій: ", decimal7) 
binary8 = '1110'
decimal8 = excess_to_decimal(binary8)
print(binary8, "в десятковій: ", decimal8)  
sum_num3 = decimal7 + decimal8
print("Сумма", decimal7, "+", decimal8, "=", sum_num3) 
binary9 = '1010'
decimal9 = excess_to_decimal(binary9)
print(binary9, "в десятковій: ", decimal9) 
binary10 = '0101'
decimal10 = excess_to_decimal(binary10)
print(binary10, "в десятковій: ", decimal10)  
sum_num4 = decimal9 + decimal10
print("Сумма", decimal9, "+", decimal10, "=", sum_num4)

# функція, яка перетворює десятковий код на двійковий 
# додатковий код:
x = result1, result2, result3, result4, result5
for item in x:
    decimal1 = excess_to_decimal(item)
    print(item, "в десятковій: ", decimal1) 
# функція, яка обчислює операцію додавання чисел в 
# двійковому додатковому коді з перевіркою на переповнення
def add_binary_with_overflow(binary1, binary2):
    def excess_to_decimal(excess_binary):
        length = len(excess_binary)
        if excess_binary[0] == '0':
            return int(excess_binary, 2)
        else:
            max_value = 2 ** (length - 1)
            complement_value = max_value - int(excess_binary[1:], 2)
            return -complement_value

    def decimal_to_excess_binary(decimal_value, length):
        if decimal_value >= 0:
            binary = bin(decimal_value)[2:].zfill(length)
        else:
            max_value = 2 ** (length - 1)
            complement_value = max_value - abs(decimal_value)
            binary = bin(complement_value)[2:].zfill(length)
        return binary

    length = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(length)
    binary2 = binary2.zfill(length)

    decimal1 = excess_to_decimal(binary1)
    decimal2 = excess_to_decimal(binary2)

    sum_decimal = decimal1 + decimal2

    # Перевірка на переповнення
    if sum_decimal < -2 ** (length - 1) or sum_decimal >= 2 ** (length - 1):
        return "Переповнення"

    sum_binary = decimal_to_excess_binary(sum_decimal, length)

    return sum_binary
numbers = [('0100', '0011'), ('0101', '0110'), ('1010', '1010'), ('1010', '0111'), ('0111', '0001')]

for a, b in numbers:
    result = add_binary_with_overflow(a, b)
    print(result)

# функції, які виконують алгоритм перетворення чисел з 
# з десяткового представлення в чотирирозрядний двійковий
# код і операцію дадавання

def decimal_to_binary(decimal_value):
    if decimal_value >= 0:
        binary = bin(decimal_value)[2:].zfill(4)
    else:
        complement_value = abs(decimal_value) ^ 0b1111
        binary = bin(complement_value + 1)[2:].zfill(4)
    return binary


def binary_to_decimal(binary_value):
    if binary_value[0] == '0':
        decimal = int(binary_value, 2)
    else:
        complement_value = int(binary_value, 2) ^ 0b1111
        decimal = -(complement_value + 1)
    return decimal


def add_binary_with_overflow_1(binary1, binary2):
    decimal1 = binary_to_decimal(binary1)
    decimal2 = binary_to_decimal(binary2)
    sum_decimal = decimal1 + decimal2

    if sum_decimal > 7:
        sum_decimal -= 16
    elif sum_decimal < -8:
        sum_decimal += 16

    sum_binary = decimal_to_binary(sum_decimal)
    return sum_binary


numbers = [('6', '-1'), ('3', '-2'), ('4', '1010'), ('2', '-4'), ('1', '5')]

for a, b in numbers:
    result = add_binary_with_overflow_1(decimal_to_binary(int(a)), decimal_to_binary(int(b)))
    decimal = binary_to_decimal(result)
    print("Десяткове", decimal, "= Бінарне", result)
    
# функція, котра перетворює комбінації бітів у двійковій
# нотації з надлишком вісім в десятковий формат:
def binary_excess_to_decimal(binary_value):
    if binary_value[0] == '1':
        decimal = int(binary_value, 2) - 8
    else:
        decimal = int(binary_value, 2)
    return decimal

combinations = ['1110', '0111', '1000', '0010', '0000', '1001']

for binary_value in combinations:
    decimal_value = binary_excess_to_decimal(binary_value)
    print("Двійкове", binary_value, "= Десяткове", decimal_value)


def find_decimal_value(binary):
    if len(binary) != 4:
        raise ValueError('Неправильний розмір бітової послідовності')

    values = {
        '0000': -8,
        '0001': -7,
        '0010': -6,
        '0011': -5,
        '0100': -4,
        '0101': -3,
        '0110': -2,
        '0111': -1,
        '1000': 0,
        '1001': 1,
        '1010': 2,
        '1011': 3,
        '1100': 4,
        '1101': 5,
        '1110': 6,
        '1111': 7
    }

    if binary not in values:
        raise ValueError('Неправильне бітове число')

    return values[binary]
combinations = ['1110', '0111', '1000', '0010', '0000', '1001']

for binary in combinations:
    decimal = find_decimal_value(binary)
    print(f"х4: Двійкове {binary} = Десяткове {decimal}")
    
def find_decimal_value(binary):
    if len(binary) != 3:
        raise ValueError('Неправильний розмір бітової послідовності')

    values = {
        '000': -4,
        '001': -3,
        '010': -2,
        '011': -1,
        '100': 0,
        '101': 1,
        '110': 2,
        '111': 3
    }

    if binary not in values:
        raise ValueError('Неправильне бітове число')

    return values[binary]    

combinations = ['110', '111', '000', '010', '000', '001']

for binary in combinations:
    decimal = find_decimal_value(binary)
    print(f"х3: Двійкове {binary} = Десяткове {decimal}")

def find_decimal_value(binary):
    if len(binary) != 5:
        raise ValueError('Неправильний розмір бітової послідовності')

    values = {
        '00000': -16,
        '00001': -15,
        '00010': -14,
        '00011': -13,
        '00100': -12,
        '00101': -11,
        '00110': -10,
        '00111': -9,
        '01000': -8,
        '01001': -7,
        '01010': -6,
        '01011': -5,
        '01100': -4,
        '01101': -3,
        '01110': -2,
        '01111': -1,
        '10000': 0,
        '10001': 1,
        '10010': 2,
        '10011': 3,
        '10100': 4,
        '10101': 5,
        '10110': 6,
        '10111': 7,
        '11000': 8,
        '11001': 9,
        '11010': 10,
        '11011': 11,
        '11100': 12,
        '11101': 13,
        '11110': 14,
        '11111': 15
    }

    if binary not in values:
        raise ValueError('Неправильне бітове число')

    return values[binary]

combinations = ['11110', '10111', '11000', '00010', '00000', '11001']

for binary in combinations:
    decimal = find_decimal_value(binary)
    print(f"х5: Двійкове {binary} = Десяткове {decimal}")

for binary in combinations:
    decimal = find_decimal_value(binary)
    print(f"хN: Двійкове {binary} = Десяткове {decimal}")

def find_decimal_value(binary):
    num_bits = len(binary)
    n = int(binary[1:], 2) if binary[0] == '0' else 2 ** (num_bits - 1)

    if binary == '00000':
        return n // 2
    else:
        return n - 1 - int(binary[1:], 2)

combinations = ['11110', '10111', '11000', '00010', '00000', '11001']

for binary in combinations:
    decimal = find_decimal_value(binary)
    print(f"Binary: {binary}, Decimal: {decimal}")