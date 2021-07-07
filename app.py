import os
import sqlite3
from flask import Flask, g, flash, redirect, render_template, request, session, url_for
from tempfile import mkdtemp

# Flask config
app = Flask(__name__)

# Connecting with Database
DATABASE = './messages.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


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
        db = get_db()
        cursor = db.execute('SELECT * FROM messages')
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

        conn = sqlite3.connect('messages.db')
        data = [name, email, subject, message]
        conn.execute("INSERT INTO messages (name, email, subject, message) VALUES (?, ?, ?, ?)",
                       (*data,))
        conn.commit()

        return redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0")