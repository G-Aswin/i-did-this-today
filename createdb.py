import sqlite3
from types import DynamicClassAttribute

open("tasks.db", "w").close()
dbcon = sqlite3.connect("tasks.db")

db = dbcon.cursor()

db.execute('''CREATE TABLE tasks
               (date text, task text)''')

db.execute("INSERT INTO tasks values ('24/05/2002', 'birth')")

dbcon.commit()
dbcon.close()

