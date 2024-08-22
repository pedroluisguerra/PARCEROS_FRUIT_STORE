import sqlite3
import csv

# Create database and products table
conn = sqlite3.connect(r'data\products.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS "products" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "unit_price" REAL NOT NULL
)
''')

# Insert data from CSV to products table
with open(r'data\products.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute('''
        INSERT INTO products (name, unit_price)
        VALUES (:name, :unit_price)
        ''', {'name': row['name'], 'unit_price': row['unit_price']})

conn.commit()
cur.close()
conn.close()
