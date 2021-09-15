import psycopg2

URI = "postgres://fmuulpqdtebiau:3d4d6289528790e78e58792a9123a6cc33c80e18e4d04c886c9998d712c99b27@ec2-54-159-35-35.compute-1.amazonaws.com:5432/d2brdfohd7o1jc"


# DATABASE_URL = os.environ.get(URI)
con = psycopg2.connect(URI)
cur = con.cursor()


cur.execute("""DROP TABLE tasks""")
con.commit()



cur.execute('''CREATE TABLE tasks (
	t_id SERIAL PRIMARY KEY,
	username TEXT NOT NULL,
	date TEXT NOT NULL,
	category TEXT NOT NULL,
	task TEXT NOT NULL,
	hours INTEGER NOT NULL
)''')

# cur.execute("INSERT INTO tasks (username, date, task, category, hours, subject) values ('aswin','24/05/2002', 'birth', 'rest', '1', 'others')")

con.commit()
con.close()
