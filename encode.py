import codecs
def encode_utf8(characters):
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
    return encoded_bytes

def create_binary_file(characters, filename):
    encoded_bytes = encode_utf8(characters)
    with open(filename, 'wb') as file:
        file.write(encoded_bytes)


def write_bytes_to_text_file(data, filename):
    with open(filename, 'w') as file:
        for byte in data:
            binary_str = bin(byte)[2:].zfill(8)  # Перетворення байта у послідовність нулів і одиниць
            file.write(binary_str + ' ')

def create_utf8_file(characters, filename):
    with open(filename, 'w') as file:
        for character in characters:
            encoded_bytes = encode_utf8(character)
            for byte in encoded_bytes:
                strbyte = str(byte)
                file.write(strbyte + " ")
                
def read_binary_file(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        decoded_characters = data.decode('utf-8')
        return decoded_characters

    
def read_utf8_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        decoded_characters = ''.join(chr(int(byte)) for byte in data.split())
        return decoded_characters
    
        
characters = input("Enter symbols: ")
binary_file = "binary.bin"
create_binary_file(characters, binary_file)
text_file = "binary_as_text.txt"
write_bytes_to_text_file(open(binary_file, 'rb').read(), text_file)

utf8_file = "utf-8.txt"


print("Binary file contents:")
print(open(binary_file, 'rb').read())

print("Binary as text:")
print(open(text_file, 'r').read())

print("UTF-8 file contents:")
print(open(utf8_file, 'r').read())

decoded_binary = read_binary_file(binary_file)
print('Decoded from binary file:', decoded_binary)
decoded_utf8 = "decoded_file.txt"
print('Decoded from UTF-8 file:', decoded_utf8) 