# import sqlite3
# def get_connection():
#         conn = sqlite3.connect('database/guitarshop.sqlite')
#         conn.execute('PRAGMA foreign_keys = ON')
#         return conn
#
# def get_all_categories():
#     rows = None
#     try:
#         with get_connection() as conn:
#             cur = conn.cursor()
#             cursor.execute('''
#             SELECT name FROM Category
#             ORDER BY category_id
#
#             ''')
#             rows = cursor.fetchall()
#         except sqlite3.Error as e:
#             print(f"failed to get data from database: {e}")
#         return rows

import sqlite3
def get_connection():
    conn = sqlite3.connect('database/guitarshop.sqlite')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def get_all_categories():
    rows = None
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT name FROM Category
            ORDER BY category_id 
            """)
            rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Failed to fetch data from database: {e}")
    return [row[0] for row in rows]

def get_all_products_in_category(category):
    rows = None
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
            SELECT Product.code, Product.name, Product.price
            FROM Product JOIN category ON Product.category_id = category.id
                           WHERE category.name = ?
                           ''', [category])
            rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Failed to fetch data from database: {e}")
    return rows

