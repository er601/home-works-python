# #ДЗУрок8 Дэдлайн 29.05.2022 23 59
    # 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
    # 2. В БД создать таблицу products
    # 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
    # 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL)
    # 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры поле плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
    # 6. Добавить поле quantity целочисленного типа данных размером 5 цифр, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
    # 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
    # 8. Добавить функцию, которая меняет количество товара по id
    # 9. Добавить функцию, которая меняет цену товара по id
    # 10. Добавить функцию, которая удаляет товар по id
    # 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
    # 12. Добавить функцию, которая бы выбирала из БД товары которые дешевле 100 сомов и количество которых больше чем 5 и распечатывала бы их в консоли
    # 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое слово “мыло”, должны соответствовать поиску товары с названием - “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)

import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_product_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
    return conn


def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products
                (product_title, price, quantity)
                VALUES(?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def update_product(conn, product):
    try:
        sql = '''UPDATE products SET
        quantity = ?, price= ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except sqlite3.Error as e:
        print(e)


def select_products_by_price_quantity_title(conn, product):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ? or product_title = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except sqlite3.Error as e:
        print(e)


create_product_table_sql = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (10) NOT NULL DEFAULT 0,

)
'''


database = r'hw.db'

conn = create_connection(database)

if conn is not None:
    print('Connected successfully!')
    # create_product_table(conn, create_product_table_sql)
    # insert_product(conn, ('Coca-Cola1', 432.54, 12345))
    # insert_product(conn, ('Coca-Cola2', 432.54, 12345))
    # insert_product(conn, ('Coca-Cola3', 432.54, 12345))
    # insert_product(conn, ('Coca-Cola4', 432.54, 12345))
    # insert_product(conn, ('Coca-Cola5', 121.54, 12345))
    # insert_product(conn, ('Coca-Cola6', 322.54, 12345))
    # insert_product(conn, ('Coca-Cola7', 332.54, 12345))
    # insert_product(conn, ('Coca-Cola8', 132.54, 12345))
    # insert_product(conn, ('Coca-Cola9', 242.54, 12345))
    # insert_product(conn, ('Coca-Cola10', 243.54, 12345))
    # insert_product(conn, ('Coca-Cola11', 420.54, 12345))
    # insert_product(conn, ('Coca-Cola12', 232.54, 12345))
    # insert_product(conn, ('Coca-Cola13', 342.54, 12345))
    # insert_product(conn, ('Coca-Cola14', 142.54, 12345))
    # insert_product(conn, ('Coca-Cola15', 214.54, 12345))

    # update_product(conn, (54321, 87453670.34, 2))

    # delete_product(conn, 15)

    # select_all_products(conn)

    # select_products_by_price_quantity_title(conn, (90.00, 10, 'Coca-Cola1'))

    conn.close()
else:
    print('ERROR! can create connection to DB ' + database)
