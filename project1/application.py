import os
import logging
from flask import Flask, session ,request ,Response
from flask import Flask, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from Registration import *
from datetime import datetime
app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# db.init_app(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Session(app)
db.init_app(app)
# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
def _init_(self, timezone=False, fsp=None):
    super(TIMESTAMP, self)._init_(timezone=timezone)
    self.fsp = fsp
@app.route("/register",methods=["GET"])
def register():
    if request.method == "GET":
        return render_template("RegistrationPage.html")
    
# @app.route("/")
# def index():
#     return render_template("HomePage.html")

@app.route("/print",methods=["POST","GET"])
def display():
        Registration.query.all()
        f = request.form.get("first-name")
        l = request.form.get("last-name")
        email = request.form.get("email")
        register = Registration(first_name=f, last_name=l,email=email,datetime=datetime.now())
        
        try:
            db.session.add(register)
            db.session.commit()
            print()
            print(f+" "+l)
            return render_template("print.html",f=f,l=l)
        except Exception :
	        return render_template("error.html", errors = "Details are already given")


