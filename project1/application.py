import os
import logging
from flask import Flask, session ,request ,Response
from flask import Flask, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/register",methods=["GET"])
def register():
    if request.method == "GET":
        return render_template("RegistrationPage.html")
    
# @app.route("/")
# def index():
#     return render_template("HomePage.html")

@app.route("/print",methods=["POST","GET"])
def display():
        
        f = request.form.get("first-name")
        l = request.form.get("last-name")
        print(f+" "+l)
        return render_template("print.html",f=f,l=l)
