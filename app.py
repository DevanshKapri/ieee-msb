import os
import psycopg2
from flask import Flask, g, flash, redirect, render_template, request, session, url_for
from tempfile import mkdtemp

# Flask config
app = Flask(__name__)

# Connecting with Database
POSTGRES_URL = "postgres://wrbrytmbdhojuo:f25be743a8861bea4a4f2a967481e70804707377b5ba3dcb41b3e9f3a6950af9@ec2-52-86-25-51.compute-1.amazonaws.com:5432/damafta2g98grd"

db = psycopg2.connect(POSTGRES_URL)

try:
    with db:
        with db.cursor() as cursor:
            cursor.execute("CREATE TABLE messages (name TEXT NOT NULL, email VARCHAR NOT NULL, subject text NOT NULL, message text NOT NULL);")
except psycopg2.errors.DuplicateTable:
    pass

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        with db:
            with db.cursor() as cursor:
                cursor.execute('SELECT * FROM messages')
                history = cursor.fetchall()
        if not history:
            return render_template("index.html")
        else:
            return render_template("index.html", history=history)

    else:
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")


        with db:
            with db.cursor() as cursor:
                cursor.execute("INSERT INTO messages (name, email, subject, message) VALUES (%s, %s, %s, %s)",
                       (name, email, subject, message))
        return redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0")