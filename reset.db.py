import sqlite3


def reset_db():
    with sqlite3.connect('database/guitarshop.sqlite') as conn:
        cursor = conn.cursor()

        cursor.executescript("""
                             DROP TABLE IF EXISTS Category;
                             DROP TABLE IF EXISTS Product;

                             create table Category
                             (
                                 category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name        TEXT NOT NULL
                             );

                             create table Product
                             (
                                 product_id  INTEGER PRIMARY KEY AUTOINCREMENT,
                                 code        TEXT    NOT NULL,
                                 name        TEXT    NOT NULL,
                                 price       REAL    NOT NULL,
                                 category_id INTEGER NOT NULL,
                                 FOREIGN KEY (category_id) references Category (category_id)
                             );

                             INSERT INTO Category (name)
                             VALUES ("Guitars"),
                                    ("Basses"),
                                    ("Drums");

                             INSERT INTO Product (code, name, price, category_id)
                             VALUES ("strat", "Fender Stratocaster", 699.00, 1),
                                    ("les_paul", "Gibson Les Paul", 799.99, 1),
                                    ("sg", "Gibson SG", 1234.00, 1),
                                    ("fg700s", "Fender FG700S", 1399.99, 1),
                                    ("rodriguez", "Rodriguez Caballero 11", 1399.99, 1);

                             INSERT INTO Product (code, name, price, category_id)
                             VALUES ("precision", "Fender Precision", 999, 2),
                                    ("hofner", "Hofner Icon", 499.99, 2);

                             INSERT INTO Product (code, name, price, category_id)
                             VALUES ("ludwig", "Ludwig 5-piece Drum Set with Cymbals", 699.99, 3),
                                    ("tama", "Tama 5-Piece Drum Set with Cymbals", 799.99, 3);
                             """)


reset_db()