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
            FROM Product JOIN category ON Product.category_id = Category.category_id
                           WHERE category.name = "Guitars"
                           ''', [category])
            rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Failed to fetch data from database: {e}")
    return rows

def add_product(category, name, code, price):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(''' SELECT category_id FROM Category WHERE name = ?
            ''', [category])
            row = cursor.fetchone()
            if row is None:
                raise ValueError(f"Category {category} does not exist")

            category_id = row[0]

            cursor.execute('''
            INSERT INTO Product (category_id, name, code, price)
                           VALUES (?, ?, ?, ?)''', [category_id, name, code, price])
            conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to add product to database: {e}")
        except ValueError as e:
            print(e)

def delete_product(code):
   try:
       with get_connection() as conn:
   cursor = get_connection()
   cursor.execute('''
                  SELECT product_id
                  FROM Product
                  WHERE code = ?
                  ''', [code]))
   row = cursor.fetchone()
   if row is None:
       raise ValueError(f"Product {code} does not exist")

    product_id = row[0]
    cursor.execute('''
    DELETE FROM Product WHERE product_id = ?
        ''', [product_id])
        conn.commit()
            except sqlite3.Error as e:
        print(f"Failed to delete product from database: {e}")
            except ValueError as e:
        print(e)

