from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("base2.html")

@app.route("/projects")
def projects():
    return render_template("base3.html")

@app.route("/contact")
def contact():
    return render_template("base4.html")

if __name__ == "__main__":
    app.run(debug=True)