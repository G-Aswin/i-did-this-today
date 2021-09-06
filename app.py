from flask import Flask, render_template, request, redirect, session, url_for, session
from flask_session import Session
from datetime import timedelta
import psycopg2, os


# Authentication Purposes
from authlib.integrations.flask_client import OAuth
app = Flask(__name__)

oauth = OAuth(app)



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL = 'postgres://fmuulpqdtebiau:3d4d6289528790e78e58792a9123a6cc33c80e18e4d04c886c9998d712c99b27@ec2-54-159-35-35.compute-1.amazonaws.com:5432/d2brdfohd7o1jc'

# db = psycopg2.connect(DATABASE_URL)

#firebase auth
config = {
    "apiKey": "AIzaSyBZv4x1rzkueJM5uNmeqKNEIBxgHahlI5U",
    "authDomain": "i-did-this-today.firebaseapp.com",
    "projectId": "i-did-this-today",
    "storageBucket": "i-did-this-today.appspot.com",
    "messagingSenderId": "572180625499",
    "appId": "1:572180625499:web:a93de145bc191b122c677e",
    "measurementId": "G-PTPWMJ0LVF"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()




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


@app.route("/analyse", methods = ["GET", "POST"])
def analyse():
    return "WORK IN PROGRESS"
        