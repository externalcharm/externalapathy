import sqlite3

def script(file):
    try:
        sqlite_connection = sqlite3.connect("days.db")
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

def select(abbreviated):
    try:
        sqlite_connection = sqlite3.connect("days.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT utter FROM calendar WHERE abbreviated = ?'''

        cursor.execute(select_query, (abbreviated,))
        records = cursor.fetchone()
        cursor.close()
        return records[0]
    except sqlite3.Error as error:
        return error
    finally:
        if sqlite_connection:
            sqlite_connection.close()