import sqlite3 #import the sqlite3 database


#declare variable to create connection.
conn = sqlite3.connect("books.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS tblbooks(id integer, title text, author text)")

conn.commit()
conn.close()