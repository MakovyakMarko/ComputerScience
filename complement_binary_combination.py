dict = {'0111':7,
        '0110':6,
        '0101':5,
        '0100':4,
        '0011':3,
        '0010':2,
        '0001':1,
        '0000':0,
        "1111":-1,
        '1110':-2,
        "1101":-3,
        "1100":-4,
        "1011":-5,
        '1010':-6,
        '1001':-7,
        '1000':-8
        }
def complement_binary_combination(binary_combination):
    # Копіюємо бінарну комбінацію справа наліво до першої зустріченої одиниці включно
    print("Передана комбінація:",binary_combination)
     
    copied_combination = binary_combination[:binary_combination.rindex('1')]
    alone = binary_combination[binary_combination.rindex('1'):]
    print("Непереведені біти: ", alone)
    print("Слайсиг, справа наліво, без заміни першої справа 1 і подальших нулів: ", copied_combination)
    
    # Замінюємо значення решти бітів їх доповненнями
    complemented_combination = ''
    for bit in copied_combination:
        if bit == '0':
            complemented_combination += '1'
        else:
            complemented_combination += '0'

    # Повертаємо результат об'єднання копійованої комбінації та доповнених бітів
    #complement_combination
    return complemented_combination + alone

def binary_to_decimal(binary_combination):
    print("Передана комбінація: ", binary_combination)
    print("Це число: ", dict[binary_combination])
    digit = binary_combination[1:]
    sign_bit = binary_combination[0]
    if sign_bit == '0':
        # Додатне число, просто перетворюємо в десяткове значення
        binary_number = complement_binary_combination(binary_combination)
    else:
        # Від'ємне число, відкидаємо знаковий біт і розглядаємо залишок
        binary_number = complement_binary_combination(binary_combination[1:])

    # Перетворення бінарного числа в десяткове
    decimal_value = int(binary_number, 2)

    if sign_bit == '1':
        # Від'ємне число, від'ємне значення
        decimal_value *= -1
    return decimal_value
binary_combination = '1010'
complemented_combination = complement_binary_combination(binary_combination)
print("Доповнений біт: ",complemented_combination)  # Результат: 0101
decimal_value = binary_to_decimal(binary_combination)
print("Результат: ", decimal_value)