"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2

"""Заполнение таблицы employees"""

with psycopg2.connect(host="localhost", database="north", user="postgres", password="DIM_dim2023") as conn:
    with conn.cursor() as cur:
        with open("north_data/employees_data.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee_id = row['employee_id']
                first_name = row['first_name']
                last_name = row['last_name']
                title = row['title']
                birth_date = row['birth_date']
                notes = row['notes']
                cur.execute(
                    "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
                    "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (employee_id) DO NOTHING",
                    (employee_id, first_name, last_name, title, birth_date, notes)
                )

"""Заполнение таблицы customers"""

with psycopg2.connect(host="localhost", database="north", user="postgres", password="DIM_dim2023") as conn:
    with conn.cursor() as cur:
        with open("north_data/customers_data.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_id = row['customer_id']
                company_name = row['company_name']
                contact_name = row['contact_name']
                cur.execute(
                    "INSERT INTO customers (customer_id, company_name, contact_name) "
                    "VALUES (%s, %s, %s) ON CONFLICT (customer_id) DO NOTHING",
                    (customer_id, company_name, contact_name)
                )

"""Заполнение таблицы orders"""

with psycopg2.connect(host="localhost", database="north", user="postgres", password="DIM_dim2023") as conn:
    with conn.cursor() as cur:
        with open("north_data/orders_data.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                order_id = row['order_id']
                customer_id = row['customer_id']
                employee_id = row['employee_id']
                order_date = row['order_date']
                ship_city = row['ship_city']
                cur.execute(
                    "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
                    "VALUES (%s, %s, %s, %s, %s) ON CONFLICT (order_id) DO NOTHING",
                    (order_id, customer_id, employee_id, order_date, ship_city)
                )

conn.close()

