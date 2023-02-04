import sqlite3

conn = sqlite3.connect("books.db")

c = conn.cursor()

id = int(input("Enter the id: "))
title = input("Enter the book name: ")
author =input("Enter the authors name: ")


#INSERT 
c.execute("""
INSERT INTO tblbooks(id, title,author)
VALUES(?,?,?)
""", (id, title,author))
print("Inserted Data Successfully")

conn.commit()
conn.close()