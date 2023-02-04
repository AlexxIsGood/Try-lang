import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

#name = input("Enter the name to search: ")
id = int(input("Enter the id you want to replace: "))
title = input("Enter the title you want to change: ")
author = input("Enter the author you want to change: ")

sql = '''UPDATE tblbooks SET id = ?, title = ?, author = ?where id = ?'''
c.execute(sql,(id,title,author, id))

getAllData = c.execute("SELECT * FROM tblbooks order by id")

for row in getAllData:
    print(row)
    
conn.commit()
conn.close()  
