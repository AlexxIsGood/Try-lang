import sqlite3

conn = sqlite3.connect("books.db")

c = conn.cursor()

for row in c.execute('SELECT * FROM tblbooks ORDER BY id'):
    print(row)