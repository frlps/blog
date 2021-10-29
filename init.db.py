import sqlite3 #Faz o ger, manipulação do DB SQLite

connection = sqlite3.connect('database.db')

#Executa o código Schema.sql
with open('schema.sql') as f:
    connection.executescript(f.read()) 

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)",('First Post', 'Content for the first post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?,?)",('Second Post', 'Content for the second post'))

connection.commit()

connection.close()