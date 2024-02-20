# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:58:29 2023

@author: Marko
"""

def encode_utf8_file(input_file, output_file, output_file_1):
    with open(input_file, 'r') as input:
        characters = input.read()
        encoded_bytes = b''
        for character in characters:
            codepoint = ord(character)
            if codepoint < 128:
                # 1-byte encoding
                encoded_bytes += codepoint.to_bytes(1, 'big')
            elif codepoint < 2048:
                # 2-byte encoding
                byte1 = 192 | (codepoint >> 6)
                byte2 = 128 | (codepoint & 63)
                encoded_bytes += bytes([byte1, byte2])
            else:
                # 3-byte encoding
                byte1 = 224 | (codepoint >> 12)
                byte2 = 128 | ((codepoint >> 6) & 63)
                byte3 = 128 | (codepoint & 63)
                encoded_bytes += bytes([byte1, byte2, byte3])
    with open(output_file, 'wb') as output:
        output.write(encoded_bytes)
    with open(output_file_1, 'w') as output:
        hex_data = ' '.join(f'{byte:02X}' for byte in encoded_bytes)
        output.write(hex_data)
    return output_file, output_file_1

def decode_hex_to_utf8(input_file_hex, output_file_utf8):
    with open(input_file_hex, 'r') as input_hex:
        hex_data = input_hex.read().replace(" ", "")
        encoded_bytes = bytes.fromhex(hex_data)
        decoded_text = ''

        i = 0
        while i < len(encoded_bytes):
            byte1 = encoded_bytes[i]
            if byte1 < 128:
                # 1-byte encoding
                decoded_text += chr(byte1)
                i += 1
            elif byte1 < 224:
                # 2-byte encoding
                byte2 = encoded_bytes[i + 1]
                codepoint = ((byte1 & 31) << 6) | (byte2 & 63)
                decoded_text += chr(codepoint)
                i += 2
            else:
                # 3-byte encoding
                byte2 = encoded_bytes[i + 1]
                byte3 = encoded_bytes[i + 2]
                codepoint = ((byte1 & 15) << 12) | ((byte2 & 63) << 6) | (byte3 & 63)
                decoded_text += chr(codepoint)
                i += 3

    with open(output_file_utf8, 'w') as output_utf8:
        output_utf8.write(decoded_text)
    return output_file_utf8

def decode_utf8_file(input_file, output_file):
    with open(input_file, 'rb') as input:
        encoded_bytes = input.read()
        decoded_text = ''
        i = 0
        while i < len(encoded_bytes):
            byte1 = encoded_bytes[i]
            if byte1 < 128:
                # 1-byte encoding
                decoded_text += chr(byte1)
                i += 1
            elif byte1 < 224:
                # 2-byte encoding
                byte2 = encoded_bytes[i + 1]
                codepoint = ((byte1 & 31) << 6) | (byte2 & 63)
                decoded_text += chr(codepoint)
                i += 2
            else:
                # 3-byte encoding
                byte2 = encoded_bytes[i + 1]
                byte3 = encoded_bytes[i + 2]
                codepoint = ((byte1 & 15) << 12) | ((byte2 & 63) << 6) | (byte3 & 63)
                decoded_text += chr(codepoint)
                i += 3

    with open(output_file, 'w') as output:
        output.write(decoded_text)
        output.close()
        
input_file = "test_text_for_encode.txt"
utf8_output_file = "encoded_to_utf8.txt"
hex_output_file = "binary_output_file.txt"
decoded_utf8_file = "binary_to_utf8.txt"
decoded_text_file = "decoded_text.txt"

# Кодування у формат UTF-8 і генерація двох файлів
encode_utf8_file(input_file, utf8_output_file, hex_output_file)

# Декодування файлу з шістнадцятковими значеннями у UTF-8
decode_hex_to_utf8(hex_output_file, decoded_utf8_file)

# Декодування UTF-8 файлу у звичайний текстовий файл
decode_utf8_file(decoded_utf8_file, decoded_text_file)