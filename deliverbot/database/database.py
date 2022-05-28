import sqlite3
import os

def convert_image_to_blob(filename):
    with open(filename, "rb") as image:
        blob = image.read()
    return blob
        
def script(file):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        with open(file, 'r') as file:
            script = file.read()
        
        cursor.executescript(script)    
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def select_menu(category):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        select_query = 'SELECT id, product_name, price, image FROM menu WHERE category = ?'

        cursor.execute(select_query, (category,))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def select_product(category, id):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT product_name, price FROM menu WHERE id = ? AND category = ?'''

        cursor.execute(select_query, (id, category))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def select_reviews():
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        select_query = 'SELECT author_review, review FROM reviews'

        cursor.execute(select_query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def insert_feedback(author, review):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        insert_query = '''INSERT INTO reviews (author_review, review)
                          VALUES (?, ?)'''

        cursor.execute(insert_query, (author, review))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()



# функции для добавления и вывода всей бд

def insert_menu(product_name, category, image, price):
    try:
        sqlite_connection = sqlite3.connect("menu.db")
        cursor = sqlite_connection.cursor()

        insert_query = '''INSERT INTO menu (product_name, category, image, price) VALUES
                          (?, ?, ?, ?)'''                   

        cursor.execute(insert_query, (product_name, category, image, price))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()

# insert_menu("Пицца маргарита", "pizza", convert_image_to_blob(r"chuvak eto put"), "10$")
# insert_menu("Пицца салями", "pizza", convert_image_to_blob(r"chuvak eto put"), "8$")
# insert_menu("Маки Роллы", "sushi", convert_image_to_blob(r"chuvak eto put"), "5$")
# insert_menu("Суши Калифорния", "sushi", convert_image_to_blob(r"chuvak eto put"), "6$")
# insert_menu("Картошка фри мал.", "snacks", convert_image_to_blob(r"chuvak eto put"), "1$")
# insert_menu("Картошка фри ср.", "snacks", convert_image_to_blob(r"chuvak eto put"), "2$")
# insert_menu("Картошка фри больш.", "snacks", convert_image_to_blob(r"chuvak eto put"), "3$")