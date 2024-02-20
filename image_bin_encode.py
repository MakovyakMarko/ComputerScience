# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:35:55 2023

@author: Marko
"""

from PIL import Image

def encode_image(image_path, output_file):
    # Відкриваємо зображення
    image = Image.open(image_path)
    
    # Отримуємо розміри зображення
    width, height = image.size
    
    # Відкриваємо файл для запису бітових даних
    with open(output_file, 'wb') as file:
        # Проходимо по кожному пікселю в зображенні
        encoded_data = bytearray()
        for y in range(height):
            for x in range(width):
                # Отримуємо значення RGB для кожного пікселя
                r, g, b = image.getpixel((x, y))
                
                # Конвертуємо значення RGB в байтовий формат
                # Якщо потрібно, ви можете здійснити подальшу обробку кожного байта
                
                # Записуємо байти у файл
                encoded_data.append(r)
                encoded_data.append(g)
                encoded_data.append(b)
        
        file.write(encoded_data)
    
    return width, height, encoded_data

def decode_image(encoded_data, width, height):
    decoded_image = Image.new("RGB", (width, height))
    pixels = decoded_image.load()
    
    index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = encoded_data[index], encoded_data[index+1], encoded_data[index+2]
            pixels[x, y] = (r, g, b)
            index += 3
    
    return decoded_image

image_path = 'PyLogo.png'
output_file = 'encoded_png_image.txt'


width, height, encoded_data = encode_image(image_path, output_file)

# Декодування зображення
decoded_image = decode_image(encoded_data, width, height)
decoded_image.show()  # Показати розкодоване зображення

def encode_png_image(image_path, output_file):
    image = Image.open(image_path)
    width, height = image.size

    encoded_data = []
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            encoded_data.append(pixel)

    with open(output_file, 'w') as file:
        for pixel_value in encoded_data:
            file.write(f'{pixel_value}\n')

    return width, height, encoded_data

def decode_png_image(encoded_data, width, height):
    decoded_image = Image.new("RGBA", (width, height))
    pixels = decoded_image.load()

    index = 0
    for y in range(height):
        for x in range(width):
            pixel_value = encoded_data[index]
            pixels[x, y] = (0, 0, 0, int(pixel_value[3])) if pixel_value[3] == 255 else (0, 0, 0, int(pixel_value[3]))
            index += 1

    return decoded_image

# Виклик функцій
image_path = 'faw_icon.png'
output_file = 'encoded_image.txt'

# Кодування зображення
width, height, encoded_data = encode_png_image(image_path, output_file)

# Декодування зображення
decoded_image = decode_png_image(encoded_data, width, height)
decoded_image.show()  # Показати розкодоване зображення