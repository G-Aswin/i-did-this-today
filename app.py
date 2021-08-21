from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import psycopg2, os
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = 'postgres://fmuulpqdtebiau:3d4d6289528790e78e58792a9123a6cc33c80e18e4d04c886c9998d712c99b27@ec2-54-159-35-35.compute-1.amazonaws.com:5432/d2brdfohd7o1jc'

# db = psycopg2.connect(DATABASE_URL)

@app.route("/", methods = ["GET", "POST"])
def index():
    db = psycopg2.connect(DATABASE_URL)
    dbcur = db.cursor()

    if request.method == "POST":
        idnum = request.form.get("id")
        print("I want to delete this id", idnum)
        dbcur.execute("""DELETE from tasks WHERE t_id = %s""", (idnum,))
        db.commit()
        # db.backup()


    dbcur.execute("SELECT * from tasks ORDER BY t_id DESC")
    rows = dbcur.fetchall()
    print(rows, "this is the row content")
    # db.close()
    return render_template("index.html", rows = rows)



@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        print("we got till here")
        date = str(request.form.get("date"))
        task = str(request.form.get("task"))
        category = str(request.form.get("category"))
        subject = str(request.form.get("subject"))
        username = "aswin"
        hours = int(request.form.get("hours"))

        db = psycopg2.connect(DATABASE_URL)
        dbcur = db.cursor()

        print(date, task, category, subject, username)
        dbcur.execute("INSERT into tasks (username, date, task, category, subject, hours) values (%s, %s, %s, %s, %s, %s)", (username, date, task, category, subject, hours))
        db.commit()
        db.close()
        return redirect("/")

        