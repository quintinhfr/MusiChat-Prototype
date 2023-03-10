from crypt import methods
from flask import Flask, url_for, redirect, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager
import mysql.connector
import sqlite3


#Database Creation - 


#App Creation -

app = Flask(__name__)
app.config['SECRET_KEY'] = "HUGRADPROJECT"





#--------------------------------------------------------------------
# HOME PAGE
#--------------------------------------------------------------------

@app.route("/", methods=['GET', 'POST'])
def Home():
    return render_template("index.html")

#--------------------------------------------------------------------
# Log In Page
#--------------------------------------------------------------------

@app.route("/log-in", methods=['GET', 'POST'])
def LogIn():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")

#--------------------------------------------------------------------
# About Page
#--------------------------------------------------------------------

@app.route("/about")
def About():
    return render_template("about.html")

#--------------------------------------------------------------------
# Create Post Page
#--------------------------------------------------------------------

@app.route("/post")
def Post():
    return render_template("post.html")

#--------------------------------------------------------------------
# Sign Up Page
#--------------------------------------------------------------------

@app.route("/sign-up", methods=['GET', 'POST'])
def signup():
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    return render_template("sign-up.html")

#--------------------------------------------------------------------
# LOGOUT
#--------------------------------------------------------------------

@app.route("/logout")
def logout():
    return redirect(url_for("app.Home"))


#----------------------
# Program Run Operation
#----------------------
if __name__ == "__main__":
    app.run()