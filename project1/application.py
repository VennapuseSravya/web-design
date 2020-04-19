import os
import logging
from flask import Flask, session ,request ,Response,url_for,redirect
from flask import Flask, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from Registration import *
from datetime import datetime
app = Flask(__name__)
app.secret_key="login"
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

# session['username']="admin"
db.init_app(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

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

@app.route("/admin")
def admin():  
    Register=Registration.query.all()
    return render_template("admin.html",register=Register)
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

     
@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    Registration.query.all()
    email = request.form.get("email")
    try:
        Member = db.session.query(Registration).filter(Registration.email == email).all()    
        print(Member[0].first_name)
        session['user'] = request.form.get("email")
        return redirect(url_for('index'))
        # return render_template("User.html")   
    except Exception :
	        return "Email is not registered"


@app.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for("register"))

   
