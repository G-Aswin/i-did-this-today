import sqlite3
from types import DynamicClassAttribute

open("tasks.db", "w").close()
dbcon = sqlite3.connect("tasks.db")

db = dbcon.cursor()

db.execute('''CREATE TABLE tasks (
	t_id INTEGER PRIMARY KEY,
	username TEXT NOT NULL,
	date TEXT NOT NULL,
	task TEXT NOT NULL,
	category TEXT NOT NULL,
	hours INTEGER NOT NULL,
	subject TEXT NOT NULL DEFAULT "others"
)''')

db.execute("INSERT INTO tasks (username, date, task, category, hours) values ('aswin','24/05/2002', 'birth', 'rest', '1')")

dbcon.commit()
dbcon.close()

