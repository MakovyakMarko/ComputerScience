# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:46:15 2023

@author: Marko
"""

import requests
from bs4 import BeautifulSoup
import mysql.connector

# Завантажуємо сторінку
url = "https://uk.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)

# Перевірка статусу відповіді
if response.status_code == 200:
    # Створюємо об'єкт BeautifulSoup для парсингу HTML
    soup = BeautifulSoup(response.content, "html.parser")
    container = soup.find("div", class_="mw-parser-output")

    # Знаходимо головний заголовок сторінки
    #page_title = container.find("h1").text.strip()
    page_title = soup.find("h1", id="firstHeading").text.strip()
    # Знаходимо усі заголовки статей та підтеми
    headers = container.find_all("span", class_="mw-headline")
    subheaders = container.find_all("span", class_="mw-headline", recursive=False)

    # Знаходимо параграфи, що стосуються кожної підтеми
    paragraphs = []
    for subheader in subheaders:
        subheader_paragraphs = []
        next_element = subheader.find_next_sibling()
        while next_element and next_element.name != "h2":
            if next_element.name == "p":
                subheader_paragraphs.append(next_element.text.strip())
            next_element = next_element.next_sibling
        paragraphs.append(subheader_paragraphs)

    # З'єднання з базою даних
    cnx = mysql.connector.connect(user='wiki_scraper', password='ERqw56qwGHqwwe#$',
                                  host='localhost', database='wiki_scraper_db')
    cursor = cnx.cursor()

    # Створення таблиць, якщо не існують
    create_table_query = """
    CREATE TABLE IF NOT EXISTS article_headers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        header VARCHAR(255),
        subheader VARCHAR(255),
        paragraph TEXT
    )
    """
    cursor.execute(create_table_query)

    # Вставка даних в базу даних
    insert_query = "INSERT INTO article_headers (header, subheader, paragraph) VALUES (%s, %s, %s)"
    data = []
    for header, subheader, subheader_paragraphs in zip(headers, subheaders, paragraphs):
        for paragraph in subheader_paragraphs:
            data.append((header.text, subheader.text, paragraph))
    cursor.executemany(insert_query, data)
    cnx.commit()

    # Закриття з'єднання з базою даних
    cursor.close()
    cnx.close()

    print("Дані успішно збережені в базу даних.")
else:
    print("Помилка при отриманні сторінки")
'''
'''
import wikipediaapi

# Створюємо об'єкт Wikipedia
wiki_wiki = wikipediaapi.Wikipedia('en')

# Отримуємо сторінку з Вікіпедії за заголовком "Python (programming language)"
page_py = wiki_wiki.page("Python (programming language)")

# Виводимо заголовок та текст сторінки
print("Page - Title: %s" % page_py.title)
print("Page - Text: %s" % page_py.text[:60])
'''
'''
import sqlite3
import wikipediaapi

# Створюємо об'єкт Wikipedia
wiki_wiki = wikipediaapi.Wikipedia('en')

# Підключаємося до бази даних SQLite
conn = sqlite3.connect('wiki_data.db')
cursor = conn.cursor()

# Створюємо таблицю для збереження даних
cursor.execute('''CREATE TABLE IF NOT EXISTS pages
                  (title TEXT PRIMARY KEY, text TEXT)''')

# Список сторінок IT, для яких ви хочете отримати дані
it_pages = ['Python (programming language)', 'JavaScript', 'Java (programming language)']

# Отримуємо дані для кожної сторінки та зберігаємо їх у базу даних
for page_title in it_pages:
    # Отримуємо сторінку з Вікіпедії за заголовком
    page = wiki_wiki.page(page_title)
    
    # Отримуємо заголовок та текст сторінки
    title = page.title
    text = page.text
    
    # Зберігаємо дані у базу даних
    cursor.execute("INSERT INTO pages (title, text) VALUES (?, ?)", (title, text))

# Зберігаємо зміни та закриваємо підключення до бази даних
conn.commit()
conn.close()
