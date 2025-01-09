# 1-masala

import psycopg2

db_info = {
    'host': 'localhost',
    'port': 5432,
    'database': 'exam',
    'user': 'postgres',
    'password': '123',
}

conn = psycopg2.connect(**db_info)
cur = conn.cursor()

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS product(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10,4) NOT NULL, 
                color VARCHAR(255) NOT NULL,
                image VARCHAR(255) NOT NULL
    );''')
    conn.commit()
    conn.close()

create_table()