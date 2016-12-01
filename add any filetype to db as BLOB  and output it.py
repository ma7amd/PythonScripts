__author__ = 'Muhammad'

import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY UNIQUE NOT NULL, note VARCHAR(1024), file BLOB, tags VARCHAR(256))")
create_table()

with open("أ.mp3", "rb") as input_file:
    ablob = input_file.read()
    cur.execute("INSERT INTO notes (id, file) VALUES(0, ?)", [sqlite3.Binary(ablob)])
    conn.commit()

with open("Output.mp3", "wb") as output_file:
    cur.execute("SELECT file FROM notes WHERE id = 0")
    ablob = cur.fetchone()
    output_file.write(ablob[0])

cur.close()
conn.close()