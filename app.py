from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import sqlite3
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# db = sqlite3.connect("database.db")


@app.route("/", methods = ["GET", "POST"])
def index():
    db = sqlite3.connect("tasks.db")

    if request.method == "POST":
        idnum = request.form.get("id")
        print("I want to delete this id", idnum)
        db.execute("DELETE from tasks WHERE t_id = ?", (idnum,))
        db.commit()

    rows = db.execute("SELECT * from tasks ORDER BY t_id DESC")
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

        db = sqlite3.connect("tasks.db")

        print(date, task, category, subject, username)
        db.execute("INSERT into tasks (username, date, task, category, subject, hours) values (?, ?, ?, ?, ?, ?)", (username, date, task, category, subject, hours))
        db.commit()
        return redirect("/")

        