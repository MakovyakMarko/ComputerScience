class LZW:
    def __init__(self):
        self.dictionary = {}

    def compress(self, data):
        self.dictionary.clear()
        compressed_data = []
        next_code = 256

        # Ініціалізація словника з початковим алфавітом
        for i in range(256):
            self.dictionary[chr(i)] = i

        current_sequence = data[0]
        for symbol in data[1:]:
            new_sequence = current_sequence + symbol

            # Якщо поточна послідовність вже присутня в словнику, продовжуємо додавати символи
            if new_sequence in self.dictionary:
                current_sequence = new_sequence
            else:
                # Виводимо код останньої відомої послідовності
                compressed_data.append(self.dictionary[current_sequence])

                # Додаємо нову послідовність до словника з новим унікальним кодом
                self.dictionary[new_sequence] = next_code
                next_code += 1

                current_sequence = symbol

        # Виводимо код останньої відомої послідовності
        compressed_data.append(self.dictionary[current_sequence])

        return compressed_data
    
lzw = LZW()

data = "ABABABAABABA"
compressed_data = lzw.compress(data)

print(compressed_data)

lzw = LZW()

data = "ABABABAABABA"
compressed_data = lzw.compress(data)

bit_representation = ""
for code in compressed_data:
    binary_code = bin(code)[2:]  # Відкидаємо префікс '0b'
    bit_representation += binary_code.zfill(16)  # Доповнюємо до 16 бітів

print(bit_representation)