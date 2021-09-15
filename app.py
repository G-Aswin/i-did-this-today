from flask import Flask, render_template, request, redirect, session, url_for, session
from flask_session import Session
from datetime import timedelta, date
import psycopg2, os
from authlib.integrations.flask_client import OAuth


# Authentication Purposes
from auth_decorator import login_required
# from dotenv import load_dotenv
# load_dotenv()


app = Flask(__name__)
# Session config
app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id="295193539103-gtsasek5gv4ucrf63cajis8gvv83mc7p.apps.googleusercontent.com",
    client_secret="1EEkZEQggeni2m-loR44Yalo",
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL = 'postgres://fmuulpqdtebiau:3d4d6289528790e78e58792a9123a6cc33c80e18e4d04c886c9998d712c99b27@ec2-54-159-35-35.compute-1.amazonaws.com:5432/d2brdfohd7o1jc'

# db = psycopg2.connect(DATABASE_URL)




@app.route("/", methods = ["GET", "POST"])
@login_required
def index():
    print(dict(session))
    # return email
    db = psycopg2.connect(DATABASE_URL)
    dbcur = db.cursor()

    if request.method == "POST":
        idnum = request.form.get("id")
        print("I want to delete this id", idnum)
        dbcur.execute("""DELETE from tasks WHERE t_id = %s""", (idnum,))
        db.commit()
        # db.backup()

    email = dict(session)['profile']['email']
    dbcur.execute("""SELECT * from tasks WHERE username = %s ORDER BY t_id DESC""", (email,))
    rows = dbcur.fetchall()
    # print(rows, "this is the row content")
    # db.close()

    # productivedata = [0]*7
    # procrastinativedata = [0]*7

    # daynum = int(date.today().strftime("%w"))
    # today = date.today()
    # print(type(today))

    # while True:
    #     dbcur.execute("""SELECT sum(hours) from tasks WHERE username = %s AND date = %s AND category = 'productive'""", (email,str(today),))
    #     val = dbcur.fetchall()
    #     productivedata[daynum] = 
    #     dbcur.execute("""SELECT sum(hours) from tasks WHERE username = %s AND date = %s AND category = 'procrastinative'""", (email,str(today),))
    #     productivedata[daynum] = dbcur.fetchall()

    #     today = date.today() - timedelta(days=1)
    #     daynum -= 1

    #     if daynum == -1:
    #         break





    # print(productivedata, procrastinativedata)



    user = dict(session)['profile']['name']
    return render_template("index.html", rows = rows, user = user)



@app.route("/add", methods = ["GET", "POST"])
@login_required
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        print("we got till here")
        username = dict(session)['profile']['email']
        date = str(request.form.get("date"))
        task = str(request.form.get("task"))
        category = str(request.form.get("category"))
        # subject = str(request.form.get("subject"))
        # username = "aswin"
        hours = int(request.form.get("hours"))

        db = psycopg2.connect(DATABASE_URL)
        dbcur = db.cursor()

        # print(date, task, category, subject, username)
        dbcur.execute("INSERT into tasks (username, date, task, category, hours) values (%s, %s, %s, %s, %s)", (username, date, task, category, hours))
        db.commit()
        db.close()
        return redirect("/")


@app.route("/analyse", methods = ["GET", "POST"])
@login_required
def analyse():
    return "WORK IN PROGRESS"


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

        