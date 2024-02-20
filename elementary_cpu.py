# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:26:09 2023

@author: Marko
"""

class VoleMachine:
    def __init__(self):
        self.registers = [0] * 16
        self.memory = [0] * 256

    def load(self, reg, address):
        self.registers[reg] = self.memory[address]

    def load_to_memory(self, reg, address):
        self.memory[address] = self.registers[reg]

    def store(self, value, address):
        self.memory[address] = value
   
    def move(self, reg1, reg2):
        self.registers[reg2] = self.registers[reg1]

    def add_integer(self, reg1, reg2, reg3):
        self.registers[reg3] = self.registers[reg1] + self.registers[reg2]

    def add_float(self, reg1, reg2, reg3):
        binary1 = bin(self.registers[reg1])[2:].zfill(8)
        binary2 = bin(self.registers[reg2])[2:].zfill(8)
    
        sign1 = int(binary1[0])
        sign2 = int(binary2[0])
        exponent1 = int(binary1[1:4], 2)
        exponent2 = int(binary2[1:4], 2)
        mantissa1 = binary1[4:]
        mantissa2 = binary2[4:]
    
        # Перевірка на нульовість чисел
        if exponent1 == 0 and mantissa1 == "0000":
            self.registers[reg3] = self.registers[reg2]
            return
        elif exponent2 == 0 and mantissa2 == "0000":
            self.registers[reg3] = self.registers[reg1]
            return
    
        # Визначення більшої степені числа
        if exponent1 > exponent2:
            exponent_diff = exponent1 - exponent2
            mantissa2 = "1" + mantissa2
            mantissa2 = mantissa2.ljust(len(mantissa1), "0")
        else:
            exponent_diff = exponent2 - exponent1
            mantissa1 = "1" + mantissa1
            mantissa1 = mantissa1.ljust(len(mantissa2), "0")
    
        # Додавання мантис чисел
        mantissa_sum = int(mantissa1, 2) + int(mantissa2, 2)
        mantissa_sum_binary = bin(mantissa_sum)[2:].zfill(len(mantissa1))
    
        # Перевірка на переповнення мантиси
        if mantissa_sum >= 2 ** len(mantissa1):
            exponent_diff += 1
            mantissa_sum_binary = mantissa_sum_binary[1:]
    
        # Знак результуючого числа
        if sign1 == sign2:
            result_sign = sign1
        else:
            if exponent1 > exponent2:
                result_sign = sign1
            else:
                result_sign = sign2
    
        # Степінь результуючого числа
        result_exponent = max(exponent1, exponent2) + exponent_diff
    
        # Мантиса результуючого числа
        result_mantissa = mantissa_sum_binary[1:]
    
        # Запис результату в регістр
        result_binary = str(result_sign) + bin(result_exponent)[2:].zfill(3) + result_mantissa
        self.registers[reg3] = int(result_binary, 2)

        
    def rotate(self, reg):
        binary = bin(self.registers[reg])[2:].zfill(8)
        rotated_binary = binary[1:] + binary[0]
        self.registers[reg] = hex(int(rotated_binary, 2))

    def bitwise_or(self, reg1, reg2, reg3):
        self.registers[reg3] = self.registers[reg1] | self.registers[reg2]

    def bitwise_and(self, reg1, reg2, reg3):
        val1 = self.registers[reg1]
        val2 = self.registers[reg2]
        self.registers[reg3] = val1 & val2  # Виконуємо операцію поразрядного І

    def bitwise_xor(self, reg1, reg2, reg3):
        self.registers[reg3] = self.registers[reg1] ^ self.registers[reg2]

    def jump(self, reg, address):
        if self.registers[reg] == self.registers[0]:
            self.registers[0] = address

    def halt(self):
        # Завершення виконання програми
        pass
    
# Створюємо екземпляр машини Vole
machine = VoleMachine()

# Записуємо значення 0x0A в адресу 0x1 в пам'ять
machine.store(0x0A, 0x1)

# Записуємо значення 0x0B в адресу 0x2 в пам'ять
machine.store(0x0B, 0x2)

# Загружаємо значення з адреси 0x1 в регістр 0x0
machine.load(0x0, 0x1)

# Загружаємо значення з адреси 0x2 в регістр 0x1
machine.load(0x1, 0x2)

# Виконуємо додавання значень регістрів 0x0 та 0x1 і зберігаємо результат у регістр 0x2
machine.add_integer(0x0, 0x1, 0x2)

# Виводимо результат у шістнадцятковому форматі
machine.load_to_memory(0x2, 0x3)
print(hex(machine.memory[0x3]))



# Записуємо значення 0x0A в адресу 0x1 в пам'ять
machine.store(0xAB, 0x4)

# Записуємо значення 0x0B в адресу 0x2 в пам'ять
machine.store(0xCD, 0x5)

# Загружаємо значення з адреси 0x1 в регістр 0x0
machine.load(0x3, 0x4)

# Загружаємо значення з адреси 0x2 в регістр 0x1
machine.load(0x4, 0x5)
# Виклик методу move
print(hex(machine.registers[0x3]),hex(machine.registers[0x4]))
machine.move(0x3, 0x5)
machine.move(0x4, 0x3)
machine.move(0x5, 0x4)
machine.load_to_memory(0x3, 0x4)
machine.load_to_memory(0x4, 0x5)
print("After move\n", hex(machine.memory[0x4]), hex(machine.memory[0x5]))


machine.registers[0x1] = 0b01101011  # Завантажуємо число 2 у регістр 0x1
machine.registers[0x2] = 0b00111100  # Завантажуємо число 1.5 у регістр 0x2

machine.add_float(0x1, 0x2, 0x3)  # Додаємо числа у регістрах 0x1 і 0x2 і результат зберігаємо в регістрі 0x3

result = hex(machine.registers[0x3])
print(hex(machine.registers[0x1]), hex(machine.registers[0x2]), result)

machine.store(0xA7, 0x7)
machine.store(0x80, 0x8)
machine.load(0x6, 0x7)
machine.load(0x7, 0x8)
machine.bitwise_or(0x6, 0x7, 0x8)
print("Reg A",hex(machine.register[0x6]),"Reg B",hex(machine.register[0x7]),"Bitwise_Or:",hex(machine_register[0x8]))



#print("Add float 0x0A+0x0B\nresult", machine.memory[0x6])

# Виклик методу rotate
#machine.rotate(2)

# Виклик методу bitwise_or
#machine.bitwise_or(3, 1, 0xA)
# Виклик методу bitwise_and
#machine.bitwise_and(5, 6, 0xB)

# Виклик методу bitwise_xor
#machine.bitwise_xor(4, 7, 0xC)

# Виклик методу jump
#machine.jump(0xA, 0x3C)

# Виклик методу halt
#machine.halt()