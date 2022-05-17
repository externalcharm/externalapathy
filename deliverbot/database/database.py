import sqlite3

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

        select_query = 'SELECT id, product_name, price FROM menu WHERE category = ?'

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