import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

title = input("Enter the title of the book to search: ")

c.execute('SELECT * FROM tblbooks WHERE title=?',(title,))
print(c.fetchall())

conn.close()  