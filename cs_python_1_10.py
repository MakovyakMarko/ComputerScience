# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:46:27 2023

@author: Marko
"""
def encode_string(input_string):
    encoded_data = ""
    for char in input_string:
        ascii_code = ord(char)
        parity_bit = bin(ascii_code).count("1") % 2
        binary_code = bin(ascii_code)[2:].zfill(8)
        encoded_data += str(parity_bit) + binary_code
    return encoded_data

def decode_string(encoded_data):
    decoded_string = ""
    i = 0
    while i < len(encoded_data):
        parity_bit = int(encoded_data[i])
        binary_code = encoded_data[i+1:i+9]
        ascii_code = int(binary_code, 2)
        if bin(ascii_code).count("1") % 2 != parity_bit:
            raise ValueError("Decoding error: parity bit mismatch")
        decoded_string += chr(ascii_code)
        i += 9
    return decoded_string

input_string1 = '"Stop!" Cheryl shouted.'
input_string2 = 'Does 2 + 3 = 5?'
encoded_data = encode_string(input_string1)
print("Encoded data:", encoded_data)

decoded_string = decode_string(encoded_data)
print("Decoded string:", decoded_string)

encoded_data = encode_string(input_string2)
print("Encoded data:", encoded_data)

decoded_string = decode_string(encoded_data)
print("Decoded string:", decoded_string)

