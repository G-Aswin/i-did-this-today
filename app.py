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
    rows = db.execute("SELECT * from tasks")
    
    return render_template("index.html", rows = rows)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        print("we got till here")
        date = str(request.form.get("date"))
        task = str(request.form.get("task"))
        db = sqlite3.connect("tasks.db")

        print(date, task)
        db.execute("INSERT into tasks values (?, ?)", (date, task))
        db.commit()
        return redirect("/")

        