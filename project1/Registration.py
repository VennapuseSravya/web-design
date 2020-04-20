from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Registration(db.Model):
    __tablename__ = "Registration details"
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False,primary_key=True)
    datetime = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)