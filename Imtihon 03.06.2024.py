import psycopg2
import string
import threading
import time

# db_name = 'new_db'
# password = '123'
# host = 'localhost'
# port = 5432
# user = 'postgres'
#
# conn = psycopg2.connect(dbname=db_name,
#                         user=user,
#                         password=password,
#                         host=host,
#                         port=port)

# cur = conn.cursor()
# 1-masala
# create_table_query = """CREATE TABLE product(
# id serial primary key,
# name varchar(255),
# price int,
# color varchar(255),
# image varchar(255));
# """
#
# cur.execute(create_table_query)
# conn.commit()
# 2-masala
# def insert_table_query():
#     insert_table_query = """INSERT INTO product (name,price,color) values (%s,%s,%s)"""
#     name = input("Enter product name: ")
#     price = int(input("Enter product price: "))
#     color = input("Enter product color: ")
#     insert_params = (name,price,color)
#
#     cur.execute(insert_table_query,insert_params)
#     conn.commit()
#
# insert_table_query()

# def select_all_product():
#     select_all_product_query = """SELECT * FROM product;"""
#     cur.execute(select_all_product_query)
#     print(cur.fetchall())
#
# select_all_product()

# def update_product():
#
#     name = input("Enter new product name: ")
#     update_param = (name,)
#     update_product = """UPDATE product SET name = %s where id = 1"""
#     cur.execute(update_product,update_param)
#     conn.commit()
#
# update_product()

# def delete_product():
#
#     delete_product_query = """DELETE from product where id = 1"""
#     cur.execute(delete_product_query)
#     conn.commit()
#
# delete_product()

# 3-masla

# my_list = list(string.ascii_uppercase)
# class Alphabet:
#     def __init__(self):
#         self.a = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         item = self.a
#         self.a = self.a + 1
#         return item
#
# alphabet = Alphabet()
#
# for i in alphabet:
#     if i == 26:
#         break
#     print(my_list[i])

# 4-masala

# def print_number():
#
#     for number in range (1,6):
#         print(number)
#         time.sleep(1)
#
# def print_letters():
#     my_letters = list(string.ascii_uppercase)
#     for letter in range(0,5):
#         print(my_letters[letter])
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=print_number)
# thread2 = threading.Thread(target=print_letters)
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

# 5-masala

# class Product:
#     def __init__(self,name,price,color):
#         self.name = name
#         self.price = price
#         self.color = color
#
#     def save(self):
#         save_query = """INSERT INTO product (name,price,color) values (%s,%s,%s);"""
#         data = (self.name,self.price,self.color)
#         cur.execute(save_query,data)
#         conn.commit()
# new_product = Product("Car",10000,"Black")
#
# new_product.save()

# 6-masala

# db_params = {"dbname" : 'new_db',
#              "password" : '123',
#              "host" : 'localhost',
#              "port" : 5432,
#              "user" : 'postgres'}
#
# conn = psycopg2.connect(**db_params)
#
# class DbConnect:
#     def __init__(self,db_params: dict):
#
#         self.db_params = db_params
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(**self.db_params)
#         self.cursor = self.conn.cursor()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.conn:
#             self.cursor.close()
#             self.conn.close()









